# factorial using recursion

def fact(n):
    if not n or n == 1:
        return n
    return n* fact(n-1)

print(fact(5))