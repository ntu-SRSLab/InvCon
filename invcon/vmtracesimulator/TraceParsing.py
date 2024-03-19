import copy
import json
import logging
import os 
import sys
sys.setrecursionlimit(2000)

from typing import List,Dict,Iterator, Optional
from Crypto.Hash import keccak
from evm_trace import TraceFrame, create_trace_frames
from evm_trace.vmtrace import VMTrace, VMTraceFrame, to_trace_frames, from_rpc_response
from evm_trace.parity import get_calltree_from_parity_trace, ParityTraceList
from evm_trace.geth import TraceMemory   
from eth_pydantic_types import HashBytes20, HexBytes     

from evm_trace.enums import CALL_OPCODES

from invconplus.plugin.quickNode import fetchAllRuntimeInformation

def keccak256(buffer: bytes) -> bytes:
    """
    Computes the keccak256 hash of the input `buffer`.

    Parameters
    ----------
    buffer :
        Input for the hashing function.

    Returns
    -------
    hash : `ethereum.base_types.Hash32`
        Output of the hash function.
    """
    k = keccak.new(digest_bits=256)
    return bytes(k.update(buffer).digest())

class Instruction:
    def __init__(self, frame: TraceFrame) -> None:
        self.frame = frame
        self.children: list["Instruction"] = []
    @property
    def op(self) -> str:
        return self.frame.op
    @property
    def stack(self) -> List[HexBytes]:
        return self.frame.stack
    @property
    def depth(self) -> int:
        return self.frame.depth
    @property
    def pc(self) -> int:
        return self.frame.pc
    @property
    def memory(self) -> TraceMemory:
        return self.frame.memory
    @property
    def storage(self) -> Dict[HexBytes, HexBytes]:
        return self.frame.storage
    
    @property
    def address(self) -> Optional[HashBytes20]:
        return self.frame.address
    
    @property
    def index_values(self):
        if self.op in  ["KECCAK256", "SHA3"]:
            return [] 
        elif self.op in ["SSTORE"]:
            return [] 
        elif self.op in ["MSTORE"]:
            value = self.stack[-2].hex()
            return [value] 
        elif self.op in ["ADD"]:
            return []
        else:
            return []

    def dependend(self, ins: "Instruction") -> bool:
        if self.op in  ["KECCAK256", "SHA3"]:
            memory_start_index = int(self.stack[-1])
            size = int(self.stack[-2])
            if ins.op in ["MSTORE", "MSTORE8"]:
                mstore_memory_start_index = int(ins.stack[-1])
                value = int(ins.stack[-2])
                if ins.op == "MSTORE":
                    word_size = 32 
                    if memory_start_index  <= mstore_memory_start_index and mstore_memory_start_index + word_size <= memory_start_index+size:
                        if value == int(self.memory[mstore_memory_start_index: mstore_memory_start_index+word_size].hex(), 16):
                            return True
                        else:
                            return False
                else:
                    word_size = 8 
                    if memory_start_index  <= mstore_memory_start_index and mstore_memory_start_index + word_size <= memory_start_index+size:
                        if value == int(self.memory[mstore_memory_start_index: mstore_memory_start_index+word_size].hex(), 16):
                            return True
                        else:
                            return False
              
        elif self.op in ["SSTORE"]:
            key =  int(self.stack[-1])
            value = int(self.stack[-2])
            if ins.op in ["KECCAK256", "SHA3"]:
                memory_start_index = int(ins.stack[-1])
                size = int(ins.stack[-2])
                data = ins.memory[memory_start_index: memory_start_index+size]
                slot = int(keccak256(bytes.fromhex(data.hex()[2:])).hex(), 16)
                if slot == key:
                    return True
                else:
                    return False
            elif ins.op in ["ADD"]:
                x = int(ins.stack[-1])
                y = int(ins.stack[-2])
                if x + y == key:
                    return True
                else:
                    return False
            elif ins.op in ["SLOAD"]:
                x = int(ins.stack[-1])
                if x == key:
                    return True 
                else:
                    return False
        elif self.op in ["MSTORE"]:
            value = int(self.stack[-2])
            if ins.op in ["ADD"]:
                x = int(ins.stack[-1])
                y = int(ins.stack[-2])
                if x + y  == value:
                    return True
                else:
                    return False
            elif ins.op in  ["KECCAK256", "SHA3"]:
                memory_start_index = int(ins.stack[-1])
                size = int(ins.stack[-2])
                data = ins.memory[memory_start_index: memory_start_index+size]
                _hash  = int(keccak256(bytes.fromhex(data.hex()[2:])).hex(), 16)
                if _hash == value:
                    return True
                else:
                    return False
        elif self.op in ["ADD"]:
            x = int(self.stack[-1])
            y = int(self.stack[-2])
            if ins.op in  ["KECCAK256", "SHA3"]:
                memory_start_index = int(ins.stack[-1])
                size = int(ins.stack[-2])
                data = ins.memory[memory_start_index: memory_start_index+size]
                _hash = int(keccak256(bytes.fromhex(data.hex()[2:])).hex(), 16)
                if _hash == x or _hash == y:
                    return True
                else:
                    return False
        
        return False
    
    def __str__(self) -> str:
        return f"{self.op} {self.stack} {self.depth} {self.pc} {self.memory} {self.storage}"
    
    def __json__(self) -> dict:
        if self.op in  ["KECCAK256", "SHA3"]:
            memory_start_index = int(self.stack[-1])
            size = int(self.stack[-2])
            data = self.memory[memory_start_index: memory_start_index+size]
            _hash = int(keccak256(bytes.fromhex(data.hex()[2:])).hex(), 16)
            return {
                "depth": self.depth,
                "op": self.op,
                "pc": self.pc,
                "data": data.hex(),
                "hash": hex(_hash),
                "children": [child.__json__() for child in self.children]
            }
        elif self.op in ["SSTORE"]:
            key =  hex(self.stack[-1])
            value = hex(self.stack[-2])
            return {
                "depth": self.depth,
                "op": self.op,
                "pc": self.pc,
                "key": key,
                "value": value,
                "children": [child.__json__() for child in self.children]
            }
        elif self.op in ["SLOAD"]:
            key =  hex(self.stack[-1])
            value = hex(self.storage.get(self.stack[-1], 0))
            return {
                "depth": self.depth,
                "op": self.op,
                "pc": self.pc,
                "key": key,
                "value": value,
                "children": [child.__json__() for child in self.children]
            }
        elif self.op in ["MSTORE"]:
            value = hex(self.stack[-2])
            return {
                "depth": self.depth,
                "op": self.op,
                "pc": self.pc,
                "value": value,
                "children": [child.__json__() for child in self.children]
            }
        elif self.op in ["MSTORE8"]:
            value = hex(self.stack[-2])
            return {
                "depth": self.depth,
                "op": self.op,
                "pc": self.pc,
                "value": value,
                "children": [child.__json__() for child in self.children]
            }
        elif self.op in ["ADD"]:
            x = hex(self.stack[-1])
            y = hex(self.stack[-2])
            return {
                "depth": self.depth,
                "op": self.op,
                "pc": self.pc,
                "x": x,
                "y": y,
                "children": [child.__json__() for child in self.children]
            }
        else:
            return {
                "depth": self.depth,
                "op": self.op,
                # "stack": self.stack,
                "pc": self.pc,
                # "memory": self.memory,
                # "storage": self.storage,
                "children": [child.__json__() for child in self.children]
            }

