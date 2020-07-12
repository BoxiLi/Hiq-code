from scipy.stats import unitary_group
import numpy as np
from numpy.linalg import inv, svd, qr
from numpy import unravel_index
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

U = np.kron(unitary_group.rvs(2), unitary_group.rvs(2))
UA, UB = dec_kron(U)
print(np.diag(np.kron(UA,UB).T.conjugate() @ U))