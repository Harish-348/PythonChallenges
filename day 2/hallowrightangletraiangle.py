# c= 5

# for i in range(c+1):
#     for j in range(i + 1):
#         if j == 0 or i==j or i==c:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# n=100
# for i in range(1,n+1):
#     if i%2==0:
#         print(i,end=' ')
n=[i%2==0 for i in range(11)]
print(n)

# squares = [x**2 for x in range(10)]
# print(squares)