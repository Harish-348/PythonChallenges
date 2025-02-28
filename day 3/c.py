# Write a Python program that uses a set comprehension to generate all prime numbers
# between 1 and 50.
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n %2 == 0:
            return False
    return True
    
prime_numbers=[n for n in range(2,51) if is_prime(n)]
sort_prime=sorted(prime_numbers)
print(prime_numbers)