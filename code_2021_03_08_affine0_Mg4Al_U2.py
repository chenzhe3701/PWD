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
	[0.9787, 0.0073, 0, 4.9617],
	[0.0026, 0.9770, 0, -2.4934],
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
	[0.9665, 0.0060, 0, 9.6122],
	[0.0007, 0.9731, 0, 1.3551],
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
	[0.9673, 0.0056, 0, 10.2552],
	[0.0010, 0.9774, 0, 3.1128],
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
	[0.9750, 0.0051, 0, 6.3250],
	[-0.0023, 0.9813, 0, 4.9297],
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
	[0.9860, 0.0059, 0, 2.9405],
	[0.0001, 0.9824, 0, 4.0871],
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
	[0.9969, 0.0054, 0, 0.0836],
	[-0.0006, 0.9836, 0, 6.0228],
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
	[0.9889, 0.0056, 0, 2.6204],
	[0.0027, 0.9761, 0, -1.0565],
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
	[0.9798, 0.0060, 0, 5.1563],
	[0.0006, 0.9718, 0, -0.2398],
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
	[0.9714, 0.0056, 0, 8.2482],
	[-0.0009, 0.9678, 0, 0.0092],
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
	[0.9768, 0.0067, 0, 5.8686],
	[-0.0065, 0.9781, 0, 5.5041],
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
	[0.9875, 0.0065, 0, 2.2995],
	[-0.0049, 0.9792, 0, 7.0309],
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
	[0.9955, 0.0049, 0, 0.0049],
	[-0.0014, 0.9808, 0, 5.2632],
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
