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

| Contract Address                           | Name                                      | Transactions | Data Download | Diff Download | Run Time |
|--------------------------------------------|-------------------------------------------|-------------:|--------------:|--------------:|---------:|
| 0x00765EaABedBC0eC71e922178B5cF6f5632EC324 | AlgorToken                                |         4660 |       2616.3s |        261.4s |       8s |
| 0x007fa227D5d693F7f29e27B1FA028fd2051Ed072 | ExchangeRate                              |            3 |         17.2s |          2.7s |      <1s |
| 0x22d982a8B875Cc0f8994cd8a4a70872161fdc000 | GizerTokenPresale                         |            2 |         36.8s |          2.5s |      <1s |
| 0x2da4bb51E59D0b156B5e19Bb3F8eFf0279E1ffA2 | PuertoRicoHurricaneRelief_SaintCoinCaller |            4 |         25.1s |          4.6s |      <1s |

If successful, at the end of the command line output should look similar to the following:
<details>
  <summary>View example bash output (click to expand)</summary>
```sh
InvCon % python3 -m invconplus.main --address 0x00765EaABedBC0eC71e922178B5cF6f5632EC324
01:44:58 [WARNING] 0x00765EaABedBC0eC71e922178B5cF6f5632EC324
Installing solc '0.4.19'...
Version '0.4.19' installed.
01:45:05 [INFO] 'solc --standard-json --allow-paths /Users/chengxuan/Documents/InvCon' running
01:45:05 [WARNING] Warning: ./crytic-export/etherscan-contracts/0x00765EaABedBC0eC71e922178B5cF6f5632EC324.etherscan.io-AlgorToken.sol:49:7: Warning: "throw" is deprecated in favour of "revert()", "require()" and "assert()".
      throw;
      ^---^

Warning: ./crytic-export/etherscan-contracts/0x00765EaABedBC0eC71e922178B5cF6f5632EC324.etherscan.io-AlgorToken.sol:62:3: Warning: No visibility specified. Defaulting to "public".
  function balanceOf(address who) constant returns (uint);
  ^------------------------------------------------------^

Warning: ./crytic-export/etherscan-contracts/0x00765EaABedBC0eC71e922178B5cF6f5632EC324.etherscan.io-AlgorToken.sol:63:3: Warning: No visibility specified. Defaulting to "public".
  function transfer(address to, uint value);
  ^----------------------------------------^

Warning: ./crytic-export/etherscan-contracts/0x00765EaABedBC0eC71e922178B5cF6f5632EC324.etherscan.io-AlgorToken.sol:82:8: Warning: "throw" is deprecated in favour of "revert()", "require()" and "assert()".
       throw;
       ^---^

Warning: ./crytic-export/etherscan-contracts/0x00765EaABedBC0eC71e922178B5cF6f5632EC324.etherscan.io-AlgorToken.sol:92:3: Warning: No visibility specified. Defaulting to "public".
  function transfer(address _to, uint _value) onlyPayloadSize(2 * 32) {
  ^
Spanning multiple lines.

Warning: ./crytic-export/etherscan-contracts/0x00765EaABedBC0eC71e922178B5cF6f5632EC324.etherscan.io-AlgorToken.sol:103:3: Warning: No visibility specified. Defaulting to "public".
  function balanceOf(address _owner) constant returns (uint balance) {
  ^
Spanning multiple lines.

Warning: ./crytic-export/etherscan-contracts/0x00765EaABedBC0eC71e922178B5cF6f5632EC324.etherscan.io-AlgorToken.sol:115:3: Warning: No visibility specified. Defaulting to "public".
  function allowance(address owner, address spender) constant returns (uint);
  ^-------------------------------------------------------------------------^

Warning: ./crytic-export/etherscan-contracts/0x00765EaABedBC0eC71e922178B5cF6f5632EC324.etherscan.io-AlgorToken.sol:116:3: Warning: No visibility specified. Defaulting to "public".
  function transferFrom(address from, address to, uint value);
  ^----------------------------------------------------------^

Warning: ./crytic-export/etherscan-contracts/0x00765EaABedBC0eC71e922178B5cF6f5632EC324.etherscan.io-AlgorToken.sol:117:3: Warning: No visibility specified. Defaulting to "public".
  function approve(address spender, uint value);
  ^--------------------------------------------^

Warning: ./crytic-export/etherscan-contracts/0x00765EaABedBC0eC71e922178B5cF6f5632EC324.etherscan.io-AlgorToken.sol:140:3: Warning: No visibility specified. Defaulting to "public".
  function transferFrom(address _from, address _to, uint _value) onlyPayloadSize(3 * 32) {
  ^
Spanning multiple lines.

Warning: ./crytic-export/etherscan-contracts/0x00765EaABedBC0eC71e922178B5cF6f5632EC324.etherscan.io-AlgorToken.sol:157:3: Warning: No visibility specified. Defaulting to "public".
  function approve(address _spender, uint _value) {
  ^
Spanning multiple lines.

Warning: ./crytic-export/etherscan-contracts/0x00765EaABedBC0eC71e922178B5cF6f5632EC324.etherscan.io-AlgorToken.sol:163:64: Warning: "throw" is deprecated in favour of "revert()", "require()" and "assert()".
    if ((_value != 0) && (allowed[msg.sender][_spender] != 0)) throw;
                                                               ^---^

Warning: ./crytic-export/etherscan-contracts/0x00765EaABedBC0eC71e922178B5cF6f5632EC324.etherscan.io-AlgorToken.sol:175:3: Warning: No visibility specified. Defaulting to "public".
  function allowance(address _owner, address _spender) constant returns (uint remaining) {
  ^
Spanning multiple lines.

Warning: ./crytic-export/etherscan-contracts/0x00765EaABedBC0eC71e922178B5cF6f5632EC324.etherscan.io-AlgorToken.sol:188:3: Warning: No visibility specified. Defaulting to "public".
  function AlgorToken() {
  ^
Spanning multiple lines.

Warning: ./crytic-export/etherscan-contracts/0x00765EaABedBC0eC71e922178B5cF6f5632EC324.etherscan.io-AlgorToken.sol:47:3: Warning: This declaration shadows a builtin symbol.
  function assert(bool assertion) internal {
  ^
Spanning multiple lines.

Warning: ./crytic-export/etherscan-contracts/0x00765EaABedBC0eC71e922178B5cF6f5632EC324.etherscan.io-AlgorToken.sol:13:3: Warning: Function state mutability can be restricted to pure
  function div(uint a, uint b) internal returns (uint) {
  ^
Spanning multiple lines.

Warning: ./crytic-export/etherscan-contracts/0x00765EaABedBC0eC71e922178B5cF6f5632EC324.etherscan.io-AlgorToken.sol:31:3: Warning: Function state mutability can be restricted to pure
  function max64(uint64 a, uint64 b) internal constant returns (uint64) {
  ^
Spanning multiple lines.

Warning: ./crytic-export/etherscan-contracts/0x00765EaABedBC0eC71e922178B5cF6f5632EC324.etherscan.io-AlgorToken.sol:35:3: Warning: Function state mutability can be restricted to pure
  function min64(uint64 a, uint64 b) internal constant returns (uint64) {
  ^
Spanning multiple lines.

Warning: ./crytic-export/etherscan-contracts/0x00765EaABedBC0eC71e922178B5cF6f5632EC324.etherscan.io-AlgorToken.sol:39:3: Warning: Function state mutability can be restricted to pure
  function max256(uint256 a, uint256 b) internal constant returns (uint256) {
  ^
Spanning multiple lines.

Warning: ./crytic-export/etherscan-contracts/0x00765EaABedBC0eC71e922178B5cF6f5632EC324.etherscan.io-AlgorToken.sol:43:3: Warning: Function state mutability can be restricted to pure
  function min256(uint256 a, uint256 b) internal constant returns (uint256) {
  ^
Spanning multiple lines.

Warning: ./crytic-export/etherscan-contracts/0x00765EaABedBC0eC71e922178B5cF6f5632EC324.etherscan.io-AlgorToken.sol:47:3: Warning: Function state mutability can be restricted to pure
  function assert(bool assertion) internal {
  ^
Spanning multiple lines.


main contract: AlgorToken
01:45:05 [WARNING] cached record number 0
01:45:10 [WARNING] 0x00765EaABedBC0eC71e922178B5cF6f5632EC324 has transactions no less than 500
01:45:10 [WARNING] size of transactions to analyze:500
PROG[16-04|02:28:47.017] [..................................................]100%     1/    1 
|████████████████████████████████████████| 500/500 [100%] in 43:36.3 (0.19/s) 
02:28:47 [WARNING] fetching state diff for 500 transactions
|████████████████████████████████████████| 500/500 [100%] in 4:21.4 (1.91/s) 
02:33:09 [INFO] 'solc --standard-json --allow-paths /Users/chengxuan/Documents/InvCon' running
02:33:10 [WARNING] Warning: crytic-export/etherscan-contracts/0x00765EaABedBC0eC71e922178B5cF6f5632EC324.etherscan.io-AlgorToken.sol:49:7: Warning: "throw" is deprecated in favour of "revert()", "require()" and "assert()".
      throw;
      ^---^

Warning: crytic-export/etherscan-contracts/0x00765EaABedBC0eC71e922178B5cF6f5632EC324.etherscan.io-AlgorToken.sol:62:3: Warning: No visibility specified. Defaulting to "public".
  function balanceOf(address who) constant returns (uint);
  ^------------------------------------------------------^

Warning: crytic-export/etherscan-contracts/0x00765EaABedBC0eC71e922178B5cF6f5632EC324.etherscan.io-AlgorToken.sol:63:3: Warning: No visibility specified. Defaulting to "public".
  function transfer(address to, uint value);
  ^----------------------------------------^

Warning: crytic-export/etherscan-contracts/0x00765EaABedBC0eC71e922178B5cF6f5632EC324.etherscan.io-AlgorToken.sol:82:8: Warning: "throw" is deprecated in favour of "revert()", "require()" and "assert()".
       throw;
       ^---^

Warning: crytic-export/etherscan-contracts/0x00765EaABedBC0eC71e922178B5cF6f5632EC324.etherscan.io-AlgorToken.sol:92:3: Warning: No visibility specified. Defaulting to "public".
  function transfer(address _to, uint _value) onlyPayloadSize(2 * 32) {
  ^
Spanning multiple lines.

Warning: crytic-export/etherscan-contracts/0x00765EaABedBC0eC71e922178B5cF6f5632EC324.etherscan.io-AlgorToken.sol:103:3: Warning: No visibility specified. Defaulting to "public".
  function balanceOf(address _owner) constant returns (uint balance) {
  ^
Spanning multiple lines.

Warning: crytic-export/etherscan-contracts/0x00765EaABedBC0eC71e922178B5cF6f5632EC324.etherscan.io-AlgorToken.sol:115:3: Warning: No visibility specified. Defaulting to "public".
  function allowance(address owner, address spender) constant returns (uint);
  ^-------------------------------------------------------------------------^

Warning: crytic-export/etherscan-contracts/0x00765EaABedBC0eC71e922178B5cF6f5632EC324.etherscan.io-AlgorToken.sol:116:3: Warning: No visibility specified. Defaulting to "public".
  function transferFrom(address from, address to, uint value);
  ^----------------------------------------------------------^

Warning: crytic-export/etherscan-contracts/0x00765EaABedBC0eC71e922178B5cF6f5632EC324.etherscan.io-AlgorToken.sol:117:3: Warning: No visibility specified. Defaulting to "public".
  function approve(address spender, uint value);
  ^--------------------------------------------^

Warning: crytic-export/etherscan-contracts/0x00765EaABedBC0eC71e922178B5cF6f5632EC324.etherscan.io-AlgorToken.sol:140:3: Warning: No visibility specified. Defaulting to "public".
  function transferFrom(address _from, address _to, uint _value) onlyPayloadSize(3 * 32) {
  ^
Spanning multiple lines.

Warning: crytic-export/etherscan-contracts/0x00765EaABedBC0eC71e922178B5cF6f5632EC324.etherscan.io-AlgorToken.sol:157:3: Warning: No visibility specified. Defaulting to "public".
  function approve(address _spender, uint _value) {
  ^
Spanning multiple lines.

Warning: crytic-export/etherscan-contracts/0x00765EaABedBC0eC71e922178B5cF6f5632EC324.etherscan.io-AlgorToken.sol:163:64: Warning: "throw" is deprecated in favour of "revert()", "require()" and "assert()".
    if ((_value != 0) && (allowed[msg.sender][_spender] != 0)) throw;
                                                               ^---^

Warning: crytic-export/etherscan-contracts/0x00765EaABedBC0eC71e922178B5cF6f5632EC324.etherscan.io-AlgorToken.sol:175:3: Warning: No visibility specified. Defaulting to "public".
  function allowance(address _owner, address _spender) constant returns (uint remaining) {
  ^
Spanning multiple lines.

Warning: crytic-export/etherscan-contracts/0x00765EaABedBC0eC71e922178B5cF6f5632EC324.etherscan.io-AlgorToken.sol:188:3: Warning: No visibility specified. Defaulting to "public".
  function AlgorToken() {
  ^
Spanning multiple lines.

Warning: crytic-export/etherscan-contracts/0x00765EaABedBC0eC71e922178B5cF6f5632EC324.etherscan.io-AlgorToken.sol:47:3: Warning: This declaration shadows a builtin symbol.
  function assert(bool assertion) internal {
  ^
Spanning multiple lines.

Warning: crytic-export/etherscan-contracts/0x00765EaABedBC0eC71e922178B5cF6f5632EC324.etherscan.io-AlgorToken.sol:13:3: Warning: Function state mutability can be restricted to pure
  function div(uint a, uint b) internal returns (uint) {
  ^
Spanning multiple lines.

Warning: crytic-export/etherscan-contracts/0x00765EaABedBC0eC71e922178B5cF6f5632EC324.etherscan.io-AlgorToken.sol:31:3: Warning: Function state mutability can be restricted to pure
  function max64(uint64 a, uint64 b) internal constant returns (uint64) {
  ^
Spanning multiple lines.

Warning: crytic-export/etherscan-contracts/0x00765EaABedBC0eC71e922178B5cF6f5632EC324.etherscan.io-AlgorToken.sol:35:3: Warning: Function state mutability can be restricted to pure
  function min64(uint64 a, uint64 b) internal constant returns (uint64) {
  ^
Spanning multiple lines.

Warning: crytic-export/etherscan-contracts/0x00765EaABedBC0eC71e922178B5cF6f5632EC324.etherscan.io-AlgorToken.sol:39:3: Warning: Function state mutability can be restricted to pure
  function max256(uint256 a, uint256 b) internal constant returns (uint256) {
  ^
Spanning multiple lines.

Warning: crytic-export/etherscan-contracts/0x00765EaABedBC0eC71e922178B5cF6f5632EC324.etherscan.io-AlgorToken.sol:43:3: Warning: Function state mutability can be restricted to pure
  function min256(uint256 a, uint256 b) internal constant returns (uint256) {
  ^
Spanning multiple lines.

Warning: crytic-export/etherscan-contracts/0x00765EaABedBC0eC71e922178B5cF6f5632EC324.etherscan.io-AlgorToken.sol:47:3: Warning: Function state mutability can be restricted to pure
  function assert(bool assertion) internal {
  ^
Spanning multiple lines.


main contract:  AlgorToken
SafeMath
ERC20Basic
BasicToken
ERC20
StandardToken
AlgorToken
02:33:10 [WARNING] createInitialPptsForFunction for approve(_spender,_value)
02:33:10 [WARNING] createInitialPptsForFunction for transferFrom(_from,_to,_value)
02:33:10 [WARNING] createInitialPptsForFunction for transfer(_to,_value)
02:33:10 [WARNING] createInitialPptsForContract...
**********

transfer(_to,_value)
{VarInfo(name='balances[msg.sender]', type='uint256', vartype=<VarType.STATEVAR: 0>, derivation=<invconplus.derivation.binary.MappingItem.MappingItem object at 0x7fca09444640>), VarInfo(name='balances[_to]', type='uint256', vartype=<VarType.STATEVAR: 0>, derivation=<invconplus.derivation.binary.MappingItem.MappingItem object at 0x7fca09444790>)}
[]
**********

onlyPayloadSize(size)
{VarInfo(name='size', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7fca092aab90>, vartype=<VarType.TXVAR: 1>, derivation=None)}
[]
**********

transferFrom(_from,_to,_value)
{VarInfo(name='_allowance', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7fca092f82b0>, vartype=<VarType.LOCALVAR: 2>, derivation=None), VarInfo(name='balances[_to]', type='uint256', vartype=<VarType.STATEVAR: 0>, derivation=<invconplus.derivation.binary.MappingItem.MappingItem object at 0x7fca094450f0>), VarInfo(name='balances[_from]', type='uint256', vartype=<VarType.STATEVAR: 0>, derivation=<invconplus.derivation.binary.MappingItem.MappingItem object at 0x7fca09445330>), VarInfo(name='allowed[_from][msg.sender]', type='uint256', vartype=<VarType.STATEVAR: 0>, derivation=<invconplus.derivation.binary.MappingItem.MappingItem object at 0x7fca09445120>)}
[]
**********

balanceOf(_owner)
set()
[]
**********

allowance(_owner,_spender)
set()
[]
**********

AlgorToken()
{VarInfo(name='balances[msg.sender]', type='uint256', vartype=<VarType.STATEVAR: 0>, derivation=<invconplus.derivation.binary.MappingItem.MappingItem object at 0x7fca09445e40>), VarInfo(name='totalSupply', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7fca091e4cd0>, vartype=<VarType.STATEVAR: 0>, derivation=None)}
[]
**********

approve(_spender,_value)
{VarInfo(name='allowed[msg.sender][_spender]', type='uint256', vartype=<VarType.STATEVAR: 0>, derivation=<invconplus.derivation.binary.MappingItem.MappingItem object at 0x7fca09446320>), VarInfo(name='_value', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7fca092ab6d0>, vartype=<VarType.TXVAR: 1>, derivation=None)}
[]
02:33:10 [WARNING] 0x7ae0c7ceb52a2252aa79d505c6379c5145efd9a2b6a59cf68f884e997281a2e0transfer(_to,_value)
02:33:10 [WARNING] 0x6b965ef85fff67a62626cc69cc6881165d58d23ecd7c160869263d2f3ca07e74transfer(_to,_value)
02:33:10 [WARNING] 0xa695c3587dfd4d5e3db702cc1cd27b7c4a21d22c654d183cbba40944bcd3a526transfer(_to,_value)
02:33:10 [WARNING] 0x3e29a56528a905600dc5115aa8fee94317bb64c1c9a3e7de863877403bb7e2fetransfer(_to,_value)
02:33:10 [WARNING] 0xfd8e406e94820725c635b0ffa0e4e898ce329818a6fce1b271a2d07520a07830transfer(_to,_value)
02:33:10 [WARNING] 0xc2f6cb0eefcefe1f354191d96268c867f05ce773945cf43169ab470f465b3e8dtransfer(_to,_value)
02:33:10 [WARNING] 0xc72c4428885c6c8640bcca7b63e9511b92d75b448ea607dc53eff2fb6a5996c1transfer(_to,_value)
02:33:11 [WARNING] 0xe308279ec6ac4bae93bdf98dd8d605cf3269a09bbdc8c6c313df4bd905b262e7transfer(_to,_value)
02:33:11 [WARNING] 0xbfb7a860d4a201ea4f7053afd9dae642efba5dc66628801580dc47d59e31cd6ctransfer(_to,_value)
02:33:11 [WARNING] 0x915c007f45825b1e2cc53a3aed97ccf3fa9a427e56c0f5c1f53aa99cd93ddf77transfer(_to,_value)
02:33:11 [WARNING] 0x7aadf22c93643d51db30873ef4fcfe0cc6531cd35d6d2e724e8a7c47a16a170btransfer(_to,_value)
02:33:11 [WARNING] 0xbae1b89eea3fd5b4453df9a15d91d234a36f2bd7916757f8398e97c3b7954ca2transfer(_to,_value)
02:33:11 [WARNING] 0xdba8ed86d8b13241d7321dc403c5b16a99a5735a2215c59cdf0f7a3786b363bdtransfer(_to,_value)
02:33:11 [WARNING] 0x0fdb24f4bd8fe17e247353ebcdfb33e611c23240d4959f0ba2545d8dbbf13c60transfer(_to,_value)
02:33:11 [WARNING] 0xb9612da7eb6e7707f48783436a3c38e9bd3891001b487863814a98d10f347ab2transfer(_to,_value)
02:33:11 [WARNING] 0xe015feef52f4b6177ae398c911b3a91d12dc1ec9a753cebf66defee28748fb1dtransfer(_to,_value)
02:33:11 [WARNING] 0xf0326ecaf812749ea529d8e8b2b7b9fc0f58122d6491876ab6a33184f2601102transfer(_to,_value)
02:33:11 [WARNING] 0x72db3df533f84d6006e29852eafb62ecfd780bb37ba13480e9d4fcf476d45b3etransfer(_to,_value)
02:33:11 [WARNING] 0x3e5086cde8bca34f599166ab3e41e59c036f459d483c44eba83a4ee2d4f04379transfer(_to,_value)
02:33:11 [WARNING] 0x47dc96a6f895fab3907fd37bef6c7c16d2e531a17ed182f4af6335da37210423transfer(_to,_value)
02:33:11 [WARNING] 0x9ee40894c60c50c9c907be8b88c354418fee0dccd6c016499816b4eb03ac8acctransfer(_to,_value)
02:33:11 [WARNING] 0xa7245d4efd5b4f40e7c9a7ab340934f0487ddea7add39afa1c66f1ad2fdfa76ctransfer(_to,_value)
02:33:11 [WARNING] 0x5768eeecda823b2fdab8870758520633d6a769b3e03baca92e92bc71e9bf5f01transfer(_to,_value)
02:33:11 [WARNING] 0xe3d070ecee9192514a045ea479feae221915c0154061e8e860a527ceb78d3e01transfer(_to,_value)
02:33:11 [WARNING] 0xaf3541cca60cc437fbc1a09a0ff4a9c53586ca82c078ea9daa82215dc501cfeatransfer(_to,_value)
02:33:11 [WARNING] 0xf29de3b4984d40c4d3b475a8e7cbbb7cce1abc65bbbd3e8707493ffceae14773transfer(_to,_value)
02:33:11 [WARNING] 0xddfb7e04a858620ffcb0f16237b0b6deef68897b3096a3f95cc6adb74bd232b5transfer(_to,_value)
02:33:11 [WARNING] 0x56a92014f50b05625a0eb388c8ec28f8033795abe574d1a89e2a21162835ea08transfer(_to,_value)
02:33:11 [WARNING] 0x59743572381bce21968e8393e05da613912fefc2711d012adbdc1524a8697044transfer(_to,_value)
02:33:11 [WARNING] 0xa88e19b3afc49da6b85722c0f4a98b61ded2ecce289dcf9e209541b98585a606transfer(_to,_value)
02:33:11 [WARNING] 0x81fdcd41605287980ceb1c3625e2edb63156266e0be1122935f06990fb6ca38ftransfer(_to,_value)
02:33:11 [WARNING] 0x5a9515ee32c60ea379a1e01585aa94386c0514ce5f865173d0d176aa2140d9actransfer(_to,_value)
02:33:11 [WARNING] 0xc554c0fe24ca77d88730587208cedf402804726e0a2d292942d6663ed282ae53transfer(_to,_value)
02:33:11 [WARNING] 0x37a0b71b5a7eba6e4596b8a97bb9039c2504a867122d131f924aadce7c767aabtransfer(_to,_value)
02:33:11 [WARNING] 0x010a19bf74f09df8383f2a6debd380daf63b0d82b5beb0f21eb1a309c4c00295transfer(_to,_value)
02:33:11 [WARNING] 0x5bc4f1203c230d37a488095ab6cd35ab4ee40bec58d5ea6c21d8a4bfd394bfbdtransfer(_to,_value)
02:33:11 [WARNING] 0xd37a379428f3828e88d1b87ba3651b7ef1a4139cc2845464479e34858bc216b6transfer(_to,_value)
02:33:11 [WARNING] 0xa3fbe589e3dc36daf2e8f944bd42de049eb609a86ae124c19dd9e7abc5e3a10ctransfer(_to,_value)
02:33:11 [WARNING] 0xdbf1fcc87accb089b05a4f0a7c6df44dbb2602ef1832850351262b4c83e99522transfer(_to,_value)
02:33:11 [WARNING] 0x91be7b98a602e254199116ce3167442377cb7e83264ae0cb8dc297c6fc13bb1btransfer(_to,_value)
02:33:11 [WARNING] 0xbeb3eb85c11a41a762dc0c16575eff1d66ef1962be0ec26b5618c0d0298a168ctransfer(_to,_value)
02:33:11 [WARNING] 0x5c0aa7f6545ab83cb086bdf278565036f9f65c51f9fad34748483997dc899196transfer(_to,_value)
02:33:11 [WARNING] 0x512efc6a3ec4baa21200953841867f78627ac8ee40a4c2e894f12539d348ede6transfer(_to,_value)
02:33:11 [WARNING] 0x70e79a2bc77e49c44a45a1cd3cae511bf7c429a957454eff3f4584380901f2e3transfer(_to,_value)
02:33:11 [WARNING] 0x1c0a0979a426d907dbca5b4103ede1248e16ac6eb9848bdf824eacbb6a2508f0transfer(_to,_value)
02:33:11 [WARNING] 0x32be271bf6f59dc47cafb4e695a3b903a8cdca9a1b311b715e8bbe9d57c1be87transfer(_to,_value)
02:33:11 [WARNING] 0x680713eb0e661eb8e3cca6d7d1f4b7603582bac10bd4205993fc85554a6ed8b5transfer(_to,_value)
02:33:11 [WARNING] 0x88e2e5207b27e5370da6cf729bfdc01d6fd60ed7f3ae96045ee6a21e6bc1be7atransfer(_to,_value)
02:33:11 [WARNING] 0x3e0366c180fe827bba65f1ddc76e5366b3d1b5199c90742595c572e30a34367ftransfer(_to,_value)
02:33:11 [WARNING] 0x0bf65b238cfdeacf7fb8cb6bdff04cb04e61ac08d784d8d5029f9bd7716d05ectransfer(_to,_value)
02:33:11 [WARNING] 0x6014db0d7ac86c2c6cfa846bc76e1949f2e51732da801e70ffa0143b82f4c43btransfer(_to,_value)
02:33:11 [WARNING] 0xa5fd1d6af3af8b17ce85738a0777850c1a48c22a9b28c538625938e19c3d0052transfer(_to,_value)
02:33:11 [WARNING] 0x65040869ed9e65489b2fa52e98e935b45f21c3c5dd85d6af0629bf12056e0a09transfer(_to,_value)
02:33:11 [WARNING] 0xb6a5a2f07f99576ec03afd6e5e03ceedb020373bed9af0b58018bd35e923f620transfer(_to,_value)
02:33:11 [WARNING] 0x7fda69b66f71181f29ee474ab2b19079b2561f7144528bdbf9ab4234f54a1a87transfer(_to,_value)
02:33:11 [WARNING] 0x3e57b3bac1d1dbe5d41f4e9e832c7361520dafc3eb9156d3299daaf753d03596transfer(_to,_value)
02:33:11 [WARNING] 0x0959c3e35d373328130ae1384f6bad83454f1156a735eddc61e0444f893997a8transfer(_to,_value)
02:33:11 [WARNING] 0x288cd4ec3c77a6ec160f9fadbca77afe9ceaec0eb835bc6dad206ac2ac1473d2transfer(_to,_value)
02:33:11 [WARNING] 0x33f076d42ebda3dff7a3cd86cb6214e93bcae1d70b022ab65e811878e9fd940ftransfer(_to,_value)
02:33:11 [WARNING] 0x347977839bdae4a7718b23dec833f822451db2fee44466b02edfd948554f2521transfer(_to,_value)
02:33:11 [WARNING] 0xd17ffc99ba588de6a988cd074cee91ecbf5399b8122dddcf55996e86e040a7a0transfer(_to,_value)
02:33:11 [WARNING] 0x84c53c6fec48ecd5520f2dcdec7ee2547af21e4401d83da07a28c6c70fc02892transfer(_to,_value)
02:33:11 [WARNING] 0x21b17853edafae465dff088c901be8d8a56906f89b2640f2aa09827b2fd48ab6transfer(_to,_value)
02:33:11 [WARNING] 0x5f21e9b2f6b74043b42516c7a97bc6cdc2d983b0d41d4346eb78a96cb53ee5aftransfer(_to,_value)
02:33:11 [WARNING] 0xf946d6a2a3e03ed2e54337b77b8bb3eafec251727aa5da6af2eb0703fb53d83ctransfer(_to,_value)
02:33:11 [WARNING] 0xdbad0a1f26b82e2a7d848216c6dec099891bb6252af4f8f07a7a3ced3c1a166atransfer(_to,_value)
02:33:11 [WARNING] 0xb4f2b3e1c4dbfb433640f7d581622bed67c34a62e2426ab5f1deb512be8843e7transfer(_to,_value)
02:33:11 [WARNING] 0x033fb19f849ba6776b87603629b9af241f4d534db733df3ad88e3159175d4729transfer(_to,_value)
02:33:11 [WARNING] 0x68e23a9c907da20b1af3ab08a708c240251dbe2ada79ba932c1b21370d3dd4b7transfer(_to,_value)
02:33:11 [WARNING] 0x896565ee29ca58546953215696d749f6704659ead14ad29ab66830b113f3b805transfer(_to,_value)
02:33:11 [WARNING] 0x9c35727d3bd4e5d74acad39e0820fed0df7d117d0bf08976efc34ada86ac07bftransfer(_to,_value)
02:33:11 [WARNING] 0xd0931ddc9938f1c2dba9d97c5b705532c3c165f0e13cabb84361805d9a35ef61transfer(_to,_value)
02:33:11 [WARNING] 0x68df2c1dadac769ab4883f52113705800178b0c10875aa4d250c58dfb22d8442transfer(_to,_value)
02:33:11 [WARNING] 0x862873b3d095a1b4e48976e786a54e1115d219de13211279f77a4068b8721ac5transfer(_to,_value)
02:33:11 [WARNING] 0xef2f21626043fbcf7c35c14b536d56f42fb5c9275a2de9e33bd1065c158a39c6transfer(_to,_value)
02:33:11 [WARNING] 0x64bdb7b22308f91e6c74e4dadf63257d8ef1e2bcab2c1821dd1dd33a8bcc949ftransfer(_to,_value)
02:33:11 [WARNING] 0xece561f8b42bbd88ee26585602588afe1f41b6d52107ea863ab1705c388edd88transfer(_to,_value)
02:33:11 [WARNING] 0x7ebc035e57940ef90b1eea91737bc2eb5b40266c137547694ae898e8fce58622transfer(_to,_value)
02:33:11 [WARNING] 0x2d86ba1e73c1fc6b50168e88e8638416c9f6181b18125a5354e30fb1893f90fbtransfer(_to,_value)
02:33:11 [WARNING] 0x10846b4405ae97ec153aae1c2fb5b661eec8263e1226f962362e22599737a54ftransfer(_to,_value)
02:33:11 [WARNING] 0x9e67714e23cb1f8d40e01feff1e45bcaacc6863a323be78c41d7568ad80a13d2transfer(_to,_value)
02:33:11 [WARNING] 0xf734204dad6af5326ad534388e370fe56c7b213e663a610aafaa0c1b0779addctransfer(_to,_value)
02:33:11 [WARNING] 0x5ec67b6ff106229b2771711c172b172a1fe573dd5fbced51b734a17ffad17b30transfer(_to,_value)
02:33:11 [WARNING] 0x6b8a538facb2517e8a958e2ddf960103d63e9dac64954b40b42910d3e0e904a7transfer(_to,_value)
02:33:11 [WARNING] 0xc7fe38d8c797afce0338ff0708f7a12847098f1f3e51167d30212581944da72etransfer(_to,_value)
02:33:11 [WARNING] 0x5997f6416f0dd76a2a3229002c787e335efca25d3e578e2d46d1e57e1ad4eb62transfer(_to,_value)
02:33:11 [WARNING] 0xde2bf10f0e308305cadeffa6bbeae484f9b1d9b8fb3658a27b18cd1767bd2b78transfer(_to,_value)
02:33:11 [WARNING] 0x0df7b5536ca83e3289e28ada901b3de7ad7c1896e1b9881d95df0d468c0821fbtransfer(_to,_value)
02:33:11 [WARNING] 0xfe9813446de5566600b7bf628f73516b340e81e54c54b313ff66cef52745cc17transfer(_to,_value)
02:33:11 [WARNING] 0xe75434759f5445f16c1adcb735eb33bc6ae5defd729da3453060419b1b490889transfer(_to,_value)
02:33:11 [WARNING] 0x1f6c8ceb2e9ea70aaf918de8b7e35de0641fd7a3e9aaa00d269cd230785c6764transfer(_to,_value)
02:33:11 [WARNING] 0xaf8ffe794e7e9154cb7035d251de37819ad25f54549c4e4b6a42f84e31c4bc44transfer(_to,_value)
02:33:11 [WARNING] 0xc38f92f7b0c3e143de825e0ae3b1534672eb066076a61c1f93749491d8014fcdtransfer(_to,_value)
02:33:11 [WARNING] 0xd800eca30438069f58e769275a47e2708d7db39b3e64d6e3eaca98688b319c2btransfer(_to,_value)
02:33:11 [WARNING] 0x24425a17a0563743ed6c871af3d75cc5de4f6130ec7bca7e126181e352a8e0a5transfer(_to,_value)
02:33:12 [WARNING] 0x7f2c65534b60c6cf1b6024d2dd9ec411befe6d9bafdd2d7b5f784249438d4532transfer(_to,_value)
02:33:12 [WARNING] 0xea746c7544fe24490dd0a3de3332759c7fba3ebb26ee7007f1d3b6b7fcd94606transfer(_to,_value)
02:33:12 [WARNING] 0x6284dbc5f26d2c8136c908fe438da11ed0525c1ecc4cdbdf52c40f46868c05bdtransfer(_to,_value)
02:33:12 [WARNING] 0x68fa323147ddd6b5090c13b2f9bf640074984bd9f8b3fd2e52242e64364124c0transfer(_to,_value)
02:33:12 [WARNING] 0x69e6f021df1f104e9ff2ee6910274e14b2293721b16b77d0c77304963c489ca8transfer(_to,_value)
02:33:12 [WARNING] 0xd2c191d570ae3154f903699181fd9d73aa8f960620fd5b2a8652008cae03357btransfer(_to,_value)
02:33:12 [WARNING] 0x9b6bda907bff85406b8b35c03d54988ad94763faa464cbdfc37e82cd764ba707transfer(_to,_value)
02:33:12 [WARNING] 0xcda26b63ff06a0124c4fc9f2b0d8912358f3e074b1b52190a52a2bf53f5c2e39transfer(_to,_value)
02:33:12 [WARNING] 0xcad1903632c4fd5a66a4577ea4a0d3dd535582218886d48cf2525cc1dc554831transfer(_to,_value)
02:33:12 [WARNING] 0x8787deb2959e365b60b79b5658e14be1edef8bd5961168e76181b384da8a6747transfer(_to,_value)
02:33:12 [WARNING] 0xb9c0fada2c690a3cb8ed1eb632d3c3ef9eaed0d9951458ded6493899d26b56b8transfer(_to,_value)
02:33:12 [WARNING] 0x36c8948621ab3b86809ec6f63716c8f87e7f80d13b752e98516625488e26f7b1transfer(_to,_value)
02:33:12 [WARNING] 0xd4b4cbf21d950b487949032e739e8a85ab249b7f9630f0794b2d1515e817bd8etransfer(_to,_value)
02:33:12 [WARNING] 0x60afff12dfd5e7c66a5e4481ac7e7c5de622c3da452b50e7fe688e9a044e54abtransfer(_to,_value)
02:33:12 [WARNING] 0x51b0adc81576d9a2a3717387b8a1af298efa830c51761019b241d8313ddc72d1transfer(_to,_value)
02:33:12 [WARNING] 0x26c50cd4be7348cc4326bfb224fddcfa8066040e18d5b19125b836a74ecf36b5transfer(_to,_value)
02:33:12 [WARNING] 0xda67574df6b61bd01eab7ce31705baddd8d2d36ff60dd248854c2124ec0587e4transfer(_to,_value)
02:33:12 [WARNING] 0x171cec8d504abc6f31a20e76814ae5809537722296d3dc25f4b2d80e5ceea4b2transfer(_to,_value)
02:33:12 [WARNING] 0x14d70ecb18a1aababc2b3feefabb6ba0d3eecdecf6e6d5a0730b8391b2326560transfer(_to,_value)
02:33:12 [WARNING] 0x4adcc927528e7be1e0096aa3ead58263d0a61a204b8a0e5fabd5bca3f900236ctransfer(_to,_value)
02:33:12 [WARNING] 0x03ae9480856ae2149b963ff33ee544cbe9fff87c60b0e2b73090e38ed36245e8transfer(_to,_value)
02:33:12 [WARNING] 0x127bf6ed83a3355a8fa129cc8c81671dccb22db219ba68251421f0f64b4f908etransfer(_to,_value)
02:33:12 [WARNING] 0x47ead26aed5e7386643cd4dfd79dd8afc0216c34c592de7dbe26a9b37b66cc18transfer(_to,_value)
02:33:12 [WARNING] 0xbeb0abb3cebea36e56ebbae183460a67c4c56458f7ad14256733636dd9f62bcftransfer(_to,_value)
02:33:12 [WARNING] 0x6ed986d94836672b11d97ef2d5594cc62e66212aef4d50d13fbbfeed9bf46561transfer(_to,_value)
02:33:12 [WARNING] 0xaeb60f0794cded0e7532a35ff091717e9656abc83304c49a887d7fc861c8c6a8transfer(_to,_value)
02:33:12 [WARNING] 0x816287bdfe71c1ccfeeddd0db9625768ede6a10e4693fa89e49c938bf49c9d25transfer(_to,_value)
02:33:12 [WARNING] 0x502c7adf918f0a44fa96dab225187ddbab0289dad68f9f00d44992cf892b69d0transfer(_to,_value)
02:33:12 [WARNING] 0x027130dcb7e9d1e552b9860ff90cdc20d28bac457d98f1432c12d69c259fce12transfer(_to,_value)
02:33:12 [WARNING] 0x3918fd9b34ff4444997097f7c68ec5f896fef2ae941a9abf29d952f249506a15transfer(_to,_value)
02:33:12 [WARNING] 0x097e2379e2b2492df975ebfa82ed556e25d704a1d16e441b3c5cf55e5a3c8a08transfer(_to,_value)
02:33:12 [WARNING] 0x178a4d7100e0a8513fc3d7ff0e49c079fd1b2103108ddee4a4335a5ae125b33btransfer(_to,_value)
02:33:12 [WARNING] 0x18bbdd9796819da82884b95249cfaadb8aee03850f016b6eac4fdd6b3152d4a2transfer(_to,_value)
02:33:12 [WARNING] 0xcb188c3431fbdce45bdc388a15ed8a77b1e630d5fb057597c8c2c290de3ad751transfer(_to,_value)
02:33:12 [WARNING] 0xa933281dba1b5e5f7a33d21a893ab1fede8b05db339d3989256f9aaf20ba2e62transfer(_to,_value)
02:33:12 [WARNING] 0x423a593dc3350874408af123d14b5f7db803825b651a3806a5d6142948fce089transfer(_to,_value)
02:33:12 [WARNING] 0x566b9d75f49e2cef2baea756801f426dc1f683654c96c7969c3d1ddca998a685transfer(_to,_value)
02:33:12 [WARNING] 0x133b69a1a26552d15c2e123b7ea85ad5f31d49c9e05ae41e95e5c58a8275f18btransfer(_to,_value)
02:33:12 [WARNING] 0x19512efd5bca80f098ea0f4e8d05e1bea424f39b22d4dc5e226b2bec540de3f3transfer(_to,_value)
02:33:12 [WARNING] 0x0a06ff0c396d7a85953b1bc3485e076ae1a5cbc10efd95afa5af0639ccd53b9dtransfer(_to,_value)
02:33:12 [WARNING] 0x874fdb51ec774e6d33500db1a2effaa7e17348d2b7af7869b80bd3c8db416c7ctransfer(_to,_value)
02:33:12 [WARNING] 0x2005bca1331fb503dfa0e2228ee9794d9b178229a6f8225e397267bebfee740dtransfer(_to,_value)
02:33:12 [WARNING] 0x925d3eebf4226738e04ce487365b68263383bd44b909be2e364f1457c06350d6transfer(_to,_value)
02:33:12 [WARNING] 0xde7930b4b46dc122dbf7a9f8d9d0d4c69eb7b9a84c053bc9578ddf2168154f50transfer(_to,_value)
02:33:12 [WARNING] 0xc51613fa006976379e66e1fd64404852fb310056643987209e1cc65b428e7c34transfer(_to,_value)
02:33:12 [WARNING] 0x7b624fa12494eff9500b6e368a470d321d27664710f447d880cfde416b451974transfer(_to,_value)
02:33:12 [WARNING] 0xc85d9e4bba9cdf8a07c75ab738281c6547555f65906550c242e5c0f1640ac3cctransfer(_to,_value)
02:33:12 [WARNING] 0x40ae22d941e3d1ec285717de92758d27f02b4c27cc6a5f87cbdb337be59a23c5transfer(_to,_value)
02:33:12 [WARNING] 0x67663f28dffc29621c84860d2787d798b275ea87a92945dddc58410efed46a8ctransfer(_to,_value)
02:33:12 [WARNING] 0x93cd87bed50ef9137ad165a13d18606bedb9a38e3be1fdcfe4408b3cc1721d31transfer(_to,_value)
02:33:12 [WARNING] 0x9a0abb233ef1a6b0e988a267d455df5fcae3b794a870010c1dd549a302426d2ftransfer(_to,_value)
02:33:12 [WARNING] 0x43e63c5f39543f33892ae52fc54d55cc67f250771e0403283b0d65e7fbcea5d8transfer(_to,_value)
02:33:12 [WARNING] 0xe5bb244a7148e66716835e90d782d745cc37350ccc87b475b0c9e1be2e025108transfer(_to,_value)
02:33:12 [WARNING] 0xe0705e16269af36f4d652b526537f3ef43e27a3f5888b78406f441dc8c6d804dtransfer(_to,_value)
02:33:12 [WARNING] 0x43504f74f0c3800ab0f7f0923eaa999bc8429523ea1f3baa7a24e9fdb6d95cbatransfer(_to,_value)
02:33:12 [WARNING] 0x171aa548877ce7d5679b6589c4cd79aba7656235bcc1b38fa0813af1d77e54e4transfer(_to,_value)
02:33:12 [WARNING] 0x8096b20f5a52c763f07b12dc3fa0984b895eae6af5e97f0e8b1cb7c19a4500f3transfer(_to,_value)
02:33:12 [WARNING] 0x58db69e0b49c087c9f572f093ec4bf5abf681183e0e302d329cc76bec6bf0be3transfer(_to,_value)
02:33:12 [WARNING] 0x9798f93e8ac56082017d1a20a8e4fe195d8784b86bf349f4bc9179ea308a0fddtransfer(_to,_value)
02:33:12 [WARNING] 0x920338767e34168313ca6f8681a6122f2c28c8e285af06cec138a7605ff1e06atransfer(_to,_value)
02:33:12 [WARNING] 0x9853e0516bccb66c9c34c250c1d5773f123f5357a0d2a011ff3c212e8933559btransfer(_to,_value)
02:33:12 [WARNING] 0x6733180763e7da20df7f7cb5f38c21c2957455973b381dbff8551d28e4c5b116transfer(_to,_value)
02:33:12 [WARNING] 0x3b1b4a0ad54df6f960e7f08165a539231a656352fd1ba4b7425e5d06318d36c3transfer(_to,_value)
02:33:12 [WARNING] 0xdea68467474980104df7e4a1b59ba7e63a942ed0e0a596948049e5917ea2b6aetransfer(_to,_value)
02:33:12 [WARNING] 0xe148b367d2fc2bc7dbad6f9babbde4c94e99fb10ea38b800941b96dd8fdb3837transfer(_to,_value)
02:33:12 [WARNING] 0x3bcdbae28c888a93fa4ba6bdb01705f20cbdd8a5488fb2c13e21202339b00c6btransfer(_to,_value)
02:33:12 [WARNING] 0x492577c7b930b3c18d33fa5a2df2d3967caf2e49b478235c6b8a0e160a0eac1dtransfer(_to,_value)
02:33:12 [WARNING] 0x79d95b468a7f6c88b1a396972b5865fa10bcf590514cfb3330ab27a4c44d1070transfer(_to,_value)
02:33:12 [WARNING] 0x0924bd68739f6bbe6b9c36015ba1e0d456628d35b40f2fe1e4af8863508f345dtransfer(_to,_value)
02:33:12 [WARNING] 0xc796abd318aa054a470009690f3746c8691ba7a99961227cb334713eac9f2c60transfer(_to,_value)
02:33:12 [WARNING] 0xa4a3358cbae63675a6e103a1eb70b957fa696ff2af135a4746d15893ba93015ftransfer(_to,_value)
02:33:12 [WARNING] 0x2415557ba9e0bdbdbc52a56df80f5a372822d7853dbef3b5155caf8445457b9etransfer(_to,_value)
02:33:12 [WARNING] 0xe97bd9585f2499a69c5e2db8da75238d999f5e5871cbbddd28ecf1321eb12dbftransfer(_to,_value)
02:33:12 [WARNING] 0x4ceae769a687927e549f4c4c60daa35a05f0d1fa1f9c7686362eaa6780aaeee6transfer(_to,_value)
02:33:12 [WARNING] 0x356007bbf155c9012f8cbe52598264e1990173ba24b5779fd851c292ac96a3fbtransfer(_to,_value)
02:33:12 [WARNING] 0xa87f2d602452499f66d387d309c4ceba529385cbc1b18f4ea8d755bc5904a66etransfer(_to,_value)
02:33:12 [WARNING] 0x9bf073c56c17b6810b54361259c27e93f821478cdf0548477ca8715690a34b37transfer(_to,_value)
02:33:12 [WARNING] 0x97edf05344e604924b56aadb279889bc9efc2efec0a1c694ea42a86904215258transfer(_to,_value)
02:33:12 [WARNING] 0x8835c2df024fe94351cb6fd8a9146de1f42fbfa4aa9b1138c083465424b998f8transfer(_to,_value)
02:33:13 [WARNING] 0xe5c5964074be4cbee3a78d9d328cd9150b1fc67d380f7fff2dad8bab78ba0c96transfer(_to,_value)
02:33:13 [WARNING] 0x9ae2dc97981ff98b7a9035ec1f478bf8d13de52026270a9590d9a88921d71bd0transfer(_to,_value)
02:33:13 [WARNING] 0x87137a7ff09bc3f4158401a78665d5a57f55f9c18bc6dfb8b41f44e3b7e1f3aatransfer(_to,_value)
02:33:13 [WARNING] 0x9095b13278a720669e69573af3313b12ba8e592cad2cf8de93c9a36b02feef44transfer(_to,_value)
02:33:13 [WARNING] 0xbfd4cb06e452fce7a613c82cf8b7eab0731ef261b1c010a7a287bf7b1decc6catransfer(_to,_value)
02:33:13 [WARNING] 0x2c7dc32eaa75b56af62b6c56f1fdfaccd6878eba3e5f71aecd2d97ef071132f6transfer(_to,_value)
02:33:13 [WARNING] 0x955464b37adbc5d8c0c6ac336f31b0655bd4aa7389096f9a5c17d5ee9adf96aftransfer(_to,_value)
02:33:13 [WARNING] 0x35dc225a289c3827de761f758cdef0535f71f9e92b5a57de4671b48e254c06f6transfer(_to,_value)
02:33:13 [WARNING] 0xf1c22e830e87c039363facb40d176b02c7df2c40170ef55a37843bbbb0890d02transfer(_to,_value)
02:33:13 [WARNING] 0xd475229e15f743330763e35d0d6e170bb32a1314e5148c31dcbdcf31b2c51afftransfer(_to,_value)
02:33:13 [WARNING] 0xa770cac0af25582496ed413a9fd2caa33cdfacb829f0bcb62ac86fb85a6aa443transfer(_to,_value)
02:33:13 [WARNING] 0xa42c7a7dc3ac9a01c06694c96fa836f9bc02bda42accdc62f7e48bb455000928transfer(_to,_value)
02:33:13 [WARNING] 0x6b0320c6ba51f0f410309ba4aaf23c3fdb57f008387adc38183811954c71ead6transfer(_to,_value)
02:33:13 [WARNING] 0x82dd21fa6bdf2492c02a86abc77b42b9fe6f65373fee86f4dd2bc2470cd979cctransfer(_to,_value)
02:33:13 [WARNING] 0xc4d0f313dc02b7c32da916fc4180cca13932ee492ec43238b5d3009c33679964transfer(_to,_value)
02:33:13 [WARNING] 0x0f5e039e2950eabbebd56f19918f1b0b0d36f7a17c77d8066c98d1a0994ace7ftransfer(_to,_value)
02:33:13 [WARNING] 0x8125ff48bda64b3dbc3d74893fa7244be9594c660ce108537df849749da9ea65transfer(_to,_value)
02:33:13 [WARNING] 0x240d8a7f890d758434ea5119e28f2ebed18b87519a1cf5d2b0c2e8fec2ed66aftransfer(_to,_value)
02:33:13 [WARNING] 0xe38e5593102c100e11d064bd09e043f590ab7ca2f7b21163acad4ef6edfd3a63transfer(_to,_value)
02:33:13 [WARNING] 0xff41522127b0eaa6475bddbd4dcb0fefbf8973b5127dfd6cc3847380e6502c78transfer(_to,_value)
02:33:13 [WARNING] 0xe766032229dd83a0089309198bcadf49b89ff61f3086bf3c14fa87939756a9eatransfer(_to,_value)
02:33:13 [WARNING] 0x09f5b5ff0ecae6fc3f1da52b5ab32f5c4949190c7234618370d6df525cd2544ctransfer(_to,_value)
02:33:13 [WARNING] 0xb93f366b17eb76f1b23b0002e25f87f38d1f1ce5783097697f82096bfb7a0f3ctransfer(_to,_value)
02:33:13 [WARNING] 0x7d393922c83944bde3ac764db9356c9cdca3dc50f2e5cc931aca49a14b9b677atransfer(_to,_value)
02:33:13 [WARNING] 0x5cdcebf947d2ebcef2ab572e24c4b3d4c251f6802ce76b778a1fe9108b5a1eb4transfer(_to,_value)
02:33:13 [WARNING] 0xa3e75d2b985f8548e64e00cea32a4bfa7cfa2b6a8d10dd37ae193347effe1827transfer(_to,_value)
02:33:13 [WARNING] 0x55c731855bc4dd01bbeee4a92a214744efef2e2b9fc48cc3c559eebc97502782transfer(_to,_value)
02:33:13 [WARNING] 0xe84b6be5a00b9af1890b8bc1db20ed1690214e5ec1161988bb2a484e825ee4b1transfer(_to,_value)
02:33:13 [WARNING] 0x201070072bddf563806cc7ca90a94106b302b6013b59fa5ae4deb7733b924d0ftransfer(_to,_value)
02:33:13 [WARNING] 0x15f615c69d6dc060c812ed1bc27992f4164ab786367d2af1004f73b49ada6cb7transfer(_to,_value)
02:33:13 [WARNING] 0x635740740e27e2dcb91641d252d9c44395398c2fe97709741affbc39235a51b1transfer(_to,_value)
02:33:13 [WARNING] 0xbaae88958aa58ea39665ce987f60f0bbcccea4a5f5381102f7d604398debc932transfer(_to,_value)
02:33:13 [WARNING] 0x40a501f14e8504222a3ca6d2d8b841a730d60887d48650fcd88983e11bda92a3transfer(_to,_value)
02:33:13 [WARNING] 0x3b1334fad9c1f48ee72ef466a9bd4f17675ccaf339f159bf6bc07fc044d4303ctransfer(_to,_value)
02:33:13 [WARNING] 0xed25c5aac2194d3189699e59ef6fd9d86b566969eaf953d67a0ff29a3eefc3d5transfer(_to,_value)
02:33:13 [WARNING] 0x8f912bfac721cbef910eca0b9112846f4a1eac14cdab4ae68945b18471bd557ftransfer(_to,_value)
02:33:13 [WARNING] 0x90b98ce3c676889f31231db7b0a205b3b6811d86524a10fed8abbf57921ff225transfer(_to,_value)
02:33:13 [WARNING] 0xbcab66ce059c76361ac2511e4893e8cba8b6247d561ea0d7fdb1b70b20f775datransfer(_to,_value)
02:33:13 [WARNING] 0xee65fd7b1dbb9ecd892033266d0cae272f383ba15256ee714018770538149e6btransfer(_to,_value)
02:33:13 [WARNING] 0x59e6bdc3b747e21f149a3bbd6638a218d07fe05f50815907f64e3e26ffb12e34transfer(_to,_value)
02:33:13 [WARNING] 0x99ee0310ecc242efb00ffc229c8793a6a66316fa3c2167836c2b2522f1647834transfer(_to,_value)
02:33:13 [WARNING] 0x007f28eba7dfd166a0a470749a5e863baf09007cb89a4e7452ba9a488a7a3c13transfer(_to,_value)
02:33:13 [WARNING] 0x5c4812032f303752d930d27bb48d376dda8237f83a9a12597af8229c39eade3atransfer(_to,_value)
02:33:13 [WARNING] 0x9fbd86193dd03e0de25c94c8cee3a66439fba710c0733022067bbd3ef55a12f5transfer(_to,_value)
02:33:13 [WARNING] 0x9975836f27908c3b38be6c7e51650005a35afcd07eabfc50c3c49c457e1d6da4transfer(_to,_value)
02:33:13 [WARNING] 0x5b7590025f11d0471f4d1548445c0b0c74a2137e8469f35d60e2f712476065f4transfer(_to,_value)
02:33:13 [WARNING] 0xbc6916934b8436d684dce3afcc8e2974410c798b6dc697215a3684171b141422transfer(_to,_value)
02:33:13 [WARNING] 0x74b0eb0334049647d35dd865cba4d23240db21874395dd370f55b4539c0f6882transfer(_to,_value)
02:33:13 [WARNING] 0x2083df4ca41e7a9d637b56a9940ad6dd514a5bfced193291ee40a852aa89ed2btransfer(_to,_value)
02:33:13 [WARNING] 0xcc194c48b895f27992f5dae9a593562b5cd2b8e66c061eab902769a493f2ce94transfer(_to,_value)
02:33:13 [WARNING] 0x45dfcf35691c12a3f79fd81ffbd778733cb0c1dd3bcdc57fc7ce749928fdc3dctransfer(_to,_value)
02:33:13 [WARNING] 0x49e18b9f113990d97ad0dfabfa23d622d0fb58cd3c3962858678d3850ac6cd95transfer(_to,_value)
02:33:13 [WARNING] 0xc31e9754ea18a3c1846568308d3c763c9815e86495e968eef075397f8732f86btransfer(_to,_value)
02:33:13 [WARNING] 0xb949907f84b07484a64290fe680456bbf881cb79de355542ed057fb20a69b507transfer(_to,_value)
02:33:13 [WARNING] 0x77ca9c17bcbc1e6d6964bebe65c67cd9d9e59490f22316d52c36f394ca6c97cetransfer(_to,_value)
02:33:13 [WARNING] 0x77e81a9fe5013f7689e2211cb0bc763aeb4084c17363116764fb38171d64a29ctransfer(_to,_value)
02:33:13 [WARNING] 0x4f5aca7f3d16a2a3799878fa495ba878f96ff0ed97950be030001b096eec96f0transfer(_to,_value)
02:33:13 [WARNING] 0x04cf21f88b41981e17430d91fc1fab36d72e65614a71256d95fb0e2c75f49833transfer(_to,_value)
02:33:13 [WARNING] 0xbecc70ff454f7bf9198406128941db67fa34604af6fb7d722ae57e9ddbbf29dbtransfer(_to,_value)
02:33:13 [WARNING] 0xdcdc28927aca2288b3b4cf6dcfca859ca294655c4caec3778341790b41c23504transfer(_to,_value)
02:33:13 [WARNING] 0x54f2e4ed9d984d103dc8fa91725f7918e2a4e9d50447101b9ce83ff2552f1081transfer(_to,_value)
02:33:13 [WARNING] 0xfd36a14bae8d94a8b3fcc10318283029ba655a3d7be89b1896a60d7fbf6369b2transfer(_to,_value)
02:33:13 [WARNING] 0x564821dee14be9d8b28cb07cb3b15f48e327b9e26cbebc6f9ea6151dc3bc3f7etransfer(_to,_value)
02:33:13 [WARNING] 0x76e72d9ce817d7e8611284b8e125476a8c82080932dd6f03293e204d26fd971ftransfer(_to,_value)
02:33:13 [WARNING] 0xfade14b7bb43e4c209e715723d0e87e56bdf16b34f6734c6a5ba2623129983cdtransfer(_to,_value)
02:33:13 [WARNING] 0x25300d0af24cc04ffd6fb5def50dfcbffcce0b6d0f6458e348fab3ce9942188ftransfer(_to,_value)
02:33:13 [WARNING] 0xdab15c0c953360cc4b56120f2726a41e8cb3c48eabe7fccd1d90e2d6fa19e574transfer(_to,_value)
02:33:13 [WARNING] 0x717fb712e0a4d258b167e46c7fe7d5157d7eac13398603cec803fec9f22efb3etransfer(_to,_value)
02:33:13 [WARNING] 0x1f49a4f979c4c567af638e4790c682ac709e258cf7ec94153f319a47abc18f5btransfer(_to,_value)
02:33:13 [WARNING] 0x66c0bd2ab6337123bb7abd4dde8cc279d21bc9386d2e6524e84f4fc1d1e66870transfer(_to,_value)
02:33:13 [WARNING] 0xdffc5474b1f13dd2d4fb567404a230e7f19710e7653e58dbe71047bfd8e834ectransfer(_to,_value)
02:33:13 [WARNING] 0x71082d120078c08f7a4634c0200c681dc1f270b07dd836889522041de4b467b0transfer(_to,_value)
02:33:13 [WARNING] 0x7c7d3809d2cfaf691826827dd780eacf2a4fa29e00dae8b8fbc12fdce1785caftransfer(_to,_value)
02:33:13 [WARNING] 0x8798a37a5e389be430fb0e068ba64668b2fc4e8ead45f4245d5b16c49ee300fetransfer(_to,_value)
02:33:13 [WARNING] 0x1dbaca6f46a9d55a5ed259e8f026e4b540cc8a592e7cba35d4d47afe609308abtransfer(_to,_value)
02:33:13 [WARNING] 0x38e8c667f52a9ee7550dd765f31bad87446908641916355c08469ecff3057064transfer(_to,_value)
02:33:13 [WARNING] 0x0a9e6de482e1409114977cb29eaea542934f0a346759aed5ccd387e6b7ba35ectransfer(_to,_value)
02:33:13 [WARNING] 0x45a9243dccb453a14c649d44754603fd0c8a4938a62d6dbaad72ab9be553fdf9transfer(_to,_value)
02:33:13 [WARNING] 0x9d18eca79f2fd20a7ef48a135ce7abc0b89ec098f3a5f8fee07f90e9353c779ctransfer(_to,_value)
02:33:14 [WARNING] 0x0d4d1b63547a33857f2b5739cb43553a03ee459c6023a686ba0a37dbed25dc44transfer(_to,_value)
02:33:14 [WARNING] 0x4e8a580bdae58e4f7f962334df63d12c219443d268ff18bbf2c39b2abf67c846transfer(_to,_value)
02:33:14 [WARNING] 0x74742550584b19aa04168c6993864677aeb36e283055817e6978d428e6c27417transfer(_to,_value)
02:33:14 [WARNING] 0xabfd1e82c4fab9a377538a3dd03a8cb9fc5993a8adcf939f871f19716d120a94transfer(_to,_value)
02:33:14 [WARNING] 0xac37affe78ccf4c47af02a48428096655fe6a44b394e35c56fa1cfc6a29c9d38transfer(_to,_value)
02:33:14 [WARNING] 0x90a7b7a3ca9db65bab7e8cf6ec5fd1e28a76716d3bc50bb49146d491f497acd3transfer(_to,_value)
02:33:14 [WARNING] 0x42b5d63de5b6c7b28ccd0e7ae7ad907be7ba99be8a25b9eec1df87b58db6c99etransfer(_to,_value)
02:33:14 [WARNING] 0x7ba6d55b1d5e342753a848dda8393942ca0e92c134a94ee48e03ea66d2995652transfer(_to,_value)
02:33:14 [WARNING] 0x9372f605285d96a2cb21d703bb5f9dbc5bba2bb8b6a15ddee5b4c5cd76ac8a26transfer(_to,_value)
02:33:14 [WARNING] 0xbb746ea0cfa9b0193efd829437fb9abf17a2b1a457866720e4036bae7a33a341transfer(_to,_value)
02:33:14 [WARNING] 0x358844f31a1e47db158280d79e4c22847556ec6b5c1280033f9a6a10dc6bdf90transfer(_to,_value)
02:33:14 [WARNING] 0xd35ac1312e6809256833c1f41f3bf437b29072d7d20256a6513fc254b8711641transfer(_to,_value)
02:33:14 [WARNING] 0x5579cc95cde26c79d50aed9ba2b126ba923ef5691ad106360b30021a21ecb537transfer(_to,_value)
02:33:14 [WARNING] 0x8355083e5ee7a840643ad55982b0e8e6a79c7fd325dc7db66782c2b73fb5615etransfer(_to,_value)
02:33:14 [WARNING] 0xa70bc035ada4b89d6830b3e88f0c45b3a961d66ca6b9ba569a90269d68322e89transfer(_to,_value)
02:33:14 [WARNING] 0x5f607c37a3091132f8303f1ed172d84553d0da778d1991a57e5ab4b90d7d9273transfer(_to,_value)
02:33:14 [WARNING] 0x95ac0349585c60f990e72cee00922804af99059f6641c24f269a80f9793c45aetransfer(_to,_value)
02:33:14 [WARNING] 0x103939ec605f2540baaeb9ae2e22ddaf9d6b8aa1206b5f630f035e4b8ae5a31ctransfer(_to,_value)
02:33:14 [WARNING] 0x86b7238d3b10fda0fe79a355a7a395ad9c54fb589926d2fee5000cecfc35137etransfer(_to,_value)
02:33:14 [WARNING] 0x33858cfdb47c49d5ee97910117a00864fd8d3dad1183d1d96aa023f9f9b02f1etransfer(_to,_value)
02:33:14 [WARNING] 0x7057cff29121a3235a4c8caefaa1ca68ea1c1f8fed2b97b9d55fc77d9079997etransfer(_to,_value)
02:33:14 [WARNING] 0x7bca9b11585dbc0cc4d6fdace70ad78f547266d3d72adf00be33b7ad4e4b7d2ctransfer(_to,_value)
02:33:14 [WARNING] 0xceb50d4b5a48c850f1d885f80017eda121017f629f9abcddae48788d45b57c79transfer(_to,_value)
02:33:14 [WARNING] 0x49a6160cb473401c78db7a674f728270260229dce8e8eeaa3a0476a23b7a51e1transfer(_to,_value)
02:33:14 [WARNING] 0x677717bfe36c5b6240924428b6318cbcc7cab8d936a4997c800494443c1e3b37transfer(_to,_value)
02:33:14 [WARNING] 0x3514346e115a1ec6f2cd75de426e8816fc54e858b3c714e0034ebd0bee1510e0transfer(_to,_value)
02:33:14 [WARNING] 0x52ac3769026fb20b132a09b02ae6d0aeacb8d0b6c7ac9d87e6fa76784fc347fftransfer(_to,_value)
02:33:14 [WARNING] 0xa55176ece251ec58390a4294654b1b223926760e46593ec1cae362bd8bb744b7transfer(_to,_value)
02:33:14 [WARNING] 0x81bc75a9d71943d29df4930a883fe8d43803bc48b37ce2a488ebc9ec98229d5ftransfer(_to,_value)
02:33:14 [WARNING] 0xc3d91037310b3b0704a934c8cb9f63fdcbe5c6c41e09f4a3024fa2be1f8cde97transfer(_to,_value)
02:33:14 [WARNING] 0x5843ac7f508f5e7b1fd91cdf3525b7b364462534736396077e82c7245d9bb2f0transfer(_to,_value)
02:33:14 [WARNING] 0x308f73b8bd2d19759d91a43aa526bf0feebc64345e23ad5338b2d05f570f1438transfer(_to,_value)
02:33:14 [WARNING] 0x754eb1375316df8504f033daaa84b98125534e1dfec4ea7e052fd798b23500dbtransfer(_to,_value)
02:33:14 [WARNING] 0xa82ec3101f2ef99e98d507efbdb1151a3197c893cfe737426392438dd39fe747transfer(_to,_value)
02:33:14 [WARNING] 0xdd13996d7cbbc62550bdb608807111f9ddb52cd2b67dcf6f12b9da01355c13e0transfer(_to,_value)
02:33:14 [WARNING] 0x91d172a961d6ea9956a5938a79317250f8410791a07831493cfa9f831f346b48transfer(_to,_value)
02:33:14 [WARNING] 0xd033cb841ccf2c5cb7a1451042109810090f08a724e835b2ffb687a58c6103cctransfer(_to,_value)
02:33:14 [WARNING] 0x918c36bc582ec87951bb3b68603748750b19a28a77d5e0420c94a8247963bf39transfer(_to,_value)
02:33:14 [WARNING] 0xb7467216d425044bb58c1ed7ffbfbacab6bff366fce125b1c7be122915416b66transfer(_to,_value)
02:33:14 [WARNING] 0x6aeb448a67262c56a89b3cc24402dbb52fa29828ac9a543296f61c24397a1a5ctransfer(_to,_value)
02:33:14 [WARNING] 0x95b73163b1bfc6abf8be55f16b130d3c16c1b926852839762e30ff6989039e8btransfer(_to,_value)
02:33:14 [WARNING] 0x015b63ea20cefb89cfb8f44bdcfe9478aa07b329b481615bee4df02da83f0ba1transfer(_to,_value)
02:33:14 [WARNING] 0x78912767fdd95db5d2c8282dd78e5332e42ec58dc5faf95ae0d55bf4ba31fd7ctransfer(_to,_value)
02:33:14 [WARNING] 0x18f49e7ada37f06297a2fa3c972a9733f584d91b154f962ab7cab51fed74fe83transfer(_to,_value)
02:33:14 [WARNING] 0x797984a9efdbcddf6dda6f059afff0a762451b969f2e1c6eca0f4c5faad7d96ctransfer(_to,_value)
02:33:14 [WARNING] 0xb8a692fb1feae53b696ff0c3292aa2784f5d33499ec8c9b9ba9b0d7fd5c58a3ftransfer(_to,_value)
02:33:14 [WARNING] 0x8749823ea544a181a8f36f3d09284c249ac85c78a2c8fd752a0789eb612d4593transfer(_to,_value)
02:33:14 [WARNING] 0xf9eb85cb82bc188469b02321da19a577477e216ae65d3fcc6a4ff97ee43b0c19transfer(_to,_value)
02:33:14 [WARNING] 0x197e7bfd9a0784663f301735e3bffcc1f9ad6ea874e70fed0e59468369df5a82transfer(_to,_value)
02:33:14 [WARNING] 0x428ce4183d3d1066d67fbfc1a1c766b835499c2c56b30a2ac5cc1e20c1b33d26transfer(_to,_value)
02:33:14 [WARNING] 0x82d4b59c9ffb6c89616a5446eb6f0c26c8ab52a2d346e8a698d4c4946a0d1588transfer(_to,_value)
02:33:14 [WARNING] 0x0846d8d1a897f6e892eefb969dae12769d810f1cb85d99789a76736805b55c2ftransfer(_to,_value)
02:33:14 [WARNING] 0xd3a9e2f8ac35f98d6839f2c84bd415121663afb68db47b445b14bab7997f3488transfer(_to,_value)
02:33:14 [WARNING] 0x361fca919f09868379f180d1d006ff5545f78d9bdcb89e3bc55aa1bac5f912eatransfer(_to,_value)
02:33:14 [WARNING] 0x3257ad7145811c49c112a6d8c61d38aca793c00adf13122b61f76c257c2acb74transfer(_to,_value)
02:33:14 [WARNING] 0x0db2fae2c7b0380a0fca28b0682a90d78dac134354e08a42fc1abdd605fe60fatransfer(_to,_value)
02:33:14 [WARNING] 0x0387226589d32b0bb598c70a6cfb7b604f341d6e6926d447a75102a4865d0399transfer(_to,_value)
02:33:14 [WARNING] 0x03a02525420c4c18e9356a0c2e1f14b2b468424d8b2c65768bf10b20cf3adee4transfer(_to,_value)
02:33:14 [WARNING] 0x43b2dba9a96ecc8a17389d0989579ee91e44b8a911c1a49d0db065661c593d4ftransfer(_to,_value)
02:33:14 [WARNING] 0x4c7fd22433a3ab8eea585b90743f5a8b2041d07b9c1abb7cc8537992cb38243atransfer(_to,_value)
02:33:14 [WARNING] 0x318730052c2d5d1a27ef3ba391c97f45f16bf1eccab3bb258239b5a170f08de3transfer(_to,_value)
02:33:14 [WARNING] 0xfc4d7fe4ce7dbc71b8a12d95198395bcf2d917627383641ef8ac04fff0b23584transfer(_to,_value)
02:33:14 [WARNING] 0x9eacbac27e6cbca3a8556a687cc2c8a30c173e4cb590c415714b30ebc847251btransfer(_to,_value)
02:33:14 [WARNING] 0x4d89f6c4a6c26bcfae55c847c5a2c38061667b180872426cb0913a66483c0efbtransfer(_to,_value)
02:33:14 [WARNING] 0x82bc60aa11d03304ff3c54ef81c7a950db38733b421eedfa42005d774907e821transfer(_to,_value)
02:33:14 [WARNING] 0x645d6ed56d95d8a6eb8c6c2f78414340240c3171f99b55bd74cfcc304b977449transfer(_to,_value)
02:33:14 [WARNING] 0x1dd9617a30547353fd31b5cc284057d1e5568f111f7fb71eae3c10b04fead48dtransfer(_to,_value)
02:33:14 [WARNING] 0xed1f9cf54767e350db599ea7fcfd0352fae11c88f80f6e96e0b76c409c94b549transfer(_to,_value)
02:33:15 [WARNING] 0xfd2db38950d26303944d980eb1ffde5715126a995e064eca5882ec5c7a219f75transfer(_to,_value)
02:33:15 [WARNING] 0x5a590def77e7ea872c6c16cdc5514fd803c2a70d9beeb1cef309f5f3c1d81d8atransfer(_to,_value)
02:33:15 [WARNING] 0x25a76384dc5677d5d0a2d03e06b835902202b0e3866d1fde505553954d96688atransfer(_to,_value)
02:33:15 [WARNING] 0x8babfe1eb02207952e9c21acd168dd9a58979fcaba6bd0ab559ec6d4758967c6transfer(_to,_value)
02:33:15 [WARNING] 0xa624b988999da23596b9f3e987500b35dc56b13947b693724f9b6e40502d5bb8transfer(_to,_value)
02:33:15 [WARNING] 0x9b00e18c0eccaadd677119682808f42b4fa68e40cb5cb3ca563dff5fa03b1feftransfer(_to,_value)
02:33:15 [WARNING] 0x1feacb3763ff20085ef630be1e04b93b465a064809bc1003d0667622d6ccbde6transfer(_to,_value)
02:33:15 [WARNING] 0x8ee2cbc1d9cefa3d7242d35f7bf119cd55774809ae00370cff80535779a1b004transfer(_to,_value)
02:33:15 [WARNING] 0x6ea4094916fce5daf2d77573f5032655f289e565709c10b36ead0be70fb1f7b8transfer(_to,_value)
02:33:15 [WARNING] 0xbce9851ecab8ebde5d80aa36da81ee9ddbac72eb67c5ee9c97e701c93e57506btransfer(_to,_value)
02:33:15 [WARNING] 0xd3cf4dd69174ae0138a6f5d3a172da210a1e1b76f1ad9cc2eaf6b54d1f9cfa5btransfer(_to,_value)
02:33:15 [WARNING] 0xc4d0caeb07375af96830fcc60eaa4fda9a6536ebb0c33b7d5a9584ddc3a7f248transfer(_to,_value)
02:33:15 [WARNING] 0x73dab0664ac3626a71244b5318501105f4e74d246f34f70bd66b9b0d0bb186b4transfer(_to,_value)
02:33:15 [WARNING] 0xb7755c9d17dbf95086c94d56bc8201f7e7a75da8b2a0aab28c37315155fb0919transfer(_to,_value)
02:33:15 [WARNING] 0xe7c490415537764271f5cd7992e666947f526d9125af3de51fdfe058cbe92588transfer(_to,_value)
02:33:15 [WARNING] 0xaababae983e95a0126e2024b117b80a7028b00cb7baff1efbea939f1d59fa519transfer(_to,_value)
02:33:15 [WARNING] 0xf7cd0e5871dced4218800fc9f54df5347e01e50db44ad5423d3255ed960c53ddtransfer(_to,_value)
02:33:15 [WARNING] 0x4d902d539a8cfa4266e91a2db3e070412265c81120b43e9ed9162c9fcfe6e2f9transfer(_to,_value)
02:33:15 [WARNING] 0xdcaba74eb4fb6778729b68c81e74629667c3a64c3ab1ec8e12b56d4cbfe7cdebtransfer(_to,_value)
02:33:15 [WARNING] 0xc39a72e05a016d5eb12c8c575d6973dbc13ed31342914bf8180182d8df5c375btransfer(_to,_value)
02:33:15 [WARNING] 0x63e09f5d2785def4c2d5206870c2f83946cc82344162738594ebb2b520e1a036transfer(_to,_value)
02:33:15 [WARNING] 0xe418b76f659ea3cce45a6773866ef0516412192bf8b5103eae70ae716936aed4transfer(_to,_value)
02:33:15 [WARNING] 0x4b91c2666a404408ffd6bed462fcc959ecc2ad52add364955c6e5f55d8ec3f3etransfer(_to,_value)
02:33:15 [WARNING] 0x3c3f10929714c38e8ec34331832863d799c732740ab9fcf8cd0264f4a1a33bf3transfer(_to,_value)
02:33:15 [WARNING] 0x8811aac5144d6da5ba98a076f7787f6f03377136b54ca0ff60b9af6b245ed90btransfer(_to,_value)
02:33:15 [WARNING] 0x44a336d4fbef3384561dd75b32924ed5cb6a989c8a94bf89f791c4b0f2423ff5transfer(_to,_value)
02:33:15 [WARNING] 0xf5491f85acb3a9e6e83286c62195707209c0e620fabd62ccdac9144123c88f4etransfer(_to,_value)
02:33:15 [WARNING] 0x5bbf38a737b23a6b04afa83934977e87ac29aba70bcdf785d56f19c38ec821ddtransfer(_to,_value)
02:33:15 [WARNING] 0x06fb22ecd74833b532c74b251ed2174657ed13c0c11e96e0d3f13ed10ee35a00transfer(_to,_value)
02:33:15 [WARNING] 0xbd11761ff738183e8376617ea9db0424e3e1c14ae5d497c116d133c4902d470ftransfer(_to,_value)
02:33:15 [WARNING] 0x547f851b82814ce164f074d9195ef6cafb53f9de76d8b46783c43ea852554fe7transfer(_to,_value)
02:33:15 [WARNING] 0x62116b225789f9534b0949e73ed528a3790c5b2b9f945820c2d1804c3a2b071etransfer(_to,_value)
02:33:15 [WARNING] 0xab31aebd26f222237de90e734e77fab3627315ee59abf5dc5d133dc2f7b3e05etransfer(_to,_value)
02:33:15 [WARNING] 0xba8105e8869a220bc1087d5122e3efdfa8e39232b0f908069943a912749b2ce3transfer(_to,_value)
02:33:15 [WARNING] 0x334b328a5c4436c7d627635fc7a1db68f1da21b13ee7807771d422ce8ef10ea8transfer(_to,_value)
02:33:15 [WARNING] 0x0aa36a0cc969fae1c1364b175dabbaa3f95b7219fbc6d5bc7d9aef424cb5e5cetransfer(_to,_value)
02:33:15 [WARNING] 0x5be8e1404db8facf8bbd57ab0100373207e85ec68f080d2f6e634ac80f770a47transfer(_to,_value)
02:33:15 [WARNING] 0x9f2bb781df16c813e601b8e7891984cca69a763783faa62a321cebb375105d48transfer(_to,_value)
02:33:15 [WARNING] 0x7c3e7fd4eda71e81adc904db28ae3892a28b648813f0e40df07d1df8d12a579dtransfer(_to,_value)
02:33:15 [WARNING] 0x917524686bfabc549a0269007d7a23c5460a5021f5403b757d72632c515be4abtransfer(_to,_value)
02:33:15 [WARNING] 0xbeea3a3892562bbc997f877d906a3831814c1a3fcc0744deeaa28303795d8bb5transfer(_to,_value)
02:33:15 [WARNING] 0x8eca27bf8e065a800f4195149037def32a92708eae2ca0f102382fbefd905b3ftransfer(_to,_value)
02:33:15 [WARNING] 0xc25f2b13679337a2142951b66ee28ece19e7ae3253df1a4f4516693e2b3ec9d6transfer(_to,_value)
02:33:15 [WARNING] 0x13951a8c2485cfdfce60b5b72c6875e1ee2199e8b8752785a99a1b60077b859ctransfer(_to,_value)
02:33:15 [WARNING] 0xe0bec90c7f744b77b0ee5d839b3c22f62739b5b729d7c7b02ee556b2d389306ftransfer(_to,_value)
02:33:15 [WARNING] 0xbca642b332e42e512832f660974222d64dbdd071a433068edd62dff7f616ff08transfer(_to,_value)
02:33:15 [WARNING] 0x32dc626e058a8306c52661ffdef7b41cb896501cb6aaf0bf195199912069e354transfer(_to,_value)
02:33:15 [WARNING] 0x633ac056b565fc078511443a16827c61d4a3717d84fad7f52e9a0d68d168433atransfer(_to,_value)
02:33:15 [WARNING] 0xaea29ee3acb06ef48bbd417cd5fb47024f97cf21adb069624260bf1681c35491transfer(_to,_value)
02:33:15 [WARNING] 0xf0f80dd3d0282c5ab79a9601675c12a394ed2fcbe1e54a9b4256f70a5f49a4a0transfer(_to,_value)
02:33:15 [WARNING] 0x297a4daa456738e830a9ac5a7f1e55ae79212889c8cb6f35ee120e62c3c558f1transfer(_to,_value)
02:33:15 [WARNING] 0xdbee0e31b80731e6377623ddfe57fc2e2f755cee4e66a59408cb0af38ef62b63transfer(_to,_value)
02:33:15 [WARNING] 0x6b0e9e0caa576ee4bb49db400ac2462d85862c3be890e86531a29eeae86b6baftransfer(_to,_value)
02:33:15 [WARNING] 0x32f79a71c8a0a92222f7576384cf97c5c1bbcc3770bbc03137409683a281c57ftransfer(_to,_value)
02:33:15 [WARNING] 0xf18661efb8d3108f2896cde9439b75aecddf6159a895cdfb71e4ec8acb86e699transfer(_to,_value)
02:33:15 [WARNING] 0xe2e7858a29afcb585b2f384748489df71128ccb800ac379dc38227d367375c4ctransfer(_to,_value)
02:33:15 [WARNING] 0x22d1cec192bef0bccdbedbc3eaa153134cff8ae7ae67f0d1baa3d38ac49ba022transfer(_to,_value)
02:33:15 [WARNING] 0x3ab4dff33785cc5aed6ad404e2e54a9660191bd5819443c770cafca97f5956detransfer(_to,_value)
02:33:15 [WARNING] 0xb1a03083c5fc9220c8c34ceeac70ae52b5f14c06fc28f4fc84ceba90c24766b2transfer(_to,_value)
02:33:15 [WARNING] 0x406e24a035ceeecf4e7cd1cc5efd109d19d333203c48c2b229659aaed863b8b0transfer(_to,_value)
02:33:15 [WARNING] 0xd4e63eefc5776cd3c1ab1e95a4bbf1d58abc65221c31c7f02f5bc2152d6db266transfer(_to,_value)
02:33:15 [WARNING] 0xd3d35cb8e84df5d8524e35c27d483794515a1c8f3f47c0e3e002620cf169348btransfer(_to,_value)
02:33:15 [WARNING] 0x085c2bdecaed23ba793f72b171a4a8927bec84cf639af3d6ddbf064934738a35transfer(_to,_value)
02:33:15 [WARNING] 0xd2d89bdb2c7834cc37b7158dbd459234c0b6bdf1afdd18b087052c55fba3cea1transfer(_to,_value)
02:33:15 [WARNING] 0x42c6a839654b851f257b5d57a87eeefc22792fa40688f7c99096ff5abd04620atransfer(_to,_value)
02:33:15 [WARNING] 0x1a089add6566ea5d84763c30caa0d87e252b55580e5db0aad2395575acebc6fftransfer(_to,_value)
02:33:15 [WARNING] 0x173ad6b9813e34a9162890994eaf9701013f90e9dd73e2a8aca31e285dd9222btransfer(_to,_value)
02:33:15 [WARNING] 0x5bddcc777a6f7567f3a40b15cfedfce61123631dc252a993a8659559ee12d00etransfer(_to,_value)
02:33:16 [WARNING] 0x6cec91f02f908b7418ec164ca4a62384947485f93dc3a23e7cfbccee3bbabb60transfer(_to,_value)
02:33:16 [WARNING] 0x60c7a2be67e7d7ccea30e21b8820da4149b77a6a4e1b18178322d545a6f4b500transfer(_to,_value)
02:33:16 [WARNING] 0xf4f54ea9e655b4cb0a8515a4ba1907f12f8683bc441b91bbf5802cf68f895612transfer(_to,_value)
02:33:16 [WARNING] 0x11325b795b8ea349ff6a7d3bd376ec9c3f1c20a4698a3cf5dbfdd4dad2cacbd0transfer(_to,_value)
02:33:16 [WARNING] 0xcd0a330bbc92b9c7dc6977c6f61b777eff8c0bddbc994ece53efc28e11dff683transfer(_to,_value)
02:33:16 [WARNING] 0x9f27f45c5d5c29f5ae82c752597e874d78ac8831af3fb6b8ee40a20324c3b288transfer(_to,_value)
02:33:16 [WARNING] 0xaae0842fab6ba5918c5160cb69e5ce435d9a233d35b9b08f00361a280ea18673transfer(_to,_value)
02:33:16 [WARNING] 0x2d8016b8dde2adc0e647448ea5a7837510ec89c37988e7053466fece02bd7397transfer(_to,_value)
02:33:16 [WARNING] 0x80a0a876c63ae978ff54573fc1c16bf263e6461ee313ef04e4406b4b7c6c2d37transfer(_to,_value)
02:33:16 [WARNING] 0xed63bae68a1ebf84ede01de2b8624d1323c20e3ff04c348f5c66cc88c78be794transfer(_to,_value)
02:33:16 [WARNING] 0xd33b57452ac2b248b03a1c893e4e49d357b1d5d3ff2cb5cfd60f1f400c83b6d4transfer(_to,_value)
02:33:16 [WARNING] 0x791d52f659e4082c8e819b33fd7cee454a7c0b91146e8ea7b5cee1dbd98dc976transfer(_to,_value)
02:33:16 [WARNING] 0x1f138f348387e7a15679a20e2804acdf74da0bf0aa69b5aa84dec2b9a682853atransfer(_to,_value)
02:33:16 [WARNING] 0xac70fdabf963800c6845dbf6d72a724db07b1df62c77ab3fb63ff8a20b320624transfer(_to,_value)
02:33:16 [WARNING] 0xd505ed588a5336f2f08f3d527a6fb8111471be0a3b07cef25e4526f5815158e4transfer(_to,_value)
02:33:16 [WARNING] 0x35b028cbf61301a884894bc99d5db7cc849aacb1331f0342f7fe668ceffcec4ftransfer(_to,_value)
02:33:16 [WARNING] 0x0d20e074ac0d24018e9b07000dd4bdb7831a6bfd179ad9f71d3a497914d70bd7transfer(_to,_value)
02:33:16 [WARNING] 0xdf3098c1655411ee6d4a8b1fee0ff125d40c664b8b9104b88931d63234ba0958transfer(_to,_value)
02:33:16 [WARNING] 0x752af80b38871d0a0307d84a5e00caa1901777b6e97838c538a360ff4412e7e9transfer(_to,_value)
02:33:16 [WARNING] 0xa5f35427859c27d44856c88de56ca4c617188782d110bcf63515b05d61d02d19transfer(_to,_value)
02:33:16 [WARNING] 0x45b4f111a65f9617dd2a8090b0ce6db859b39624b2f11046e6ee48713c267859transfer(_to,_value)
02:33:16 [WARNING] 0x4e72ea474e57c646dca0f3d4b4ae887a3a3675ad8c1acfb7658bcba3405279f2transfer(_to,_value)
02:33:16 [WARNING] 0xfd08564d2be6b8c33da76c81bcca1d91fda33bc88433917e60ca1cd8e351b531transfer(_to,_value)
02:33:16 [WARNING] 0x1eb957a8563a07bc6b13bbae9245f3afd4e7b6c38dd6bdf9ee24e82d99d87e66transfer(_to,_value)
02:33:16 [WARNING] 0x5dba7f84852a5d3c7e0c8c5cabfa4630dd817f947649319cf34868b69e22fc26transfer(_to,_value)
02:33:16 [WARNING] 0x6bfa122d0865a1765aba85233df37cf7901c76a37e6646272c42525121e51ec2transfer(_to,_value)
02:33:16 [WARNING] 0x0db6d4942b62e59204aba06503a96814214d001be14d0e34fd296d2d842111a1transfer(_to,_value)
02:33:16 [WARNING] 0xf26a94ec76316da4184423e421bb0b3e025338adc07dff04029d3ecd4fafdb75transfer(_to,_value)
02:33:16 [WARNING] 0x04940511176d13d3d59271721f110b3d4c625982463bdc910635be072fcfaf2dtransfer(_to,_value)
02:33:16 [WARNING] 0x8e84bd29c0cd5161e19c96016e4ec7a892f5150eb74cb4391832e64b4647a701transfer(_to,_value)
02:33:16 [WARNING] 0xbfc42f7e3e59b1678665ba7693cbea6f9024ad93f09f6fa4edc8bd9fb3fd2973transfer(_to,_value)
02:33:16 [WARNING] 0xe977ba0a87277307cd331b92e5dba805baf707c674f1a0c5d3b64338ab2c0e0ctransfer(_to,_value)
02:33:16 [WARNING] 0x2b88ee8994094bfd0986e17f92d9d5a99773c42de1cc23306f4e9ecb56645e2etransfer(_to,_value)
02:33:16 [WARNING] 0x0a88ebad2eded08f80c1271e317c59c6dd1eaac76a5f1231f7609097ecb9ca2ftransfer(_to,_value)
02:33:16 [WARNING] 0x8d4e73f1ce99c2822b47677d70691e23a84662746cd06c51250ded3acf4ab7adtransfer(_to,_value)
02:33:16 [WARNING] 0xa6d97ad91bdaea668cd13e8c5b92a6296b987c9b6598f428bcdbb6e2eaf12b7atransfer(_to,_value)
02:33:16 [WARNING] 0xa81a22e1360d72f6d3eb940d933037e0639364d767552a6d3ae40d3916ebcb90transfer(_to,_value)
02:33:16 [WARNING] 0xf194d8fc5ab30d9258df89aff7a985e298f5c5720b562013a8e7538d7dc32f36transfer(_to,_value)
02:33:16 [WARNING] 0xb77f4053066c2d87ac12119835f65af6c230d20300ed61d789e0a72a0df4eecatransfer(_to,_value)
02:33:16 [WARNING] 0xf910373048f8cff5a73c988a9f1fb9d371ae826964e3e2854837310cf8c8df1ftransfer(_to,_value)
02:33:16 [WARNING] 0x118a28f54a25e65c138a0152025e37f551c5804fe5ac41b7a0a46d993ba611eatransfer(_to,_value)
02:33:16 [WARNING] 0xb4ce97b186273df78b089a2289b1dc1cf1d90441039be86517b2a0423a551164transfer(_to,_value)
02:33:16 [WARNING] 0x2a71402383648de2c986ce366f439fb7d1499aabdf0f78c073bcb2d66a4aaae5transfer(_to,_value)
02:33:16 [WARNING] 0x484d345aa5824e3bf97b0edb01197dbc41c7f2e95b7dbf7f173fda5d819d67b2transfer(_to,_value)
02:33:16 [WARNING] 0x41cd684f4d007f7f2aaabe92298ce6deee6b396d7047d4b8d3d00ddf86e469f9transfer(_to,_value)
02:33:16 [WARNING] 0x1447daf9c6ee2d38f2ae11ea9e54e1d92afc2c71d5c7af1f3755d877ec1d6c36transfer(_to,_value)
02:33:16 [WARNING] 0xe0449d132a0432aa5dbdef261bc17745770dca17582586467d5c4a472116dbfetransfer(_to,_value)
02:33:16 [WARNING] 0x6d8db30b635c65a3e96e4062b72e13dad7af17c191756a071364de6413d59356transfer(_to,_value)
02:33:16 [WARNING] 0xa869603246212a245fc605158f338d8059259f4a68a345803c974e08054573b6transfer(_to,_value)
02:33:16 [WARNING] 0xb7cc731d974db9eb342ffae71c397878294b3c7a53b4e683c61ab965abdeccf9transfer(_to,_value)
02:33:16 [WARNING] 0x69f4bfbe10fa4638c8595882f91ae81301e7f2b8cc60b3f85c61a5f37b2c2b70transfer(_to,_value)
02:33:16 [WARNING] 0x6505ac4de3db06d320a914b2bf38776db9090c194fbc8106ada779948fe8bbb3transfer(_to,_value)
02:33:16 [WARNING] 0x53541cb5afb667a81b43328c6d64c815b03370b764ef5287b389fe55a871e2d8transfer(_to,_value)
02:33:16 [WARNING] 0xd7cc162876e0a5e05c56d23701b3a849a29c597bfebfd1085aa44d03a701687ctransfer(_to,_value)
02:33:16 [WARNING] 0x15adfc35a3bf3b9833e41a99f1e24ffb526948b900c3a71dc454ed9610202dcatransfer(_to,_value)
02:33:16 [WARNING] 0x3b34767cd9aafef00dc4b0f6f7940cfeccedc67da97a2ce34bc537aefac23b6etransfer(_to,_value)
02:33:16 [WARNING] 0x3d1613f6242577b7a9e4ad7281c56b9bdff17e9526a20ab17c0cb818435af9b2transfer(_to,_value)
02:33:16 [WARNING] 0x1ac183a649cd57e8259982c2ec07381afccafabb0f8194482384541c592b42catransfer(_to,_value)
02:33:16 [WARNING] 0xe45c086ea9dcb2af0d1b329e52b5ecc4d9828e64b8cf4989125ec3b6b455bef7transfer(_to,_value)
02:33:16 [WARNING] 0xaaefa1f5203d50bdb3ea9b1a54585a17934ba94778be5d770ae6bc68dd631a79transfer(_to,_value)
02:33:16 [WARNING] 0x610ebec11efefa675e41f597c0adfa30133dd23ec7af18777154a7de914c659atransfer(_to,_value)
02:33:17 [WARNING] 0x59487e2e27af4a27b94dfc18f2358259d37d52db7020c85ae29889f1e3edf234transfer(_to,_value)
02:33:17 [WARNING] 0xf39ca1ec7cea153689871ee0ea12666066d7cc1eb9d8e7c0925fe66354c5ee49transfer(_to,_value)
02:33:17 [WARNING] 0x0224166d7e92cfd49de04dadc5d7f44870fd86216fcd0b8bac3d13022e43de93transfer(_to,_value)
02:33:17 [WARNING] 0xdf9fcd6dfad0ada68161b20d332e2e22d0e58b5b00a621d684389f2f8ad98636transfer(_to,_value)
02:33:17 [WARNING] 0x0f50aa041474f6db4c46f4deee2e3ce21e9e4f5f704b504a89ec9649b33be416transfer(_to,_value)
02:33:17 [WARNING] 0x043279eaf0b977ac00da3428b31744a042ca3bcedad871c3f8d0fc41e1ed1359transfer(_to,_value)
02:33:17 [WARNING] 0x40fe28b03b9f981beecb55ad48408445b35a08e229f9a253d2d1acb69ae8b864transfer(_to,_value)
02:33:17 [WARNING] 0x8f32c6090f4ad3c8aa5bcdf4e5d54158264da33b0f338161c4011d07ddf46ff7transfer(_to,_value)
02:33:17 [WARNING] 0x9df858056baaa1608319354ff541280ff8dbda150d96beb5982c43b83583ef3ctransfer(_to,_value)
02:33:17 [WARNING] 0xba757959989e37bf20b88ae597aec7d84c225e462680e4de1f4e9bcd1456fcf2transfer(_to,_value)
02:33:17 [WARNING] 0x76228477acc3b04f44afc8d43c92504c17ed8d18bd0330a34a2cebc05142b68etransfer(_to,_value)
02:33:17 [WARNING] 0x45ebd2cdc161be3171f9a8a76dfc32610c0290e2a98f4603a96fd1eb909890e2transfer(_to,_value)
02:33:17 [WARNING] 0xfe75a7701f2fe006468ef96377d096c0deddabd9d70f03ac73e48e03821fba5ctransfer(_to,_value)
02:33:17 [WARNING] 0x7bbdddbd8e86443275ea164aec92ca3a258bb6c1b6fb49ec8a37942b85875d00transfer(_to,_value)
02:33:17 [WARNING] 0xd169a80697e95a3ab040d6c1d5462ab4f1b1f7f86ae4ee3269139347797f3cb8transfer(_to,_value)
02:33:17 [WARNING] 0x974e0c61e26891335957b3a7a58cd28db369b4e8d6febeca84fb012001e27f46transfer(_to,_value)
02:33:17 [WARNING] 0x70db8689da71e57d28bf4cd1a761b168a2c75e907067fddcbd7ea36e549a4156transfer(_to,_value)
02:33:17 [WARNING] 0x8a3db47c0321a922aaea73de7297ffc7296b958a5db99366cd69e2da0e4b7507transfer(_to,_value)
02:33:17 [WARNING] 0x1c0641c40afdebc5d2fab4905e6abe76ea0de3867ee56a0c93d45b6ea41ecc0etransfer(_to,_value)
02:33:17 [WARNING] 0xe811304f9b5ac1098ae0712dd5e0ffacaedadb542ea062e96caa9e0f40ce223dtransfer(_to,_value)
02:33:17 [WARNING] 0x2e8d9f27ad6e34816cf39698d5e166dcb424c2c70a71093969df8276e44c90f3transfer(_to,_value)
02:33:17 [WARNING] 0xafa53e39a5c14d4221d1715daef1aca9a090d425e76d005cd94dfe716c22a1b0transfer(_to,_value)
02:33:17 [WARNING] 0xbdb9e726076264f82af9de28a0dbc71af43c9f034eed15f01a91661ae433221etransfer(_to,_value)
02:33:17 [WARNING] 0x070136050a1255322d8b7e017ccbecbc7a9d09e28fe41569a6a18056699780eftransfer(_to,_value)
02:33:17 [WARNING] 0x3d3deaa55f7bf3f35099d1dc6008958532aebe4fd23484f807227da448bebdf3transfer(_to,_value)
02:33:17 [WARNING] 0x5c76cc62bf18c9197ee5236c604596df518c0be3101f1bff05e1dece4d6d8759transfer(_to,_value)
02:33:17 [WARNING] 0x089f1313fc017cc82d481a94853e981e8b64f69c2e35d1a6228004f386eda638transfer(_to,_value)
02:33:17 [WARNING] 0x7cd22dd16b23e027ad5d940581b84b92d090e924e00b4d7e735db08322aa31detransfer(_to,_value)
02:33:17 [WARNING] 0xbb5d6a3c3e551402135fb06d2a1af9daaebcde7617b7e11c7d304a638b08e823transfer(_to,_value)
02:33:17 [WARNING] 0x484281969e02b753b4f38eecdbc4b668b6f008d9ee906440d0020d147ecb9e9dtransfer(_to,_value)
02:33:17 [WARNING] 0x31acbcf1b0c5b0ca034ec1e03c2a032b69f3df86042cf198bde808f3075ba4eetransfer(_to,_value)
02:33:17 [WARNING] 0x4b6fd5b359fb4d0c1edd00fb2c17288a6ef6c2959272388e12f939a766da8094transfer(_to,_value)
02:33:17 [WARNING] 0x4477176933a12bb774fc3d31e0adeffb37d0dcaa61ec232c82b99eae9a84224dtransfer(_to,_value)
02:33:17 [WARNING] 0x9a6ad9a5ae03663674e148d7091b014ea256afab0fb15ca9dc95fee4c6d467c9transfer(_to,_value)
02:33:17 [WARNING] 0x2f2eb316f55471b8d3441b7258ea0c3a6d048ec0307372d388fb370d71a004cdtransfer(_to,_value)
02:33:17 [WARNING] 0x0be4b1761c49d2f8c800920ff522019e64f2153539a435ef445db69978f2860ctransfer(_to,_value)
02:33:17 [WARNING] 0x45e678c2409f4ac636be9a6a1123425ad75b6184c29d543e1e26a54ad5d01095transfer(_to,_value)
02:33:17 [WARNING] 0x67a59328617aaf569c27444de5b5b9572544864feafbbd88e8e3b24748658e89transfer(_to,_value)
02:33:17 [WARNING] 0x85bc0d60c04cc1d5789393ef8079fdfed7bd596be49697a9d55e8a1796bf5671transfer(_to,_value)
02:33:17 [WARNING] 0x84f5d87a4553cd2c257e2d895359b7427aaa90d2e1fd5839e859c7149d049f4atransfer(_to,_value)
02:33:17 [WARNING] 0xdb0da9b39b90526e9376aaf62b184cae661a3b1582cbfa01e79f7b3fc683d754transfer(_to,_value)
02:33:17 [WARNING] 0xe91c1a100289db3f2c7c4fa736651c1b88a469c444710c0d9206c83533dbb835transfer(_to,_value)
02:33:17 [WARNING] 0x18ef435d419db32c162678000a236e548ced53f7cb07f1877be8756accc43d6etransfer(_to,_value)
02:33:17 [WARNING] 0x9a868641e95236490919b95277dbeac95b412e50c343e49d145a6904f065adb2transfer(_to,_value)
02:33:17 [WARNING] 0xa566928664061e197917963cd59939222b8e8805a768d9f82755737dd2d22a08transfer(_to,_value)
02:33:17 [WARNING] 0xd343df4a2436144fa5bd3d277251b3660166741b2e9b94067d600e03050627d9transfer(_to,_value)
02:33:17 [WARNING] Generating invariants... for 499 txs
02:33:17 [WARNING] Time used: 2899.0556149482727 seconds
02:33:17 [WARNING] Time Usage Detail: initializePpts(2892.2272398471832), readTx(5.529199123382568), processData(1.2149944305419922)
02:33:17 [WARNING] 

02:33:17 [WARNING] approve(_spender,_value)
02:33:17 [WARNING] PptType.EXIT
02:33:17 [WARNING] TxType.NORMAL
02:33:17 [WARNING] 
02:33:17 [WARNING] 

02:33:17 [WARNING] approve(_spender,_value)
02:33:17 [WARNING] PptType.EXIT
02:33:17 [WARNING] TxType.REVERSION
02:33:17 [WARNING] 
02:33:17 [WARNING] 

02:33:17 [WARNING] transferFrom(_from,_to,_value)
02:33:17 [WARNING] PptType.EXIT
02:33:17 [WARNING] TxType.NORMAL
02:33:17 [WARNING] 
02:33:17 [WARNING] 

02:33:17 [WARNING] transferFrom(_from,_to,_value)
02:33:17 [WARNING] PptType.EXIT
02:33:17 [WARNING] TxType.REVERSION
02:33:17 [WARNING] 
02:33:17 [WARNING] 

02:33:17 [WARNING] transfer(_to,_value)
02:33:17 [WARNING] PptType.EXIT
02:33:17 [WARNING] TxType.NORMAL
02:33:17 [WARNING] ori(Sum(balances[...])) > 0
ori(Sum(balances[...])) == 10000000000000000000000000000
ori(Sum(balances[...])) one of [10000000000000000000000000000]
_to != 0
msg.sender != 0
_value > 0
Sum(balances[...]) > 0
Sum(balances[...]) == 10000000000000000000000000000
Sum(balances[...]) one of [10000000000000000000000000000]
balances[_to] > 0
totalSupply > 0
totalSupply == 10000000000000000000000000000
totalSupply one of [10000000000000000000000000000]
ori(decimals) > 0
ori(decimals) == 18
ori(decimals) one of [18]
elem of balances[...] is one of [10000000000000000000000000000]
decimals > 0
decimals == 18
decimals one of [18]
ori(totalSupply) > 0
ori(totalSupply) == 10000000000000000000000000000
ori(totalSupply) one of [10000000000000000000000000000]
ori(balances[_to]) one of [0,1000000000000000000,165000000000000000000,100000000000000000000,103000000000000000000]
ori(balances[msg.sender]) > 0
msg.value == 0
msg.value == 0
msg.value one of [0]
ori(Sum(balances[...])) >= _value
ori(Sum(balances[...])) > _value
ori(Sum(balances[...])) != _value
ori(Sum(balances[...])) == Sum(balances[...])
ori(Sum(balances[...])) >= Sum(balances[...])
ori(Sum(balances[...])) <= Sum(balances[...])
ori(Sum(balances[...])) >= balances[_to]
ori(Sum(balances[...])) == totalSupply
ori(Sum(balances[...])) >= totalSupply
ori(Sum(balances[...])) <= totalSupply
ori(Sum(balances[...])) >= ori(decimals)
ori(Sum(balances[...])) > ori(decimals)
ori(Sum(balances[...])) != ori(decimals)
ori(Sum(balances[...])) >= decimals
ori(Sum(balances[...])) > decimals
ori(Sum(balances[...])) != decimals
ori(Sum(balances[...])) == ori(totalSupply)
ori(Sum(balances[...])) >= ori(totalSupply)
ori(Sum(balances[...])) <= ori(totalSupply)
ori(Sum(balances[...])) >= ori(balances[_to])
ori(Sum(balances[...])) > ori(balances[_to])
ori(Sum(balances[...])) != ori(balances[_to])
ori(Sum(balances[...])) >= ori(balances[msg.sender])
ori(Sum(balances[...])) >= balances[msg.sender]
ori(Sum(balances[...])) > balances[msg.sender]
ori(Sum(balances[...])) != balances[msg.sender]
ori(Sum(balances[...])) >= msg.value
ori(Sum(balances[...])) > msg.value
ori(Sum(balances[...])) != msg.value
_to != msg.sender
_value <= Sum(balances[...])
_value < Sum(balances[...])
_value != Sum(balances[...])
_value <= balances[_to]
_value <= totalSupply
_value < totalSupply
_value != totalSupply
_value >= ori(decimals)
_value > ori(decimals)
_value != ori(decimals)
_value >= decimals
_value > decimals
_value != decimals
_value <= ori(totalSupply)
_value < ori(totalSupply)
_value != ori(totalSupply)
_value != ori(balances[_to])
_value <= ori(balances[msg.sender])
_value != balances[msg.sender]
_value >= msg.value
_value > msg.value
_value != msg.value
Sum(balances[...]) >= balances[_to]
Sum(balances[...]) == totalSupply
Sum(balances[...]) >= totalSupply
Sum(balances[...]) <= totalSupply
Sum(balances[...]) >= ori(decimals)
Sum(balances[...]) > ori(decimals)
Sum(balances[...]) != ori(decimals)
Sum(balances[...]) >= decimals
Sum(balances[...]) > decimals
Sum(balances[...]) != decimals
Sum(balances[...]) == ori(totalSupply)
Sum(balances[...]) >= ori(totalSupply)
Sum(balances[...]) <= ori(totalSupply)
Sum(balances[...]) >= ori(balances[_to])
Sum(balances[...]) > ori(balances[_to])
Sum(balances[...]) != ori(balances[_to])
Sum(balances[...]) >= ori(balances[msg.sender])
Sum(balances[...]) >= balances[msg.sender]
Sum(balances[...]) > balances[msg.sender]
Sum(balances[...]) != balances[msg.sender]
Sum(balances[...]) >= msg.value
Sum(balances[...]) > msg.value
Sum(balances[...]) != msg.value
balances[_to] <= totalSupply
balances[_to] >= ori(decimals)
balances[_to] > ori(decimals)
balances[_to] != ori(decimals)
balances[_to] >= decimals
balances[_to] > decimals
balances[_to] != decimals
balances[_to] <= ori(totalSupply)
balances[_to] >= ori(balances[_to])
balances[_to] > ori(balances[_to])
balances[_to] != ori(balances[_to])
balances[_to] != ori(balances[msg.sender])
balances[_to] != balances[msg.sender]
balances[_to] >= msg.value
balances[_to] > msg.value
balances[_to] != msg.value
totalSupply >= ori(decimals)
totalSupply > ori(decimals)
totalSupply != ori(decimals)
totalSupply >= decimals
totalSupply > decimals
totalSupply != decimals
totalSupply == ori(totalSupply)
totalSupply >= ori(totalSupply)
totalSupply <= ori(totalSupply)
totalSupply >= ori(balances[_to])
totalSupply > ori(balances[_to])
totalSupply != ori(balances[_to])
totalSupply >= ori(balances[msg.sender])
totalSupply >= balances[msg.sender]
totalSupply > balances[msg.sender]
totalSupply != balances[msg.sender]
totalSupply >= msg.value
totalSupply > msg.value
totalSupply != msg.value
ori(decimals) == decimals
ori(decimals) >= decimals
ori(decimals) <= decimals
ori(decimals) <= ori(totalSupply)
ori(decimals) < ori(totalSupply)
ori(decimals) != ori(totalSupply)
ori(decimals) != ori(balances[_to])
ori(decimals) <= ori(balances[msg.sender])
ori(decimals) < ori(balances[msg.sender])
ori(decimals) != ori(balances[msg.sender])
ori(decimals) != balances[msg.sender]
ori(decimals) >= msg.value
ori(decimals) > msg.value
ori(decimals) != msg.value
decimals <= ori(totalSupply)
decimals < ori(totalSupply)
decimals != ori(totalSupply)
decimals != ori(balances[_to])
decimals <= ori(balances[msg.sender])
decimals < ori(balances[msg.sender])
decimals != ori(balances[msg.sender])
decimals != balances[msg.sender]
decimals >= msg.value
decimals > msg.value
decimals != msg.value
ori(totalSupply) >= ori(balances[_to])
ori(totalSupply) > ori(balances[_to])
ori(totalSupply) != ori(balances[_to])
ori(totalSupply) >= ori(balances[msg.sender])
ori(totalSupply) >= balances[msg.sender]
ori(totalSupply) > balances[msg.sender]
ori(totalSupply) != balances[msg.sender]
ori(totalSupply) >= msg.value
ori(totalSupply) > msg.value
ori(totalSupply) != msg.value
ori(balances[_to]) <= ori(balances[msg.sender])
ori(balances[_to]) < ori(balances[msg.sender])
ori(balances[_to]) != ori(balances[msg.sender])
ori(balances[_to]) != balances[msg.sender]
ori(balances[_to]) >= msg.value
ori(balances[msg.sender]) >= balances[msg.sender]
ori(balances[msg.sender]) > balances[msg.sender]
ori(balances[msg.sender]) != balances[msg.sender]
ori(balances[msg.sender]) >= msg.value
ori(balances[msg.sender]) > msg.value
ori(balances[msg.sender]) != msg.value
balances[msg.sender] >= msg.value
balances[msg.sender] + _value == ori(balances[msg.sender])
02:33:17 [WARNING] 

02:33:17 [WARNING] transfer(_to,_value)
02:33:17 [WARNING] PptType.EXIT
02:33:17 [WARNING] TxType.REVERSION
02:33:17 [WARNING] 
02:33:17 [WARNING] 

02:33:17 [WARNING] None
02:33:17 [WARNING] PptType.CONTRACT
02:33:17 [WARNING] TxType.NORMAL
02:33:17 [WARNING] decimals > 0
decimals == 18
decimals one of [18]
ori(Sum(balances[...])) > 0
ori(Sum(balances[...])) == 10000000000000000000000000000
ori(Sum(balances[...])) one of [10000000000000000000000000000]
elem of balances[...] is one of [10000000000000000000000000000]
ori(totalSupply) > 0
ori(totalSupply) == 10000000000000000000000000000
ori(totalSupply) one of [10000000000000000000000000000]
ori(decimals) > 0
ori(decimals) == 18
ori(decimals) one of [18]
Sum(balances[...]) > 0
Sum(balances[...]) == 10000000000000000000000000000
Sum(balances[...]) one of [10000000000000000000000000000]
totalSupply > 0
totalSupply == 10000000000000000000000000000
totalSupply one of [10000000000000000000000000000]
decimals <= ori(Sum(balances[...]))
decimals < ori(Sum(balances[...]))
decimals != ori(Sum(balances[...]))
decimals <= ori(totalSupply)
decimals < ori(totalSupply)
decimals != ori(totalSupply)
decimals == ori(decimals)
decimals >= ori(decimals)
decimals <= ori(decimals)
decimals <= Sum(balances[...])
decimals < Sum(balances[...])
decimals != Sum(balances[...])
decimals <= totalSupply
decimals < totalSupply
decimals != totalSupply
ori(Sum(balances[...])) == ori(totalSupply)
ori(Sum(balances[...])) >= ori(totalSupply)
ori(Sum(balances[...])) <= ori(totalSupply)
ori(Sum(balances[...])) >= ori(decimals)
ori(Sum(balances[...])) > ori(decimals)
ori(Sum(balances[...])) != ori(decimals)
ori(Sum(balances[...])) == Sum(balances[...])
ori(Sum(balances[...])) >= Sum(balances[...])
ori(Sum(balances[...])) <= Sum(balances[...])
ori(Sum(balances[...])) == totalSupply
ori(Sum(balances[...])) >= totalSupply
ori(Sum(balances[...])) <= totalSupply
ori(totalSupply) >= ori(decimals)
ori(totalSupply) > ori(decimals)
ori(totalSupply) != ori(decimals)
ori(totalSupply) == Sum(balances[...])
ori(totalSupply) >= Sum(balances[...])
ori(totalSupply) <= Sum(balances[...])
ori(totalSupply) == totalSupply
ori(totalSupply) >= totalSupply
ori(totalSupply) <= totalSupply
ori(decimals) <= Sum(balances[...])
ori(decimals) < Sum(balances[...])
ori(decimals) != Sum(balances[...])
ori(decimals) <= totalSupply
ori(decimals) < totalSupply
ori(decimals) != totalSupply
Sum(balances[...]) == totalSupply
Sum(balances[...]) >= totalSupply
Sum(balances[...]) <= totalSupply
</details>
```

## Advanced Usage

Other than dynamic invariant detection, InvCon also includes a module to facilitate formal verification on the invariant results.
To use this formal verification procedure 