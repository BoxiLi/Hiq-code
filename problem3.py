"""
An example of decomposing controlled rotation gate into CX, CZ and single rotation
"""
import copy
from copy import deepcopy
import projectq
import numpy as np
from projectq.backends import CommandPrinter
from projectq.ops import Allocate, Measure, All, H, X, Y, Z, H, S, T, CX, CZ, Rx, Ry, Rz, Ph
from projectq.meta import Loop, Compute, Uncompute, Control
from projectq.setups import restrictedgateset
from projectq.cengines import (MainEngine,
                               AutoReplacer,
                               LocalOptimizer,
                               TagRemover,
                               DecompositionRuleSet)
from hiq.projectq.cengines import GreedyScheduler, HiQMainEngine
from hiq.projectq.backends import SimulatorMPI
import projectq.setups.decompositions

from mpi4py import MPI

backend = SimulatorMPI(gate_fusion=True, num_local_qubits=20)

cache_depth = 10
rule_set = DecompositionRuleSet(modules=[projectq.setups.decompositions])
engines = [TagRemover()
            , LocalOptimizer(cache_depth)
            , AutoReplacer(rule_set)
            , TagRemover()
            , LocalOptimizer(cache_depth)
            , GreedyScheduler()
            ]

restric_engine = restrictedgateset.get_engine_list(one_qubit_gates=(X,Y,Z,H,S,T,Rx,Ry,Rz),
                                                two_qubit_gates=(CZ,CX))

# eng = HiQMainEngine(backend, engine_list=[CommandPrinter()] + engines + [CommandPrinter()])
eng = HiQMainEngine(backend, engine_list= engines)
Qureg = eng.allocate_qureg(14)

theta1=0
theta2=0
theta3=0
theta4=0
theta5=0

from circuit import example_circuit

example_circuit(Qureg, theta1, theta2, theta3, theta4, theta5)

All(Measure) | Qureg