class DependencyGraph:
    def __init__(self, ins: Instruction) -> None:
        self.root =  ins
        self.visited = list()
    
    def add_child(self, ins: "Instruction") -> None:
        self._add_child(self.root, ins)
        self.visited =  list()
    
    def _add_child(self, ins_bottom: "Instruction", ins_dependent: "Instruction") -> None:
        if ins_bottom in self.visited:
            return 
        self.visited.append(ins_bottom)
        if ins_bottom.dependend(ins_dependent):
            ins_bottom.children.append(ins_dependent)
        else:
            for child in ins_bottom.children:
                self._add_child(child, ins_dependent)
    
    def visitGetIndexValues(self):
        index_values = []
        self._visitGetIndexValues(self.root, index_values)
        return index_values
    
    def _visitGetIndexValues(self, ins: Instruction, index_values: list = []):
        index_values.extend(ins.index_values)
        for child in ins.children:
            self._visitGetIndexValues(child, index_values)

    def __str__(self) -> str:
        return str(self.root)
    
    def __json__(self) -> dict:
        return self.root.__json__()
    
class Call_Node:
    entry_frame = None
    exit_frame = None
    depth = 0
    children: List =[]
    storage_graphs: List[DependencyGraph] = []
    interested_frames: List = []
    traceAddress: List = []
    sstore_result: Dict = {}
    
    def __init__(self, depth=0, entry_frame=None) -> None:
        self.depth = depth 
        self.entry_frame = entry_frame
        self.children = []
        self.storage_graphs = []
        self.interested_frames = []
        self.traceAddress = []
        self.sstore_result = dict()

    def to_json(self):
        return dict(depth=self.depth, traceAddress=self.traceAddress, sstore_result=self.sstore_result)

    def add_frame(self, frame):
        self.interested_frames.append(frame)

    def add_child(self, call_node):
        assert self!=call_node, "Cannot add child to a call_node"
        self.children.append(call_node)
        call_node.traceAddress = self.traceAddress + [str(len(self.children) -1)]
        
    def add_dependency_graph(self, graph: DependencyGraph):
        self.storage_graphs.append(graph)
    
    def add_exit_frame(self, exit_frame):
        self.exit_frame = exit_frame
    
    def compute_sstore_dependency_graph(self):
        for frame in reversed(self.interested_frames):  
            if frame.op == "SSTORE":
                graph = DependencyGraph(Instruction(frame))
                self.add_dependency_graph(graph)
            for graph in self.storage_graphs:
                graph.add_child(Instruction(frame))
        
        for child in self.children:
            child.compute_sstore_dependency_graph()

    def print(self):
            print("------------------------------------------------")
            print(self.entry_frame.__str__())
            for graph  in self.storage_graphs:
                print(hex(graph.root.stack[-1]), hex(graph.root.stack[-2]))
                # if hex(graph.root.stack[-1]) == slot:
                if False:
                    print(json.dumps(graph.__json__(), indent=4))
                    # print("--------------------------------------------------")
                    # print(set(graph.visitGetIndexValues()))
                    print("--------------------------------------------------")
    def print_state_sstore(self, address):

        if self.entry_frame.address.lower() == address.lower():
            for child in self.children:
                if child.entry_frame.op in ["DELEGATECALL"]:
                   child.print()
                   for child in child.children:
                       child.print_state_sstore(address)
                else:
                    child.print_state_sstore(address)
            self.print()
           
        else:
            for child in self.children:
                child.print_state_sstore(address)
    
    def get_state_update_result(self):
            result = dict()
            for graph  in self.storage_graphs:
                # print(hex(graph.root.stack[-1]), hex(graph.root.stack[-2]))
                if hex(graph.root.stack[-1]) in result:
                    print(hex(graph.root.stack[-1]), "has been updated")
                    pass 
                # result[hex(graph.root.stack[-1])] = (self.interested_frames.index(graph.root.frame), hex(graph.root.stack[-2]))
                result[hex(graph.root.stack[-1])] = (self.interested_frames.index(graph.root.frame), '0x{0:0{1}x}'.format(graph.root.stack[-2], 64))
            return result 

    def get_state_sstore_all_result(self, address):
        result = dict()
        if self.entry_frame.address.lower() == address.lower() and self.entry_frame.op == "CALL":
            _result3 = self.get_state_update_result()
            for child in self.children:
                if len(_result3)!=0:
                    for key in copy.copy(_result3):
                        exec_op_counter, value = _result3[key]
                        if exec_op_counter < self.interested_frames.index(child.entry_frame):
                            _result3.pop(key)
                            result[key] = value 
                if child.entry_frame.op in ["DELEGATECALL"]:
                    _result = child.get_state_update_result() 
                    for _child in child.children:
                        if len(_result)!=0:
                            for key in copy.copy(_result):
                                exec_op_counter, value = _result[key]
                                if exec_op_counter < child.interested_frames.index(_child.entry_frame):
                                    _result.pop(key)
                                    result[key] = value 
                        _result2 = _child.get_state_sstore_all_result(address)
                        for key in _result2:
                            result[key] = _result2[key]
                        
                    for key in copy.copy(_result):
                            exec_op_counter, value = _result[key]  
                            result[key] = value 
                            _result.pop(key)
                else:
                    _result = child.get_state_sstore_all_result(address)
                    for key in _result:
                        result[key] = _result[key]
                
            for key in copy.copy(_result3):
                        exec_op_counter, value = _result3[key]  
                        result[key] = value 
                        _result3.pop(key)
        else:
            for child in self.children:
                _result:dict = child.get_state_sstore_all_result(address)
                for key in _result:
                    result[key] = _result[key]

        self.sstore_result = {address: result}
        return result 
    
    def query_calls(self, address, traceAddress):
            if self.entry_frame.address.lower() == address.lower() and self.entry_frame.op == "CALL":
                self.traceAddress = traceAddress
                return [self]
            else:
                result = []
                index = 0
                for child in self.children:
                    _result = child.query_calls(address, traceAddress + [str(index)])
                    result.extend(_result)
                    index = index + 1
                return result 

