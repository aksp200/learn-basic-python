print("for loop")

for i in range(0,5):
    print(i)
    
    
print("for loop count down")

for i in range(10,0,-1):
    print(i)
    
    
print("\n\n for loop with skip 3")
for i in range(1,10,1):
    if(i==3):
        continue
    print(i)


print("\n\n for loop with break at 3")
for i in range(1,10,1):
    if(i==3):
        break
    print(i)
    



print("\n merge list")
print([1,2,3]+[5,4,3])


list=[1,2,3]
print("\n\n for loop list")

for item in list:
    print(item)


    

    