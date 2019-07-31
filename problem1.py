# -*- coding: utf-8 -*-
# File name: problem1.py
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

##############################
import numpy as np
from numpy.linalg import inv, svd, qr
from numpy import unravel_index
##############################

def exp_sig_x(A, delta_t):
    x =  A * delta_t
    return np.array([[np.cos(x),
                           1j * np.sin(x)],
                          [1j * np.sin(x),
                           np.cos(x)]])

def exp_sig_z(A, delta_t):
    x = A * delta_t
    return np.array([[np.exp(1j * x), 0],
                      [0, np.exp(-1j * x)]])

def exp_sig_xx(A, delta_t):
    x = A * delta_t
    return np.array([[np.cos(x), 0, 0, 1j*np.sin(x)],
                      [0, np.cos(x), 1j*np.sin(x), 0],
                      [0, 1j*np.sin(x), np.cos(x), 0],
                      [1j*np.sin(x), 0, 0, np.cos(x)]])

def exp_sig_zz(A, delta_t):
    x = A * delta_t
    return np.array([[np.exp(1j * x), 0, 0, 0],
                     [0, np.exp(-1j * x), 0, 0],
                     [0, 0, np.exp(-1j * x), 0],
                     [0, 0, 0, np.exp(1j * x)]])

def rx(phi):
    return np.array([[np.cos(phi / 2), -1j * np.sin(phi / 2)],
                     [-1j * np.sin(phi / 2), np.cos(phi / 2)]])

def ry(phi):
    return np.array([[np.cos(phi / 2), -np.sin(phi / 2)],
                     [np.sin(phi / 2), np.cos(phi / 2)]])

def rz(phi):
    return np.array([[np.exp(-1j * phi / 2), 0],
                     [0, np.exp(1j * phi / 2)]])

MMAT = (1/np.sqrt(2.)*
    np.array([[ 1,  0,  0, 1j],
            [ 0, 1j,  1,  0],
            [ 0, 1j, -1,  0],
            [ 1,  0,  0,-1j]], dtype=np.complex))

Lamda = np.array([[ 1, 1,-1, 1],
                [ 1, 1, 1,-1],
                [ 1,-1,-1,-1],
                [ 1,-1, 1, 1]], dtype=np.complex)

###########################
# Mainly follow the paper http://cds.cern.ch/record/931003/files/0602174.pdf
def zyz_dec(U):
    if abs(U[0, 0]) < 1.e-10:
        gamma = np.pi/2
    else:
        gamma = np.arctan(np.abs(U[0,1] / U[0,0]))
    if abs(np.sin(gamma)) < 1.e-6:
        beta = (np.angle(U[1,1]) - np.angle(U[0,0]))/2.
        return beta, 0., 0.
    if abs(np.cos(gamma)) < 1.e-6:
        delta =(np.angle(U[0,1]) - np.angle(U[1,0])-np.pi)/2.
        return 0, delta, np.pi/2.
    phia = np.angle(U[0,0]/np.cos(gamma))
    # phib = np.angle(U[0,1]/np.sin(gamma))
    phic = np.angle(U[1,0]/np.sin(gamma))
    phid = np.angle(U[1,1]/np.cos(gamma))

    # alpha = (phia + phid) / 2.
    beta = (phic - phia) / 2.
    delta = (phid - phic) / 2.
    return beta, delta, gamma
    #     print()
    #     print(beta, delta)
    #     print()
    # new_U = rz(2*beta) @ ry(2*gamma) @ rz(2*delta) * np.exp(1.j*alpha)


def apply_zyz(qureg, id, beta, delta, gamma):
    if delta==0. and gamma==0.:
        Rz(2*beta) | qureg[id]
    elif beta==0. and gamma==np.pi/2.:
        Ry(2*gamma) | qureg[id]
        Rz(2*delta) | qureg[id]
    else:
        Rz(2*beta) | qureg[id]
        Ry(2*gamma) | qureg[id]
        Rz(2*delta) | qureg[id]


def dec_kron(mat2dec):
    UA = np.ones((2, 2), dtype=np.complex)
    a = 0
    max_ind = None
    for (i,j) in [(0,0), (0,2), (2,0), (2,2)]:
        nor = np.linalg.norm(mat2dec[i:i+2, j:j+2])
        if nor > a:
            a = nor
            max_ind = (i, j)

    max_pos_sub_mat2dec = np.argmax(np.abs(mat2dec[max_ind[0]:max_ind[0]+2, max_ind[1]:max_ind[1]+2]))
    row_ind, col_ind = unravel_index(max_pos_sub_mat2dec, (2,2))
    for (i,j) in [(0,0), (0,1), (1,0), (1,1)]:
        UA[i,j] = mat2dec[2*i+row_ind, 2*j+col_ind]
    UA = UA/np.sqrt((UA.T.conjugate() @ UA)[0,0])

    UB = mat2dec[max_ind[0]:max_ind[0]+2, max_ind[1]:max_ind[1]+2]
    UB = np.array(UB)
    UB = UB/np.sqrt((UB.T.conjugate() @ UB)[0,0])
    return UA, UB


