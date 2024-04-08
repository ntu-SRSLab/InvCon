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
11:07:49 [INFO] 'solc --standard-json --allow-paths /home/liuye/Project/github-tool-opensource/InvCon' running
main contract:  GameChannel
ConflictResolutionInterface
MathUtil
Ownable
Activatable
ConflictResolutionManager
Pausable
Destroyable
GameChannelBase
GameChannelConflict
GameChannel
SafeCast
SafeMath
11:07:51 [WARNING] createInitialPptsForFunction for activate()
11:07:51 [WARNING] createInitialPptsForFunction for setGameIdCntr(_gameIdCntr)
11:07:51 [WARNING] createInitialPptsForFunction for withdraw()
11:07:51 [WARNING] createInitialPptsForFunction for unpause()
11:07:51 [WARNING] createInitialPptsForFunction for serverEndGame(_roundId,_balance,_serverHash,_userHash,_gameId,_contractAddress,_userAddress,_userSig)
11:07:51 [WARNING] createInitialPptsForFunction for claimOwnership()
11:07:51 [WARNING] createInitialPptsForFunction for addHouseStake()
11:07:51 [WARNING] createInitialPptsForFunction for withdrawHouseStake(value)
11:07:51 [WARNING] createInitialPptsForFunction for destroy()
11:07:51 [WARNING] createInitialPptsForFunction for pause()
11:07:51 [WARNING] createInitialPptsForFunction for withdrawAll()
11:07:51 [WARNING] createInitialPptsForFunction for userEndGameConflict(_roundId,_gameType,_num,_value,_balance,_serverHash,_userHash,_gameId,_contractAddress,_serverSig,_userSeed)
11:07:51 [WARNING] createInitialPptsForFunction for serverEndGameConflict(_roundId,_gameType,_num,_value,_balance,_serverHash,_userHash,_gameId,_contractAddress,_userSig,_userAddress,_serverSeed,_userSeed)
11:07:51 [WARNING] createInitialPptsForFunction for userCancelActiveGame(_gameId)
11:07:51 [WARNING] createInitialPptsForFunction for setProfitTransferTimeSpan(_profitTransferTimeSpan)
11:07:51 [WARNING] createInitialPptsForFunction for activateConflictResolution()
11:07:51 [WARNING] createInitialPptsForFunction for serverCancelActiveGame(_userAddress,_gameId)
11:07:51 [WARNING] createInitialPptsForFunction for createGame(_userEndHash,_previousGameId,_createBefore,_serverEndHash,_serverSig)
11:07:51 [WARNING] createInitialPptsForFunction for userForceGameEnd(_gameId)
11:07:51 [WARNING] createInitialPptsForFunction for updateConflictResolution(_newConflictResAddress)
11:07:51 [WARNING] createInitialPptsForFunction for serverForceGameEnd(_userAddress,_gameId)
11:07:51 [WARNING] createInitialPptsForFunction for setStakeRequirements(_minStake,_maxStake)
11:07:51 [WARNING] createInitialPptsForFunction for userEndGame(_roundId,_balance,_serverHash,_userHash,_gameId,_contractAddress,_serverSig)
11:07:51 [WARNING] createInitialPptsForFunction for setHouseAddress(_houseAddress)
11:07:51 [WARNING] createInitialPptsForFunction for transferOwnership(_newOwner)
11:07:51 [WARNING] createInitialPptsForFunction for transferProfitToHouse()
11:07:51 [WARNING] createInitialPptsForContract...
**********

unpause()
{VarInfo(name='paused', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b2c304e50>, vartype=<VarType.STATEVAR: 0>, derivation=None), VarInfo(name='timePaused', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b2c0f9f10>, vartype=<VarType.STATEVAR: 0>, derivation=None)}
[]
**********

safeSend(_address)
{VarInfo(name='valueToSend', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b2acff040>, vartype=<VarType.LOCALVAR: 2>, derivation=None), VarInfo(name='pendingReturns[_address]', type='uint256', vartype=<VarType.STATEVAR: 0>, derivation=<invconplus.derivation.binary.MappingItem.MappingItem object at 0x7f0b29d358b0>)}
[]
**********

addHouseStake()
{VarInfo(name='houseStake', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b2c015d30>, vartype=<VarType.STATEVAR: 0>, derivation=None)}
[]
**********

updateConflictResolution(_newConflictResAddress)
{VarInfo(name='newConflictRes', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b2c1a3f10>, vartype=<VarType.STATEVAR: 0>, derivation=None), VarInfo(name='block.timestamp', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b29d3c1f0>, vartype=<VarType.LOCALVAR: 2>, derivation=None), VarInfo(name='_newConflictResAddress', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b2aff58e0>, vartype=<VarType.TXVAR: 1>, derivation=None), VarInfo(name='updateTime', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b2c2fbfa0>, vartype=<VarType.STATEVAR: 0>, derivation=None)}
[]
**********

withdrawHouseStake(value)
{VarInfo(name='value', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b2b044340>, vartype=<VarType.TXVAR: 1>, derivation=None), VarInfo(name='houseStake', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b2c015d30>, vartype=<VarType.STATEVAR: 0>, derivation=None), VarInfo(name='minHouseStake', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b2ad8ba60>, vartype=<VarType.LOCALVAR: 2>, derivation=None), VarInfo(name='houseProfit', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b2c015f40>, vartype=<VarType.STATEVAR: 0>, derivation=None)}
[]
**********

userEndGame(_roundId,_balance,_serverHash,_userHash,_gameId,_contractAddress,_serverSig)
set()
[]
**********

withdraw()
{VarInfo(name='toTransfer', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b2addbbb0>, vartype=<VarType.LOCALVAR: 2>, derivation=None), VarInfo(name='pendingReturns[msg.sender]', type='uint256', vartype=<VarType.STATEVAR: 0>, derivation=<invconplus.derivation.binary.MappingItem.MappingItem object at 0x7f0b29d40370>)}
[]
**********

destroy()
set()
[]
**********

setGameIdCntr(_gameIdCntr)
{VarInfo(name='gameIdCntr', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b2c0158e0>, vartype=<VarType.STATEVAR: 0>, derivation=None), VarInfo(name='_gameIdCntr', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b2b03d790>, vartype=<VarType.TXVAR: 1>, derivation=None)}
[]
**********

transferProfitToHouse()
{VarInfo(name='houseStake', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b2c015d30>, vartype=<VarType.STATEVAR: 0>, derivation=None), VarInfo(name='block.timestamp', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b29d40c70>, vartype=<VarType.LOCALVAR: 2>, derivation=None), VarInfo(name='houseProfit', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b2c015f40>, vartype=<VarType.STATEVAR: 0>, derivation=None), VarInfo(name='lastProfitTransferTimestamp', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b2c01d5e0>, vartype=<VarType.STATEVAR: 0>, derivation=None)}
[]
**********

payOut(_userAddress,_stake,_balance)
{VarInfo(name='valueUser', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b2ad5d9a0>, vartype=<VarType.LOCALVAR: 2>, derivation=None), VarInfo(name='houseStake', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b2c015d30>, vartype=<VarType.STATEVAR: 0>, derivation=None), VarInfo(name='houseProfit', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b2c015f40>, vartype=<VarType.STATEVAR: 0>, derivation=None), VarInfo(name='pendingReturns[_userAddress]', type='uint256', vartype=<VarType.STATEVAR: 0>, derivation=<invconplus.derivation.binary.MappingItem.MappingItem object at 0x7f0b29d40eb0>), VarInfo(name='_balance', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b2b050eb0>, vartype=<VarType.TXVAR: 1>, derivation=None), VarInfo(name='houseStakeInt', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b2ad5d640>, vartype=<VarType.LOCALVAR: 2>, derivation=None), VarInfo(name='_stake', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b2a4f36d0>, vartype=<VarType.TXVAR: 1>, derivation=None), VarInfo(name='stakeInt', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b2c1b1af0>, vartype=<VarType.LOCALVAR: 2>, derivation=None)}
[]
**********

pause()
{VarInfo(name='paused', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b2c304e50>, vartype=<VarType.STATEVAR: 0>, derivation=None), VarInfo(name='timePaused', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b2c0f9f10>, vartype=<VarType.STATEVAR: 0>, derivation=None), VarInfo(name='block.timestamp', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b29d40430>, vartype=<VarType.LOCALVAR: 2>, derivation=None)}
[]
**********

claimOwnership()
{VarInfo(name='owner', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b2c36fdf0>, vartype=<VarType.STATEVAR: 0>, derivation=None), VarInfo(name='pendingOwner', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b2c36fbb0>, vartype=<VarType.STATEVAR: 0>, derivation=None)}
[]
**********

closeGame(_game,_gameId,_roundId,_userAddress,_reason,_balance)
{VarInfo(name='activeGames', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b2c0156d0>, vartype=<VarType.STATEVAR: 0>, derivation=None)}
[]
**********

signatureSplit(_signature)
{VarInfo(name='v', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b2aff51f0>, vartype=<VarType.LOCALVAR: 2>, derivation=None)}
[]
**********

userCancelActiveGame(_gameId)
{VarInfo(name='userAddress', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b2aef7af0>, vartype=<VarType.LOCALVAR: 2>, derivation=None), VarInfo(name='GameStatus.ACTIVE', type='enum GameChannelBase.GameStatus', vartype=<VarType.ENUM: 3>, derivation=None), VarInfo(name='msg.sender', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b29d448e0>, vartype=<VarType.TXVAR: 1>, derivation=None), VarInfo(name='userGameId[userAddress]', type='uint256', vartype=<VarType.STATEVAR: 0>, derivation=<invconplus.derivation.binary.MappingItem.MappingItem object at 0x7f0b29d44f40>), VarInfo(name='gameIdGame[gameId]', type='struct GameChannelBase.Game storage ref', vartype=<VarType.STATEVAR: 0>, derivation=<invconplus.derivation.binary.MappingItem.MappingItem object at 0x7f0b29d48190>), VarInfo(name='_gameId', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b2b090dc0>, vartype=<VarType.TXVAR: 1>, derivation=None), VarInfo(name='game', type=<slither.core.solidity_types.user_defined_type.UserDefinedType object at 0x7f0b2af065e0>, vartype=<VarType.LOCALVAR: 2>, derivation=None), VarInfo(name='GameStatus.SERVER_INITIATED_END', type='enum GameChannelBase.GameStatus', vartype=<VarType.ENUM: 3>, derivation=None), VarInfo(name='gameId', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b2af060a0>, vartype=<VarType.LOCALVAR: 2>, derivation=None)}
[]
**********

serverForceGameEnd(_userAddress,_gameId)
{VarInfo(name='userGameId[_userAddress]', type='uint256', vartype=<VarType.STATEVAR: 0>, derivation=<invconplus.derivation.binary.MappingItem.MappingItem object at 0x7f0b29d48940>), VarInfo(name='gameIdGame[gameId]', type='struct GameChannelBase.Game storage ref', vartype=<VarType.STATEVAR: 0>, derivation=<invconplus.derivation.binary.MappingItem.MappingItem object at 0x7f0b29d48b80>), VarInfo(name='game', type=<slither.core.solidity_types.user_defined_type.UserDefinedType object at 0x7f0b2aec16a0>, vartype=<VarType.LOCALVAR: 2>, derivation=None), VarInfo(name='GameStatus.SERVER_INITIATED_END', type='enum GameChannelBase.GameStatus', vartype=<VarType.ENUM: 3>, derivation=None), VarInfo(name='gameId', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b2aec1220>, vartype=<VarType.LOCALVAR: 2>, derivation=None), VarInfo(name='_gameId', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b2b098760>, vartype=<VarType.TXVAR: 1>, derivation=None)}
[]
**********

calcHash(_roundId,_gameType,_num,_value,_balance,_serverHash,_userHash,_gameId)
set()
[]
**********

constructor()
{VarInfo(name='owner', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b2c36fdf0>, vartype=<VarType.STATEVAR: 0>, derivation=None), VarInfo(name='msg.sender', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b29d4c340>, vartype=<VarType.TXVAR: 1>, derivation=None), VarInfo(name='pendingOwner', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b2c36fbb0>, vartype=<VarType.STATEVAR: 0>, derivation=None)}
[]
**********

verify(_hash,_sig,_address)
{VarInfo(name='addressRecover', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b2ad242b0>, vartype=<VarType.LOCALVAR: 2>, derivation=None), VarInfo(name='_address', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b2b063af0>, vartype=<VarType.TXVAR: 1>, derivation=None)}
[]
**********

cancelActiveGame(_game,_gameId,_userAddress)
{VarInfo(name='stake', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b2ae1f850>, vartype=<VarType.LOCALVAR: 2>, derivation=None), VarInfo(name='newBalance', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b2ae1f730>, vartype=<VarType.LOCALVAR: 2>, derivation=None)}
[]
**********

serverEndGameConflictImpl(_roundId,_gameType,_num,_value,_balance,_serverHash,_userHash,_serverSeed,_userSeed,_gameId,_userAddress)
{VarInfo(name='userGameId[_userAddress]', type='uint256', vartype=<VarType.STATEVAR: 0>, derivation=<invconplus.derivation.binary.MappingItem.MappingItem object at 0x7f0b29d4f0a0>), VarInfo(name='GameStatus.ACTIVE', type='enum GameChannelBase.GameStatus', vartype=<VarType.ENUM: 3>, derivation=None), VarInfo(name='_userHash', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b2b0ac670>, vartype=<VarType.TXVAR: 1>, derivation=None), VarInfo(name='_balance', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b2b0ac370>, vartype=<VarType.TXVAR: 1>, derivation=None), VarInfo(name='gameIdGame[gameId]', type='struct GameChannelBase.Game storage ref', vartype=<VarType.STATEVAR: 0>, derivation=<invconplus.derivation.binary.MappingItem.MappingItem object at 0x7f0b29d4c490>), VarInfo(name='maxBalance', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b2ae615e0>, vartype=<VarType.LOCALVAR: 2>, derivation=None), VarInfo(name='gameStake', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b2ae61820>, vartype=<VarType.LOCALVAR: 2>, derivation=None), VarInfo(name='GameStatus.USER_INITIATED_END', type='enum GameChannelBase.GameStatus', vartype=<VarType.ENUM: 3>, derivation=None), VarInfo(name='game', type=<slither.core.solidity_types.user_defined_type.UserDefinedType object at 0x7f0b2ae616d0>, vartype=<VarType.LOCALVAR: 2>, derivation=None), VarInfo(name='_roundId', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b2b0a3d30>, vartype=<VarType.TXVAR: 1>, derivation=None), VarInfo(name='gameId', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b2ae4e790>, vartype=<VarType.LOCALVAR: 2>, derivation=None), VarInfo(name='_serverHash', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b2b0ac4f0>, vartype=<VarType.TXVAR: 1>, derivation=None), VarInfo(name='_gameId', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b2b0acaf0>, vartype=<VarType.TXVAR: 1>, derivation=None)}
[]
**********

onlyValidHouseStake(_activeGames)
{VarInfo(name='houseStake', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b2c015d30>, vartype=<VarType.STATEVAR: 0>, derivation=None), VarInfo(name='minHouseStake', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b2b01bfa0>, vartype=<VarType.LOCALVAR: 2>, derivation=None)}
[]
**********

serverCancelActiveGame(_userAddress,_gameId)
{VarInfo(name='userGameId[_userAddress]', type='uint256', vartype=<VarType.STATEVAR: 0>, derivation=<invconplus.derivation.binary.MappingItem.MappingItem object at 0x7f0b29d4f1f0>), VarInfo(name='GameStatus.ACTIVE', type='enum GameChannelBase.GameStatus', vartype=<VarType.ENUM: 3>, derivation=None), VarInfo(name='gameIdGame[gameId]', type='struct GameChannelBase.Game storage ref', vartype=<VarType.STATEVAR: 0>, derivation=<invconplus.derivation.binary.MappingItem.MappingItem object at 0x7f0b29d4f400>), VarInfo(name='GameStatus.USER_INITIATED_END', type='enum GameChannelBase.GameStatus', vartype=<VarType.ENUM: 3>, derivation=None), VarInfo(name='game', type=<slither.core.solidity_types.user_defined_type.UserDefinedType object at 0x7f0b2af2c130>, vartype=<VarType.LOCALVAR: 2>, derivation=None), VarInfo(name='gameId', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b2af1dc70>, vartype=<VarType.LOCALVAR: 2>, derivation=None), VarInfo(name='_gameId', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b2b0982b0>, vartype=<VarType.TXVAR: 1>, derivation=None)}
[]
**********

