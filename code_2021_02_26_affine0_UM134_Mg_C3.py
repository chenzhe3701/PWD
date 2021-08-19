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
	[0.9646, -0.0052, 0, 15.4289],
	[0.0004, 0.9608, 0, -18.9303],
	[0, 0, 1, 0],
	[0, 0, 0, 1]])

T, R, Z, S = transforms3d.affines.decompose(A)
print('T= {}'.format(T))
print('R= {}'.format(R))
print('Z= {}'.format(Z))
print('S= {}'.format(S))
zoom_value[iE,0:2] = Z[0:2]

# iE = 2
iE = 2
print('')
print('iE = 2')
A = np.array([
	[0.9536, -0.0042, 0, 22.1497],
	[0.0076, 0.9744, 0, -15.0397],
	[0, 0, 1, 0],
	[0, 0, 0, 1]])

T, R, Z, S = transforms3d.affines.decompose(A)
print('T= {}'.format(T))
print('R= {}'.format(R))
print('Z= {}'.format(Z))
print('S= {}'.format(S))
zoom_value[iE,0:2] = Z[0:2]

# iE = 3
iE = 3
print('')
print('iE = 3')
A = np.array([
	[0.9445, -0.0053, 0, 25.3995],
	[0.0076, 0.9773, 0, -19.7291],
	[0, 0, 1, 0],
	[0, 0, 0, 1]])

T, R, Z, S = transforms3d.affines.decompose(A)
print('T= {}'.format(T))
print('R= {}'.format(R))
print('Z= {}'.format(Z))
print('S= {}'.format(S))
zoom_value[iE,0:2] = Z[0:2]

# iE = 4
iE = 4
print('')
print('iE = 4')
A = np.array([
	[0.9495, -0.0039, 0, 22.7058],
	[0.0049, 1.0064, 0, -11.8009],
	[0, 0, 1, 0],
	[0, 0, 0, 1]])

T, R, Z, S = transforms3d.affines.decompose(A)
print('T= {}'.format(T))
print('R= {}'.format(R))
print('Z= {}'.format(Z))
print('S= {}'.format(S))
zoom_value[iE,0:2] = Z[0:2]

# iE = 5
iE = 5
print('')
print('iE = 5')
A = np.array([
	[0.9616, -0.0014, 0, 17.3889],
	[0.0036, 1.0068, 0, -5.4045],
	[0, 0, 1, 0],
	[0, 0, 0, 1]])

T, R, Z, S = transforms3d.affines.decompose(A)
print('T= {}'.format(T))
print('R= {}'.format(R))
print('Z= {}'.format(Z))
print('S= {}'.format(S))
zoom_value[iE,0:2] = Z[0:2]

# iE = 6
iE = 6
print('')
print('iE = 6')
A = np.array([
	[0.9817, 0.0007, 0, 7.8754],
	[0.0082, 1.0008, 0, -4.0876],
	[0, 0, 1, 0],
	[0, 0, 0, 1]])

T, R, Z, S = transforms3d.affines.decompose(A)
print('T= {}'.format(T))
print('R= {}'.format(R))
print('Z= {}'.format(Z))
print('S= {}'.format(S))
zoom_value[iE,0:2] = Z[0:2]

# iE = 7
iE = 7
print('')
print('iE = 7')
A = np.array([
	[0.9975, 0.0038, 0, 0.2687],
	[0.0074, 0.9988, 0, -1.7693],
	[0, 0, 1, 0],
	[0, 0, 0, 1]])

T, R, Z, S = transforms3d.affines.decompose(A)
print('T= {}'.format(T))
print('R= {}'.format(R))
print('Z= {}'.format(Z))
print('S= {}'.format(S))
zoom_value[iE,0:2] = Z[0:2]

# iE = 8
iE = 8
print('')
print('iE = 8')
A = np.array([
	[0.9779, -0.0032, 0, 9.0721],
	[0.0151, 0.9489, 0, -22.6226],
	[0, 0, 1, 0],
	[0, 0, 0, 1]])

T, R, Z, S = transforms3d.affines.decompose(A)
print('T= {}'.format(T))
print('R= {}'.format(R))
print('Z= {}'.format(Z))
print('S= {}'.format(S))
zoom_value[iE,0:2] = Z[0:2]

# iE = 9
iE = 9
print('')
print('iE = 9')
A = np.array([
	[0.9606, -0.0047, 0, 18.6798],
	[0.0124, 0.9712, 0, -21.8943],
	[0, 0, 1, 0],
	[0, 0, 0, 1]])

T, R, Z, S = transforms3d.affines.decompose(A)
print('T= {}'.format(T))
print('R= {}'.format(R))
print('Z= {}'.format(Z))
print('S= {}'.format(S))
zoom_value[iE,0:2] = Z[0:2]

# iE = 10
iE = 10
print('')
print('iE = 10')
A = np.array([
	[0.9462, -0.0068, 0, 24.8381],
	[0.0104, 0.9751, 0, -21.2029],
	[0, 0, 1, 0],
	[0, 0, 0, 1]])

T, R, Z, S = transforms3d.affines.decompose(A)
print('T= {}'.format(T))
print('R= {}'.format(R))
print('Z= {}'.format(Z))
print('S= {}'.format(S))
zoom_value[iE,0:2] = Z[0:2]

# iE = 11
iE = 11
print('')
print('iE = 11')
A = np.array([
	[0.9621, -0.0027, 0, 17.3862],
	[0.0050, 1.0064, 0, -7.6711],
	[0, 0, 1, 0],
	[0, 0, 0, 1]])

T, R, Z, S = transforms3d.affines.decompose(A)
print('T= {}'.format(T))
print('R= {}'.format(R))
print('Z= {}'.format(Z))
print('S= {}'.format(S))
zoom_value[iE,0:2] = Z[0:2]

# iE = 12
iE = 12
print('')
print('iE = 12')
A = np.array([
	[0.9812, -0.0002, 0, 8.7382],
	[0.0074, 1.0007, 0, -3.6172],
	[0, 0, 1, 0],
	[0, 0, 0, 1]])

T, R, Z, S = transforms3d.affines.decompose(A)
print('T= {}'.format(T))
print('R= {}'.format(R))
print('Z= {}'.format(Z))
print('S= {}'.format(S))
zoom_value[iE,0:2] = Z[0:2]

# iE = 13
iE = 13
print('')
print('iE = 13')
A = np.array([
	[0.9964, 0.0025, 0, 0.9035],
	[0.0068, 0.9979, 0, 0.2614],
	[0, 0, 1, 0],
	[0, 0, 0, 1]])

T, R, Z, S = transforms3d.affines.decompose(A)
print('T= {}'.format(T))
print('R= {}'.format(R))
print('Z= {}'.format(Z))
print('S= {}'.format(S))
zoom_value[iE,0:2] = Z[0:2]



myString = ""
for iE in np.arange(14):
	myString += f"{zoom_value[iE,0]:0.4f}, "

print(myString)
