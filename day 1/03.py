# second largest number in the list
l=[1,2,3,4,5,6,890,90000]
m=list(set(l))
m.sort()
print("second largest number:",m[-2])