setStakeRequirements(_minStake,_maxStake)
{VarInfo(name='minStake', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b2c01d1c0>, vartype=<VarType.STATEVAR: 0>, derivation=None), VarInfo(name='maxStake', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b2c01d2e0>, vartype=<VarType.STATEVAR: 0>, derivation=None), VarInfo(name='_minStake', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b2b044bb0>, vartype=<VarType.TXVAR: 1>, derivation=None), VarInfo(name='_maxStake', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b2b044d30>, vartype=<VarType.TXVAR: 1>, derivation=None)}
[]
**********

serverEndGameConflict(_roundId,_gameType,_num,_value,_balance,_serverHash,_userHash,_gameId,_contractAddress,_userSig,_userAddress,_serverSeed,_userSeed)
set()
[]
**********

onlyOwner()
{VarInfo(name='owner', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b2c36fdf0>, vartype=<VarType.STATEVAR: 0>, derivation=None), VarInfo(name='msg.sender', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b29d556d0>, vartype=<VarType.TXVAR: 1>, derivation=None)}
[]
**********

activateConflictResolution()
{VarInfo(name='MIN_TIMEOUT', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b2c2de2b0>, vartype=<VarType.STATEVAR: 0>, derivation=None), VarInfo(name='block.timestamp', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b29d57160>, vartype=<VarType.LOCALVAR: 2>, derivation=None), VarInfo(name='conflictRes', type=<slither.core.solidity_types.user_defined_type.UserDefinedType object at 0x7f0b2c1a3f70>, vartype=<VarType.STATEVAR: 0>, derivation=None), VarInfo(name='MAX_TIMEOUT', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b2c2de610>, vartype=<VarType.STATEVAR: 0>, derivation=None), VarInfo(name='updateTime', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b2c2fbfa0>, vartype=<VarType.STATEVAR: 0>, derivation=None), VarInfo(name='newConflictRes', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b2c1a3f10>, vartype=<VarType.STATEVAR: 0>, derivation=None)}
[]
**********

withdrawAll()
{VarInfo(name='toTransfer', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b2ada57c0>, vartype=<VarType.LOCALVAR: 2>, derivation=None), VarInfo(name='houseProfit', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b2c015f40>, vartype=<VarType.STATEVAR: 0>, derivation=None), VarInfo(name='houseStake', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b2c015d30>, vartype=<VarType.STATEVAR: 0>, derivation=None)}
[]
**********

onlyPausedSince(timeSpan)
set()
[]
**********

setHouseAddress(_houseAddress)
{VarInfo(name='_houseAddress', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b2b044850>, vartype=<VarType.TXVAR: 1>, derivation=None), VarInfo(name='houseAddress', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b2c015c40>, vartype=<VarType.STATEVAR: 0>, derivation=None)}
[]
**********

verifyCreateSig(_userAddress,_previousGameId,_createBefore,_serverEndHash,_serverSig)
{VarInfo(name='this', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b29d57f70>, vartype=<VarType.LOCALVAR: 2>, derivation=None), VarInfo(name='contractAddress', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b2afa5af0>, vartype=<VarType.LOCALVAR: 2>, derivation=None)}
[]
**********

onlyNotPaused()
set()
[]
**********

userEndGameConflict(_roundId,_gameType,_num,_value,_balance,_serverHash,_userHash,_gameId,_contractAddress,_serverSig,_userSeed)
set()
[]
**********

userEndGameConflictImpl(_roundId,_gameType,_num,_value,_balance,_userHash,_userSeed,_gameId,_userAddress)
{VarInfo(name='userGameId[_userAddress]', type='uint256', vartype=<VarType.STATEVAR: 0>, derivation=<invconplus.derivation.binary.MappingItem.MappingItem object at 0x7f0b29d4f9d0>), VarInfo(name='GameStatus.ACTIVE', type='enum GameChannelBase.GameStatus', vartype=<VarType.ENUM: 3>, derivation=None), VarInfo(name='GameStatus.SERVER_INITIATED_END', type='enum GameChannelBase.GameStatus', vartype=<VarType.ENUM: 3>, derivation=None), VarInfo(name='_userHash', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b2b0a3580>, vartype=<VarType.TXVAR: 1>, derivation=None), VarInfo(name='_balance', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b2b0a3400>, vartype=<VarType.TXVAR: 1>, derivation=None), VarInfo(name='gameIdGame[gameId]', type='struct GameChannelBase.Game storage ref', vartype=<VarType.STATEVAR: 0>, derivation=<invconplus.derivation.binary.MappingItem.MappingItem object at 0x7f0b29d5b550>), VarInfo(name='maxBalance', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b2ae8e490>, vartype=<VarType.LOCALVAR: 2>, derivation=None), VarInfo(name='gameStake', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b2ae8e6d0>, vartype=<VarType.LOCALVAR: 2>, derivation=None), VarInfo(name='game', type=<slither.core.solidity_types.user_defined_type.UserDefinedType object at 0x7f0b2ae8e580>, vartype=<VarType.LOCALVAR: 2>, derivation=None), VarInfo(name='_roundId', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b2b098dc0>, vartype=<VarType.TXVAR: 1>, derivation=None), VarInfo(name='gameId', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b2ae7c640>, vartype=<VarType.LOCALVAR: 2>, derivation=None), VarInfo(name='_gameId', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b2b0a3880>, vartype=<VarType.TXVAR: 1>, derivation=None)}
[]
**********

activate()
{VarInfo(name='activated', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b2c2fb640>, vartype=<VarType.STATEVAR: 0>, derivation=None)}
[]
**********

createGame(_userEndHash,_previousGameId,_createBefore,_serverEndHash,_serverSig)
{VarInfo(name='block.timestamp', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b29d60b80>, vartype=<VarType.LOCALVAR: 2>, derivation=None), VarInfo(name='gameIdCntr', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b2c0158e0>, vartype=<VarType.STATEVAR: 0>, derivation=None), VarInfo(name='newGame', type=<slither.core.solidity_types.user_defined_type.UserDefinedType object at 0x7f0b2aff4b50>, vartype=<VarType.LOCALVAR: 2>, derivation=None), VarInfo(name='userGameId[msg.sender]', type='uint256', vartype=<VarType.STATEVAR: 0>, derivation=<invconplus.derivation.binary.MappingItem.MappingItem object at 0x7f0b29d603d0>), VarInfo(name='previousGameId', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b2aff41c0>, vartype=<VarType.LOCALVAR: 2>, derivation=None), VarInfo(name='GameStatus.ENDED', type='enum GameChannelBase.GameStatus', vartype=<VarType.ENUM: 3>, derivation=None), VarInfo(name='activeGames', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b2c0156d0>, vartype=<VarType.STATEVAR: 0>, derivation=None), VarInfo(name='_previousGameId', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b2b00b340>, vartype=<VarType.TXVAR: 1>, derivation=None), VarInfo(name='_createBefore', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b2b00b4c0>, vartype=<VarType.TXVAR: 1>, derivation=None), VarInfo(name='gameIdGame[gameId]', type='struct GameChannelBase.Game storage ref', vartype=<VarType.STATEVAR: 0>, derivation=<invconplus.derivation.binary.MappingItem.MappingItem object at 0x7f0b29d649d0>), VarInfo(name='game', type=<slither.core.solidity_types.user_defined_type.UserDefinedType object at 0x7f0b2aff4730>, vartype=<VarType.LOCALVAR: 2>, derivation=None), VarInfo(name='gameIdGame[previousGameId]', type='struct GameChannelBase.Game storage ref', vartype=<VarType.STATEVAR: 0>, derivation=<invconplus.derivation.binary.MappingItem.MappingItem object at 0x7f0b29d605e0>), VarInfo(name='gameId', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b2aff44c0>, vartype=<VarType.LOCALVAR: 2>, derivation=None)}
[]
**********

onlyServer()
{VarInfo(name='serverAddress', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b2c015b20>, vartype=<VarType.STATEVAR: 0>, derivation=None), VarInfo(name='msg.sender', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b29d60af0>, vartype=<VarType.TXVAR: 1>, derivation=None)}
[]
**********

userForceGameEnd(_gameId)
{VarInfo(name='userAddress', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b2aed8940>, vartype=<VarType.LOCALVAR: 2>, derivation=None), VarInfo(name='msg.sender', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b29d643d0>, vartype=<VarType.TXVAR: 1>, derivation=None), VarInfo(name='userGameId[userAddress]', type='uint256', vartype=<VarType.STATEVAR: 0>, derivation=<invconplus.derivation.binary.MappingItem.MappingItem object at 0x7f0b29d64af0>), VarInfo(name='gameIdGame[gameId]', type='struct GameChannelBase.Game storage ref', vartype=<VarType.STATEVAR: 0>, derivation=<invconplus.derivation.binary.MappingItem.MappingItem object at 0x7f0b29d64d30>), VarInfo(name='GameStatus.USER_INITIATED_END', type='enum GameChannelBase.GameStatus', vartype=<VarType.ENUM: 3>, derivation=None), VarInfo(name='_gameId', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b2b098a90>, vartype=<VarType.TXVAR: 1>, derivation=None), VarInfo(name='game', type=<slither.core.solidity_types.user_defined_type.UserDefinedType object at 0x7f0b2aed8f70>, vartype=<VarType.LOCALVAR: 2>, derivation=None), VarInfo(name='gameId', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b2aed8a30>, vartype=<VarType.LOCALVAR: 2>, derivation=None)}
[]
**********

constructor(_conflictResAddress)
{VarInfo(name='_conflictResAddress', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b2aff5580>, vartype=<VarType.TXVAR: 1>, derivation=None), VarInfo(name='conflictRes', type=<slither.core.solidity_types.user_defined_type.UserDefinedType object at 0x7f0b2c1a3f70>, vartype=<VarType.STATEVAR: 0>, derivation=None)}
[]
**********

setProfitTransferTimeSpan(_profitTransferTimeSpan)
{VarInfo(name='_profitTransferTimeSpan', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b2b03de20>, vartype=<VarType.TXVAR: 1>, derivation=None), VarInfo(name='profitTransferTimeSpan', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b2c01d3d0>, vartype=<VarType.STATEVAR: 0>, derivation=None)}
[]
**********

onlyValidValue()
{VarInfo(name='msg.value', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b29d67c70>, vartype=<VarType.TXVAR: 1>, derivation=None), VarInfo(name='maxStake', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b2c01d2e0>, vartype=<VarType.STATEVAR: 0>, derivation=None), VarInfo(name='minStake', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b2c01d1c0>, vartype=<VarType.STATEVAR: 0>, derivation=None)}
[]
**********

regularEndGame(_userAddress,_roundId,_balance,_gameId,_contractAddress)
{VarInfo(name='this', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b29d6a4c0>, vartype=<VarType.LOCALVAR: 2>, derivation=None), VarInfo(name='userGameId[_userAddress]', type='uint256', vartype=<VarType.STATEVAR: 0>, derivation=<invconplus.derivation.binary.MappingItem.MappingItem object at 0x7f0b29d55940>), VarInfo(name='GameStatus.ACTIVE', type='enum GameChannelBase.GameStatus', vartype=<VarType.ENUM: 3>, derivation=None), VarInfo(name='_contractAddress', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b2b01bac0>, vartype=<VarType.TXVAR: 1>, derivation=None), VarInfo(name='_balance', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b2b01b7c0>, vartype=<VarType.TXVAR: 1>, derivation=None), VarInfo(name='gameIdGame[gameId]', type='struct GameChannelBase.Game storage ref', vartype=<VarType.STATEVAR: 0>, derivation=<invconplus.derivation.binary.MappingItem.MappingItem object at 0x7f0b29d57b80>), VarInfo(name='maxBalance', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b2af3d8b0>, vartype=<VarType.LOCALVAR: 2>, derivation=None), VarInfo(name='gameStake', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b2af3daf0>, vartype=<VarType.LOCALVAR: 2>, derivation=None), VarInfo(name='game', type=<slither.core.solidity_types.user_defined_type.UserDefinedType object at 0x7f0b2af3d9a0>, vartype=<VarType.LOCALVAR: 2>, derivation=None), VarInfo(name='_roundId', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b2b01b640>, vartype=<VarType.TXVAR: 1>, derivation=None), VarInfo(name='gameId', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b2af3d5b0>, vartype=<VarType.LOCALVAR: 2>, derivation=None), VarInfo(name='_gameId', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b2b01b940>, vartype=<VarType.TXVAR: 1>, derivation=None)}
[]
**********

onlyValidTransferTimeSpan(transferTimeout)
{VarInfo(name='MAX_TRANSFER_TIMSPAN', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b2c2e82e0>, vartype=<VarType.STATEVAR: 0>, derivation=None), VarInfo(name='MIN_TRANSFER_TIMESPAN', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b2c2e80a0>, vartype=<VarType.STATEVAR: 0>, derivation=None), VarInfo(name='transferTimeout', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b2b0e9730>, vartype=<VarType.TXVAR: 1>, derivation=None)}
[]
**********

onlyNotActivated()
set()
[]
**********

onlyPendingOwner()
{VarInfo(name='msg.sender', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b29d6ad30>, vartype=<VarType.TXVAR: 1>, derivation=None), VarInfo(name='pendingOwner', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b2c36fbb0>, vartype=<VarType.STATEVAR: 0>, derivation=None)}
[]
**********

onlyActivated()
set()
[]
**********

onlyPaused()
set()
[]
**********

endGameConflict(_game,_gameId,_userAddress)
set()
[]
**********

verifySig(_roundId,_gameType,_num,_value,_balance,_serverHash,_userHash,_gameId,_contractAddress,_sig,_address)
{VarInfo(name='_contractAddress', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b2b063190>, vartype=<VarType.TXVAR: 1>, derivation=None), VarInfo(name='this', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b29d6e850>, vartype=<VarType.LOCALVAR: 2>, derivation=None), VarInfo(name='contractAddress', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b2ad0b6d0>, vartype=<VarType.LOCALVAR: 2>, derivation=None)}
[]
**********

transferOwnership(_newOwner)
{VarInfo(name='_newOwner', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b2aff5f70>, vartype=<VarType.TXVAR: 1>, derivation=None), VarInfo(name='pendingOwner', type=<slither.core.solidity_types.elementary_type.ElementaryType object at 0x7f0b2c36fbb0>, vartype=<VarType.STATEVAR: 0>, derivation=None)}
[]
**********

serverEndGame(_roundId,_balance,_serverHash,_userHash,_gameId,_contractAddress,_userAddress,_userSig)
set()
[]
**********

