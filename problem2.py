# -*- coding: utf-8 -*-
# File name: problem2.py
import math
from projectq import MainEngine
from projectq.ops import X, Y, Z, H, S, T, CX, CZ, Rx, Ry, Rz, Measure, All
from projectq.meta import Loop, Compute, Uncompute, Control
from projectq.cengines import (MainEngine,
AutoReplacer,
LocalOptimizer,
TagRemover,
InstructionFilter,
DecompositionRuleSet)
import projectq.setups.decompositions
from hiq.projectq.backends import SimulatorMPI
from hiq.projectq.cengines import GreedyScheduler, HiQMainEngine
from mpi4py import MPI



######################################
from projectq.backends import CommandPrinter
import numpy as np
from copy import deepcopy
from projectq.ops import FlushGate, Command, StatePreparation, CNOT

def my_receive(self, command_list):
    """
    Receive commands from the previous engine and cache them.
    If a flush gate arrives, the entire buffer is sent on.
    """
    command_list = self.add_swap(command_list)
    for cmd in command_list:
        if cmd.gate == FlushGate():  # flush gate --> optimize and flush
            for idx in self._l:
                self._optimize(idx)
                self._send_qubit_pipeline(idx, len(self._l[idx]))
            new_dict = dict()
            for idx in self._l:
                if len(self._l[idx]) > 0:
                    new_dict[idx] = self._l[idx]
            self._l = new_dict
            assert self._l == dict()
            self.send([cmd])
        else:
            self._cache_cmd(cmd)


def add_swap(self, command_list):
    new_cmd_list = []
    # print("old cmd")
    # for cmd in command_list:
    #     if cmd.control_qubits and (cmd.gate!=Z or cmd.gate!=X):
    #         print(cmd.gate)
    # print()
    for cmd in command_list:
        if not cmd.control_qubits or (cmd.gate!=Z and cmd.gate!=X): # not control
            new_cmd_list.append(cmd)
            continue
        control_id = cmd.all_qubits[0][0].id
        target_id = cmd.all_qubits[1][0].id
        if (control_id, target_id) in self.connections:
            new_cmd_list.append(cmd)
            continue
        shortest_path = dijsktra(self.graph, control_id, target_id)
        ### TODO not found
        # print(shortest_path)
        engine = cmd.engine
        tags = cmd.tags
        gate = CNOT
        new_cmd_list = []
        qureg = self.qureg
        for i in range(len(shortest_path)-2):
            q1 = shortest_path[i]
            q2 = shortest_path[i+1]
            cmd_temp = Command(engine=engine,
                        gate = X,
                        tags = tags,
                        # carefull with id
                        controls = [qureg[q1]],
                        qubits = ([qureg[q2]],))
            new_cmd_list.append(cmd_temp)
            cmd_temp = Command(engine=engine,
                        gate = X,
                        tags = tags,
                        # carefull with id
                        controls = [qureg[q2]],
                        qubits = ([qureg[q1]],))
            new_cmd_list.append(cmd_temp)
            cmd_temp = Command(engine=engine,
                        gate = X,
                        tags = tags,
                        # carefull with id
                        controls = [qureg[q1]],
                        qubits = ([qureg[q2]],))
            # print("first")
            # print(cmd_temp)
            new_cmd_list.append(cmd_temp)
        # print("middle")
        cmd_temp = Command(engine=engine,
                    gate = cmd.gate,
                    tags = tags,
                    # carefull with id
                    controls = [qureg[shortest_path[-2]]],
                    qubits = ([qureg[shortest_path[-1]]],))
        # print(cmd_temp)
        # print()
        new_cmd_list.append(cmd_temp)
        for i in range(len(shortest_path)-2, 0, -1):
            # print(list(range(len(shortest_path)-2, 0, -1)))
            q1 = shortest_path[i]
            q2 = shortest_path[i-1]
            cmd_temp = Command(engine=engine,
                        gate = X,
                        tags = tags,
                        # carefull with id
                        controls = [qureg[q1]],
                        qubits = ([qureg[q2]],))
            new_cmd_list.append(cmd_temp)            
            cmd_temp = Command(engine=engine,
                        gate = X,
                        tags = tags,
                        # carefull with id
                        controls = [qureg[q2]],
                        qubits = ([qureg[q1]],))
            new_cmd_list.append(cmd_temp)            
            cmd_temp = Command(engine=engine,
                        gate = X,
                        tags = tags,
                        # carefull with id
                        controls = [qureg[q1]],
                        qubits = ([qureg[q2]],))
            new_cmd_list.append(cmd_temp)
    return new_cmd_list


