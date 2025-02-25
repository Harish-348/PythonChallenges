##Find the closest number to 0 in the list
# l=[-1,2,3,4,7,10,1]
# closest=min(l)
# print(closest)

# How to swap the numbers without using third variable
# a=10
# b=20
# a=a+b
# b=a-b
# a=a-b
# print(a)
# print(b)

# Find the second largest number in the list
# l=[1,2,7,9,900,600,500,5,900]
# m=list(set(l))
# m.sort()
# print("sorted numbers:",m[-2])

# dict contains names as keys and values as scrores .you need to return the name and the score of the highest scorer
d={"Harish":99,"siddu":98,"pavan":98,"harry":98.5}


highest_name = None
highest_score = float('-inf')

for k,v in d.items():
    if v > highest_score:
        highest_name =k
        highest_score = v

print(highest_name, highest_score)

# Remove duplicates from list and return it to the user  

# l=[1,2,3,4,3,3,4,5,6,7]
# m=list(set(l))
# print(m)

# Good Pairs[leet code]
# l=[1,2,3,4]
# count=0
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if l[i]==l[j] and i<j:
#             count+=1
# print(count)