class Simulator:
    graphs: List[DependencyGraph]
    data: object
    address: HashBytes20 
    tx_hash: str 
    def __init__(self, address, tx_hash) -> None:
        # assert os.path.exists(os.path.join(workdir, contract_name, address, tx_hash+".json"))
        # self.data = json.load(open(os.path.join(workdir, contract_name, address, tx_hash+".json")))
        self.graphs = []
        self.address = address.lower()
        self.tx_hash = tx_hash
        logging.debug("analyzing transaction#{0}".format(tx_hash))
        if not os.path.exists(f"./tmp/txs"):
            os.mkdir("./tmp/txs")
        if os.path.exists(f"./tmp/txs/{tx_hash}.json"):
            self.data = json.loads(open(f"./tmp/txs/{tx_hash}.json", "r").read())
        else:
            self.data = fetchAllRuntimeInformation(tx_hash=tx_hash)
            json.dump(self.data, open(f"./tmp/txs/{tx_hash}.json","w"), indent=4)

        if os.path.exists(f"./tmp/txs/{tx_hash}.query.json"):
            self.queries_cache = json.loads(open(f"./tmp/txs/{tx_hash}.query.json", "r").read())
        else:
            self.queries_cache = dict()

    def loadAndexec(self):
        vm_trace = from_rpc_response(buffer=json.dumps(self.data).encode("utf-8"))
        trace_frames = list(to_trace_frames(vm_trace))
        self.graphs = list()
        interested_frames = list()
        callee_address_stack = []
        callee_address_stack.append(self.address)

        parity_trace = ParityTraceList(self.data["result"]["trace"])
        self.call_tree  = get_calltree_from_parity_trace(parity_trace)
        self.rootCallNode = None 
        currentCallNode = None
        rootCallNodes: List[Call_Node]= []

        call_frames = []
        first = True 
        calls = []
        for index, frame in enumerate(trace_frames):
            if first:
                currentCallNode = Call_Node(entry_frame=frame)
                self.rootCallNode = currentCallNode
                rootCallNodes.append(currentCallNode)
                first = False 
                calls.append(frame.depth)
                calls.append(frame.op)
                continue
            if frame.op in ["KECCAK256", "SHA3", "SSTORE", "MSTORE", "ADD", "SLOAD"] + list(CALL_OPCODES) + ["RETURN", "REVERT", "STOP", "SELFDESTRUCT"]:
                
                if frame.op in ["RETURN", "REVERT", "STOP", "SELFDESTRUCT"]:
                    calls.append(frame.depth)
                    calls.append(frame.op)
                    
                    if len(callee_address_stack) > 0:
                        callee_address_stack.pop()
                    rootCallNodes[-1].add_exit_frame(frame) 
                    rootCallNodes.pop()
                    continue

                if frame.op in list(CALL_OPCODES): # ["CALL", "CREATE", "CREATE2"]:
                    
                    if frame.address in ["0x1", "0x2", "0x3", "0x4"]: # 0x1: ECREC; 0x2: SHA256; 0x3: RIP160; 0x4: IDENTITY 
                        continue

                    if frame.depth == trace_frames[index+1].depth:
                        # looks like a fallback function that will be enabled by normal ether transfer by default
                        # In rare rare cases, "CALL" opcode does not increase the depth 
                        continue
                      

                    callee_address_stack.append(frame.address) 
                    calls.append(frame.depth)
                    calls.append(frame.op)
 
                    call_frames.append(frame)
                    currentCallNode = Call_Node(frame.depth, frame)
                    rmNodes = []
                    while rootCallNodes[-1].depth != currentCallNode.depth-1:
                        # Notice: there will be a gasless send 
                        rmNode = rootCallNodes.pop()
                        rmNodes.append(rmNode)
                    
                    # for rmNode in rmNodes:
                    #     rootCallNodes[-1].children.remove(rmNode)

                    assert rootCallNodes[-1] != currentCallNode, "two objects are the same"
                    rootCallNode = rootCallNodes[-1]
                    rootCallNodes[-1].add_frame(frame)
                    rootCallNode.add_child(currentCallNode)
                    rootCallNodes.append(currentCallNode)
                else:
                    rootCallNodes[-1].add_frame(frame)
                    interested_frames.append(frame)

        
        for frame in reversed(interested_frames):  
            if frame.op == "SSTORE":
                graph = DependencyGraph(Instruction(frame))
                self.graphs.append(graph)
            for graph in self.graphs:
                graph.add_child(Instruction(frame))

        def structure_equiv(treeNode, callNode):
            if treeNode.call_type.name == callNode.entry_frame.op and len(treeNode.calls) == len(callNode.children):
                return True 
            else:
                return False
       
        def auto_fix(tree, rootCall):
            if structure_equiv(tree, rootCall):
                for i in range(len(tree.calls)):
                    rootCall.children[i].entry_frame.address = tree.calls[i].address.hex().lower()
                    if not auto_fix(tree.calls[i], rootCall.children[i]):
                        return False
                return True
            else:
                if len(rootCall.children) < len(tree.calls):
                    return False
                k = 0
                matched_children = []
                for i in range(len(tree.calls)): 
                    for j in range(k, len(rootCall.children)):
                        k = j + 1
                        if auto_fix(tree.calls[i], rootCall.children[j]):
                            rootCall.children[j].entry_frame.address = tree.calls[i].address.hex().lower()
                            matched_children.append(rootCall.children[j])
                            break
                if len(matched_children) == len(tree.calls):
                    rootCall.children = matched_children
                    return True 
                else:
                    return False
      
        
        ret =auto_fix(self.call_tree, self.rootCallNode)
        # assert ret == True, "fix error"
    
    def query(self, slot):
        result = []
        for graph in self.graphs:
            slot = slot if isinstance(slot, str) and slot.startswith("0x") else hex(slot)
            if int(graph.root.stack[-1]) == int(slot, 16):
                result = graph.visitGetIndexValues()
                break
        if len(result) == 0:
            logging.debug("query storage slot {0} with result {1}".format(slot, set(result)))
        else:
            logging.debug("query storage slot {0} with result {1}".format(slot, set(result)))
        return set(result)

    def get_state_diff(self):
        stateDiff: Dict[str, str] = dict() 
        for graph in self.graphs:
            # sstore slot value
            current_address = "0x" + graph.root.address.hex()

            if current_address not in stateDiff:
                stateDiff[current_address] = dict()

            _stateDiff = stateDiff[current_address]

            slot, value = graph.root.stack[-1].hex(), graph.root.stack[-2].hex()
            if slot in _stateDiff:
                continue 
            # find the earliest sload 
            old_value = None 
            for child in graph.root.children:
                if child.op == "SLOAD":
                    old_value = child.storage.get(graph.root.stack[-1]).hex()
            if old_value is not None:
                _stateDiff[slot] = (old_value, value)
            else:
                _stateDiff[slot] = (None, value)
        # print(json.dumps(stateDiff))
        return stateDiff
    
    def print_storage_value(self):
        
        print("--------------------------------------------------")
        print("Storage\t\tValue")
        for graph in self.graphs:
            print(hex(graph.root.stack[-1]), hex(graph.root.stack[-2]))
            # if hex(graph.root.stack[-1]) == slot:
            if True:
                print(json.dumps(graph.__json__(), indent=4))
                # print("--------------------------------------------------")
                # print(set(graph.visitGetIndexValues()))
                print("--------------------------------------------------")
        print("--------------------------------------------------")

    def query_contract_calls(self):
        self.rootCallNode.compute_sstore_dependency_graph()
        self.rootCallNode.get_state_sstore_all_result(self.address)
        calls = self.rootCallNode.query_calls(self.address, [])
        json.dump([call.to_json() for call in calls], open(f"./tmp/txs/{self.tx_hash}-{self.address}.calls.json", "w"),  indent=4)
        return calls 

   