constructor(_serverAddress,_minStake,_maxStake,_conflictResAddress,_houseAddress,_chainId)
set()
[]
11:08:32 [WARNING] 0x774bc9a515c0171968e5f08380f82f5a54251f3c07db704c5c6693f0a18af30asetGameIdCntr(_gameIdCntr)
11:08:33 [WARNING] 0x1147b3538f4600902faf1a5e6a2c8dac84d58a0245a21b3049aaa8ad26c1bd17activate()
11:08:33 [WARNING] 0x13255e82d8a6d9e33f86aaab057b06ce6db7f0afbcc6e5aadf80b18e9aab9c61addHouseStake()
11:08:33 [WARNING] 0x2b516ebdf3a101726c397707afae67cd7cfff3806b83d91eea33f92e23a54250addHouseStake()
11:08:33 [WARNING] 0xd0d540e44e4cff7feeb9990d071b1c804a7a4014d2431d4dd24558b6f3ea9c76unpause()
11:08:33 [WARNING] 0xe65302d5f8b0282217260c729c391fc4ab5c0eb6afabe06fcd94d211206c127ccreateGame(_userEndHash,_previousGameId,_createBefore,_serverEndHash,_serverSig)
11:08:33 [WARNING] 0x5f8b05f27dcbd1a51b8b50ad6bf3f8b05fee1b4af14ddde015195d88e8ffe5f5serverEndGame(_roundId,_balance,_serverHash,_userHash,_gameId,_contractAddress,_userAddress,_userSig)
11:08:33 [WARNING] 0xc7ba0c813e987507825b16f830f259a955113f1a636d884f852e0b1ef96eb800createGame(_userEndHash,_previousGameId,_createBefore,_serverEndHash,_serverSig)
11:08:33 [WARNING] 0xb3b0743bc7f846692f98276205f724fc95c128ad91202bcb1cfc6df1c5b6c73ccreateGame(_userEndHash,_previousGameId,_createBefore,_serverEndHash,_serverSig)
11:08:33 [WARNING] 0x58f7db173837bd29e52ec8f7d78667b4c938a0cea4d8625ed32cb4c6993037aaserverEndGame(_roundId,_balance,_serverHash,_userHash,_gameId,_contractAddress,_userAddress,_userSig)
11:08:33 [WARNING] 0x475829c8f4f68cd09701189e12012017b7deaf720ba096390355ff523e16eaf8createGame(_userEndHash,_previousGameId,_createBefore,_serverEndHash,_serverSig)
11:08:33 [WARNING] 0xf58b3792ee4740fd0f89bb44c1f81ba6021fe5d4d137198ae84a1e434772517cserverEndGame(_roundId,_balance,_serverHash,_userHash,_gameId,_contractAddress,_userAddress,_userSig)
11:08:33 [WARNING] 0x1d7c5a7bc61c6b841b6c02c95a4dd0017ac0ce8eeb8852b7224da3617e58cf80createGame(_userEndHash,_previousGameId,_createBefore,_serverEndHash,_serverSig)
11:08:33 [WARNING] 0x63e530ecff707e015185dadf511e195029cf4ad28234ac18ae5807894d29a415createGame(_userEndHash,_previousGameId,_createBefore,_serverEndHash,_serverSig)
11:08:33 [WARNING] 0xb7118f1337a66723bff5155dad7c1770c85abae36a916af3f6042365ab4dd642serverEndGame(_roundId,_balance,_serverHash,_userHash,_gameId,_contractAddress,_userAddress,_userSig)
11:08:33 [WARNING] 0xf6482f919f6c3193be58908cf1269d399e42f767b9d52e2ec57bc5cdde5a7b01createGame(_userEndHash,_previousGameId,_createBefore,_serverEndHash,_serverSig)
11:08:33 [WARNING] 0x53e022501a0dea3b967448285854a655c05de106183813c29dd5f81ebce210d9serverEndGame(_roundId,_balance,_serverHash,_userHash,_gameId,_contractAddress,_userAddress,_userSig)
11:08:34 [WARNING] 0xf4bdcd0b7ff6f68b9a24499a80f24fa66a28442493a225107b64c9c08450897ccreateGame(_userEndHash,_previousGameId,_createBefore,_serverEndHash,_serverSig)
11:08:34 [WARNING] 0x1222b1c70f04b7ec8f963972fbb285f8beb410ec4ba5f074708427d18515d46dserverEndGame(_roundId,_balance,_serverHash,_userHash,_gameId,_contractAddress,_userAddress,_userSig)
11:08:34 [WARNING] 0x3d8f7105d0c71b6c97c6f8ad5a14c8f7311a764cf3c6ffc8d8e8d970372eea3ecreateGame(_userEndHash,_previousGameId,_createBefore,_serverEndHash,_serverSig)
11:08:34 [WARNING] 0xbd09747b684d3e275ea5b1dd95976590dd9aaed1823046bb09e980dff96991abserverEndGame(_roundId,_balance,_serverHash,_userHash,_gameId,_contractAddress,_userAddress,_userSig)
11:08:34 [WARNING] 0x9b7947b213110655fc2ac6d7abff95ba503bcdb6154e514aa012f52ebadf0f25createGame(_userEndHash,_previousGameId,_createBefore,_serverEndHash,_serverSig)
11:08:34 [WARNING] 0x7db3929d8f79b43b27ea67d61b94e13da43e1e3c70df4e15dc698aece488d313serverEndGame(_roundId,_balance,_serverHash,_userHash,_gameId,_contractAddress,_userAddress,_userSig)
11:08:34 [WARNING] 0x1a450e7c3d24bde82e301ceb86bf4f59c87f2cd7c4edbda18e4fd36907d93d0dcreateGame(_userEndHash,_previousGameId,_createBefore,_serverEndHash,_serverSig)
11:08:34 [WARNING] 0xdbe2cdd9dad11caa7251bf6b94281dba61b147a7dcf5b821c7922b8e5b28dec4serverEndGame(_roundId,_balance,_serverHash,_userHash,_gameId,_contractAddress,_userAddress,_userSig)
11:08:34 [WARNING] 0xb66939ab1439457150ff0a0e79bd43d45dd598f2d5994f9b2bb821d2405abfa5createGame(_userEndHash,_previousGameId,_createBefore,_serverEndHash,_serverSig)
11:08:34 [WARNING] 0xf0a8a800c1b4b5a32dfdb1ce8057dd819a217ef110c5197d1649501f34d009bdserverEndGameConflict(_roundId,_gameType,_num,_value,_balance,_serverHash,_userHash,_gameId,_contractAddress,_userSig,_userAddress,_serverSeed,_userSeed)
11:08:34 [WARNING] 0x08a0ad5be8432828f94cfa909223efdb4ee714f0e3e4242e035e03ce6ea38624serverEndGame(_roundId,_balance,_serverHash,_userHash,_gameId,_contractAddress,_userAddress,_userSig)
11:08:34 [WARNING] 0xe4dfe800dcc95b75cfb6312bb9d95d782f8486ec76dfb66c371889f9574fbf40serverEndGame(_roundId,_balance,_serverHash,_userHash,_gameId,_contractAddress,_userAddress,_userSig)
11:08:34 [WARNING] 0x9136d84b8d43405bd14547ad7565ffe3f30a9229b7b5b66ea4d7c575f69c43bbcreateGame(_userEndHash,_previousGameId,_createBefore,_serverEndHash,_serverSig)
11:08:34 [WARNING] 0x52865aca3bb216113d69609cfc1cd5cb755ce3a4fd76ed7ed6d148ac914ebaf0serverEndGame(_roundId,_balance,_serverHash,_userHash,_gameId,_contractAddress,_userAddress,_userSig)
11:08:35 [WARNING] 0xf05024c8c4dbc2aac58171bffea5ee3dd638d233f470355ba4b167652da9ee5ecreateGame(_userEndHash,_previousGameId,_createBefore,_serverEndHash,_serverSig)
11:08:35 [WARNING] 0x63547bc652c9473433b18410f05aeb297c486f6d2436e5ecd4f494006999a90acreateGame(_userEndHash,_previousGameId,_createBefore,_serverEndHash,_serverSig)
11:08:35 [WARNING] 0xbbf0050d2c72f0f385ec093e5170431e5cbb1fe0cec3ebf0f3273b9f521aa7fcserverEndGame(_roundId,_balance,_serverHash,_userHash,_gameId,_contractAddress,_userAddress,_userSig)
11:08:35 [WARNING] 0x5d9456fe147e7341d79ae2b011bcb503b5f1485c6167f7e5ca5b0f6f14c04696createGame(_userEndHash,_previousGameId,_createBefore,_serverEndHash,_serverSig)
11:08:35 [WARNING] 0x33cb7716c9459bf6dce7e0dfe0326b6d03b4e167e33e599d5749cc0d7964146eserverEndGame(_roundId,_balance,_serverHash,_userHash,_gameId,_contractAddress,_userAddress,_userSig)
11:08:35 [WARNING] 0xa4e05084b5ee173b4e255befcbfa070ea7fce54eff4bad4dceb9e4a074d7b129createGame(_userEndHash,_previousGameId,_createBefore,_serverEndHash,_serverSig)
11:08:35 [WARNING] 0x22ce39dfcc22175d080738663af0452c97c24a11fad3f35b8d76f4a258d94c3fserverEndGame(_roundId,_balance,_serverHash,_userHash,_gameId,_contractAddress,_userAddress,_userSig)
11:08:35 [WARNING] 0xd927d0ac8d15a228f3297da72384d76a9a67a10399be32210f980fe3fc09e0a6createGame(_userEndHash,_previousGameId,_createBefore,_serverEndHash,_serverSig)
11:08:35 [WARNING] 0xdfd5212f03f17fad7ed5d61d1ae0075859967b402326d90b6fbe38c1f41be69dserverEndGame(_roundId,_balance,_serverHash,_userHash,_gameId,_contractAddress,_userAddress,_userSig)
11:08:35 [WARNING] 0xd21887853f2246a046539eae0f63211b99f38807cd185352baa58e6b7ccf3ffdcreateGame(_userEndHash,_previousGameId,_createBefore,_serverEndHash,_serverSig)
11:08:35 [WARNING] 0x3498d1bde818748007db4e36e4a8e13f907ed384fe65b0c055ab10083b07b5dfserverEndGame(_roundId,_balance,_serverHash,_userHash,_gameId,_contractAddress,_userAddress,_userSig)
11:08:35 [WARNING] 0xee31ce3b65a8c80e3ba8d1631628c957dcbf7802c2ba78028b6bd9fdd9772a16serverForceGameEnd(_userAddress,_gameId)
11:08:35 [WARNING] 0x7cee4550e742d3a36fbddda4c887592352740e34e8ed5092773db599978a5e93serverCancelActiveGame(_userAddress,_gameId)
11:08:35 [WARNING] 0xa1d725e1529d1d748f2eb0a85d0fbd82e68dcc2587d685127cd68919ee136141createGame(_userEndHash,_previousGameId,_createBefore,_serverEndHash,_serverSig)
11:08:36 [WARNING] 0xa3e8b726728defb97c3ca433b441a34b1386108917913fa0b42f389c330c05f7serverEndGame(_roundId,_balance,_serverHash,_userHash,_gameId,_contractAddress,_userAddress,_userSig)
11:08:36 [WARNING] 0x3c9bbeb2c7ade1bf5001b699ba2019e0202ef79337bc648ac86c90c3087c169bcreateGame(_userEndHash,_previousGameId,_createBefore,_serverEndHash,_serverSig)
11:08:36 [WARNING] 0xba756b727835c508acc53b84a35c751055fe6aa5027806b83f50deacc6ea9fa1serverForceGameEnd(_userAddress,_gameId)
11:08:36 [WARNING] 0x10ee8373d50336e2fd2b5ae0679b8402cf34883384b75da6a0f9faa1220b5ae6createGame(_userEndHash,_previousGameId,_createBefore,_serverEndHash,_serverSig)
11:08:36 [WARNING] 0x9bebeecaf0a8045c87b86c2c1b5dca1a283bb989194d34a1eaccc5ddb307b5f1serverEndGame(_roundId,_balance,_serverHash,_userHash,_gameId,_contractAddress,_userAddress,_userSig)
11:08:36 [WARNING] 0xc1bbf9fa03cb9d8391d6880be611e9ce94610fb9f7a9cc471583159d76f263aaserverEndGame(_roundId,_balance,_serverHash,_userHash,_gameId,_contractAddress,_userAddress,_userSig)
11:08:36 [WARNING] 0x37fc48b43ae1457b88216b05f11401a90ac3e0aa2a7ff72a5f498eb23507ca36createGame(_userEndHash,_previousGameId,_createBefore,_serverEndHash,_serverSig)
11:08:36 [WARNING] 0x761bbbf79cef350fc62bbb3aeb7f2b0018f5ce44ae8fed9522dc21592268d3feserverEndGame(_roundId,_balance,_serverHash,_userHash,_gameId,_contractAddress,_userAddress,_userSig)
11:08:36 [WARNING] 0x79275906f5ce73533526a7e48c24d7fd3a7fac7309f5bc2204a3ac767212433ecreateGame(_userEndHash,_previousGameId,_createBefore,_serverEndHash,_serverSig)
11:08:36 [WARNING] 0x9fa54c8ada5e6c4f7e00fc42af4ddaf5f0e1da4236c4f54df15ebc16d3d287daserverEndGame(_roundId,_balance,_serverHash,_userHash,_gameId,_contractAddress,_userAddress,_userSig)
11:08:36 [WARNING] 0xb83a09ec3ec66ca0274efd9ce12dd5a4db1026a3f0f2bf6834f1249ad7df1264createGame(_userEndHash,_previousGameId,_createBefore,_serverEndHash,_serverSig)
11:08:36 [WARNING] 0x7a8201f9298560a16c7f77b375038fa127277f1661ee1b34c7695ec63d007ef5createGame(_userEndHash,_previousGameId,_createBefore,_serverEndHash,_serverSig)
11:08:36 [WARNING] 0xcdc4d1a11935c81fd031399d380f7e584f7e05a5004d40aa238e719c209ceb80serverEndGame(_roundId,_balance,_serverHash,_userHash,_gameId,_contractAddress,_userAddress,_userSig)
11:08:37 [WARNING] 0x48147031c686047d5e8fd2e02ecef98ac50420234c5a9b5fb17086d645922648serverEndGame(_roundId,_balance,_serverHash,_userHash,_gameId,_contractAddress,_userAddress,_userSig)
11:08:37 [WARNING] 0x0ec7c574027adba95fc87f421e3b632770d74f889a415423e37c690731ca72eacreateGame(_userEndHash,_previousGameId,_createBefore,_serverEndHash,_serverSig)
11:08:37 [WARNING] 0x97e92b1549cbe55551b3f696deb21d25101e59b5c53f7a6dde64e88c3626a30dserverEndGame(_roundId,_balance,_serverHash,_userHash,_gameId,_contractAddress,_userAddress,_userSig)
11:08:37 [WARNING] 0x49730e0bbf3d8f8b5895d99f936efc1ce80c3f746f41681dd4a5849a8175a7b0createGame(_userEndHash,_previousGameId,_createBefore,_serverEndHash,_serverSig)
11:08:37 [WARNING] 0xe94b79400e846650cb944869de2af67f1685c1b6e46543a8942ae3302f887aa4serverEndGame(_roundId,_balance,_serverHash,_userHash,_gameId,_contractAddress,_userAddress,_userSig)
11:08:37 [WARNING] 0x5945ce0601fe35d2cdc23ee76ff38478a35ca33fa648cca668395306b5a0d483createGame(_userEndHash,_previousGameId,_createBefore,_serverEndHash,_serverSig)
11:08:37 [WARNING] 0x623e39985fe4efc8acd52e6524d2a814884154d38a3d70d4610fa955bf103698createGame(_userEndHash,_previousGameId,_createBefore,_serverEndHash,_serverSig)
11:08:37 [WARNING] 0xa151fd6af799bb1f19236b2175ce2bae19c73769d8e7202add6552aecf1323b4serverEndGame(_roundId,_balance,_serverHash,_userHash,_gameId,_contractAddress,_userAddress,_userSig)
11:08:37 [WARNING] 0xfbc6b9110b20f05cebf7d910cf855da6621026d6fc07f644f140724ab9666537createGame(_userEndHash,_previousGameId,_createBefore,_serverEndHash,_serverSig)
11:08:37 [WARNING] 0x9492c60836ea57f4ac40e915442ab6ffde552433d44c0a99ccdb81be2cc1b375serverEndGame(_roundId,_balance,_serverHash,_userHash,_gameId,_contractAddress,_userAddress,_userSig)
11:08:37 [WARNING] 0x865d3e2b0173a37db4de13054ba171255b53258824de153524048a27557e40e1createGame(_userEndHash,_previousGameId,_createBefore,_serverEndHash,_serverSig)
11:08:37 [WARNING] 0xdfa4d930ff56b1579a19b6294cde73cf09fae6e88dc2b50d215aaeb4ee59c23ecreateGame(_userEndHash,_previousGameId,_createBefore,_serverEndHash,_serverSig)
11:08:37 [WARNING] 0x33d831838713a336fca4c2e14505a721b6f6cd27806731c42be292d07c2c9979serverEndGame(_roundId,_balance,_serverHash,_userHash,_gameId,_contractAddress,_userAddress,_userSig)
11:08:37 [WARNING] 0x41af0ae5438d0b15509832bd55bf28a8ea8a65eae8320c14f519846517086af2createGame(_userEndHash,_previousGameId,_createBefore,_serverEndHash,_serverSig)
11:08:38 [WARNING] 0x2130077a43aba52d3a23622c71f42a9f1e5228931a442ab9054e7047845add8dserverEndGame(_roundId,_balance,_serverHash,_userHash,_gameId,_contractAddress,_userAddress,_userSig)
11:08:38 [WARNING] 0x72fddb6c04f3855d6697f9d0f054575eb843570017707dc88e114f40a197451cserverEndGame(_roundId,_balance,_serverHash,_userHash,_gameId,_contractAddress,_userAddress,_userSig)
11:08:38 [WARNING] 0x41921428aeedc6094e1560a5f7e744f1201382eb1632cd770230a441916139c1createGame(_userEndHash,_previousGameId,_createBefore,_serverEndHash,_serverSig)
11:08:38 [WARNING] 0xba4ae9cc1c9a14d48ae97af3ed330477890a7493dd5d83fbcca767f8c5397be9serverEndGame(_roundId,_balance,_serverHash,_userHash,_gameId,_contractAddress,_userAddress,_userSig)
11:08:38 [WARNING] 0x8fe02c629d629d3b935a33cda223c84583503243d28c626e1e86a36634463c8bcreateGame(_userEndHash,_previousGameId,_createBefore,_serverEndHash,_serverSig)
11:08:38 [WARNING] 0x4450bd6416b7dcc2d143e3b456fe07f2c22348be15af45eaa08beda53ce864f9createGame(_userEndHash,_previousGameId,_createBefore,_serverEndHash,_serverSig)
11:08:38 [WARNING] 0x0144005244050caa11c605c3fa425ef7374481e117000d46e4d23b7f6df35c3cserverEndGame(_roundId,_balance,_serverHash,_userHash,_gameId,_contractAddress,_userAddress,_userSig)
11:08:38 [WARNING] 0xf1a0c0a4f88b46d9d0d6c002fa482541e260bd7ca054d8341b663736737ab6d4serverEndGame(_roundId,_balance,_serverHash,_userHash,_gameId,_contractAddress,_userAddress,_userSig)
11:08:38 [WARNING] 0xf3ddf6d9b5f54d8183b8c58a64afdff83ab5d64ba31a1dc3e91e73c1fb217cb1createGame(_userEndHash,_previousGameId,_createBefore,_serverEndHash,_serverSig)
11:08:38 [WARNING] 0xe0c792b4397e101dec959ab16617e49c4efe6d8364b3152465099a053b6d7d6fserverEndGame(_roundId,_balance,_serverHash,_userHash,_gameId,_contractAddress,_userAddress,_userSig)
11:08:38 [WARNING] 0x9dae15552d913598a93ceb9dc2a60bb809e37ef7851f72e09b15c28d533d0774createGame(_userEndHash,_previousGameId,_createBefore,_serverEndHash,_serverSig)
11:08:38 [WARNING] 0xc00f00d69f65245e07d8164fbd9c553f016056f4947bd03107656d7b3398d4c0createGame(_userEndHash,_previousGameId,_createBefore,_serverEndHash,_serverSig)
11:08:39 [WARNING] 0x858f2cd0430766ba957dad6a23e2adec8749e0033a9644674ad40c6861433cf8serverEndGame(_roundId,_balance,_serverHash,_userHash,_gameId,_contractAddress,_userAddress,_userSig)
11:08:39 [WARNING] 0x51e7fc58b2a3da99295c21fc7e0da4a7e6a31332284ce19015ea7afd52a273a9createGame(_userEndHash,_previousGameId,_createBefore,_serverEndHash,_serverSig)
11:08:39 [WARNING] 0x9a09db3fb52cbcf686fe3ba53325d7e632a702d88c5d0fe35ce81439be62823eserverCancelActiveGame(_userAddress,_gameId)
11:08:39 [WARNING] 0x56f90410aea7acfefad3ea7f2fdb48c1a1feb6d54ba0992eb35b45dedecada0fserverEndGame(_roundId,_balance,_serverHash,_userHash,_gameId,_contractAddress,_userAddress,_userSig)
11:08:39 [WARNING] 0x9f83cc6b2bcc5c884089679bf526642f5aad005b23b9bff5c18a71084ce6e8eacreateGame(_userEndHash,_previousGameId,_createBefore,_serverEndHash,_serverSig)
11:08:39 [WARNING] 0x5753e2237de34a33983f22c9ed2cb9823806694dc2a9d6961754a71b4590dc3eserverEndGameConflict(_roundId,_gameType,_num,_value,_balance,_serverHash,_userHash,_gameId,_contractAddress,_userSig,_userAddress,_serverSeed,_userSeed)
11:08:39 [WARNING] 0x6b4cde62e5e61a151d59448e6e7fcbcce858c2f3f62ad78ff339b512d915d1f3serverEndGameConflict(_roundId,_gameType,_num,_value,_balance,_serverHash,_userHash,_gameId,_contractAddress,_userSig,_userAddress,_serverSeed,_userSeed)
11:08:39 [WARNING] 0x42941356323e1c4b93c256198b92383619f5621c0d59ba4e64f4d92582a495c6serverForceGameEnd(_userAddress,_gameId)
11:08:39 [WARNING] 0xb64a2184ff814426a37e86bc53a8eb306beec02677f8c025d7d8588cd017befaserverForceGameEnd(_userAddress,_gameId)
11:08:39 [WARNING] 0x2fbb06cf109ded1911056c7dc8dfc01fc05942047f7a5c371466b753c8091f6bcreateGame(_userEndHash,_previousGameId,_createBefore,_serverEndHash,_serverSig)
11:08:39 [WARNING] 0x34200ee9a95f325b7b65c1d268b113280e1a0f2c2b56934a3972a23ebf2bef8fserverEndGame(_roundId,_balance,_serverHash,_userHash,_gameId,_contractAddress,_userAddress,_userSig)
11:08:39 [WARNING] 0xed48e0d075d4a3ef00a0dbde5ba94f3889ad80d22754e54958dcb4f0166e409bcreateGame(_userEndHash,_previousGameId,_createBefore,_serverEndHash,_serverSig)
11:08:39 [WARNING] 0x846509131c99490575b1a99f07d61a44a7f835a562d7f4e2dfa8ddecc6c75676serverEndGame(_roundId,_balance,_serverHash,_userHash,_gameId,_contractAddress,_userAddress,_userSig)
11:08:40 [WARNING] 0x2f8bf2ad73c907d82fb52620b53fb568d518b804a2f85674503e91d1ad067508createGame(_userEndHash,_previousGameId,_createBefore,_serverEndHash,_serverSig)
11:08:40 [WARNING] 0x3cdae51e04d63ae07d9bea8ffc83ccad7b44df64a04fa887628ad9a97039da9bserverEndGame(_roundId,_balance,_serverHash,_userHash,_gameId,_contractAddress,_userAddress,_userSig)
11:08:40 [WARNING] 0x9c922a9b8f2f8c20b5fe6141a9ab70d0fbd0b2474e88985eb85b3c0b16f47116createGame(_userEndHash,_previousGameId,_createBefore,_serverEndHash,_serverSig)
11:08:40 [WARNING] 0xa24e86fe5979ba15f9b4816326b88c6d4ccb69651acc95def79eb18302ba7a9acreateGame(_userEndHash,_previousGameId,_createBefore,_serverEndHash,_serverSig)
11:08:40 [WARNING] 0x00a2655c9b5aceb96a2a23727d0c3b84bd769458bfde7ed574203c2b58467016serverEndGame(_roundId,_balance,_serverHash,_userHash,_gameId,_contractAddress,_userAddress,_userSig)
11:08:40 [WARNING] 0x7736827a7e1ad49b0bacab95aed90a7efd3dc98e27c2e87bcb9fec73c6889698createGame(_userEndHash,_previousGameId,_createBefore,_serverEndHash,_serverSig)
11:08:40 [WARNING] 0x6be56164193bcfb779042461c88e40c6dd7fb99cd62ce4d8ffad7b4f3c5e8437serverForceGameEnd(_userAddress,_gameId)
11:08:40 [WARNING] 0x1deedb332c4484e0cd4dcca96fe8a7d66204ed9a7d3f14c0cc0c3fe0a1a802a5serverEndGame(_roundId,_balance,_serverHash,_userHash,_gameId,_contractAddress,_userAddress,_userSig)
11:08:40 [WARNING] 0xc64353af25606f882889daa6ba99d660b921723da7655c4b8dc1738e4d1bba76createGame(_userEndHash,_previousGameId,_createBefore,_serverEndHash,_serverSig)
11:08:40 [WARNING] 0x2e00bb4d61246a81add9f5507376e664626cabf4d440f4188e0af18911824a8aserverEndGame(_roundId,_balance,_serverHash,_userHash,_gameId,_contractAddress,_userAddress,_userSig)
11:08:40 [WARNING] 0x46cfb33288062cf528cf0a8edc37c6adef7feaa2bf179caf1a4754670c2e1a46serverEndGame(_roundId,_balance,_serverHash,_userHash,_gameId,_contractAddress,_userAddress,_userSig)
11:08:40 [WARNING] 0x5e2e01f62dbcc7edcc9c1903f56be754ff4d2c9506fe6b9f024798f57fa5674bcreateGame(_userEndHash,_previousGameId,_createBefore,_serverEndHash,_serverSig)
11:08:41 [WARNING] 0x1bf532d112d44de932d8d438934848e8333f2e4505597caa5c558b6d962944f4createGame(_userEndHash,_previousGameId,_createBefore,_serverEndHash,_serverSig)
11:08:41 [WARNING] 0xa45fb0cb2a99e24198934aea6144b90c495c45e0ffe6cf0869e9c7d992ee6c81serverEndGame(_roundId,_balance,_serverHash,_userHash,_gameId,_contractAddress,_userAddress,_userSig)
11:08:41 [WARNING] 0x33b44d7bfa4b5cb3c38d91c9c769de888d29b8478f5a362b6dcfa67c620e481ccreateGame(_userEndHash,_previousGameId,_createBefore,_serverEndHash,_serverSig)
11:08:41 [WARNING] 0x21cafbc6afae78add89afafc8acb087858b06fa9a2a66e6c4b67eace7cbcd919serverEndGame(_roundId,_balance,_serverHash,_userHash,_gameId,_contractAddress,_userAddress,_userSig)
11:08:41 [WARNING] 0x205997757258947ba45d088dd54f93c496d89238df585133b98972d595daf764createGame(_userEndHash,_previousGameId,_createBefore,_serverEndHash,_serverSig)
11:08:41 [WARNING] 0x26c77c0b752de292b806042af6ef6d0ecb22a9fa8f673f963a7952db02019b4eserverEndGame(_roundId,_balance,_serverHash,_userHash,_gameId,_contractAddress,_userAddress,_userSig)
11:08:41 [WARNING] 0x857ca7a9a139e6edfcaaa5c9a8c226d534c7387b51b263807001dea102be54e2createGame(_userEndHash,_previousGameId,_createBefore,_serverEndHash,_serverSig)
11:08:41 [WARNING] 0xacaed4d7b93d07904c850fc199fd0a0db968f5595eee92ff2b791662dbdb59a6serverEndGame(_roundId,_balance,_serverHash,_userHash,_gameId,_contractAddress,_userAddress,_userSig)
11:08:41 [WARNING] 0xba15302eb1959286156dd550f59f80f96badc271f015c577a946d92412612bd2createGame(_userEndHash,_previousGameId,_createBefore,_serverEndHash,_serverSig)
11:08:41 [WARNING] 0x531295bfc996f88cc61922b17a5f5dbaffca2d34621144bd18f5b01cf913d292createGame(_userEndHash,_previousGameId,_createBefore,_serverEndHash,_serverSig)
11:08:41 [WARNING] 0x905d7dea6c84355414475ba6bd53b77ac19fa3c37a2c5921f3dd894f4926d09cserverEndGame(_roundId,_balance,_serverHash,_userHash,_gameId,_contractAddress,_userAddress,_userSig)
11:08:41 [WARNING] 0xf2b3809a795129f072c95647bccd4afcef779fedfe93aa8fb61330d97a79370bserverEndGame(_roundId,_balance,_serverHash,_userHash,_gameId,_contractAddress,_userAddress,_userSig)
11:08:42 [WARNING] 0x6c40acce06dc5ce03c3911b494d920c7e9bb2eb73adc4c02fa2c3e604807f04ccreateGame(_userEndHash,_previousGameId,_createBefore,_serverEndHash,_serverSig)
11:08:42 [WARNING] 0x3c182048c80e1ec1a36f346c7e8a765da02e403fd6f265afdcf66775563a933cserverEndGame(_roundId,_balance,_serverHash,_userHash,_gameId,_contractAddress,_userAddress,_userSig)
11:08:42 [WARNING] 0xceb25939b9d5e671c86007061af416c8909b36dbd0e90ebfc2b36f985da9cb7dcreateGame(_userEndHash,_previousGameId,_createBefore,_serverEndHash,_serverSig)
11:08:42 [WARNING] 0x6da3da54951524cd183a83990a04657372e12d689ed217b929a3ecb57a4e1486serverEndGame(_roundId,_balance,_serverHash,_userHash,_gameId,_contractAddress,_userAddress,_userSig)
11:08:42 [WARNING] 0x0642ce632b655fa9ed1882c0dd18b804e743338593a7109a04123fbdd4498c55createGame(_userEndHash,_previousGameId,_createBefore,_serverEndHash,_serverSig)
11:08:42 [WARNING] 0xf761e58761e47ef6666c08e8abc7e34206920b1d255c61b99e62b883a28dd3a3serverEndGame(_roundId,_balance,_serverHash,_userHash,_gameId,_contractAddress,_userAddress,_userSig)
11:08:42 [WARNING] 0xeb19602eccefabe98f99c23fe3976adea660d486f3386e040b0ce0ce93b97112createGame(_userEndHash,_previousGameId,_createBefore,_serverEndHash,_serverSig)
11:08:42 [WARNING] 0x615351f94b76579792ca1efeaaee285bf9ce55f6ed53ca170f5b60d5b67c7136serverEndGame(_roundId,_balance,_serverHash,_userHash,_gameId,_contractAddress,_userAddress,_userSig)
11:08:42 [WARNING] 0xf02bf46f101861a9c8acdcfed497243f7197d78c90f6ebfc0d8dcfb8d1b62147createGame(_userEndHash,_previousGameId,_createBefore,_serverEndHash,_serverSig)
11:08:42 [WARNING] 0xd9f72759cb725f033db9dce3a894647cfff1afb4530d055cc725010a8f8b04d2serverEndGame(_roundId,_balance,_serverHash,_userHash,_gameId,_contractAddress,_userAddress,_userSig)
11:08:42 [WARNING] 0xd1edca536ae27f90715bbbc49fe91aad91448206d6fb892fe788ab356e9cb369serverEndGame(_roundId,_balance,_serverHash,_userHash,_gameId,_contractAddress,_userAddress,_userSig)
11:08:42 [WARNING] 0x37da06db33bde1d959f1d60b4c3d253455274d603efd7a413c8d18c7c1e7c1f1createGame(_userEndHash,_previousGameId,_createBefore,_serverEndHash,_serverSig)
11:08:43 [WARNING] 0xb5be6e0d1409a0183449032d10c8f715e60e5c6baaea03c6d741795e4c9bce6fserverEndGame(_roundId,_balance,_serverHash,_userHash,_gameId,_contractAddress,_userAddress,_userSig)
11:08:43 [WARNING] 0x95da6b3a25289adbe6ed58c8833ee6998eb348f513274eaa992814c3e435592dcreateGame(_userEndHash,_previousGameId,_createBefore,_serverEndHash,_serverSig)
11:08:43 [WARNING] 0x1f8934928fa0824effa948b05398380d2b608c4b52e7c1638d9506780ebbd7ddserverEndGame(_roundId,_balance,_serverHash,_userHash,_gameId,_contractAddress,_userAddress,_userSig)
11:08:43 [WARNING] 0xd6b5e372b991d3a13d9a4309ff2e946ac464908dee0d126a62d4beb9caecd49acreateGame(_userEndHash,_previousGameId,_createBefore,_serverEndHash,_serverSig)
11:08:43 [WARNING] 0x0e8ce6ab92abd341fe6fadb04f31456fa7ea5531540b306739e4716c0205adbcserverEndGame(_roundId,_balance,_serverHash,_userHash,_gameId,_contractAddress,_userAddress,_userSig)
11:08:43 [WARNING] 0x6f3caa6d28fe9e045f6aaa4ebab8e5d061257a701c57bd1a6ab875d2d5f08bffcreateGame(_userEndHash,_previousGameId,_createBefore,_serverEndHash,_serverSig)
11:08:43 [WARNING] 0x48bb7917568ccaa651d7b3d937015d27bf7311ff0965fde80cb901c47d860fd7serverEndGame(_roundId,_balance,_serverHash,_userHash,_gameId,_contractAddress,_userAddress,_userSig)
11:08:43 [WARNING] 0x0d3bb131e3265f3c6cd6c02896fd6db6bb35f7d66934213e52e28933994a49f2createGame(_userEndHash,_previousGameId,_createBefore,_serverEndHash,_serverSig)
11:08:43 [WARNING] 0xa88f7e2db36eae6e70f8e3d403d982140b7f85e9792feb22f77a927e2d03e2d7serverEndGame(_roundId,_balance,_serverHash,_userHash,_gameId,_contractAddress,_userAddress,_userSig)
11:08:43 [WARNING] 0x2882b75c3e7fa71d25876e96009210bdc4317b61537111f5c2a2b9cea0971b11createGame(_userEndHash,_previousGameId,_createBefore,_serverEndHash,_serverSig)
11:08:43 [WARNING] 0xdcda209f1a4f35a72f4be1753fe181dbc4728abb40fcba427b008d6954138fa1serverEndGame(_roundId,_balance,_serverHash,_userHash,_gameId,_contractAddress,_userAddress,_userSig)
11:08:44 [WARNING] 0xb1cf6de01e0e5dd6951f9de970736fd485eed47882ef191db276e56ded7c238bcreateGame(_userEndHash,_previousGameId,_createBefore,_serverEndHash,_serverSig)
11:08:44 [WARNING] 0x6e34b5f9551772784c48bd478dd6c17d31cdf698b37b8175b81baa9d9065ed83serverEndGame(_roundId,_balance,_serverHash,_userHash,_gameId,_contractAddress,_userAddress,_userSig)
11:08:44 [WARNING] 0x4f7eb3e3d193ca869568e141b092d13e29a4380d8666c7e268edf2a2cc22045dcreateGame(_userEndHash,_previousGameId,_createBefore,_serverEndHash,_serverSig)
11:08:44 [WARNING] 0xd1c3a68c85f1fdb5a9bbfcb93ddae6419b7c54216f0cd303ac8790fd985a4f4fserverEndGame(_roundId,_balance,_serverHash,_userHash,_gameId,_contractAddress,_userAddress,_userSig)
11:08:44 [WARNING] 0x6dfaae51b1ec7d9d43d3fde315dd535ec185d152225f4b13948d8cc69566ae18createGame(_userEndHash,_previousGameId,_createBefore,_serverEndHash,_serverSig)
11:08:44 [WARNING] 0x2220c0160ad718a70319bf7cc5e216b7ace885ccad6790972811cd4140756a0dcreateGame(_userEndHash,_previousGameId,_createBefore,_serverEndHash,_serverSig)
11:08:44 [WARNING] 0xd3500243f3f7810f2935d19aaa21ecd9ed304b06ac78e8d0644ffb9c23f4697fserverEndGame(_roundId,_balance,_serverHash,_userHash,_gameId,_contractAddress,_userAddress,_userSig)
11:08:44 [WARNING] 0xc580bb07218ea5784000b8bf87713f0eb43c472cfc033dffb18acda8d9faaf35createGame(_userEndHash,_previousGameId,_createBefore,_serverEndHash,_serverSig)
11:08:44 [WARNING] 0xfe46ba42b499fbf97905992bd7c3b26a33c87ad3e1d179c8a7fd61c0ee6c2634serverEndGame(_roundId,_balance,_serverHash,_userHash,_gameId,_contractAddress,_userAddress,_userSig)
11:08:44 [WARNING] 0xb69938be79878b2aee6e390bcc9a7cda5c468a639c7f7b2bc87eabd96a2b3240createGame(_userEndHash,_previousGameId,_createBefore,_serverEndHash,_serverSig)
11:08:44 [WARNING] 0xe4b360f9f9bf44a6634bb7d28d9458842ab9bf48aacfec0ad8392ad3c0590238createGame(_userEndHash,_previousGameId,_createBefore,_serverEndHash,_serverSig)
11:08:44 [WARNING] 0x86c1e27425fbc5eaf4818a08f2c62f17093a1ec2ed0bc1460e3ec281ff00b2e4serverEndGame(_roundId,_balance,_serverHash,_userHash,_gameId,_contractAddress,_userAddress,_userSig)
11:08:45 [WARNING] 0x0f5e6e0fdcdba11c9a8999901dc9362526f83c86c71326c59f83a0efd2bb4851createGame(_userEndHash,_previousGameId,_createBefore,_serverEndHash,_serverSig)
11:08:45 [WARNING] 0xee3d3de01363c63411c8e1b1d89840579705de0b6f8f56b188e92145b5085e08createGame(_userEndHash,_previousGameId,_createBefore,_serverEndHash,_serverSig)
11:08:45 [WARNING] 0x73c92b1b5bcc3daa7b825cc44a63560f554cde7dd6ced706bf82c9eb1904c3afserverEndGame(_roundId,_balance,_serverHash,_userHash,_gameId,_contractAddress,_userAddress,_userSig)
11:08:45 [WARNING] 0x91df45c066be7071ec8aac496a2fc3d89747c3dcf1730da032b542eae97de637serverEndGame(_roundId,_balance,_serverHash,_userHash,_gameId,_contractAddress,_userAddress,_userSig)
11:08:45 [WARNING] 0x1b9cda98816e21e2fc85e7346083c9de7610ee507273fdef1c1e06bb245e91e0serverEndGame(_roundId,_balance,_serverHash,_userHash,_gameId,_contractAddress,_userAddress,_userSig)
11:08:45 [WARNING] 0x9619452c8d7e76f2e4253d6976ecaec4e06f61c2687b4d26b1c5010b347c8febcreateGame(_userEndHash,_previousGameId,_createBefore,_serverEndHash,_serverSig)
11:08:45 [WARNING] 0xcda8aac881a63780f1abd2bf8416eeba89ef2347571ce3e0a8fb4e576f5202a0serverEndGame(_roundId,_balance,_serverHash,_userHash,_gameId,_contractAddress,_userAddress,_userSig)
11:08:45 [WARNING] 0x1ef208dfbddee06a8806d5d7e07d5a439d07c817a321c7ba3d25e7a2f57d6962serverEndGameConflict(_roundId,_gameType,_num,_value,_balance,_serverHash,_userHash,_gameId,_contractAddress,_userSig,_userAddress,_serverSeed,_userSeed)
11:08:45 [WARNING] 0x7ab05aa46bc7eace1284b349254fec3b021225d58cbf957fd92a0a05859fdbefcreateGame(_userEndHash,_previousGameId,_createBefore,_serverEndHash,_serverSig)
11:08:45 [WARNING] 0x18de23214564ad7fbef8844924eee98853c78a6003b189cdaa6dcb320031f181serverEndGame(_roundId,_balance,_serverHash,_userHash,_gameId,_contractAddress,_userAddress,_userSig)
11:08:46 [WARNING] 0x86fc74deb87ce16fa86453bd43b933ea291f183765f0aec277a1d67297367817createGame(_userEndHash,_previousGameId,_createBefore,_serverEndHash,_serverSig)
11:08:46 [WARNING] 0x9e975bfed174b21a093961d14c0ca59e2cd6a4e3438458ecc8fdf2ecd4d5963eserverForceGameEnd(_userAddress,_gameId)
11:08:46 [WARNING] 0xd2e78e1ca88dea7fabc9ec46a2a7fccd4a6ebd8acf588927a402d20e86e2960acreateGame(_userEndHash,_previousGameId,_createBefore,_serverEndHash,_serverSig)
11:08:46 [WARNING] 0xdb44fcc346268bba0dc0f434cd4c9e2fda78875470b4f7f41c7e72d28a71877eserverEndGame(_roundId,_balance,_serverHash,_userHash,_gameId,_contractAddress,_userAddress,_userSig)
11:08:46 [WARNING] 0xd024e4458dcf457151bc462e8bc3e438a328794e590c7fdf6a0b3af905469a5ecreateGame(_userEndHash,_previousGameId,_createBefore,_serverEndHash,_serverSig)
11:08:46 [WARNING] 0x657c7dd9d739f146f204a724eeae845ef445e883766afe67b2c0b844487b7d19serverEndGame(_roundId,_balance,_serverHash,_userHash,_gameId,_contractAddress,_userAddress,_userSig)
11:08:46 [WARNING] 0x4f7673f7d613089c0af946a549fbec455bb5d72a7054658181dbc8e7d81c4f30createGame(_userEndHash,_previousGameId,_createBefore,_serverEndHash,_serverSig)
11:08:46 [WARNING] 0xd5e481bc28c2206ea618e7471aebed8e5f05e9362df17c486f14a63ebd69c310serverEndGame(_roundId,_balance,_serverHash,_userHash,_gameId,_contractAddress,_userAddress,_userSig)
11:08:46 [WARNING] 0x76ca625d7e856ab244719a576f25c3b9b398346ca70d274cc3f3fb5eafb8e84acreateGame(_userEndHash,_previousGameId,_createBefore,_serverEndHash,_serverSig)
11:08:46 [WARNING] 0x66140460ef88b2b89bdb16d41219addd6cddd25154e1df2bf74dea7c91cf6df7createGame(_userEndHash,_previousGameId,_createBefore,_serverEndHash,_serverSig)
11:08:46 [WARNING] 0x8178b9e57d21a6c8904ba5c9f29d005bf667c87dced10f58f0f646ed9e1a1511createGame(_userEndHash,_previousGameId,_createBefore,_serverEndHash,_serverSig)
11:08:47 [WARNING] 0xcd06451c91b8182b3e1b3e6d75773c017993c23603dde83ba0f5c64e0c9ed806serverEndGame(_roundId,_balance,_serverHash,_userHash,_gameId,_contractAddress,_userAddress,_userSig)
11:08:47 [WARNING] 0x4a24b510128c6ea0b1b85a999db9fe66121327a1abcc4ea4129465da3a6ed15bserverEndGameConflict(_roundId,_gameType,_num,_value,_balance,_serverHash,_userHash,_gameId,_contractAddress,_userSig,_userAddress,_serverSeed,_userSeed)
11:08:47 [WARNING] 0x380e7152d60c44ee967bd7e7da9215b85be27f40703d6c2e49c1af56da6e7771createGame(_userEndHash,_previousGameId,_createBefore,_serverEndHash,_serverSig)
11:08:47 [WARNING] 0xd4c11872edc2629b03cf1c9e6a9d163e38889416168e689e29773bd93968fe96createGame(_userEndHash,_previousGameId,_createBefore,_serverEndHash,_serverSig)
11:08:47 [WARNING] 0x994d1d5b06c61832dd88f0e45eb35a4174d65a87beafb7b182ac10fb74c7dda4serverEndGame(_roundId,_balance,_serverHash,_userHash,_gameId,_contractAddress,_userAddress,_userSig)
11:08:47 [WARNING] 0xbc9da23fd89adcda8ad209523f5d877d9827c144e0510dc1043f06b3abeb3f88createGame(_userEndHash,_previousGameId,_createBefore,_serverEndHash,_serverSig)
11:08:47 [WARNING] 0x843d7ab5e347c6a680767a9a2a2aaf697b99e3c9a4edc411dc81a5ba7881435dcreateGame(_userEndHash,_previousGameId,_createBefore,_serverEndHash,_serverSig)
11:08:47 [WARNING] 0xd0aa5fbcaa854e5db7ee2ca4d7ce50301d3ea8faf978b6409a7746e767e61341serverEndGame(_roundId,_balance,_serverHash,_userHash,_gameId,_contractAddress,_userAddress,_userSig)
11:08:47 [WARNING] 0x787b09f5204cebed8779eda40
...
ori(minStake) > ori(lastProfitTransferTimestamp)
ori(minStake) != ori(lastProfitTransferTimestamp)
ori(minStake) >= userGameId[_userAddress]
ori(minStake) > userGameId[_userAddress]
ori(minStake) != userGameId[_userAddress]
ori(minStake) >= ori(activeGames)
ori(minStake) > ori(activeGames)
ori(minStake) != ori(activeGames)
ori(minStake) >= pendingReturns[_userAddress]
ori(minStake) > pendingReturns[_userAddress]
ori(minStake) != pendingReturns[_userAddress]
ori(minStake) >= timePaused
ori(minStake) > timePaused
ori(minStake) != timePaused
ori(minStake) >= ori(gameIdCntr)
ori(minStake) > ori(gameIdCntr)
ori(minStake) != ori(gameIdCntr)
ori(minStake) >= msg.value
ori(minStake) > msg.value
ori(minStake) != msg.value
ori(minStake) >= lastProfitTransferTimestamp
ori(minStake) > lastProfitTransferTimestamp
ori(minStake) != lastProfitTransferTimestamp
ori(minStake) >= ori(userGameId[_userAddress])
ori(minStake) > ori(userGameId[_userAddress])
ori(minStake) != ori(userGameId[_userAddress])
ori(minStake) >= ori(Sum(userGameId[...]))
ori(minStake) > ori(Sum(userGameId[...]))
ori(minStake) != ori(Sum(userGameId[...]))
ori(minStake) >= ori(Sum(pendingReturns[...]))
ori(minStake) > ori(Sum(pendingReturns[...]))
ori(minStake) != ori(Sum(pendingReturns[...]))
ori(minStake) >= Sum(userGameId[...])
ori(minStake) > Sum(userGameId[...])
ori(minStake) != Sum(userGameId[...])
ori(minStake) >= Sum(pendingReturns[...])
ori(minStake) > Sum(pendingReturns[...])
ori(minStake) != Sum(pendingReturns[...])
_gameId <= ori(lastProfitTransferTimestamp)
_gameId < ori(lastProfitTransferTimestamp)
_gameId != ori(lastProfitTransferTimestamp)
_gameId == userGameId[_userAddress]
_gameId >= userGameId[_userAddress]
_gameId <= userGameId[_userAddress]
_gameId >= ori(activeGames)
_gameId > ori(activeGames)
_gameId != ori(activeGames)
_gameId >= pendingReturns[_userAddress]
_gameId > pendingReturns[_userAddress]
_gameId != pendingReturns[_userAddress]
_gameId >= timePaused
_gameId > timePaused
_gameId != timePaused
_gameId <= ori(gameIdCntr)
_gameId < ori(gameIdCntr)
_gameId != ori(gameIdCntr)
_gameId >= msg.value
_gameId > msg.value
_gameId != msg.value
_gameId <= lastProfitTransferTimestamp
_gameId < lastProfitTransferTimestamp
_gameId != lastProfitTransferTimestamp
_gameId == ori(userGameId[_userAddress])
_gameId >= ori(userGameId[_userAddress])
_gameId <= ori(userGameId[_userAddress])
_gameId <= ori(Sum(userGameId[...]))
_gameId < ori(Sum(userGameId[...]))
_gameId != ori(Sum(userGameId[...]))
_gameId >= ori(Sum(pendingReturns[...]))
_gameId > ori(Sum(pendingReturns[...]))
_gameId != ori(Sum(pendingReturns[...]))
_gameId <= Sum(userGameId[...])
_gameId < Sum(userGameId[...])
_gameId != Sum(userGameId[...])
_gameId >= Sum(pendingReturns[...])
_gameId > Sum(pendingReturns[...])
_gameId != Sum(pendingReturns[...])
ori(lastProfitTransferTimestamp) >= userGameId[_userAddress]
ori(lastProfitTransferTimestamp) > userGameId[_userAddress]
ori(lastProfitTransferTimestamp) != userGameId[_userAddress]
ori(lastProfitTransferTimestamp) >= ori(activeGames)
ori(lastProfitTransferTimestamp) > ori(activeGames)
ori(lastProfitTransferTimestamp) != ori(activeGames)
ori(lastProfitTransferTimestamp) >= pendingReturns[_userAddress]
ori(lastProfitTransferTimestamp) > pendingReturns[_userAddress]
ori(lastProfitTransferTimestamp) != pendingReturns[_userAddress]
ori(lastProfitTransferTimestamp) >= timePaused
ori(lastProfitTransferTimestamp) > timePaused
ori(lastProfitTransferTimestamp) != timePaused
ori(lastProfitTransferTimestamp) >= ori(gameIdCntr)
ori(lastProfitTransferTimestamp) > ori(gameIdCntr)
ori(lastProfitTransferTimestamp) != ori(gameIdCntr)
ori(lastProfitTransferTimestamp) >= msg.value
ori(lastProfitTransferTimestamp) > msg.value
ori(lastProfitTransferTimestamp) != msg.value
ori(lastProfitTransferTimestamp) == lastProfitTransferTimestamp
ori(lastProfitTransferTimestamp) >= lastProfitTransferTimestamp
ori(lastProfitTransferTimestamp) <= lastProfitTransferTimestamp
ori(lastProfitTransferTimestamp) >= ori(userGameId[_userAddress])
ori(lastProfitTransferTimestamp) > ori(userGameId[_userAddress])
ori(lastProfitTransferTimestamp) != ori(userGameId[_userAddress])
ori(lastProfitTransferTimestamp) >= ori(Sum(userGameId[...]))
ori(lastProfitTransferTimestamp) > ori(Sum(userGameId[...]))
ori(lastProfitTransferTimestamp) != ori(Sum(userGameId[...]))
ori(lastProfitTransferTimestamp) >= ori(Sum(pendingReturns[...]))
ori(lastProfitTransferTimestamp) > ori(Sum(pendingReturns[...]))
ori(lastProfitTransferTimestamp) != ori(Sum(pendingReturns[...]))
ori(lastProfitTransferTimestamp) >= Sum(userGameId[...])
ori(lastProfitTransferTimestamp) > Sum(userGameId[...])
ori(lastProfitTransferTimestamp) != Sum(userGameId[...])
ori(lastProfitTransferTimestamp) >= Sum(pendingReturns[...])
ori(lastProfitTransferTimestamp) > Sum(pendingReturns[...])
ori(lastProfitTransferTimestamp) != Sum(pendingReturns[...])
ori(houseAddress) != serverAddress
ori(houseAddress) != _userAddress
ori(houseAddress) != ori(conflictRes)
ori(houseAddress) != owner
ori(houseAddress) != ori(serverAddress)
ori(houseAddress) != newConflictRes
userGameId[_userAddress] >= ori(activeGames)
userGameId[_userAddress] > ori(activeGames)
userGameId[_userAddress] != ori(activeGames)
userGameId[_userAddress] >= pendingReturns[_userAddress]
userGameId[_userAddress] > pendingReturns[_userAddress]
userGameId[_userAddress] != pendingReturns[_userAddress]
userGameId[_userAddress] >= timePaused
userGameId[_userAddress] > timePaused
userGameId[_userAddress] != timePaused
userGameId[_userAddress] <= ori(gameIdCntr)
userGameId[_userAddress] < ori(gameIdCntr)
userGameId[_userAddress] != ori(gameIdCntr)
userGameId[_userAddress] >= msg.value
userGameId[_userAddress] > msg.value
userGameId[_userAddress] != msg.value
userGameId[_userAddress] <= lastProfitTransferTimestamp
userGameId[_userAddress] < lastProfitTransferTimestamp
userGameId[_userAddress] != lastProfitTransferTimestamp
userGameId[_userAddress] == ori(userGameId[_userAddress])
userGameId[_userAddress] >= ori(userGameId[_userAddress])
userGameId[_userAddress] <= ori(userGameId[_userAddress])
userGameId[_userAddress] <= ori(Sum(userGameId[...]))
userGameId[_userAddress] < ori(Sum(userGameId[...]))
userGameId[_userAddress] != ori(Sum(userGameId[...]))
userGameId[_userAddress] >= ori(Sum(pendingReturns[...]))
userGameId[_userAddress] > ori(Sum(pendingReturns[...]))
userGameId[_userAddress] != ori(Sum(pendingReturns[...]))
userGameId[_userAddress] <= Sum(userGameId[...])
userGameId[_userAddress] < Sum(userGameId[...])
userGameId[_userAddress] != Sum(userGameId[...])
userGameId[_userAddress] >= Sum(pendingReturns[...])
userGameId[_userAddress] > Sum(pendingReturns[...])
userGameId[_userAddress] != Sum(pendingReturns[...])
ori(activeGames) >= pendingReturns[_userAddress]
ori(activeGames) > pendingReturns[_userAddress]
ori(activeGames) != pendingReturns[_userAddress]
ori(activeGames) >= timePaused
ori(activeGames) > timePaused
ori(activeGames) != timePaused
ori(activeGames) <= ori(gameIdCntr)
ori(activeGames) < ori(gameIdCntr)
ori(activeGames) != ori(gameIdCntr)
ori(activeGames) >= msg.value
ori(activeGames) > msg.value
ori(activeGames) != msg.value
ori(activeGames) <= lastProfitTransferTimestamp
ori(activeGames) < lastProfitTransferTimestamp
ori(activeGames) != lastProfitTransferTimestamp
ori(activeGames) <= ori(userGameId[_userAddress])
ori(activeGames) < ori(userGameId[_userAddress])
ori(activeGames) != ori(userGameId[_userAddress])
ori(activeGames) <= ori(Sum(userGameId[...]))
ori(activeGames) < ori(Sum(userGameId[...]))
ori(activeGames) != ori(Sum(userGameId[...]))
ori(activeGames) >= ori(Sum(pendingReturns[...]))
ori(activeGames) > ori(Sum(pendingReturns[...]))
ori(activeGames) != ori(Sum(pendingReturns[...]))
ori(activeGames) <= Sum(userGameId[...])
ori(activeGames) < Sum(userGameId[...])
ori(activeGames) != Sum(userGameId[...])
ori(activeGames) >= Sum(pendingReturns[...])
ori(activeGames) > Sum(pendingReturns[...])
ori(activeGames) != Sum(pendingReturns[...])
pendingReturns[_userAddress] == timePaused
pendingReturns[_userAddress] >= timePaused
pendingReturns[_userAddress] <= timePaused
pendingReturns[_userAddress] <= ori(gameIdCntr)
pendingReturns[_userAddress] < ori(gameIdCntr)
pendingReturns[_userAddress] != ori(gameIdCntr)
pendingReturns[_userAddress] == msg.value
pendingReturns[_userAddress] >= msg.value
pendingReturns[_userAddress] <= msg.value
pendingReturns[_userAddress] <= lastProfitTransferTimestamp
pendingReturns[_userAddress] < lastProfitTransferTimestamp
pendingReturns[_userAddress] != lastProfitTransferTimestamp
pendingReturns[_userAddress] <= ori(userGameId[_userAddress])
pendingReturns[_userAddress] < ori(userGameId[_userAddress])
pendingReturns[_userAddress] != ori(userGameId[_userAddress])
pendingReturns[_userAddress] <= ori(Sum(userGameId[...]))
pendingReturns[_userAddress] < ori(Sum(userGameId[...]))
pendingReturns[_userAddress] != ori(Sum(userGameId[...]))
pendingReturns[_userAddress] == ori(Sum(pendingReturns[...]))
pendingReturns[_userAddress] >= ori(Sum(pendingReturns[...]))
pendingReturns[_userAddress] <= ori(Sum(pendingReturns[...]))
pendingReturns[_userAddress] <= Sum(userGameId[...])
pendingReturns[_userAddress] < Sum(userGameId[...])
pendingReturns[_userAddress] != Sum(userGameId[...])
pendingReturns[_userAddress] == Sum(pendingReturns[...])
pendingReturns[_userAddress] >= Sum(pendingReturns[...])
pendingReturns[_userAddress] <= Sum(pendingReturns[...])
ori(paused) != ori(activated)
timePaused <= ori(gameIdCntr)
timePaused < ori(gameIdCntr)
timePaused != ori(gameIdCntr)
timePaused == msg.value
timePaused >= msg.value
timePaused <= msg.value
timePaused <= lastProfitTransferTimestamp
timePaused < lastProfitTransferTimestamp
timePaused != lastProfitTransferTimestamp
timePaused <= ori(userGameId[_userAddress])
timePaused < ori(userGameId[_userAddress])
timePaused != ori(userGameId[_userAddress])
timePaused <= ori(Sum(userGameId[...]))
timePaused < ori(Sum(userGameId[...]))
timePaused != ori(Sum(userGameId[...]))
timePaused == ori(Sum(pendingReturns[...]))
timePaused >= ori(Sum(pendingReturns[...]))
timePaused <= ori(Sum(pendingReturns[...]))
timePaused <= Sum(userGameId[...])
timePaused < Sum(userGameId[...])
timePaused != Sum(userGameId[...])
timePaused == Sum(pendingReturns[...])
timePaused >= Sum(pendingReturns[...])
timePaused <= Sum(pendingReturns[...])
serverAddress != _userAddress
serverAddress != ori(conflictRes)
serverAddress != owner
serverAddress == ori(serverAddress)
serverAddress != newConflictRes
_userAddress != ori(conflictRes)
_userAddress != owner
_userAddress != ori(serverAddress)
_userAddress != newConflictRes
ori(conflictRes) != owner
ori(conflictRes) != ori(serverAddress)
ori(conflictRes) != newConflictRes
owner != ori(serverAddress)
owner != newConflictRes
ori(gameIdCntr) >= msg.value
ori(gameIdCntr) > msg.value
ori(gameIdCntr) != msg.value
ori(gameIdCntr) <= lastProfitTransferTimestamp
ori(gameIdCntr) < lastProfitTransferTimestamp
ori(gameIdCntr) != lastProfitTransferTimestamp
ori(gameIdCntr) >= ori(userGameId[_userAddress])
ori(gameIdCntr) > ori(userGameId[_userAddress])
ori(gameIdCntr) != ori(userGameId[_userAddress])
ori(gameIdCntr) <= ori(Sum(userGameId[...]))
ori(gameIdCntr) < ori(Sum(userGameId[...]))
ori(gameIdCntr) != ori(Sum(userGameId[...]))
ori(gameIdCntr) >= ori(Sum(pendingReturns[...]))
ori(gameIdCntr) > ori(Sum(pendingReturns[...]))
ori(gameIdCntr) != ori(Sum(pendingReturns[...]))
ori(gameIdCntr) <= Sum(userGameId[...])
ori(gameIdCntr) < Sum(userGameId[...])
ori(gameIdCntr) != Sum(userGameId[...])
ori(gameIdCntr) >= Sum(pendingReturns[...])
ori(gameIdCntr) > Sum(pendingReturns[...])
ori(gameIdCntr) != Sum(pendingReturns[...])
ori(serverAddress) != newConflictRes
msg.value <= lastProfitTransferTimestamp
msg.value < lastProfitTransferTimestamp
msg.value != lastProfitTransferTimestamp
msg.value <= ori(userGameId[_userAddress])
msg.value < ori(userGameId[_userAddress])
msg.value != ori(userGameId[_userAddress])
msg.value <= ori(Sum(userGameId[...]))
msg.value < ori(Sum(userGameId[...]))
msg.value != ori(Sum(userGameId[...]))
msg.value == ori(Sum(pendingReturns[...]))
msg.value >= ori(Sum(pendingReturns[...]))
msg.value <= ori(Sum(pendingReturns[...]))
msg.value <= Sum(userGameId[...])
msg.value < Sum(userGameId[...])
msg.value != Sum(userGameId[...])
msg.value == Sum(pendingReturns[...])
msg.value >= Sum(pendingReturns[...])
msg.value <= Sum(pendingReturns[...])
lastProfitTransferTimestamp >= ori(userGameId[_userAddress])
lastProfitTransferTimestamp > ori(userGameId[_userAddress])
lastProfitTransferTimestamp != ori(userGameId[_userAddress])
lastProfitTransferTimestamp >= ori(Sum(userGameId[...]))
lastProfitTransferTimestamp > ori(Sum(userGameId[...]))
lastProfitTransferTimestamp != ori(Sum(userGameId[...]))
lastProfitTransferTimestamp >= ori(Sum(pendingReturns[...]))
lastProfitTransferTimestamp > ori(Sum(pendingReturns[...]))
lastProfitTransferTimestamp != ori(Sum(pendingReturns[...]))
lastProfitTransferTimestamp >= Sum(userGameId[...])
lastProfitTransferTimestamp > Sum(userGameId[...])
lastProfitTransferTimestamp != Sum(userGameId[...])
lastProfitTransferTimestamp >= Sum(pendingReturns[...])
lastProfitTransferTimestamp > Sum(pendingReturns[...])
lastProfitTransferTimestamp != Sum(pendingReturns[...])
ori(userGameId[_userAddress]) <= ori(Sum(userGameId[...]))
ori(userGameId[_userAddress]) < ori(Sum(userGameId[...]))
ori(userGameId[_userAddress]) != ori(Sum(userGameId[...]))
ori(userGameId[_userAddress]) >= ori(Sum(pendingReturns[...]))
ori(userGameId[_userAddress]) > ori(Sum(pendingReturns[...]))
ori(userGameId[_userAddress]) != ori(Sum(pendingReturns[...]))
ori(userGameId[_userAddress]) <= Sum(userGameId[...])
ori(userGameId[_userAddress]) < Sum(userGameId[...])
ori(userGameId[_userAddress]) != Sum(userGameId[...])
ori(userGameId[_userAddress]) >= Sum(pendingReturns[...])
ori(userGameId[_userAddress]) > Sum(pendingReturns[...])
ori(userGameId[_userAddress]) != Sum(pendingReturns[...])
ori(Sum(userGameId[...])) >= ori(Sum(pendingReturns[...]))
ori(Sum(userGameId[...])) > ori(Sum(pendingReturns[...]))
ori(Sum(userGameId[...])) != ori(Sum(pendingReturns[...]))
ori(Sum(userGameId[...])) == Sum(userGameId[...])
ori(Sum(userGameId[...])) >= Sum(userGameId[...])
ori(Sum(userGameId[...])) <= Sum(userGameId[...])
ori(Sum(userGameId[...])) >= Sum(pendingReturns[...])
ori(Sum(userGameId[...])) > Sum(pendingReturns[...])
ori(Sum(userGameId[...])) != Sum(pendingReturns[...])
ori(Sum(pendingReturns[...])) <= Sum(userGameId[...])
ori(Sum(pendingReturns[...])) < Sum(userGameId[...])
ori(Sum(pendingReturns[...])) != Sum(userGameId[...])
ori(Sum(pendingReturns[...])) == Sum(pendingReturns[...])
ori(Sum(pendingReturns[...])) >= Sum(pendingReturns[...])
ori(Sum(pendingReturns[...])) <= Sum(pendingReturns[...])
Sum(userGameId[...]) >= Sum(pendingReturns[...])
Sum(userGameId[...]) > Sum(pendingReturns[...])
Sum(userGameId[...]) != Sum(pendingReturns[...])
11:09:28 [WARNING] 

