# InvCon+: Automated Invariant Generation for Solidity Smart Contracts 
---
The latest version of this repository can be found at [NTU-SRSLab](git@github.com:ntu-SRSLab/InvCon.git).

InvCon+ is a dynamic invariant detector for Solidity smart contracts and it also integrate with a modular verifier VeriSol to produce correct invariants.

## Prerequisites
+ Mac, Linux (tested on Ubuntu 20.04 LTS)
+ Python3 (tested on 3.10) 
+ [TrueBlocks](https://trueblocks.io/docs/). Indexing for EVM-based blockchains. 
TrueBlocks runs on Linux and Mac and do not support Windows. Please follow its detailed installation instructions from [https://trueblocks.io/docs/install/install-core/](https://trueblocks.io/docs/install/install-core/). 
When ``chifra`` command is installed and properly configured. Please run ``chifra init -a`` to cache all blockchain indexing dataset, where the storage use is estimated to be 60GB-80GB.
+ QuickNode API key. (Currently provide a one and will delete it later)
+ Etherscan API key. (Currently has hardcode it and will delete it later)

## Get Started
Clone this repository, install all the python libraries and test on a given examples whose transaction data has been cached.
```sh 
# clone this repository
git clone git@github.com:ntu-SRSLab/InvCon.git
cd InvCon
# install python dependencies
pip3 install -r requirements.txt
# test it on a given example whose data has been cached
bash scripts/batch.sh # or python3 -m invconplus.main --address 0x7e0178e1720e8b3a52086a23187947f35b6f3fc4
```

Time estimation: 2 minutes (on modern hardware with good network condition)

If successful, at the end of the command line output should look similar to the following:
```sh
11:07:41 [WARNING] 0x7e0178e1720e8b3a52086a23187947f35b6f3fc4
11:07:41 [WARNING] cached record number 2893
11:07:45 [WARNING] 0x7e0178e1720e8b3a52086a23187947f35b6f3fc4 has transactions no less than 500
11:07:45 [WARNING] size of transactions to analyze:500
|████████████████████████████████████████| 500/500 [100%] in 0.0s (238268.69/s) 
11:07:46 [WARNING] fetching state diff for 2893 transactions
|████████████████████████████████████████| 2893/2893 [100%] in 0.0s (157236.42/s) 

...

ori(Sum(userGameId[...])) >= ori(Sum(pendingReturns[...]))
ori(Sum(userGameId[...])) <= Sum(userGameId[...])
ori(Sum(userGameId[...])) >= Sum(pendingReturns[...])
ori(Sum(pendingReturns[...])) <= Sum(userGameId[...])
ori(Sum(pendingReturns[...])) == Sum(pendingReturns[...])
ori(Sum(pendingReturns[...])) >= Sum(pendingReturns[...])
ori(Sum(pendingReturns[...])) <= Sum(pendingReturns[...])
Sum(userGameId[...]) >= Sum(pendingReturns[...])
```

## Advanced Usage

Other than dynamic invariant detection, InvCon also includes a module to facilitate formal verification on the invariant results.
To use this formal verification procedure 

