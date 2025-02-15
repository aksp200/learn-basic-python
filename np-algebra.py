import numpy as np

a = np.array([[1,2,3],[4,5,6],[7,8,9]])
b = np.ones(a.shape)

print(a)
print(b)

print("find covariance of a matrix")
print(np.cov(a))

print("find mean of a matrix")
print(np.mean(a))

print("find median of a matrix")
print(np.median(a))

print("find standard deviation of a matrix")
print(np.std(b))
print("find determinant")
print(np.linalg.det(a))
print(np.matrix(b))
print(np.matrix(b).I)
print(np.matrix(b).I.I)
print(np.matrix(b).I*np.matrix(b).I.I)


def distance(p1,p2):
    d =-1
    d = np.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)
    return d

p1=np.array([1,1])
p2=np.array([3,3])
print(distance(p1,p2))