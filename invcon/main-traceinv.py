import argparse
import logging
import json 
import os 
from invconplus.model.Replayer import TransactionReplayer
from invconplus.engine import InvConPlus
from invconplus.ppt import PptTopLevel
from invconplus.trace.traceslice import TraceSlice, Trace, covertTx2Event, default
from invconplus.const import RESULT_DIR 
import time 

def main(address, configuration=None, maxCount=500, minSupport=50, training_ratio=None, hack_tx = None):
    if training_ratio is not None:
        assert training_ratio <= 1.0 and training_ratio >= 0, "Training ratio must be between 0 and 1"
    logging.warning(address)
    statistics = dict()
    start_time = time.time()
    txreplayer = TransactionReplayer(contract_address=address, maxCount= maxCount, hack_tx = hack_tx)
    invcon = InvConPlus(address, txreplayer.contractName, txreplayer.getDeclModel(), txreplayer.getABISpec())
    invcon.initializePpts()

    statistics["initializePpts"] = time.time() - start_time 
    statistics["readTx"] = list()
    statistics["processData"] = list()
    read_start_time = time.time()
    tx = txreplayer.readPerTx()
    statistics["readTx"].append(time.time() - read_start_time)
    if not os.path.exists(RESULT_DIR):
        os.mkdir(RESULT_DIR)

    if hack_tx is not None:
        maxCount = txreplayer.total_transaction_count
        
    count = 0
    test_mode = False
    result_tests = dict() 
    if configuration is None:
        while (not txreplayer.done()) and count < maxCount:
            read_start_time = time.time()
            try:
                is_creation, txs, offset, reason = txreplayer.readPerTx()
            except:
                break
            statistics["readTx"].append(time.time() - read_start_time)
            count += 1
            count += offset
            if txs is None or len(txs) == 0:
                continue
            
            logging.warning(txs[0].tx_hash  + " ".join([str(tx.func) if tx.func is not None else "" for tx in txs]))
            if not is_creation:
                process_time = time.time() 
                for tx in txs:
                    false_invs = invcon.process_data(tx, test_mode)
                    statistics["processData"].append(time.time() - process_time)
                    if test_mode:
                        if tx.tx_hash not in result_tests:
                            result_tests[tx.tx_hash] = []
                        result_tests[tx.tx_hash].append(dict(func=tx.func, reverted = tx.hasRevert(), violated_invs = [inv.__str__() for inv in false_invs]))
            if training_ratio is not None:
                if count >= int(txreplayer.total_transaction_count*training_ratio) and not test_mode:
                    invcon.generate_invariants(inv_file= os.path.join(RESULT_DIR, address + "-" +txreplayer.contractName+".training.inv"))
                    test_mode = True
          
    else:
        slice_configuration = json.load(open(configuration))
        trace = Trace()
        slicer = TraceSlice(trace=trace)
        slicer.setSliceCriteriaByInterestedParams(interested_params=slice_configuration)
        while (not txreplayer.done()) and count < maxCount:
            firstOrMultiple, tx = txreplayer.readPerTx()
            if tx is None:
                continue
            logging.warning(tx.tx_hash + (str(tx.func) if tx.func is not None else ""))
            logging.debug((str(tx.func[0]) if tx.func is not None and len(tx.func)>0 else "") + json.dumps(tx.envs) if tx.envs is not None else None)
            if not firstOrMultiple:
                invcon.process_data(tx)
                if not tx.hasRevert():
                    newSubEvents = slicer.onlineSlice(covertTx2Event(tx))
                    for newSubEvent in newSubEvents:
                        event, pre_slice_states, post_slice_states = newSubEvent
                        ppt :PptTopLevel = invcon.dynamicCreateOrGetSlicePPT(funcName=event.methodName, key_parameters=event.parameters, slice_states=post_slice_states)
                        ppt.loadSliceEvent(tx=tx, slice_states= pre_slice_states + post_slice_states)
            count += 1
        
        invcon.generate_trace_slice_invariants(inv_file = os.path.join(RESULT_DIR, address+"-"+ txreplayer.contractName+"-trace.inv"))
        json.dump(slicer.to_list(), open(os.path.join(RESULT_DIR, address + "-" + txreplayer.contractName + "-" + "trace_slices.json"), "w"), indent=4)
    
    if test_mode:
        json.dump(result_tests, open(os.path.join(RESULT_DIR, address+"-"+txreplayer.contractName+".test.violation.inv"), "w"), indent=4)

    if count > minSupport:
        logging.warning("Generating invariants... for {0} txs".format(count))
        logging.warning("Time used: {0} seconds".format(str(time.time() - start_time)))
        logging.warning("Time Usage Detail: initializePpts({0}), readTx({1}), processData({2})".format( statistics["initializePpts"], sum(statistics["readTx"]), sum(statistics["processData"])))
        invcon.generate_invariants(inv_file= os.path.join(RESULT_DIR, address + "-" +txreplayer.contractName+".inv"))
        txreplayer.toStateJson(os.path.join(RESULT_DIR, address + "-" +txreplayer.contractName+".json"))

GameChannel_Address = "0x7e0178e1720e8b3a52086a23187947f35b6f3fc4"
Token_Address = "0x1dac5649e2a0c943ffc4211d708f6ddde4742fd6"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=\
                                     'InvCon: A Dynamic Invariant Detector for Ethereum Smart Contracts!')
    parser.add_argument('--address', type=str, required=False, default=GameChannel_Address, 
                        help='address of Ethereum smart contract,\
                              default (0x7e0178e1720e8b3a52086a23187947f35b6f3fc4-GameChannel)')
    
    parser.add_argument('--configuration', type=str, required=False, default=None, 
                        help='configuration of slice criteria (.json),\
                              (e.g., ./invconplus/slicecriteria/GameChannel.json)')
    
    parser.add_argument('--output_dir', type=str, required=False, default=None, 
                        help='directory where the invariant results will be stored')
    
    parser.add_argument('--training_ratio', type=float, required=False, default=None, 
                        help='the proportion of transactions used training to produce invariants,\
                              (default, 1)')
    
    parser.add_argument('--hack_tx', type=str, required=False, default=None, 
                        help='the hack tx to be used for testing')
    
    parser.add_argument('--maxCount', type=int, required=False, default=500, 
                        help='the number of transactions used,\
                              (default, 500)')
    
    parser.add_argument('--minSupport', type=int, required=False, default=50, 
                        help='the number of minimum transactions used,\
                              (default, 50)')
    
    args = parser.parse_args()
    if args.output_dir is not None:
        RESULT_DIR = args.output_dir

    main(args.address, args.configuration, args.maxCount, args.minSupport, args.training_ratio, args.hack_tx)
    