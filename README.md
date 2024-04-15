# InvCon+: Automated Invariant Generation for Solidity Smart Contracts 
---
The latest version of this repository can be found at [NTU-SRSLab](git@github.com:ntu-SRSLab/InvCon.git).

InvCon+ is a dynamic invariant detector for Solidity smart contracts and it also integrate with a modular verifier VeriSol to produce correct invariants.

## Prerequisites
+ Mac, Linux (tested on Ubuntu 20.04 LTS)
+ Python3 (tested on 3.10) 
+ [TrueBlocks](https://trueblocks.io/docs/). Indexing for EVM-based blockchains. 
TrueBlocks runs on Linux and Mac and do not support Windows. Please follow its detailed installation instructions from [https://trueblocks.io/docs/install/install-core/](https://trueblocks.io/docs/install/install-core/). 
When ``chifra`` command is installed and properly configured. Please run ``chifra init --all`` to cache all blockchain indexing dataset, where the storage use is estimated to be 60GB-80GB.
+ [Anaconda](https://docs.anaconda.com/free/anaconda/install/index.html). Managing python environments for different versions of python. 
+ QuickNode API key. (Currently provide a one and will delete it later)
+ Etherscan API key. (Currently has hardcode it and will delete it later)

## Get Started
Clone this repository.
```sh 
# clone this repository
git clone git@github.com:ntu-SRSLab/InvCon.git
# Change to the invcon dir
cd InvCon
```

Create a new anaconda environment with python 3.10 and activate the environment.
```sh
conda create -n invcon+ python=3.10
conda activate invcon+
```

Install the required python dependencies.
```sh
# install python dependencies
pip3 install -r requirements.txt
# test it on a given example whose data has been cached
bash scripts/batch.sh # or python3 -m invconplus.main --address 0x0148650ef8e216e8d0999fe8d4b5c1871b71771a
```

Time estimation: 2 minutes (on modern hardware with good network condition)

If successful, at the end of the command line output should look similar to the following:
```sh
python3 -m invconplus.main --address 0x0148650ef8e216e8d0999fe8d4b5c1871b71771a
16:26:35 [WARNING] 0x0148650ef8e216e8d0999fe8d4b5c1871b71771a
16:26:35 [WARNING] cached record number 11
16:26:38 [WARNING] 0x0148650ef8e216e8d0999fe8d4b5c1871b71771a has transactions no less than 11
16:26:38 [WARNING] size of transactions to analyze:11
|████████████████████████████████████████| 11/11 [100%] in 0.0s (55627.05/s) 
16:26:38 [WARNING] fetching state diff for 11 transactions
|████████████████████████████████████████| 11/11 [100%] in 0.0s (102037.24/s) 
16:26:39 [INFO] &apos;solc --standard-json running
main contract:  TokenERC20
tokenRecipient
TokenERC20
16:26:39 [WARNING] createInitialPptsForFunction for approve(_spender,_value)
16:26:39 [WARNING] createInitialPptsForFunction for transferFrom(_from,_to,_value)
16:26:39 [WARNING] createInitialPptsForFunction for burn(_value)
16:26:39 [WARNING] createInitialPptsForFunction for burnFrom(_from,_value)
16:26:39 [WARNING] createInitialPptsForFunction for transfer(_to,_value)
16:26:39 [WARNING] createInitialPptsForFunction for approveAndCall(_spender,_value,_extraData)
16:26:39 [WARNING] createInitialPptsForContract...
**********

burnFrom(_from,_value)
{VarInfo(name=&apos;totalSupply&apos;, type=&lt;slither.core.solidity_types.elementary_type.ElementaryType object at 0x7c6d7d652770&gt;, vartype=&lt;VarType.STATEVAR: 0&gt;, derivation=None), VarInfo(name=&apos;_value&apos;, type=&lt;slither.core.solidity_types.elementary_type.ElementaryType object at 0x7c6d7d652170&gt;, vartype=&lt;VarType.TXVAR: 1&gt;, derivation=None), VarInfo(name=&apos;allowance[_from][msg.sender]&apos;, type=&apos;uint256&apos;, vartype=&lt;VarType.STATEVAR: 0&gt;, derivation=&lt;invconplus.derivation.binary.MappingItem.MappingItem object at 0x7c6d7cc42bf0&gt;), VarInfo(name=&apos;balanceOf[_from]&apos;, type=&apos;uint256&apos;, vartype=&lt;VarType.STATEVAR: 0&gt;, derivation=&lt;invconplus.derivation.binary.MappingItem.MappingItem object at 0x7c6d7cc42530&gt;)}
[]
**********

burn(_value)
{VarInfo(name=&apos;totalSupply&apos;, type=&lt;slither.core.solidity_types.elementary_type.ElementaryType object at 0x7c6d7d652770&gt;, vartype=&lt;VarType.STATEVAR: 0&gt;, derivation=None), VarInfo(name=&apos;_value&apos;, type=&lt;slither.core.solidity_types.elementary_type.ElementaryType object at 0x7c6d7d651db0&gt;, vartype=&lt;VarType.TXVAR: 1&gt;, derivation=None), VarInfo(name=&apos;balanceOf[msg.sender]&apos;, type=&apos;uint256&apos;, vartype=&lt;VarType.STATEVAR: 0&gt;, derivation=&lt;invconplus.derivation.binary.MappingItem.MappingItem object at 0x7c6d7cc42ec0&gt;)}
[]
**********

TokenERC20(initialSupply,tokenName,tokenSymbol)
{VarInfo(name=&apos;decimals&apos;, type=&lt;slither.core.solidity_types.elementary_type.ElementaryType object at 0x7c6d7d652530&gt;, vartype=&lt;VarType.STATEVAR: 0&gt;, derivation=None), VarInfo(name=&apos;name&apos;, type=&lt;slither.core.solidity_types.elementary_type.ElementaryType object at 0x7c6d7d61c880&gt;, vartype=&lt;VarType.STATEVAR: 0&gt;, derivation=None), VarInfo(name=&apos;symbol&apos;, type=&lt;slither.core.solidity_types.elementary_type.ElementaryType object at 0x7c6d7d652440&gt;, vartype=&lt;VarType.STATEVAR: 0&gt;, derivation=None), VarInfo(name=&apos;balanceOf[msg.sender]&apos;, type=&apos;uint256&apos;, vartype=&lt;VarType.STATEVAR: 0&gt;, derivation=&lt;invconplus.derivation.binary.MappingItem.MappingItem object at 0x7c6d7cc43880&gt;), VarInfo(name=&apos;tokenName&apos;, type=&lt;slither.core.solidity_types.elementary_type.ElementaryType object at 0x7c6d7d61fdf0&gt;, vartype=&lt;VarType.TXVAR: 1&gt;, derivation=None), VarInfo(name=&apos;initialSupply&apos;, type=&lt;slither.core.solidity_types.elementary_type.ElementaryType object at 0x7c6d7d61c520&gt;, vartype=&lt;VarType.TXVAR: 1&gt;, derivation=None), VarInfo(name=&apos;tokenSymbol&apos;, type=&lt;slither.core.solidity_types.elementary_type.ElementaryType object at 0x7c6d7d61feb0&gt;, vartype=&lt;VarType.TXVAR: 1&gt;, derivation=None), VarInfo(name=&apos;totalSupply&apos;, type=&lt;slither.core.solidity_types.elementary_type.ElementaryType object at 0x7c6d7d652770&gt;, vartype=&lt;VarType.STATEVAR: 0&gt;, derivation=None)}
[]
**********

transferFrom(_from,_to,_value)
{VarInfo(name=&apos;_value&apos;, type=&lt;slither.core.solidity_types.elementary_type.ElementaryType object at 0x7c6d7d6510c0&gt;, vartype=&lt;VarType.TXVAR: 1&gt;, derivation=None), VarInfo(name=&apos;allowance[_from][msg.sender]&apos;, type=&apos;uint256&apos;, vartype=&lt;VarType.STATEVAR: 0&gt;, derivation=&lt;invconplus.derivation.binary.MappingItem.MappingItem object at 0x7c6d7cc43820&gt;)}
[]
**********

approveAndCall(_spender,_value,_extraData)
{VarInfo(name=&apos;_spender&apos;, type=&lt;slither.core.solidity_types.elementary_type.ElementaryType object at 0x7c6d7d651720&gt;, vartype=&lt;VarType.TXVAR: 1&gt;, derivation=None), VarInfo(name=&apos;spender&apos;, type=&lt;slither.core.solidity_types.user_defined_type.UserDefinedType object at 0x7c6d7cdc08b0&gt;, vartype=&lt;VarType.LOCALVAR: 2&gt;, derivation=None)}
[]
**********

transfer(_to,_value)
set()
[]
**********

approve(_spender,_value)
{VarInfo(name=&apos;_value&apos;, type=&lt;slither.core.solidity_types.elementary_type.ElementaryType object at 0x7c6d7d650580&gt;, vartype=&lt;VarType.TXVAR: 1&gt;, derivation=None), VarInfo(name=&apos;allowance[msg.sender][_spender]&apos;, type=&apos;uint256&apos;, vartype=&lt;VarType.STATEVAR: 0&gt;, derivation=&lt;invconplus.derivation.binary.MappingItem.MappingItem object at 0x7c6d7cc9d1b0&gt;)}
[]
**********

_transfer(_from,_to,_value)
{VarInfo(name=&apos;previousBalances&apos;, type=&lt;slither.core.solidity_types.elementary_type.ElementaryType object at 0x7c6d7d6f0640&gt;, vartype=&lt;VarType.LOCALVAR: 2&gt;, derivation=None), VarInfo(name=&apos;balanceOf[_from]&apos;, type=&apos;uint256&apos;, vartype=&lt;VarType.STATEVAR: 0&gt;, derivation=&lt;invconplus.derivation.binary.MappingItem.MappingItem object at 0x7c6d7cc9d600&gt;), VarInfo(name=&apos;_value&apos;, type=&lt;slither.core.solidity_types.elementary_type.ElementaryType object at 0x7c6d7d61f580&gt;, vartype=&lt;VarType.TXVAR: 1&gt;, derivation=None), VarInfo(name=&apos;balanceOf[_to]&apos;, type=&apos;uint256&apos;, vartype=&lt;VarType.STATEVAR: 0&gt;, derivation=&lt;invconplus.derivation.binary.MappingItem.MappingItem object at 0x7c6d7cc9d9f0&gt;), VarInfo(name=&apos;_to&apos;, type=&lt;slither.core.solidity_types.elementary_type.ElementaryType object at 0x7c6d7d61cd90&gt;, vartype=&lt;VarType.TXVAR: 1&gt;, derivation=None)}
[]
16:26:39 [WARNING] 0x41f8270928fd02877caeb2f4a9329c2fa99e364314b10d8d1e6994150dd1d84etransfer(_to,_value)
16:26:39 [WARNING] 0x4a76df5febaf4b8605e93804caf08088cc90a12b0ab20398b67ebc0f8be3d341approve(_spender,_value)
16:26:39 [WARNING] 0x4ffff6c33fb3fd4382271d55b1902bfd22df92196b4da34d2d16a839333897fctransferFrom(_from,_to,_value)
16:26:39 [WARNING] 0x871ec44b88e46ce756f651a804213c87fd8bcf87dffaf2159dcd3e6b1b8c03dctransfer(_to,_value)
16:26:39 [WARNING] 0x2890b1f94dcca062584589d2d9c90f95c96e7a6ebef5d6d7353694c0f232721etransferFrom(_from,_to,_value)
16:26:39 [WARNING] 0x2a595385f098f70d5388b9d4605c0d68c68cf17e35895b4e622291a4ed3ae6b8transfer(_to,_value)
16:26:39 [WARNING] 0xc3ce7d12c427e9534282ff65880b287206e8898c233b084ccc276bc22b045337transfer(_to,_value)
16:26:39 [WARNING] 0xda9403c84fad19886a44ab76b42326cc4586aae8cccebb9ec9fa63ce3f160487transfer(_to,_value)
16:26:39 [WARNING] 0xa36c795bc3e351b65fe8862b8216760247f69a5826f800768344a0aabfac3e61approve(_spender,_value)
16:26:39 [WARNING] 0xa18458c239fefd9d104e134ebc65808ba9659e2d68b65a4e62aac9ae3e79c22dtransferFrom(_from,_to,_value)
```

## Advanced Usage

Other than dynamic invariant detection, InvCon also includes a module to facilitate formal verification on the invariant results.
To use this formal verification procedure 