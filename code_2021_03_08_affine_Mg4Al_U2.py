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
	[0.9915, 0.0041, 0, 2.9385],
	[0.0011, 0.9892, 0, -3.8876],
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
	[0.9780, 0.0060, 0, 5.3015],
	[0.0032, 0.9841, 0, -5.4671],
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
	[0.9658, 0.0040, 0, 10.4347],
	[0.0009, 0.9830, 0, -2.2604],
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
	[0.9657, 0.0038, 0, 11.2859],
	[0.0015, 0.9866, 0, -0.2084],
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
	[0.9732, 0.0035, 0, 7.3291],
	[-0.0016, 0.9899, 0, 1.5738],
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
	[0.9850, 0.0045, 0, 3.5272],
	[0.0000, 0.9890, 0, 1.4799],
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
	[0.9968, 0.0050, 0, 0.2979],
	[-0.0015, 0.9876, 0, 4.9853],
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
	[0.9888, 0.0045, 0, 3.0304],
	[0.0024, 0.9804, 0, -2.6812],
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
	[0.9793, 0.0050, 0, 5.6617],
	[0.0017, 0.9780, 0, -3.1143],
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
	[0.9703, 0.0040, 0, 9.1110],
	[0.0004, 0.9771, 0, -3.6401],
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
	[0.9765, 0.0050, 0, 6.5358],
	[-0.0057, 0.9874, 0, 2.0018],
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
	[0.9870, 0.0059, 0, 2.6581],
	[-0.0036, 0.9861, 0, 4.2052],
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
	[0.9955, 0.0043, 0, 0.1603],
	[-0.0017, 0.9855, 0, 3.7037],
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