def main():
    address = "0x051EBD717311350f1684f89335bed4ABd083a2b6"
    tx_hash = "0x395675b56370a9f5fe8b32badfa80043f5291443bd6c8273900476880fb5221e"
    
    # "0x25e484b97f3c4c455b1e036b4a9f13e871f000261400a4e618c30cd74ae7deec"
    # "0x1789548a9d809fac1baf8d7a0c6ed93e79d8db9ed819985eff94123d9a17892d"
    # "0x7b1fb133ed1d6d32bcd139f32ce2ae781abdeedad321a86756ecd6f4a7a6cd7b"
    # tx_hash = "0x948b94e827664564401571632d0b2405c09776f1d2bbbdd16f8a068e80e161e1"
    simulator = Simulator(address=address, tx_hash=tx_hash)
    simulator.loadAndexec()

    print("--------------------------------------------------")
    print("Storage\t\tValue")
    for graph in simulator.graphs:
        print(hex(graph.root.stack[-1]), hex(graph.root.stack[-2]))
        # if hex(graph.root.stack[-1]) == slot:
        if False:
            print(json.dumps(graph.__json__(), indent=4))
            # print("--------------------------------------------------")
            # print(set(graph.visitGetIndexValues()))
            print("--------------------------------------------------")
    print("--------------------------------------------------")


    simulator.query_contract_calls()
    # simulator.rootCallNode.print_state_sstore(address=address)

if __name__ == "__main__":
    main()