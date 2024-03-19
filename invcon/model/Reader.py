from typing import Dict, List, Union
import logging 
from invconplus.model.model import *
from ..plugin.BlockchainDataProvider import BlockchainDataProvider 
from .web3util import decodeFunctionInput
class Reader:
    contract_address: str 
    contractName: str 
    storageLayout: Dict 
    abi: List 
    transactions: List
    txCursor: int 
    def __init__(self, contract_address, maxCount, hack_tx) -> None:
        self.contract_address = contract_address 
        bdProvider = BlockchainDataProvider(params = dict(contract_address=contract_address), maxCount=maxCount, hack_tx=hack_tx)
        self.contractName, self.storageLayout, self.abi, self.constants, self.transactions = bdProvider.read()
        self.txCursor = 0 
    
    @property
    def total_transaction_count(self):
        return len(self.transactions)

    # @output, the environments of the parameter values, including block and transaction parameters
    def iterateTx(self, proxy_implementation):
        funcNames = list()
        traceAddresses = list()
        traceErrors = list()
        traceEnvs = list()
        envs = list()
        reverted = "error" in self.transactions[self.txCursor][0] and self.transactions[self.txCursor][0]["error"]!="" and self.transactions[self.txCursor][0]["error"]!="0"
        stateDiff =  self.transactions[self.txCursor][0]["stateDiff"]
        tx_hash = self.transactions[self.txCursor][0]["transactionHash"]
        # there could be multiple traces per transaction
        # the interesting trace(s) are the ones that the field `to` of `action` equals to the contract address
        # and the contract type is either `create` (maybe `create2`) or `call`
        foundAction = False
        for i in range(len(self.transactions[self.txCursor])):
                trace = self.transactions[self.txCursor][i]
                # this is a transaction that contains contract creation call 
                if "from" in trace["action"] and trace["action"]["from"].lower()!="0x0" \
                    and (trace["action"]["to"].lower() == self.contract_address.lower() \
                          or trace["action"]["to"].lower() == "0x0") \
                    and trace["type"] in ["create", "create2", "call"]:
                    _envs = list()
                    
                    
                    _envs.append(dict(name ="block.number", value = trace["blockNumber"]))
                    _envs.append(dict(name ="tx.hash", value = trace["transactionHash"]))
                    _envs.append(dict(name ="block.timestamp", value = trace["timestamp"]))
                    _envs.append(dict(name ="msg.sender", value = trace["action"]["from"]))
                    _envs.append(dict(name ="msg.gas", value = trace["action"]["gas"] if "gas" in trace["action"] else 0))
                    _envs.append(dict(name ="msg.value", value = trace["action"]["value"]))

                    envs.extend(_envs)

                    foundAction = True
                    try:
                        if "input" in trace["action"] and  trace["action"]["input"]!="" and trace["action"]["input"]!="0x":
                            try:
                                result = decodeFunctionInput(address=trace["action"]["to"], abi = self.abi, tx_input=trace["action"]["input"])
                                funcName =  result["name"]
                                inputs = result["inputs"]
                                self.transactions[self.txCursor][i]["articulatedTrace"] = result
                                fullName = self._findFullFuncName(funcName, inputs.keys())
                                funcNames.append(fullName)
                                for variable in inputs:
                                    if isinstance(inputs[variable], bytes):
                                        inputs[variable] = "0x"+inputs[variable].hex()
                                    elif isinstance(inputs[variable], list):
                                        inputs[variable] = ["0x"+item.hex() if isinstance(item, bytes) else item for item in inputs[variable] ]
                                    _envs.append(dict(name =variable, value = inputs[variable]))
                                    envs.append(dict(name =variable, value = inputs[variable]))
                            except:
                                if proxy_implementation is None:
                                    raise Exception("Could not find any function with matching selector")
                                else:
                                    proxy_implementation_reader = Reader(contract_address=proxy_implementation, maxCount=0)
                                    result = decodeFunctionInput(address=proxy_implementation, abi = proxy_implementation_reader.abi, tx_input=trace["action"]["input"])
                                    funcName =  result["name"]
                                    inputs = result["inputs"]
                                    self.transactions[self.txCursor][i]["articulatedTrace"] = result
                                    fullName = proxy_implementation_reader._findFullFuncName(funcName, inputs.keys())
                                    funcNames.append(fullName)
                                    for variable in inputs:
                                        if isinstance(inputs[variable], bytes):
                                            inputs[variable] = "0x"+inputs[variable].hex()
                                        elif isinstance(inputs[variable], list):
                                            inputs[variable] = ["0x"+item.hex() if isinstance(item, bytes) else item for item in inputs[variable] ]
                                        _envs.append(dict(name =variable, value = inputs[variable]))
                                        envs.append(dict(name =variable, value = inputs[variable]))
                            traceAddress = trace["traceAddress"] 
                            if traceAddress is None:
                                traceAddress = []
                            else:
                                if isinstance(traceAddress, str):
                                    traceAddress = traceAddress.split("-")
                                else:
                                    traceAddress = list(map(str, traceAddress))
                            traceAddresses.append(traceAddress)
                            if "error" in trace:
                                traceErrors.append(trace["error"] in ["", "0"])
                            else:
                                traceErrors.append(False)

                           
                            
                            traceEnvs.append(_envs)
                        else:
                            pass 
                    except:
                        pass 
        if len(self.constants) > 0:
            envs.extend(self.constants)      

        if not foundAction:  
            self.txCursor += 1
            return None, "Invalid", None, None, None, None, None, None, None
        else:           
            self.txCursor += 1
            isFirstTx = self.txCursor == 1
            return isFirstTx, tx_hash, funcNames, traceAddresses, traceErrors, traceEnvs, envs, stateDiff, reverted 
    
    def done(self):
        return self.txCursor>=len(self.transactions)
    
    def _findFullFuncName(self, shortFuncName, variables):
        matched_func = None
        for func in self.abi:
            if "name" in func and func["name"] ==  shortFuncName:
                if len(variables)!=len(func["inputs"]):
                    continue 
                matched = True 
                for input in func["inputs"]:
                    if input["name"] not in variables:
                        matched = False 
                if matched:
                    matched_func = func 
                    break 
        if matched_func is None:
            return None 
        fullfuncName = matched_func["name"]+ "("+",".join([ item["name"] if item["name"]!="" else item["type"] for item in matched_func["inputs"]]) + ")"
        return fullfuncName
                
        

class StorageModelReader:
    def __init__(self, storageLayout) -> None:
        self.model = createDataModel(storageLayout)

    def getModel(self):
        return self.model 
    
    def read(self, slot: Union[str, int], oldVal, newVal):
        if isinstance(slot, str) and slot.startswith("0x"):
            slot = int(slot[2:], base=16)
        if not self.model.setValue(slot, newVal):
            logging.log(logging.DEBUG, "missing (slot: {0}, value: {1})".format(hex(slot), newVal))
            return False 
        return True