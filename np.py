import numpy as np

a = np.array([1,2,3])

print(a)


a = np.array([[1,2],[3,4],[5,6],[7,8]])
print(a)

print(a.size)
print(a.shape)
print(a.ndim)


'''array has only 1 argument
This will not work
a = np.array(2,3)
'''


a = a.reshape(2,4)
print(a)

a = np.arange(20)
print(a)

a = np.arange(20).reshape(4,5)
print(a)

a = np.arange(20).reshape(-1,5)
print(a)


print("\n print zeros in 2x3 array")
a = np.zeros((2,3))
print(a)


print("\n print ones in 3x4 array")
a = np.ones((3,4))
print(a)


a = np.ones((3,3))
b = np.ones((3,3))

print(a+b)

print(a-b)

print(np.sin(a))

a=np.array([[1,2,3],[4,5,6],[7,8,9]])

print("add 1 in every element")
print(a+1)

print("multiple every element by 2")
print(a*2)

print("square every element")
print(a**2)

print("matrix multiplication")
print(a@a)

print("matrix transpose")
print(a.T)

