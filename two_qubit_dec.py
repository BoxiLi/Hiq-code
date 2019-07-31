import numpy as np
from numpy.linalg import inv, svd, qr
from numpy import unravel_index
np.set_printoptions(precision=4)
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

U2 = M.T.conjugate() @ U @ M
UR = (U2 + U2.T.conjugate()) / 2
UI = (U2 - U2.T.conjugate()) / 2.j
V2, S, Xd = svd(UI)

T = UR @ Xd
V1, tempC = qr(T)
C = np.diagonal(tempC)
V1 = T/C

mat2dec = M @ V1 @ M.T.conjugate()

def dec_kron(mat2dec):
    UA = np.ones((2, 2), dtype=np.complex)
    a = 0
    max_ind = None
    for (i,j) in [(0,0), (0,2), (2,0), (2,2)]:
        nor = np.linalg.norm(mat2dec[i:i+2, j:j+2])
        if nor > a:
            a = nor
            max_ind = (i, j)

    max_in_sub_mat2dec = np.argmax(np.abs(mat2dec[max_ind[0]:max_ind[0]+2, max_ind[1]:max_ind[1]+2]))
    row_ind, col_ind = unravel_index(max_in_sub_mat2dec, (2,2))
    for (i,j) in [(0,0), (0,1), (1,0), (1,1)]:
        UA[i,j] = mat2dec[2*i+row_ind, 2*j+col_ind]
    UA = UA/np.dot(UA[0,:].conjugate(), UA[:,0])

    UB = mat2dec[max_ind[0]:max_ind[0]+2, max_ind[1]:max_ind[1]+2]
    UB = np.array(UB)
    UB = UB/np.dot(UB[0,:].conjugate(), UB[:,0])
    return UA, UB

UA, UB = dec_kron(M @ V1 @ M.T.conjugate())
VA, VB = dec_kron(M @ Xd @ M.T.conjugate())

