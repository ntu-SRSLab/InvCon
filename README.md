# InvCon+: Automated Invariant Generation for Solidity Smart Contracts 
---
The latest version of this repository can be found at [NTU-SRSLab](git@github.com:ntu-SRSLab/InvCon.git).

InvCon+ is a dynamic invariant detector for Solidity smart contracts and it also integrate with a modular verifier VeriSol to produce correct invariants.

## Prerequisites
+ Mac, Linux (tested on Ubuntu 20.04 LTS)
+ Python3 (tested on 3.11) 
+ [TrueBlocks](https://trueblocks.io/docs/). Indexing for EVM-based blockchains. 
TrueBlocks runs on Linux and Mac and do not support Windows. Please follow its detailed installation instructions from [https://trueblocks.io/docs/install/install-core/](https://trueblocks.io/docs/install/install-core/). 
When ``chifra`` command is installed and properly configured. Please run ``chifra init –all`` to cache all blockchain indexing dataset, where the storage use is estimated to be 60GB-80GB.
+ QuickNode API key.
+ Etherscan API key.

## Get Started
Clone this repository, install all the python libraries and test on a given examples whose transaction data has been cached.
```sh 
# clone this repository
git clone git@github.com:ntu-SRSLab/InvCon.git
cd InvCon
# install python dependencies
pip3 install -r requirements.txt
# test it on a given example whose data has been cached
python3 -m  invcon.main --address {0xxxx}
```

Time estimation: xx-xx minutes (on modern hardware with good network condition)

If successful, at the end of the command line output should look similar to the following:
```sh
```

## Advanced Usage

Other than dynamic invariant detection, InvCon also includes a module to facilitate formal verification on the invariant results.
To use this formal verification procedure 