11:09:28 [WARNING] serverForceGameEnd(_userAddress,_gameId)
11:09:28 [WARNING] PptType.EXIT
11:09:28 [WARNING] TxType.REVERSION
11:09:28 [WARNING] 
11:09:28 [WARNING] 

11:09:28 [WARNING] setStakeRequirements(_minStake,_maxStake)
11:09:28 [WARNING] PptType.EXIT
11:09:28 [WARNING] TxType.NORMAL
11:09:28 [WARNING] 
11:09:28 [WARNING] 

11:09:28 [WARNING] setStakeRequirements(_minStake,_maxStake)
11:09:28 [WARNING] PptType.EXIT
11:09:28 [WARNING] TxType.REVERSION
11:09:28 [WARNING] 
11:09:28 [WARNING] 

11:09:28 [WARNING] userEndGame(_roundId,_balance,_serverHash,_userHash,_gameId,_contractAddress,_serverSig)
11:09:28 [WARNING] PptType.EXIT
11:09:28 [WARNING] TxType.NORMAL
11:09:28 [WARNING] 
11:09:28 [WARNING] 

11:09:28 [WARNING] userEndGame(_roundId,_balance,_serverHash,_userHash,_gameId,_contractAddress,_serverSig)
11:09:28 [WARNING] PptType.EXIT
11:09:28 [WARNING] TxType.REVERSION
11:09:28 [WARNING] 
11:09:28 [WARNING] 

