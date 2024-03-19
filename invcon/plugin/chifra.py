#!/usr/bin/env python

import logging
import subprocess
import sys
import pprint
import json
from time import sleep
from .src import chifra
from alive_progress import alive_bar 
import math
import argparse

def test():
    sys.argv = sys.argv[1:]
    obj = chifra().dispatch()
    pprint.pprint(obj)

def run():
    return chifra().dispatch()

def fetchBatchTransaction(tx_ids: list):
    global sys 
    cmds =  ["chifra",  "traces"]
    for tx_hash in tx_ids:
        cmds.append("{0}".format(tx_hash))
    cmds.extend(["--fmt", "json"])
    while True:
        p =  subprocess.Popen(cmds, stdout=subprocess.PIPE)
        out, err = p.communicate()
        if err:
            logging.error(err)
            assert False
        if out.decode() == "":
            print(cmds)
            sleep(5)
            continue
        try:
            result =  json.loads(out.decode())
            break
        except:
            continue

    # sys.argv =  cmds 
    # result = run()
    # while result is None or "data" not in result or len(result["data"]) == 0:
    #     result = run()
    #     sleep(1)
    new_results = list()
    for tx_id in tx_ids:
        new_result = list()
        for tx in result["data"]:
            if int(tx["transactionIndex"]) == int(tx_id.split(".")[1]) and int(tx["blockNumber"]) == int(tx_id.split(".")[0]):
                new_result.append(tx)
        new_results.append(new_result)
    return new_results

def fetchTransaction(block, txid):
    global sys 
    cmds =  ["chifra", "traces", "{0}.{1}".format(block, txid)]
    cmds.extend(["--fmt", "json"])
    while True :
        p =  subprocess.Popen(cmds, stdout=subprocess.PIPE)
        out, err = p.communicate()
        if err:
            logging.error(err)
            assert False
        if out.decode() == "":
            sleep(1)
            continue
        result =  json.loads(out.decode())
        break 

    # cmds =  ["chifra", "traces", "{0}.{1}".format(block, txid), "-o", "-a"]
    # sys.argv =  cmds
    # result = run()
    # while result is None or "data" not in result or len(result["data"]) == 0:
    #     result = run()

    return result["data"]

def fetchTransactionByHash(txhash):
    global sys 
    cmds =  ["chifra", "transactions", "{0}".format(txhash)]
    cmds.extend(["--fmt", "json"])
    while True :
        p =  subprocess.Popen(cmds, stdout=subprocess.PIPE)
        out, err = p.communicate()
        if err:
            logging.error(err)
            assert False
        if out.decode() == "":
            sleep(1)
            continue
        result =  json.loads(out.decode())
        break 
    return result["data"]

def fetchTransactionsForAccount(address, maxCount=10000, hack_tx = None,  cached_transactions=[]):
    global sys 
    maxBlockNumber = None 
    if hack_tx is not None:
        assert hack_tx.startswith("0x"), f"{hack_tx} does not start with 0x"
        transaction = fetchTransactionByHash(hack_tx)
        # print(transaction)
        maxBlockNumber = transaction[0]["blockNumber"]

    transactions: list = cached_transactions
    if maxBlockNumber is None:
        p = subprocess.Popen(["chifra", "list", address, "--fmt", "json", "-e", str(maxCount)], stdout=subprocess.PIPE)
        out, err = p.communicate()
        if err:
            logging.error(err)
            assert False
        result =  json.loads(out.decode())
        batch_size = 25
        result = list(result["data"])
    else:
        p = subprocess.Popen(["chifra", "list", address, "--fmt", "json", "-L", str(maxBlockNumber)], stdout=subprocess.PIPE)
        out, err = p.communicate()
        if err:
            logging.error(err)
            assert False
        result =  json.loads(out.decode())
        batch_size = 25
        result = list(result["data"])
        maxCount = len(result)
    logging.warning(address + " has transactions no less than "+ str(len(result)))
    logging.warning("size of transactions to analyze:"+str(min(maxCount, len(result))))
    with alive_bar(min(maxCount, len(result))) as bar:
        tx_ids = list()
        for i in range(0, min(maxCount, len(result))):
            tx = result[i]
            block_id = tx["blockNumber"]
            transaction_index = tx["transactionIndex"]
            if i < len(transactions):
                cached_tx = transactions[i]
                cached_block_id = cached_tx[0]["blockNumber"]
                cached_tx_index = cached_tx[0]["transactionIndex"]
                if block_id == cached_block_id and transaction_index == cached_tx_index:
                    pass 
                else:
                    tx_ids.append(str(block_id)+"."+str(transaction_index))
                    _results = fetchBatchTransaction(tx_ids=tx_ids)
                    for j in range(len(tx_ids)):
                        while len(_results[j]) == 0:
                            logging.warning("empty transaction output, retry...")
                            _results[j] = fetchBatchTransaction(tx_ids=[tx_ids[j]])[0]
                        transactions.insert(i+j, _results[j])
                    tx_ids = list()
            else:
                tx_ids.append(str(block_id)+"."+str(transaction_index))
                if len(tx_ids) == batch_size or i == min(maxCount, len(result))-1:
                    _results = fetchBatchTransaction(tx_ids=tx_ids)
                    for j in range(len(tx_ids)):
                        while len(_results[j]) == 0:
                            logging.warning("empty transaction output, retry...")
                            _results[j] = fetchBatchTransaction(tx_ids=[tx_ids[j]])[0]
                        transactions.append(_results[j])
                    tx_ids = list()
            bar()
    return transactions 

def fetchTransactionsCountForAccount(address, maxCount=100000, cached_record_number=0):
    global sys 
    transactions = list()
    p = subprocess.Popen(["chifra", "list", address, "--fmt", "json", "-c", str(cached_record_number+1), "-e", str(maxCount)], stdout=subprocess.PIPE)
    out, err = p.communicate()
    if err:
        logging.error(err)
        assert False
    result =  json.loads(out.decode())
    result = list(result["data"])
    if len(result) < maxCount:
        logging.warning(address + " has transactions number "+ str(len(result)))
    else:
        logging.warning(address + " has more than transactions number "+ str(len(result)))
   

def test():
    TokenAddress = "0x000ae26329aa0c57b9badbdee2996624272905e9"
    fetchTransactionsCountForAccount(address=TokenAddress)

    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--address", help="address to fetch transactions")
    args  = parser.parse_args()
    if args.address is None:
        print("please specify address")
        exit(1)
    address = args.address
    fetchTransactionsCountForAccount(address=address)
  

    