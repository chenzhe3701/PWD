import numpy as np
import transforms3d

# example
T = [20, 30, 40] # translations
R = [[0, -1, 0], [1, 0, 0], [0, 0, 1]] # rotation matrix
Z = [2.0, 3.0, 4.0] # zooms
A = transforms3d.affines.compose(T, R, Z)

print('A= {}'.format(A))

T, R, Z, S = transforms3d.affines.decompose(A)
print('T= {}'.format(T))
print('R= {}'.format(R))
print('Z= {}'.format(Z))
print('S= {}'.format(S))

zoom_value = np.ones([14,2])

# Look at tforms{iE}.tdata.T' in .mat file
# iE = 1
iE = 1
print('')
print('iE = 1')
A = np.array([
	[0.9921, 0.0043, 0, 2.8102],
	[0.0008, 0.9862, 0, -2.2570],
	[0, 0, 1, 0],
	[0, 0, 0, 1]])

def decompose_affine(M):
    A = np.array([
        [M[0,0], M[0,1], 0, M[0,2]],
        [M[1,0], M[1,1], 0, M[1,2]],
        [0, 0, 1, 0],
        [M[2,0], M[2,1], 0, M[2,2]],
    ])
    T, R, Z, S = transforms3d.affines.decompose(A)

    return T,R,Z,S


