import numpy as np
from numpy.linalg import inv, svd, qr

def sig_xx(A, delta_t):
    x = A * delta_t
    return np.array([[np.cos(x), 0, 0, -1j*np.sin(x)],
                      [0, np.cos(x), -1j*np.sin(x), 0],
                      [0, -1j*np.sin(x), np.cos(x), 0],
                      [-1j*np.sin(x), 0, 0, np.cos(x)]])
U = sig_xx(1, np.pi/4)

M = (1/np.sqrt(2.)*
    np.array([[ 1,  0,  0, 1j],
              [ 0, 1j,  1,  0],
              [ 0, 1j, -1,  0],
              [ 1,  0,  0,-1j]]))

Lamda = np.array([[ 1, 1,-1, 1],
                  [ 1, 1, 1,-1],
                  [ 1,-1,-1,-1],
                  [ 1,-1, 1, 1]])

U2 = M.conjugate()@ U @ M
UR = (U2 + U2.conjugate()) / 2
UI = (U2 - U2.conjugate()) / 2.j
V2, S, Xd = svd(UI)
print(np.linalg.norm((V2 @ np.diag(S) @ Xd - UI)))

T = UR @ Xd
V1, tempC = qr(T)
C = np.diagonal(tempC)
V1 = T/C
print(np.linalg.norm((V1 @ np.diag(C) @ Xd - UR)))

