import web3 
from web3 import Web3
import json 
from multiprocessing import Pool
from web3_input_decoder import decode_constructor

my_provider = Web3.HTTPProvider("https://eth.llamarpc.com")
w3 = web3.Web3(my_provider)

def my_decode_constructor(contract_abi, tx_input, bytecode):
    result = decode_constructor(abi=contract_abi, tx_input=tx_input, bytecode=bytecode)
    result_dict = dict()
    for item in result:
       variable = item[1]
       value = item[2]
       result_dict[variable] = value 
    return result_dict

def decodeFunctionInput(address, abi, tx_input):
    contract = w3.eth.contract(address=Web3.to_checksum_address(address), abi=abi)
    result = contract.decode_function_input(tx_input)
    funcName = result[0].fn_name
    inputs =  result[1]
    decoded_input = dict(name=funcName, inputs = inputs)
    return decoded_input

def decode_all(address):
    contractobject = json.load(open("./tmp/"+address+".json"))
    abi = contractobject["abi"]
    transactions = contractobject["transactions"]
    for transaction in transactions[1:]:
        call = transaction[0]
        if address.lower() != call["action"]["to"].lower():
            continue
        articulatedTrace = call["articulatedTrace"] if "articulatedTrace" in call else None
        if articulatedTrace is not None:
            inputs = articulatedTrace["inputs"] if "inputs" in articulatedTrace else {}
        if "input" not in call["action"]:
            continue
        call_input = call["action"]["input"]
        try:
            result = decodeFunctionInput(address=address, abi=abi, tx_input=call_input)
        except:
            continue
        my_inputs = result["inputs"]
        for variable in my_inputs:
                if isinstance(my_inputs[variable], bytes):
                    my_inputs[variable] = "0x"+my_inputs[variable].hex()
                elif isinstance(my_inputs[variable], list):
                    my_inputs[variable] = ["0x"+item.hex() if isinstance(item, bytes) else item for item in my_inputs[variable] ]
        result["inputs"] = my_inputs
        call["articulatedTrace"] = result
    contractobject["transactions"] = transactions
    return contractobject

if __name__ == "__main__":
    # address = "0x1dac5649e2a0c943ffc4211d708f6ddde4742fd6"
    # contractobject = json.load(open("./tmp/"+address+".json"))
    # abi = contractobject["abi"]
    # tx_input = "0x211e28b60000000000000000000000000000000000000000000000000000000000000000"
    # decodeFunctionInput(address=address, abi=abi, tx_input=tx_input)
    addresses = "0xC95D227a1CF92b6FD156265AA8A3cA7c7DE0F28e 0xbf8b9092e809de87932b28ffaa00d520b04359aa 0x3e07881993c7542a6da9025550b54331474b21dd 0xeb6f4ec38a347110941e86e691c2ca03e271df3b 0x9919d97e50397b7483e9ea61e027e4c4419c8171 0xaec1f783b29aab2727d7c374aa55483fe299fefa 0xa867bF8447eC6f614EA996057e3D769b76a8aa0e".split(" ")
    addresses = ["0x41a322b28d0ff354040e2cbc676f0320d8c8850d"]
    for address in addresses:
        print(address)
        contractobject = decode_all(address=address)
        json.dump(contractobject, open("./tmp/"+address+".clean.json", "w"), indent=4)
