# Good Pairs[leet code]
l=[1,2,3,4]
count=0
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]==l[j] and i<j:
            count+=1
print(count)