import numpy as np
from numpy.linalg import inv, svd, qr
from numpy import unravel_index
np.set_printoptions(precision=4)

########################
def exp_sig_x(A, delta_t):
    x =  A * delta_t
    return np.array([[np.cos(x),
                           -1j * np.sin(x)],
                          [-1j * np.sin(x),
                           np.cos(x)]])

# A = exp_sig_x(-B, delta_t)
# print(A)

# a = -1j*delta_t*(-B)/2*np.array([[0,1],[1,0]])
# print(sc.expm(a))

def exp_sig_z(A, delta_t):
    x = A * delta_t
    return np.array([[-np.exp(1j * x), 0],
                      [0, np.exp(1j * x)]])

# print(exp_sig_z(-B, delta_t))

# b = -1j*delta_t*(-B)/2*np.array([[1,0],[0,-1]])
# print(sc.expm(b))

def exp_sig_xx(A, delta_t):
    x = A * delta_t
    return np.array([[np.cos(x), 0, 0, -1j*np.sin(x)],
                      [0, np.cos(x), -1j*np.sin(x), 0],
                      [0, -1j*np.sin(x), np.cos(x), 0],
                      [-1j*np.sin(x), 0, 0, np.cos(x)]])

# c0 = exp_sig_xx(-B, delta_t)
# print(c0)
# print('')
# c1 = -1j*delta_t*(-B)*np.kron(np.array([[0,1],[1,0]]),np.array([[0,1],[1,0]]))
# c2 = sc.expm(c1)
# print(c2)
# print(c0-c2)

def exp_sig_zz(A, delta_t):
    x = A * delta_t
    return np.array([[np.exp(-1j * x), 0, 0, 0],
                     [0, np.exp(1j * x), 0, 0],
                     [0, 0, np.exp(1j * x), 0],
                     [0, 0, 0, np.exp(-1j * x)]])

# d0 = sig_zz(-B, delta_t)

# d1 = -1j*delta_t*(-B)*np.kron(np.array([[1,0],[0,-1]]),np.array([[1,0],[0,-1]]))
# d2 = sc.expm(d1)
# print(d0-d2)
##################################

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


MMAT = (1/np.sqrt(2.)*
    np.array([[ 1,  0,  0, 1j],
            [ 0, 1j,  1,  0],
            [ 0, 1j, -1,  0],
            [ 1,  0,  0,-1j]]))

Lamda = np.array([[ 1, 1,-1, 1],
                [ 1, 1, 1,-1],
                [ 1,-1,-1,-1],
                [ 1,-1, 1, 1]])

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

    #############################################
    theta = inv(Lamda) @ np.angle(np.diag(V1.T.conjugate() @ U2 @ Xd.T.conjugate()))
    print(theta)

    X = np.array([[0, 1],
        [1, 0]])

    Z = np.array([[ 1,  0],
        [ 0, -1]])

    I2 = np.array([[1 , 0],
        [0 , 1]])


    Ra1 = UA
    Rb1 = UB
    Ra2 = (1j / np.sqrt(2)) * (X + Z) * exp_sig_x(theta[0] + np.pi / 2 , 1)
    Rb2 = exp_sig_z(theta[2] , 1)
    Ra3 = (1j / np.sqrt(2)) * (X + Z)
    Rb3 = exp_sig_z(-1 * theta[1] , 1)
    Ra4 = VA @ (I2-1j*X) * (1 / np.sqrt(2))
    Rb4 = inv(VB @ (I2-1j*X) * (1 / np.sqrt(2)))


