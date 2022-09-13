import numpy as np

phi = 15.0
tetha = 30.0
betha = 45.0
x = 20
y = 30
z = 60
P = np.array([[x],[y],[z]])
print('P = \n', P)
phi = phi / 180 * np.pi # convert to radians
tetha = tetha / 180 * np.pi # convert to radians
betha = betha / 180 * np.pi # convert to radians
print('phi dalam radian = ', phi)
xrot =  np.array([[1,0,0],[0,np.cos(phi), -np.sin(phi)],[0,np.sin(phi), np.cos(phi)]])
print('matrix rotasi rot = \n', xrot)
yrot =  np.array([[np.cos(tetha),0, np.sin(tetha)],[0,1,0],[- np.sin(tetha),0, np.cos(tetha)]])
print('matrix rotasi rot = \n', yrot)
zrot =  np.array([[np.cos(betha), -np.sin(betha), 0],[np.sin(betha), np.cos(betha),0], [0,0,1]])
print('matrix rotasi rot = \n', zrot)

P1 = xrot @ P
P2 = yrot @ P1
P3 = zrot @ P2

x2 = P1[0,0]
y2 = P2[1,0]
z2 = P3[2,0]

print('p  = \n', P2)
print('x  = ', x2)
print('y  = ', y2)
print('z  = ', z2)