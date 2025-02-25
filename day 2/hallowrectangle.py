rows=4
colomns=4
for i in range(rows):
    for j in range(colomns):
        if (i==0 or i==rows-1 or j==0 or j==colomns-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()