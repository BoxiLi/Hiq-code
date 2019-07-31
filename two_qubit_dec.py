import numpy as np
from numpy.linalg import inv, svd, qr
np.set_printoptions(precision=4)
def sig_xx(A, delta_t):
    x = A * delta_t
    return np.matrix([[np.cos(x), 0, 0, -1j*np.sin(x)],
                      [0, np.cos(x), -1j*np.sin(x), 0],
                      [0, -1j*np.sin(x), np.cos(x), 0],
                      [-1j*np.sin(x), 0, 0, np.cos(x)]])
U = sig_xx(1, np.pi/4)

M = (1/np.sqrt(2.)*
    np.matrix([[ 1,  0,  0, 1j],
              [ 0, 1j,  1,  0],
              [ 0, 1j, -1,  0],
              [ 1,  0,  0,-1j]]))

Lamda = np.matrix([[ 1, 1,-1, 1],
                  [ 1, 1, 1,-1],
                  [ 1,-1,-1,-1],
                  [ 1,-1, 1, 1]])

U2 = M.H @ U @ M
UR = (U2 + U2.H) / 2
UI = (U2 - U2.H) / 2.j
V2, S, Xd = svd(UI)
print(np.linalg.norm((V2 @ np.diag(S) @ Xd - UI)))

T = UR @ Xd
V1, tempC = qr(T)
C = np.diagonal(tempC)
V1 = T/C
print(np.linalg.norm((V1 @ np.diag(C) @ Xd - UR)))

temp = M @ V1 @ M.H
UA = np.ones((2, 2), dtype=np.complex)
UA[0,1] = temp[0, 2]
UA[1,0] = temp[2, 0]
UA[1,1] = temp[2, 2]
UB = temp[0:2, 0:2]

res = np.linalg.norm(np.kron(UA, UB)-temp)
print(res)

