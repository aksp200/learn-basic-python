print("\n merge list")
print([1,2,3]+[5,4,3])


list=[1,2,3,4,1,2]
print("\n\n for loop list")

for item in list:
    print(item)

print("\n set ")

print(set(list))

for item in set(list):
    print(item)
    
print("\n set substraction")
print({1,2,3,4}-{4})

    
print("\n unorder list aks tuple")

t = (1,2,4,3,5,9,6)

for item in t:
    print(item)