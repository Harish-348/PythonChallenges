c=5
for i in range(c):
    for j in range(i+1,c):
        print(" ",end=" ")
    for j in range(2*i+1):
        print("*",end=" ")
        
    print()