def two_qubits_dec(U):
    U2 = MMAT.T.conjugate() @ U @ MMAT
    UR = (U2 + U2.T.conjugate()) / 2
    UI = (U2 - U2.T.conjugate()) / 2.j
    V2, S, Xd = svd(UI)

    T = UR @ Xd
    V1, tempC = qr(T)
    C = np.diagonal(tempC)
    V1 = T/C

    UA, UB = dec_kron(MMAT @ V1 @ MMAT.T.conjugate())
    VA, VB = dec_kron(MMAT @ Xd @ MMAT.T.conjugate())

    theta = inv(Lamda) @ np.angle(np.diag(V1.T.conjugate() @ U2 @ Xd.T.conjugate()))

    X = np.array([[0, 1],
        [1, 0]], dtype=np.complex)

    Z = np.array([[ 1,  0],
        [ 0, -1]], dtype=np.complex)

    I2 = np.array([[1 , 0],
        [0 , 1]], dtype=np.complex)


    Ra1 = UA
    Rb1 = UB
    Ra2 = 1.j / np.sqrt(2) * (X + Z) @ exp_sig_x(theta[1] + np.pi / 2, -1)
    Ra2 = (1j / np.sqrt(2)) * (X + Z) @ exp_sig_x(theta[1] + np.pi / 2 , -1)
    Rb2 = exp_sig_z(theta[3] , -1)
    Ra3 = -(1j / np.sqrt(2)) * (X + Z)
    Rb3 = exp_sig_z(theta[2] , 1)
    Ra4 = VA @ (I2-1j*X) / np.sqrt(2)
    Rb4 = VB @ inv((I2 - 1j*X) / np.sqrt(2))
    return Ra1, Ra2, Ra3, Ra4, Rb1, Rb2, Rb3, Rb4


#########################
N = 3
num_of_qubit = 3
alpha = 0.5
beta = 1
B = 0.5
J = 2
T = 3

dt = 0.1
n_t = int(T/dt)
M = 20

from functools import reduce
from scipy.sparse import bsr_matrix
H1 = bsr_matrix(np.zeros((2**N, 2**N)))
I2 = np.array([[1.,0.],[0.,1.]])
I2_list = ([I2]*N)
for i in range(N):
    l1 = I2_list
    l1[i] = X.matrix
    l2 = I2_list
    l2[i] = Z.matrix
    H1 += reduce(np.kron, l1)
    H1 += reduce(np.kron, l2)
I2_list = ([I2]*(N-2))
for i in range(N-1):
    l1 = I2_list
    l1.insert(i, np.kron(X.matrix, X.matrix))
    l2 = I2_list
    l2.insert(i, np.kron(Z.matrix, Z.matrix))
    H1 += reduce(np.kron, l1)
    H1 += reduce(np.kron, l2)

# H1 += -alpha * reduce(np.kron, [X.matrix]*N)
# H1 += -beta * reduce(np.kron, [Z.matrix]*N)
# H1 += -J * reduce(np.kron, [np.kron]