11:09:28 [WARNING] setHouseAddress(_houseAddress)
11:09:28 [WARNING] PptType.EXIT
11:09:28 [WARNING] TxType.NORMAL
11:09:28 [WARNING] 
11:09:28 [WARNING] 

11:09:28 [WARNING] setHouseAddress(_houseAddress)
11:09:28 [WARNING] PptType.EXIT
11:09:28 [WARNING] TxType.REVERSION
11:09:28 [WARNING] 
11:09:28 [WARNING] 

11:09:28 [WARNING] transferOwnership(_newOwner)
11:09:28 [WARNING] PptType.EXIT
11:09:28 [WARNING] TxType.NORMAL
11:09:28 [WARNING] 
11:09:28 [WARNING] 

11:09:28 [WARNING] transferOwnership(_newOwner)
11:09:28 [WARNING] PptType.EXIT
11:09:28 [WARNING] TxType.REVERSION
11:09:28 [WARNING] 
11:09:28 [WARNING] 

11:09:28 [WARNING] transferProfitToHouse()
11:09:28 [WARNING] PptType.EXIT
11:09:28 [WARNING] TxType.NORMAL
11:09:28 [WARNING] 
11:09:28 [WARNING] 

11:09:28 [WARNING] transferProfitToHouse()
11:09:28 [WARNING] PptType.EXIT
11:09:28 [WARNING] TxType.REVERSION
11:09:28 [WARNING] 
11:09:28 [WARNING] 

