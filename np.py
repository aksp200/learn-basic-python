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

print("\n matrix multiplication")
print(a@a)
print("\n matrix multiplication one array dot other")
print(a.dot(a))

print("\n matrix multiplication pass two arrays in np.dot")
print(np.dot(a,a))

a=np.array([[1,2,3],[1,1,1],[9,8,5]])

print("\n find min of an axis with array.min")
print(a)
print(a.min(axis=0))
print(a.min(axis=1))

a=np.array([[1,2,3],[4,5,6],[7,8,9]])
b=np.ones(3,3)
print("access elements in the matrix")
print(a[0,0])
print(a[1,0])
print(a[1,2])

print(a[:,1])
print(a[1,:])

print(a<5)


print("a.shape: ")
print(a.shape)
print("b.shape: ")
print(b.shape)

print("\n vstack arrays of same shape")
print(np.vstack((a,b)))
print("ab.shape: ")
print(np.vstack((a,b)).shape)


print("\n hstack arrays of same shape")
print(np.hstack((a,b)))
print("ab.shape: ")
print(np.hstack((a,b)).shape)

print("\n reference same array")
a=b
b[1,1]=20
print(a)
b[1,1]=1
print("\n copy an array rather than just referencing the same array")
a=b.copy();
b[1,1]=50
print(a)


print("ab.shape: ")
print(np.vstack((a,b)).shape)


