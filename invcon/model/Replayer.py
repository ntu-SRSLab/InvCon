import copy
import logging
import json 
from dataclasses import asdict
from .Tx import Transaction, TxType
from .Reader import Reader, StorageModelReader
from . import model as model
from invconplus.vmtracesimulator.main import Simulator
from invconplus.vmtracesimulator.TraceParsing import Simulator as Simulator2
from invconplus.const import ENABLE_READ_MODEL_FLATTENVALUE

File = str 
Tx = str
class TransactionReplayer:
    contract_address: str 
    contractName: str 
    myreader: Reader 
    modelReader: StorageModelReader
    def __init__(self, contract_address, maxCount, hack_tx) -> None:
        self.contract_address = contract_address.lower()
        self.myreader = Reader(contract_address=contract_address, maxCount=maxCount, hack_tx=hack_tx)
        self.modelReader = StorageModelReader(self.myreader.storageLayout)
        self.contractName =  self.myreader.contractName 
    
    @property
    def total_transaction_count(self):
        return self.myreader.total_transaction_count
    

    def readFuncCall(self, preState, stateDiff, tx_hash, func, envs, error):
                if error:
                    return Transaction(tx_hash=tx_hash, pre_state=preState, post_state=preState, envs=envs, contract=self.contractName, func=func,  tx_type=TxType.REVERSION)

                model.GLOBAL_INNER_KEYS.clear()
                missed_data = list()
                def readEnvs():
                    results =  set()
                    for item in self.envs:
                        if item["value"] is not None:
                            if isinstance(item["value"], list):
                                results.update([ val.lower() if isinstance(val, str) and val.startswith("0x") else val for val in  item["value"] ])
                            else:
                                results.add(item["value"].lower() if isinstance(item["value"], str) and item["value"].startswith("0x") 
                                                            else item["value"])
                    return results 
                myenvs = readEnvs() 
                
                if self.contract_address.lower() in stateDiff:
                    stateenvs = self.modelReader.getModel().getFlatVarValues()
                    model.GLOBAL_INNER_KEYS = list(myenvs) + list(stateenvs)
                    if "storage" in stateDiff[self.contract_address.lower()]:    
                        for slot in stateDiff[self.contract_address.lower()]["storage"]:
                            slotchange = stateDiff[self.contract_address]["storage"][slot]
                            for mark in slotchange:
                                if mark == "+":
                                    # initialize
                                    oldVal = "0x"+"".join(["0"]*64)
                                    newVal = slotchange[mark]
                                    break 
                                elif mark == "*":
                                    oldVal = slotchange[mark]["from"]
                                    newVal = slotchange[mark]["to"]
                                    break 
                                else:
                                    assert False 

                            if not self.modelReader.read(slot, oldVal=oldVal, newVal=newVal):
                                missed_data.append((slot, oldVal, newVal)) 
                    else:
                        for slot in stateDiff[self.contract_address.lower()]:
                            newVal = stateDiff[self.contract_address][slot]
                            if not self.modelReader.read(slot, oldVal="0xcaffe", newVal=newVal):
                                missed_data.append((slot, "0xcaffe", newVal)) 
                    
                    if len(missed_data) > 0:
                        logging.debug("missing state changes in transaction#{0}".format(tx_hash))
                        simulator = Simulator(tx_hash = tx_hash)
                        simulator.loadAndexec()

                        maxTimes = 3 # recheck all the miss data twice to compute the correct variable 
                                    # mapping and update the corresponding variable
                        count = 0
                        while count < maxTimes and len(missed_data) > 0:
                            count += 1
                            for missed_slot in copy.copy(missed_data):
                                slot, oldVal, newVal = missed_slot
                                constants = simulator.query(slot)
                                model.GLOBAL_INNER_KEYS = list(constants)
                                if self.modelReader.read(slot, oldVal=oldVal, newVal=newVal):
                                    missed_data.remove(missed_slot)
                        
                        if len(missed_data) > 0:
                            logging.warning("missing {0} state changes: {1}".format(len(missed_data), missed_data))
                        else:
                            logging.warning("succeed in updating variables")
                    
                # postState = copy.deepcopy(self.modelReader.getModel())
                postState = self.modelReader.getModel()
                return Transaction(tx_hash=tx_hash, pre_state=preState, post_state=postState, envs=envs, contract=self.contractName, func=func,  tx_type=TxType.NORMAL)

    def readPerTx(self):
        assert not self.done()
        preState = copy.deepcopy(self.modelReader.getModel())
        proxy_implementation = preState.getVarValue("implementation")        
        
        offset = 0 
        isFirstTx, tx_hash, funcNames, traceAddresses, traceErrors, traceEnvs, envs, stateDiff, reverted = self.myreader.iterateTx(proxy_implementation)
        while tx_hash == "Invalid" and not self.done():
            isFirstTx, tx_hash, funcNames, traceAddresses, traceErrors, traceEnvs, envs, stateDiff, reverted = self.myreader.iterateTx(proxy_implementation)
            offset += 1
        if tx_hash == "Invalid":
            return None, None, offset, "Invalid Transaction"

        self.envs = envs 

        logging.debug("process transaction {0}".format(tx_hash))

        if reverted:
            return None, None, offset, "Reverted Transaction" 
        else:
            if isFirstTx:
                error = False
                tx = self.readFuncCall(preState=preState, stateDiff=stateDiff, tx_hash=tx_hash, func="constructor", envs = envs, error=error)
                return True, [tx], offset, "Creation Transaction"
            
            if len(funcNames) == 0:
                error = False
                tx = self.readFuncCall(preState=preState, stateDiff=stateDiff, tx_hash=tx_hash, func="", envs = envs, error=error)
                return False, [tx], offset, "Unnamed Function Calls" 
            elif len(funcNames) == 1:
                error = traceErrors[0]
              
                tx = self.readFuncCall(preState=preState, stateDiff=stateDiff, tx_hash=tx_hash, func=funcNames[0], envs = traceEnvs[0], error=error)
                return False, [tx], offset, "Single Function Call" 
            else:
                simulator = Simulator2(tx_hash=tx_hash, address=self.contract_address)
                simulator.loadAndexec()
                calls = simulator.query_contract_calls()
                transactions: list[Transaction] = [] 
                for call in calls:
                    if traceAddresses.count(call.traceAddress) == 0:
                        # raise Exception(f" contract call with address '{call.traceAddress}' not found in simulator traces: {traceAddresses}")
                        continue
                    loc = traceAddresses.index(call.traceAddress) 
                    error = traceErrors[loc]
                    func = funcNames[loc]
                    stateDiff = call.sstore_result

                    tx = self.readFuncCall(preState=preState, stateDiff=stateDiff, tx_hash=tx_hash, func=func, envs = traceEnvs[loc], error=error)
                    preState = copy.deepcopy(tx.post_state)
                    transactions.append(tx)
                return False, transactions, offset, "Multiple Function Calls"

        
    def done(self):
        return self.myreader.done()
    
    def toStateJson(self, json_file):
        json.dump(asdict(self.modelReader.getModel()), open(json_file, "w"), indent=4)    
    
    def getABISpec(self):
        return self.myreader.abi
    
    def getDeclModel(self):
        return self.modelReader.getModel()


if __name__ == "__main__":
    TokenAddress = "0x1dac5649e2a0c943ffc4211d708f6ddde4742fd6"
    txreplayer = TransactionReplayer(contract_address=TokenAddress)
    while not txreplayer.done():
        firstOrMultiple, txObject = txreplayer.readPerTx()
        if not firstOrMultiple:
            print(txObject.tx_hash, txObject.func, txObject.tx_type)
    txreplayer.toStateJson(txreplayer.contractName+".json")