11:09:28 [WARNING] None
11:09:28 [WARNING] PptType.CONTRACT
11:09:28 [WARNING] TxType.NORMAL
11:09:28 [WARNING] ori(updateTime) == 0
ori(updateTime) == 0
ori(updateTime) one of [0]
conflictRes != 0
ori(profitTransferTimeSpan) > 0
ori(profitTransferTimeSpan) == 1209600
ori(profitTransferTimeSpan) one of [1209600]
pendingOwner == 0
updateTime == 0
updateTime == 0
updateTime one of [0]
ori(timePaused) one of [0,1549483363]
ori(maxStake) > 0
ori(maxStake) == 30000000000000000000
ori(maxStake) one of [30000000000000000000]
activeGames one of [0,1,2,3,4,5,6]
houseAddress != 0
maxStake > 0
maxStake == 30000000000000000000
maxStake one of [30000000000000000000]
profitTransferTimeSpan > 0
profitTransferTimeSpan == 1209600
profitTransferTimeSpan one of [1209600]
gameIdCntr > 0
minStake > 0
minStake == 10000000000000000
minStake one of [10000000000000000]
elem of userGameId[...] is one of [0]
ori(pendingOwner) == 0
ori(newConflictRes) == 0
ori(owner) != 0
gameIdGame[...].userSeed != ""
ori(minStake) > 0
ori(minStake) == 10000000000000000
ori(minStake) one of [10000000000000000]
ori(lastProfitTransferTimestamp) > 0
ori(lastProfitTransferTimestamp) == 1549483363
ori(lastProfitTransferTimestamp) one of [1549483363]
ori(DOMAIN_SEPERATOR) != ""
ori(houseAddress) != 0
ori(activeGames) one of [0,1,2,3,4,5,6]
DOMAIN_SEPERATOR != ""
timePaused one of [0,1549483363]
serverAddress != 0
gameIdGame[...].serverSeed != ""
ori(conflictRes) != 0
owner != 0
ori(gameIdCntr) > 0
ori(serverAddress) != 0
lastProfitTransferTimestamp > 0
lastProfitTransferTimestamp == 1549483363
lastProfitTransferTimestamp one of [1549483363]
elem of pendingReturns[...] is one of [0]
elem of pendingReturns[...] is one of []
ori(Sum(pendingReturns[...])) == 0
ori(Sum(pendingReturns[...])) == 0
ori(Sum(pendingReturns[...])) one of [0]
newConflictRes == 0
Sum(pendingReturns[...]) == 0
Sum(pendingReturns[...]) == 0
Sum(pendingReturns[...]) one of [0]
ori(updateTime) <= ori(profitTransferTimeSpan)
ori(updateTime) < ori(profitTransferTimeSpan)
ori(updateTime) != ori(profitTransferTimeSpan)
ori(updateTime) == updateTime
ori(updateTime) >= updateTime
ori(updateTime) <= updateTime
ori(updateTime) <= ori(timePaused)
ori(updateTime) <= ori(maxStake)
ori(updateTime) < ori(maxStake)
ori(updateTime) != ori(maxStake)
ori(updateTime) <= activeGames
ori(updateTime) <= maxStake
ori(updateTime) < maxStake
ori(updateTime) != maxStake
ori(updateTime) <= ori(houseStake)
ori(updateTime) <= profitTransferTimeSpan
ori(updateTime) < profitTransferTimeSpan
ori(updateTime) != profitTransferTimeSpan
ori(updateTime) <= gameIdCntr
ori(updateTime) < gameIdCntr
ori(updateTime) != gameIdCntr
ori(updateTime) <= houseStake
ori(updateTime) <= minStake
ori(updateTime) < minStake
ori(updateTime) != minStake
ori(updateTime) <= ori(minStake)
ori(updateTime) < ori(minStake)
ori(updateTime) != ori(minStake)
ori(updateTime) <= ori(lastProfitTransferTimestamp)
ori(updateTime) < ori(lastProfitTransferTimestamp)
ori(updateTime) != ori(lastProfitTransferTimestamp)
ori(updateTime) <= ori(activeGames)
ori(updateTime) <= timePaused
ori(updateTime) <= ori(gameIdCntr)
ori(updateTime) < ori(gameIdCntr)
ori(updateTime) != ori(gameIdCntr)
ori(updateTime) <= lastProfitTransferTimestamp
ori(updateTime) < lastProfitTransferTimestamp
ori(updateTime) != lastProfitTransferTimestamp
ori(updateTime) <= ori(Sum(userGameId[...]))
ori(updateTime) == ori(Sum(pendingReturns[...]))
ori(updateTime) >= ori(Sum(pendingReturns[...]))
ori(updateTime) <= ori(Sum(pendingReturns[...]))
ori(updateTime) <= Sum(userGameId[...])
ori(updateTime) == Sum(pendingReturns[...])
ori(updateTime) >= Sum(pendingReturns[...])
ori(updateTime) <= Sum(pendingReturns[...])
conflictRes != pendingOwner
conflictRes != houseAddress
conflictRes != ori(pendingOwner)
conflictRes != ori(newConflictRes)
conflictRes != ori(owner)
conflictRes != ori(houseAddress)
conflictRes != serverAddress
conflictRes == ori(conflictRes)
conflictRes != owner
conflictRes != ori(serverAddress)
conflictRes != newConflictRes
ori(profitTransferTimeSpan) >= updateTime
ori(profitTransferTimeSpan) > updateTime
ori(profitTransferTimeSpan) != updateTime
ori(profitTransferTimeSpan) != ori(timePaused)
ori(profitTransferTimeSpan) <= ori(maxStake)
ori(profitTransferTimeSpan) < ori(maxStake)
ori(profitTransferTimeSpan) != ori(maxStake)
ori(profitTransferTimeSpan) >= activeGames
ori(profitTransferTimeSpan) > activeGames
ori(profitTransferTimeSpan) != activeGames
ori(profitTransferTimeSpan) <= maxStake
ori(profitTransferTimeSpan) < maxStake
ori(profitTransferTimeSpan) != maxStake
ori(profitTransferTimeSpan) != ori(houseStake)
ori(profitTransferTimeSpan) == profitTransferTimeSpan
ori(profitTransferTimeSpan) >= profitTransferTimeSpan
ori(profitTransferTimeSpan) <= profitTransferTimeSpan
ori(profitTransferTimeSpan) >= gameIdCntr
ori(profitTransferTimeSpan) > gameIdCntr
ori(profitTransferTimeSpan) != gameIdCntr
ori(profitTransferTimeSpan) != houseStake
ori(profitTransferTimeSpan) <= minStake
ori(profitTransferTimeSpan) < minStake
ori(profitTransferTimeSpan) != minStake
ori(profitTransferTimeSpan) <= ori(minStake)
ori(profitTransferTimeSpan) < ori(minStake)
ori(profitTransferTimeSpan) != ori(minStake)
ori(profitTransferTimeSpan) <= ori(lastProfitTransferTimestamp)
ori(profitTransferTimeSpan) < ori(lastProfitTransferTimestamp)
ori(profitTransferTimeSpan) != ori(lastProfitTransferTimestamp)
ori(profitTransferTimeSpan) >= ori(activeGames)
ori(profitTransferTimeSpan) > ori(activeGames)
ori(profitTransferTimeSpan) != ori(activeGames)
ori(profitTransferTimeSpan) != timePaused
ori(profitTransferTimeSpan) >= ori(gameIdCntr)
ori(profitTransferTimeSpan) > ori(gameIdCntr)
ori(profitTransferTimeSpan) != ori(gameIdCntr)
ori(profitTransferTimeSpan) <= lastProfitTransferTimestamp
ori(profitTransferTimeSpan) < lastProfitTransferTimestamp
ori(profitTransferTimeSpan) != lastProfitTransferTimestamp
ori(profitTransferTimeSpan) >= ori(Sum(userGameId[...]))
ori(profitTransferTimeSpan) > ori(Sum(userGameId[...]))
ori(profitTransferTimeSpan) != ori(Sum(userGameId[...]))
ori(profitTransferTimeSpan) >= ori(Sum(pendingReturns[...]))
ori(profitTransferTimeSpan) > ori(Sum(pendingReturns[...]))
ori(profitTransferTimeSpan) != ori(Sum(pendingReturns[...]))
ori(profitTransferTimeSpan) >= Sum(userGameId[...])
ori(profitTransferTimeSpan) > Sum(userGameId[...])
ori(profitTransferTimeSpan) != Sum(userGameId[...])
ori(profitTransferTimeSpan) >= Sum(pendingReturns[...])
ori(profitTransferTimeSpan) > Sum(pendingReturns[...])
ori(profitTransferTimeSpan) != Sum(pendingReturns[...])
pendingOwner != houseAddress
pendingOwner == ori(pendingOwner)
pendingOwner == ori(newConflictRes)
pendingOwner != ori(owner)
pendingOwner != ori(houseAddress)
pendingOwner != serverAddress
pendingOwner != ori(conflictRes)
pendingOwner != owner
pendingOwner != ori(serverAddress)
pendingOwner == newConflictRes
updateTime <= ori(timePaused)
updateTime <= ori(maxStake)
updateTime < ori(maxStake)
updateTime != ori(maxStake)
updateTime <= activeGames
updateTime <= maxStake
updateTime < maxStake
updateTime != maxStake
updateTime <= ori(houseStake)
updateTime <= profitTransferTimeSpan
updateTime < profitTransferTimeSpan
updateTime != profitTransferTimeSpan
updateTime <= gameIdCntr
updateTime < gameIdCntr
updateTime != gameIdCntr
updateTime <= houseStake
updateTime <= minStake
updateTime < minStake
updateTime != minStake
updateTime <= ori(minStake)
updateTime < ori(minStake)
updateTime != ori(minStake)
updateTime <= ori(lastProfitTransferTimestamp)
updateTime < ori(lastProfitTransferTimestamp)
updateTime != ori(lastProfitTransferTimestamp)
updateTime <= ori(activeGames)
updateTime <= timePaused
updateTime <= ori(gameIdCntr)
updateTime < ori(gameIdCntr)
updateTime != ori(gameIdCntr)
updateTime <= lastProfitTransferTimestamp
updateTime < lastProfitTransferTimestamp
updateTime != lastProfitTransferTimestamp
updateTime <= ori(Sum(userGameId[...]))
updateTime == ori(Sum(pendingReturns[...]))
updateTime >= ori(Sum(pendingReturns[...]))
updateTime <= ori(Sum(pendingReturns[...]))
updateTime <= Sum(userGameId[...])
updateTime == Sum(pendingReturns[...])
updateTime >= Sum(pendingReturns[...])
updateTime <= Sum(pendingReturns[...])
ori(timePaused) <= ori(maxStake)
ori(timePaused) < ori(maxStake)
ori(timePaused) != ori(maxStake)
ori(timePaused) <= maxStake
ori(timePaused) < maxStake
ori(timePaused) != maxStake
ori(timePaused) != ori(houseStake)
ori(timePaused) != profitTransferTimeSpan
ori(timePaused) != gameIdCntr
ori(timePaused) != houseStake
ori(timePaused) <= minStake
ori(timePaused) < minStake
ori(timePaused) != minStake
ori(timePaused) <= ori(minStake)
ori(timePaused) < ori(minStake)
ori(timePaused) != ori(minStake)
ori(timePaused) <= ori(lastProfitTransferTimestamp)
ori(timePaused) >= timePaused
ori(timePaused) != ori(gameIdCntr)
ori(timePaused) <= lastProfitTransferTimestamp
ori(timePaused) >= ori(Sum(pendingReturns[...]))
ori(timePaused) != Sum(userGameId[...])
ori(timePaused) >= Sum(pendingReturns[...])
ori(maxStake) >= activeGames
ori(maxStake) > activeGames
ori(maxStake) != activeGames
ori(maxStake) == maxStake
ori(maxStake) >= maxStake
ori(maxStake) <= maxStake
ori(maxStake) != ori(houseStake)
ori(maxStake) >= profitTransferTimeSpan
ori(maxStake) > profitTransferTimeSpan
ori(maxStake) != profitTransferTimeSpan
ori(maxStake) >= gameIdCntr
ori(maxStake) > gameIdCntr
ori(maxStake) != gameIdCntr
ori(maxStake) != houseStake
ori(maxStake) >= minStake
ori(maxStake) > minStake
ori(maxStake) != minStake
ori(maxStake) >= ori(minStake)
ori(maxStake) > ori(minStake)
ori(maxStake) != ori(minStake)
ori(maxStake) >= ori(lastProfitTransferTimestamp)
ori(maxStake) > ori(lastProfitTransferTimestamp)
ori(maxStake) != ori(lastProfitTransferTimestamp)
ori(maxStake) >= ori(activeGames)
ori(maxStake) > ori(activeGames)
ori(maxStake) != ori(activeGames)
ori(maxStake) >= timePaused
ori(maxStake) > timePaused
ori(maxStake) != timePaused
ori(maxStake) >= ori(gameIdCntr)
ori(maxStake) > ori(gameIdCntr)
ori(maxStake) != ori(gameIdCntr)
ori(maxStake) >= lastProfitTransferTimestamp
ori(maxStake) > lastProfitTransferTimestamp
ori(maxStake) != lastProfitTransferTimestamp
ori(maxStake) >= ori(Sum(userGameId[...]))
ori(maxStake) > ori(Sum(userGameId[...]))
ori(maxStake) != ori(Sum(userGameId[...]))
ori(maxStake) >= ori(Sum(pendingReturns[...]))
ori(maxStake) > ori(Sum(pendingReturns[...]))
ori(maxStake) != ori(Sum(pendingReturns[...]))
ori(maxStake) >= Sum(userGameId[...])
ori(maxStake) > Sum(userGameId[...])
ori(maxStake) != Sum(userGameId[...])
ori(maxStake) >= Sum(pendingReturns[...])
ori(maxStake) > Sum(pendingReturns[...])
ori(maxStake) != Sum(pendingReturns[...])
activeGames <= maxStake
activeGames < maxStake
activeGames != maxStake
activeGames <= ori(houseStake)
activeGames <= profitTransferTimeSpan
activeGames < profitTransferTimeSpan
activeGames != profitTransferTimeSpan
activeGames <= gameIdCntr
activeGames < gameIdCntr
activeGames != gameIdCntr
activeGames <= houseStake
activeGames <= minStake
activeGames < minStake
activeGames != minStake
activeGames <= ori(minStake)
activeGames < ori(minStake)
activeGames != ori(minStake)
activeGames <= ori(lastProfitTransferTimestamp)
activeGames < ori(lastProfitTransferTimestamp)
activeGames != ori(lastProfitTransferTimestamp)
activeGames <= ori(gameIdCntr)
activeGames < ori(gameIdCntr)
activeGames != ori(gameIdCntr)
activeGames <= lastProfitTransferTimestamp
activeGames < lastProfitTransferTimestamp
activeGames != lastProfitTransferTimestamp
activeGames >= ori(Sum(pendingReturns[...]))
activeGames <= Sum(userGameId[...])
activeGames >= Sum(pendingReturns[...])
houseAddress != ori(pendingOwner)
houseAddress != ori(newConflictRes)
houseAddress != ori(owner)
houseAddress == ori(houseAddress)
houseAddress != serverAddress
houseAddress != ori(conflictRes)
houseAddress != owner
houseAddress != ori(serverAddress)
houseAddress != newConflictRes
maxStake != ori(houseStake)
maxStake >= profitTransferTimeSpan
maxStake > profitTransferTimeSpan
maxStake != profitTransferTimeSpan
maxStake >= gameIdCntr
maxStake > gameIdCntr
maxStake != gameIdCntr
maxStake != houseStake
maxStake >= minStake
maxStake > minStake
maxStake != minStake
maxStake >= ori(minStake)
maxStake > ori(minStake)
maxStake != ori(minStake)
maxStake >= ori(lastProfitTransferTimestamp)
maxStake > ori(lastProfitTransferTimestamp)
maxStake != ori(lastProfitTransferTimestamp)
maxStake >= ori(activeGames)
maxStake > ori(activeGames)
maxStake != ori(activeGames)
maxStake >= timePaused
maxStake > timePaused
maxStake != timePaused
maxStake >= ori(gameIdCntr)
maxStake > ori(gameIdCntr)
maxStake != ori(gameIdCntr)
maxStake >= lastProfitTransferTimestamp
maxStake > lastProfitTransferTimestamp
maxStake != lastProfitTransferTimestamp
maxStake >= ori(Sum(userGameId[...]))
maxStake > ori(Sum(userGameId[...]))
maxStake != ori(Sum(userGameId[...]))
maxStake >= ori(Sum(pendingReturns[...]))
maxStake > ori(Sum(pendingReturns[...]))
maxStake != ori(Sum(pendingReturns[...]))
maxStake >= Sum(userGameId[...])
maxStake > Sum(userGameId[...])
maxStake != Sum(userGameId[...])
maxStake >= Sum(pendingReturns[...])
maxStake > Sum(pendingReturns[...])
maxStake != Sum(pendingReturns[...])
ori(houseStake) != profitTransferTimeSpan
ori(houseStake) != gameIdCntr
ori(houseStake) != minStake
ori(houseStake) != ori(minStake)
ori(houseStake) != ori(lastProfitTransferTimestamp)
ori(houseStake) >= ori(activeGames)
ori(houseStake) != timePaused
ori(houseStake) != ori(gameIdCntr)
ori(houseStake) != lastProfitTransferTimestamp
ori(houseStake) >= ori(Sum(userGameId[...]))
ori(houseStake) >= ori(Sum(pendingReturns[...]))
ori(houseStake) >= Sum(userGameId[...])
ori(houseStake) >= Sum(pendingReturns[...])
profitTransferTimeSpan >= gameIdCntr
profitTransferTimeSpan > gameIdCntr
profitTransferTimeSpan != gameIdCntr
profitTransferTimeSpan != houseStake
profitTransferTimeSpan <= minStake
profitTransferTimeSpan < minStake
profitTransferTimeSpan != minStake
profitTransferTimeSpan <= ori(minStake)
profitTransferTimeSpan < ori(minStake)
profitTransferTimeSpan != ori(minStake)
profitTransferTimeSpan <= ori(lastProfitTransferTimestamp)
profitTransferTimeSpan < ori(lastProfitTransferTimestamp)
profitTransferTimeSpan != ori(lastProfitTransferTimestamp)
profitTransferTimeSpan >= ori(activeGames)
profitTransferTimeSpan > ori(activeGames)
profitTransferTimeSpan != ori(activeGames)
profitTransferTimeSpan != timePaused
profitTransferTimeSpan >= ori(gameIdCntr)
profitTransferTimeSpan > ori(gameIdCntr)
profitTransferTimeSpan != ori(gameIdCntr)
profitTransferTimeSpan <= lastProfitTransferTimestamp
profitTransferTimeSpan < lastProfitTransferTimestamp
profitTransferTimeSpan != lastProfitTransferTimestamp
profitTransferTimeSpan >= ori(Sum(userGameId[...]))
profitTransferTimeSpan > ori(Sum(userGameId[...]))
profitTransferTimeSpan != ori(Sum(userGameId[...]))
profitTransferTimeSpan >= ori(Sum(pendingReturns[...]))
profitTransferTimeSpan > ori(Sum(pendingReturns[...]))
profitTransferTimeSpan != ori(Sum(pendingReturns[...]))
profitTransferTimeSpan >= Sum(userGameId[...])
profitTransferTimeSpan > Sum(userGameId[...])
profitTransferTimeSpan != Sum(userGameId[...])
profitTransferTimeSpan >= Sum(pendingReturns[...])
profitTransferTimeSpan > Sum(pendingReturns[...])
profitTransferTimeSpan != Sum(pendingReturns[...])
gameIdCntr != houseStake
gameIdCntr <= minStake
gameIdCntr < minStake
gameIdCntr != minStake
gameIdCntr <= ori(minStake)
gameIdCntr < ori(minStake)
gameIdCntr != ori(minStake)
gameIdCntr <= ori(lastProfitTransferTimestamp)
gameIdCntr < ori(lastProfitTransferTimestamp)
gameIdCntr != ori(lastProfitTransferTimestamp)
gameIdCntr >= ori(activeGames)
gameIdCntr > ori(activeGames)
gameIdCntr != ori(activeGames)
gameIdCntr != timePaused
gameIdCntr >= ori(gameIdCntr)
gameIdCntr <= lastProfitTransferTimestamp
gameIdCntr < lastProfitTransferTimestamp
gameIdCntr != lastProfitTransferTimestamp
gameIdCntr != ori(Sum(userGameId[...]))
gameIdCntr >= ori(Sum(pendingReturns[...]))
gameIdCntr > ori(Sum(pendingReturns[...]))
gameIdCntr != ori(Sum(pendingReturns[...]))
gameIdCntr != Sum(userGameId[...])
gameIdCntr >= Sum(pendingReturns[...])
gameIdCntr > Sum(pendingReturns[...])
gameIdCntr != Sum(pendingReturns[...])
houseStake != minStake
houseStake != ori(minStake)
houseStake != ori(lastProfitTransferTimestamp)
houseStake >= ori(activeGames)
houseStake != timePaused
houseStake != ori(gameIdCntr)
houseStake != lastProfitTransferTimestamp
houseStake >= ori(Sum(userGameId[...]))
houseStake >= ori(Sum(pendingReturns[...]))
houseStake >= Sum(userGameId[...])
houseStake >= Sum(pendingReturns[...])
minStake == ori(minStake)
minStake >= ori(minStake)
minStake <= ori(minStake)
minStake >= ori(lastProfitTransferTimestamp)
minStake > ori(lastProfitTransferTimestamp)
minStake != ori(lastProfitTransferTimestamp)
minStake >= ori(activeGames)
minStake > ori(activeGames)
minStake != ori(activeGames)
minStake >= timePaused
minStake > timePaused
minStake != timePaused
minStake >= ori(gameIdCntr)
minStake > ori(gameIdCntr)
minStake != ori(gameIdCntr)
minStake >= lastProfitTransferTimestamp
minStake > lastProfitTransferTimestamp
minStake != lastProfitTransferTimestamp
minStake >= ori(Sum(userGameId[...]))
minStake > ori(Sum(userGameId[...]))
minStake != ori(Sum(userGameId[...]))
minStake >= ori(Sum(pendingReturns[...]))
minStake > ori(Sum(pendingReturns[...]))
minStake != ori(Sum(pendingReturns[...]))
minStake >= Sum(userGameId[...])
minStake > Sum(userGameId[...])
minStake != Sum(userGameId[...])
minStake >= Sum(pendingReturns[...])
minStake > Sum(pendingReturns[...])
minStake != Sum(pendingReturns[...])
ori(pendingOwner) == ori(newConflictRes)
ori(pendingOwner) != ori(owner)
ori(pendingOwner) != ori(houseAddress)
ori(pendingOwner) != serverAddress
ori(pendingOwner) != ori(conflictRes)
ori(pendingOwner) != owner
ori(pendingOwner) != ori(serverAddress)
ori(pendingOwner) == newConflictRes
ori(newConflictRes) != ori(owner)
ori(newConflictRes) != ori(houseAddress)
ori(newConflictRes) != serverAddress
ori(newConflictRes) != ori(conflictRes)
ori(newConflictRes) != owner
ori(newConflictRes) != ori(serverAddress)
ori(newConflictRes) == newConflictRes
ori(owner) != ori(houseAddress)
ori(owner) != serverAddress
ori(owner) != ori(conflictRes)
ori(owner) == owner
ori(owner) != ori(serverAddress)
ori(owner) != newConflictRes
ori(minStake) >= ori(lastProfitTransferTimestamp)
ori(minStake) > ori(lastProfitTransferTimestamp)
ori(minStake) != ori(lastProfitTransferTimestamp)
ori(minStake) >= ori(activeGames)
ori(minStake) > ori(activeGames)
ori(minStake) != ori(activeGames)
ori(minStake) >= timePaused
ori(minStake) > timePaused
ori(minStake) != timePaused
ori(minStake) >= ori(gameIdCntr)
ori(minStake) > ori(gameIdCntr)
ori(minStake) != ori(gameIdCntr)
ori(minStake) >= lastProfitTransferTimestamp
ori(minStake) > lastProfitTransferTimestamp
ori(minStake) != lastProfitTransferTimestamp
ori(minStake) >= ori(Sum(userGameId[...]))
ori(minStake) > ori(Sum(userGameId[...]))
ori(minStake) != ori(Sum(userGameId[...]))
ori(minStake) >= ori(Sum(pendingReturns[...]))
ori(minStake) > ori(Sum(pendingReturns[...]))
ori(minStake) != ori(Sum(pendingReturns[...]))
ori(minStake) >= Sum(userGameId[...])
ori(minStake) > Sum(userGameId[...])
ori(minStake) != Sum(userGameId[...])
ori(minStake) >= Sum(pendingReturns[...])
ori(minStake) > Sum(pendingReturns[...])
ori(minStake) != Sum(pendingReturns[...])
ori(lastProfitTransferTimestamp) >= ori(activeGames)
ori(lastProfitTransferTimestamp) > ori(activeGames)
ori(lastProfitTransferTimestamp) != ori(activeGames)
ori(lastProfitTransferTimestamp) >= timePaused
ori(lastProfitTransferTimestamp) >= ori(gameIdCntr)
ori(lastProfitTransferTimestamp) > ori(gameIdCntr)
ori(lastProfitTransferTimestamp) != ori(gameIdCntr)
ori(lastProfitTransferTimestamp) == lastProfitTransferTimestamp
ori(lastProfitTransferTimestamp) >= lastProfitTransferTimestamp
ori(lastProfitTransferTimestamp) <= lastProfitTransferTimestamp
ori(lastProfitTransferTimestamp) >= ori(Sum(userGameId[...]))
ori(lastProfitTransferTimestamp) > ori(Sum(userGameId[...]))
ori(lastProfitTransferTimestamp) != ori(Sum(userGameId[...]))
ori(lastProfitTransferTimestamp) >= ori(Sum(pendingReturns[...]))
ori(lastProfitTransferTimestamp) > ori(Sum(pendingReturns[...]))
ori(lastProfitTransferTimestamp) != ori(Sum(pendingReturns[...]))
ori(lastProfitTransferTimestamp) >= Sum(userGameId[...])
ori(lastProfitTransferTimestamp) > Sum(userGameId[...])
ori(lastProfitTransferTimestamp) != Sum(userGameId[...])
ori(lastProfitTransferTimestamp) >= Sum(pendingReturns[...])
ori(lastProfitTransferTimestamp) > Sum(pendingReturns[...])
ori(lastProfitTransferTimestamp) != Sum(pendingReturns[...])
ori(houseAddress) != serverAddress
ori(houseAddress) != ori(conflictRes)
ori(houseAddress) != owner
ori(houseAddress) != ori(serverAddress)
ori(houseAddress) != newConflictRes
ori(activeGames) <= ori(gameIdCntr)
ori(activeGames) < ori(gameIdCntr)
ori(activeGames) != ori(gameIdCntr)
ori(activeGames) <= lastProfitTransferTimestamp
ori(activeGames) < lastProfitTransferTimestamp
ori(activeGames) != lastProfitTransferTimestamp
ori(activeGames) <= ori(Sum(userGameId[...]))
ori(activeGames) >= ori(Sum(pendingReturns[...]))
ori(activeGames) <= Sum(userGameId[...])
ori(activeGames) >= Sum(pendingReturns[...])
timePaused != ori(gameIdCntr)
timePaused <= lastProfitTransferTimestamp
timePaused >= ori(Sum(pendingReturns[...]))
timePaused >= Sum(pendingReturns[...])
serverAddress != ori(conflictRes)
serverAddress != owner
serverAddress == ori(serverAddress)
serverAddress != newConflictRes
ori(conflictRes) != owner
ori(conflictRes) != ori(serverAddress)
ori(conflictRes) != newConflictRes
owner != ori(serverAddress)
owner != newConflictRes
ori(gameIdCntr) <= lastProfitTransferTimestamp
ori(gameIdCntr) < lastProfitTransferTimestamp
ori(gameIdCntr) != lastProfitTransferTimestamp
ori(gameIdCntr) != ori(Sum(userGameId[...]))
ori(gameIdCntr) >= ori(Sum(pendingReturns[...]))
ori(gameIdCntr) > ori(Sum(pendingReturns[...]))
ori(gameIdCntr) != ori(Sum(pendingReturns[...]))
ori(gameIdCntr) >= Sum(pendingReturns[...])
ori(gameIdCntr) > Sum(pendingReturns[...])
ori(gameIdCntr) != Sum(pendingReturns[...])
ori(serverAddress) != newConflictRes
lastProfitTransferTimestamp >= ori(Sum(userGameId[...]))
lastProfitTransferTimestamp > ori(Sum(userGameId[...]))
lastProfitTransferTimestamp != ori(Sum(userGameId[...]))
lastProfitTransferTimestamp >= ori(Sum(pendingReturns[...]))
lastProfitTransferTimestamp > ori(Sum(pendingReturns[...]))
lastProfitTransferTimestamp != ori(Sum(pendingReturns[...]))
lastProfitTransferTimestamp >= Sum(userGameId[...])
lastProfitTransferTimestamp > Sum(userGameId[...])
lastProfitTransferTimestamp != Sum(userGameId[...])
lastProfitTransferTimestamp >= Sum(pendingReturns[...])
lastProfitTransferTimestamp > Sum(pendingReturns[...])
lastProfitTransferTimestamp != Sum(pendingReturns[...])
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

