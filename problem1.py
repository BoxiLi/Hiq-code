from projectq.ops import X, Y, Z, T, H, CNOT, SqrtX, All, Measure
from hiq.projectq.backends import SimulatorMPI
from hiq.projectq.cengines import GreedyScheduler, HiQMainEngine
from projectq.backends import CommandPrinter
from projectq.setups.default import get_engine_list
import scipy.linalg as sc
import numpy as np
import random
import copy
from mpi4py import MPI

eng = HiQMainEngine(engine_list=get_engine_list()+[CommandPrinter()])


num_of_qubit = 13
alpha = 0.5
beta = 1
B = 0.5
J = 2
T = 3
delta_t = 3/20
k = 5
A0 = 1
A1 = 1

def sig_x(A, delta_t):
    x =  A * delta_t / 2
    return np.array([[np.cos(x),
                           -1j * np.sin(x)],
                          [-1j * np.sin(x),
                           np.cos(x)]])

# A = sig_x(-B, delta_t)
# print(A)

# a = -1j*delta_t*(-B)/2*np.array([[0,1],[1,0]])
# print(sc.expm(a))

def sig_z(A, delta_t):
    x = A * delta_t / 2
    return np.array([[-np.exp(1j * x), 0],
                      [0, np.exp(1j * x)]])

# print(sig_z(-B, delta_t))

# b = -1j*delta_t*(-B)/2*np.array([[1,0],[0,-1]])
# print(sc.expm(b))

def sig_xx(A, delta_t):
    x = A * delta_t
    return np.array([[np.cos(x), 0, 0, -1j*np.sin(x)],
                      [0, np.cos(x), -1j*np.sin(x), 0],
                      [0, -1j*np.sin(x), np.cos(x), 0],
                      [-1j*np.sin(x), 0, 0, np.cos(x)]])

# c0 = sig_xx(-B, delta_t)
# print(c0)
# print('')
# c1 = -1j*delta_t*(-B)*np.kron(np.array([[0,1],[1,0]]),np.array([[0,1],[1,0]]))
# c2 = sc.expm(c1)
# print(c2)
# print(c0-c2)

def sig_zz(A, delta_t):
    x = A * delta_t
    return np.array([[np.exp(-1j * x), 0, 0, 0],
                     [0, np.exp(1j * x), 0, 0],
                     [0, 0, np.exp(1j * x), 0],
                     [0, 0, 0, np.exp(-1j * x)]])

# d0 = sig_zz(-B, delta_t)

# d1 = -1j*delta_t*(-B)*np.kron(np.array([[1,0],[0,-1]]),np.array([[1,0],[0,-1]]))
# d2 = sc.expm(d1)
# print(d0-d2)