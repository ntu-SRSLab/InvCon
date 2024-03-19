import copy
from invconplus.plugin.Provider import Provider
from invconplus.plugin.SourcecodeProvider import SourcecodeProvider 
from invconplus.plugin.StateDiffProvider import StateDiffProvider 
from invconplus.plugin.TransactionProvider import TransactionProvider 
from typing import Dict, Any 
import logging
import os 
import json 
from alive_progress import alive_bar 
from invconplus.const import ENABLE_CACHE

CONTRACT_ADDRESS = "contract_address"
class BlockchainDataProvider(Provider):
    def __init__(self, params: Dict, maxCount, hack_tx) -> None:
        super().__init__(params)
        self.maxCount = maxCount
        self.hack_tx = hack_tx
    
    def _read(self, export_file):

        if os.path.exists(export_file) and ENABLE_CACHE:
            result = json.load(open(export_file))
            transactions = result["transactions"]
            contractName = result["contractName"]
            storageLayout =  result["storageLayout"]
            cached_record_number = result["cached_record_number"]
            if len(storageLayout) == 0 or "constants" not in result:
                storageLayout = dict()
                scProvider = SourcecodeProvider(self.params)
                try:
                    _, storageLayout, _, constants = scProvider.read()
                    result["storageLayout"] = storageLayout
                    result["constants"] = constants
                    json.dump(result, open(os.path.join(export_file), "w"), indent=4)
                except:
                    logging.error("storage layout is empty or constants is not found")
                    exit(-1)
            
            abi = result["abi"]
            constants = result["constants"]

            
            txProvider = TransactionProvider(self.params, self.maxCount, self.hack_tx, transactions)
            transactions = txProvider.read()

            result["cached_record_number"] = len(transactions)

            logging.warning("fetching state diff for {0} transactions".format(len(transactions)))
            with alive_bar(len(transactions)) as bar:
                    # recheck state diff data which is critical for the results
                    for i in range(len(transactions)):
                        while "stateDiff" not in transactions[i][0] or len(transactions[i][0]["stateDiff"]) == 0:
                            tx_hash = transactions[i][0]["transactionHash"]
                            logging.warning(tx_hash + " stateDiff fetch")
                            params = dict(tx_hash=tx_hash)
                            sdProvider = StateDiffProvider(params=params)
                            stateDiff = sdProvider.read()
                            transactions[i][0]["stateDiff"] =  stateDiff
                        bar()
             
            result["transactions"] = transactions
            json.dump(result, open(os.path.join(export_file), "w"), indent=4)
            if len(result["transactions"]) >= self.maxCount and self.hack_tx is None:
                return contractName, storageLayout, abi, constants, transactions[:self.maxCount]
            else:
                return contractName, storageLayout, abi, constants, transactions
            
        else:
            scProvider =  SourcecodeProvider(self.params)
            storageLayoutFlag = True
         
            contractName, storageLayout, abi, constants = scProvider.read()

            assert contractName is not None and storageLayout is not None and abi is not None 
            
            txProvider = TransactionProvider(self.params, self.maxCount, self.hack_tx)
            transactions = txProvider.read()
            cached_record_number = len(transactions)

            logging.warning("fetching state diff for {0} transactions".format(len(transactions)))
            with alive_bar(len(transactions)) as bar:
                for transaction in copy.copy(transactions):
                    if len(transaction) != 0 and "transactionHash" in transaction[0]:
                        tx_hash = transaction[0]["transactionHash"]
                        params = dict(tx_hash=tx_hash)
                        sdProvider = StateDiffProvider(params=params)
                        stateDiff = sdProvider.read()
                        transaction[0]["stateDiff"] =  stateDiff
                    else:
                        transactions.remove(transaction)
                    bar()
            if storageLayoutFlag:
                json.dump(dict(contractName = contractName, storageLayout = storageLayout, abi=abi, constants = constants, cached_record_number = cached_record_number, transactions = transactions),
                open(os.path.join(export_file), "w"), indent=4)        
            else:
                json.dump(dict(contractName = contractName, storageLayout = dict(), abi=abi, constants = constants, cached_record_number = cached_record_number,  transactions = transactions),
                open(os.path.join(export_file), "w"), indent=4)        

            return contractName, storageLayout, abi, constants, transactions

    # @input, read a contract blockchain address
    # @output, produce a dictionary consisting of source code (including abi, storage layout), transactions, state changes 
    def read(self, export_dir = "./tmp/"):
        logging.debug(self.params[CONTRACT_ADDRESS])
        export_file = os.path.join(export_dir, self.params[CONTRACT_ADDRESS] +".json")

        return self._read(export_file=export_file)
    
if __name__ == "__main__":
    params = dict()
    params[CONTRACT_ADDRESS] = "0x1dac5649e2a0c943ffc4211d708f6ddde4742fd6"
    bdProvider = BlockchainDataProvider(params=params)
    bdProvider.read()
