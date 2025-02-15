import numpy as np

a = np.array([1,2,3])

print(a)


a = np.array([[1,2],[3,4],[5,6],[7,8]])
print(a)

print(a.size)
print(a.shape)
print(a.ndim)

a = a.reshape(2,4)
print(a)

a = np.arange(20)
print(a)

a = np.arange(20).reshape(4,5)
print(a)

a = np.arange(20).reshape(-1,5)
print(a)



