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
	[0.9708, -0.0050, 0, 11.0512],
	[0.0046, 0.9662, 0, -23.9794],
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
	[0.9614, -0.0040, 0, 17.1095],
	[0.0147, 0.9816, 0, -20.0166],
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
	[0.9534, -0.0062, 0, 20.0777],
	[0.0156, 0.9861, 0, -25.1753],
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
	[0.9585, -0.0039, 0, 16.9593],
	[0.0137, 1.0139, 0, -15.9325],
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
	[0.9686, -0.0020, 0, 12.9939],
	[0.0102, 1.0143, 0, -8.6523],
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
	[0.9854, 0.0013, 0, 5.3352],
	[0.0129, 1.0062, 0, -6.8029],
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
	[0.9987, 0.0051, 0, -0.9333],
	[0.0100, 1.0018, 0, -3.4523],
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
	[0.9819, -0.0019, 0, 6.0088],
	[0.0194, 0.9543, 0, -28.1694],
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
	[0.9678, -0.0037, 0, 13.8556],
	[0.0189, 0.9772, 0, -26.7382],
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
	[0.9560, -0.0072, 0, 19.0244],
	[0.0192, 0.9834, 0, -26.9938],
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
	[0.9698, -0.0039, 0, 13.1894],
	[0.0109, 1.0130, 0, -10.1516],
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
	[0.9854, 0.0010, 0, 6.0941],
	[0.0126, 1.0059, 0, -6.2102],
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
	[0.9983, 0.0042, 0, -0.3837],
	[0.0113, 1.0015, 0, -1.8197],
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
