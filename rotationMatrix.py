import numpy as np

theta = 15.0
x = 20
y = 30
P = np.array([[x],[y]])
print('P = \n', P)
theta = theta/180 * np.pi # convert to radians
print('theta = ', theta)
rot = np.array([[np.cos(theta), -np.sin(theta)],[np.sin(theta), np.cos(theta)]])
print('matrix rotasi rot = \n', rot)

P2 = rot.dot(P)
x2 = P2[0,0]
y2 = P2[1,0]

print('p  = ', P2)
print('x  = ', x2)
print('y  = ', y2)