#############
def adiabatic_simulation(eng):
    """The function you need to modify.
    Returns:
    real_energy(float):
    The final ideally continously evolved energy.
    simulated_energy(float):
    The final energy simulated by your model.
    """
    qureg = eng.allocate_qureg(num_of_qubit)

    ####################loop
    tlist = np.linspace(0, T, n_t)
    for t in tlist:

        s = np.floor(t / T * M) /M
        c1 = -(1 - s) * B - s * alpha
        c2 = -s * beta
        c3 = -s * J
        c4 = -s * J
        N = 3
        dt = 0.01
        mat_pos_list = []

        # sigmax/2
        mat1 = exp_sig_x(-c1, t / 2.)
        beta_x, delta_x, gamma_x = zyz_dec(mat1)
        for id in range(num_of_qubit):
            apply_zyz(qureg, id, beta_x, delta_x, gamma_x)

        # sigmaz/2
        mat2 = exp_sig_z(-c2, t / 2.)
        beta_z, delta_z, gamma_z = zyz_dec(mat2)
        for id in range(num_of_qubit):
            apply_zyz(qureg, id, beta_z, delta_z, gamma_z)

        # sigmazz/2
        mat3 = exp_sig_zz(-c4, t / 2.)
        Ra1, Ra2, Ra3, Ra4, Rb1, Rb2, Rb3, Rb4 = two_qubits_dec(mat3)
        dec_data1_zz = zyz_dec(Ra1)
        dec_data2_zz = zyz_dec(Rb1)
        dec_data3_zz = zyz_dec(Ra2)
        dec_data4_zz = zyz_dec(Rb2)
        dec_data5_zz = zyz_dec(Ra3)
        dec_data6_zz = zyz_dec(Rb3)
        dec_data7_zz = zyz_dec(Ra4)
        dec_data8_zz = zyz_dec(Rb4)
        for id in range(num_of_qubit - 1):
            apply_zyz(qureg, id, *dec_data1_zz)
            apply_zyz(qureg, id+1, *dec_data2_zz)
            CX | (qureg[id], qureg[id+1])
            apply_zyz(qureg, id, *dec_data3_zz)
            apply_zyz(qureg, id+1, *dec_data4_zz)
            CX | (qureg[id], qureg[id+1])
            apply_zyz(qureg, id, *dec_data5_zz)
            apply_zyz(qureg, id+1, *dec_data6_zz)
            CX | (qureg[id], qureg[id+1])
            apply_zyz(qureg, id, *dec_data7_zz)
            apply_zyz(qureg, id+1, *dec_data8_zz)

        # sigmaxx
        mat4 = exp_sig_xx(-c3, t)
        Ra1, Ra2, Ra3, Ra4, Rb1, Rb2, Rb3, Rb4 = two_qubits_dec(mat4)
        dec_data1 = zyz_dec(Ra1)
        dec_data2 = zyz_dec(Rb1)
        dec_data3 = zyz_dec(Ra2)
        dec_data4= zyz_dec(Rb2)
        dec_data5 = zyz_dec(Ra3)
        dec_data6 = zyz_dec(Rb3)
        dec_data7 = zyz_dec(Ra4)
        dec_data8 = zyz_dec(Rb4)
        for id in range(num_of_qubit - 1):
            apply_zyz(qureg, id, *dec_data1)
            apply_zyz(qureg, id+1, *dec_data2)
            CX | (qureg[id], qureg[id+1])
            apply_zyz(qureg, id, *dec_data3)
            apply_zyz(qureg, id+1, *dec_data4)
            CX | (qureg[id], qureg[id+1])
            apply_zyz(qureg, id, *dec_data5)
            apply_zyz(qureg, id+1, *dec_data6)
            CX | (qureg[id], qureg[id+1])
            apply_zyz(qureg, id, *dec_data7)
            apply_zyz(qureg, id+1, *dec_data8)

        # sigmazz/2
        for id in range(num_of_qubit - 1):
            apply_zyz(qureg, id, *dec_data1_zz)
            apply_zyz(qureg, id+1, *dec_data2_zz)
            CX | (qureg[id], qureg[id+1])
            apply_zyz(qureg, id, *dec_data3_zz)
            apply_zyz(qureg, id+1, *dec_data4_zz)
            CX | (qureg[id], qureg[id+1])
            apply_zyz(qureg, id, *dec_data5_zz)
            apply_zyz(qureg, id+1, *dec_data6_zz)
            CX | (qureg[id], qureg[id+1])
            apply_zyz(qureg, id, *dec_data7_zz)
            apply_zyz(qureg, id+1, *dec_data8_zz)

        # sigmaz/2
        # mat2 = exp_sig_z(-c2, t / 2.)
        # beta_z, delta_z, gamma_z = zyz_dec(mat2)
        for id in range(num_of_qubit):
            apply_zyz(qureg, id, beta_z, delta_z, gamma_z)

        # sigmax/2
        # mat1 = exp_sig_x(-c1, t / 2.)
        # beta_x, delta_x, gamma_x = zyz_dec(mat1)
        for id in range(num_of_qubit):
            apply_zyz(qureg, id, beta_x, delta_x, gamma_x)

    simulated_energy = 0
    real_energy = 0
    
    All(Measure) | qureg
    return simulated_energy, real_energy


from projectq.cengines import MainEngine
if __name__ == "__main__":
    # use projectq simulator
    #eng = MainEngine()
    # use hiq simulator
    cache_depth = 10
    rule_set = DecompositionRuleSet(modules=[projectq.setups.decompositions])
    # make the compiler and run the circuit on the simulator backend
    eng = MainEngine()

    simulated_energy, real_energy = adiabatic_simulation(eng)
    simulated_error = simulated_energy - real_energy
    print(simulated_error)