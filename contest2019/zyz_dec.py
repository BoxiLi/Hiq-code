import numpy as np
from numpy.linalg import solve
np.set_printoptions(precision=4)

def rx(phi):
    return np.array([[np.cos(phi / 2), -1j * np.sin(phi / 2)],
                     [-1j * np.sin(phi / 2), np.cos(phi / 2)]])

def ry(phi):
    return np.array([[np.cos(phi / 2), -np.sin(phi / 2)],
                     [np.sin(phi / 2), np.cos(phi / 2)]])

def rz(phi):
    return np.array([[np.exp(-1j * phi / 2), 0],
                     [0, np.exp(1j * phi / 2)]])

def exp_sig_x(A, delta_t):
    x =  A * delta_t
    return np.array([[np.cos(x),
                           -1j * np.sin(x)],
                          [-1j * np.sin(x),
                           np.cos(x)]])


def zyz_dec(U, qureg, id):
    gamma = np.arctan(np.abs(U[0,1] / U[0,0]))
    phia = np.angle(U[0,0]/np.cos(gamma))
    phib = np.angle(U[0,1]/np.sin(gamma))
    phic = np.angle(U[1,0]/np.sin(gamma))
    phid = np.angle(U[1,1]/np.cos(gamma))

    alpha = (phia + phid) / 2.
    beta = (phic - phia) / 2.
    delta = (phid - phic) / 2.

    # new_U = rz(2*beta) @ ry(2*gamma) @ rz(2*delta) * np.exp(1.j*alpha)
    Rz(2*beta) | qureg[id]
    Ry(2*gamma) | qureg[id]
    Rz(2*delta) | qureg[id]
