#!/bin/bash

# addresses=$(ls ../Experiment/FinalReportERC20/booksum)
# for address in ${addresses[@]};
# do 
#     echo "python3 -m invconplus.main --address" $address
#     python3 -m invconplus.main --address $address >> batch.log 2>&1 
# done 

# addresses=$(ls ~/Projects/SpecCon-Tool/crawlerpy/query-result/)
# for address in ${addresses[@]};
# do 
#     echo "python3 -m invconplus.main --address" $address
#     python3 -m invconplus.main --address $address >> batch.log 2>&1 
# done 

# ERC 20 
# Token List 

# addresses=(0xdAC17F958D2ee523a2206206994597C13D831ec7 0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48 0x6B175474E89094C44Da98b954EedeAC495271d0F 0x1f9840a85d5aF5bf1D1762F925BDADdC4201F984 0x6090A6e47849629b7245Dfa1Ca21D94cd15878Ef 0x06012c8cf97bead5deae237070f9587f8e7a266d 0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d)
# # addresses=(0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48 0x6B175474E89094C44Da98b954EedeAC495271d0F 0x1f9840a85d5aF5bf1D1762F925BDADdC4201F984 0x6090A6e47849629b7245Dfa1Ca21D94cd15878Ef 0x06012c8cf97bead5deae237070f9587f8e7a266d 0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d)
# for address in ${addresses[@]};
# do 
#     echo "python3 -m invconplus.main --address" $address
#     python3 -m invconplus.main --address $address >> batch.log 2>&1 
# done 

missed_address=(0x1f9840a85d5aF5bf1D1762F925BDADdC4201F984 0x6090A6e47849629b7245Dfa1Ca21D94cd15878Ef 0x41a322b28d0ff354040e2cbc676f0320d8c8850d 0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d 0xdAC17F958D2ee523a2206206994597C13D831ec7)

for address in ${missed_address[@]};
do 
    echo "python3 -m invconplus.main --address" $address
    python3 -m invconplus.main --address $address --maxCount 50 >> batch.log 2>&1 
done 