# Remove duplicates from list and return it to the user  

# l=[1,2,3,4,3,3,4,5,6,7]
# m=list(set(l))
# print(m)

l=[1,2,3,2,4,5,4,5,4,5]
dup=[]
seen=set()
for i in l:
    if i not in dup:
        dup.append(l)
    elif i in dup:
        seen.append(l)
print(list(set(l)))