#####################################
from collections import defaultdict


class Graph():
    def __init__(self, connections):
        """
        self.edges is a dict of all possible next nodes
        e.g. {'X': ['A', 'B', 'C', 'E'], ...}
        self.weights has all the weights between two nodes,
        with the two nodes as a tuple as the key
        e.g. {('X', 'A'): 7, ('X', 'B'): 2, ...}
        """
        self.edges = defaultdict(list)
        self.weights = {}
        for i,j in connections:
            self.edges[i].append(j)
        for key in self.edges:
            self.edges[key] = sorted(self.edges[key])
        for path in connections:
            self.weights[path] = 1
    
    def add_edge(self, from_node, to_node, weight):
        # Note: assumes edges are bi-directional
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.weights[(from_node, to_node)] = weight
        self.weights[(to_node, from_node)] = weight


def dijsktra(graph, initial, end):
    # shortest paths is a dict of nodes
    # whose value is a tuple of (previous node, weight)
    shortest_paths = {initial: (None, 0)}
    current_node = initial
    visited = set()
    
    while current_node != end:
        visited.add(current_node)
        destinations = graph.edges[current_node]
        weight_to_current_node = shortest_paths[current_node][1]

        for next_node in destinations:
            weight = graph.weights[(current_node, next_node)] + weight_to_current_node
            if next_node not in shortest_paths:
                shortest_paths[next_node] = (current_node, weight)
            else:
                current_shortest_weight = shortest_paths[next_node][1]
                if current_shortest_weight > weight:
                    shortest_paths[next_node] = (current_node, weight)
        
        next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}
        if not next_destinations:
            return "Route Not Possible"
        # next node is the destination with the lowest weight
        current_node = min(next_destinations, key=lambda k: next_destinations[k][1])
    
    # Work back through destinations in shortest path
    path = []
    while current_node is not None:
        path.append(current_node)
        next_node = shortest_paths[current_node][0]
        current_node = next_node
    # Reverse path
    path = path[::-1]
    return path


#####################################
### Begin main programm


def circuit_generator(eng, state, mapper):
    ############## need to change
    connections = set([(j,i) for i,j in mapper] + mapper)


    LocalOptimizer.receive = my_receive
    LocalOptimizer.add_swap = add_swap
    LocalOptimizer.graph = Graph(connections)
    LocalOptimizer.connections = connections


    n = int(np.log2(len(state)))
    qureg = eng.allocate_qureg(n)
    LocalOptimizer.qureg = qureg

    StatePreparation(state) | qureg

    eng.flush() # In order to have all the above gates sent to the simulator and executed
    mappting, wave_func = deepcopy(eng.backend.cheat())
    All(Measure) | qureg
    print(sum(wave_func.conj() * state))
    return None


backend = SimulatorMPI(gate_fusion=True, num_local_qubits=20)
cache_depth = 10
rule_set = DecompositionRuleSet(modules=[projectq.setups.decompositions])
engines = [TagRemover()
            , LocalOptimizer(cache_depth)
            , AutoReplacer(rule_set)
            , TagRemover()
            , LocalOptimizer(cache_depth)
            , GreedyScheduler()
            , CommandPrinter()]
eng = HiQMainEngine(backend, engines)

n = 5
state = np.random.rand(2**n) + np.random.rand(2**n)

mapper = [(0, 1), (1, 2), (1, 3), (2, 3), (2, 4), (3, 4)]

state = state / np.linalg.norm(state)

circuit_generator(eng, state, mapper)
