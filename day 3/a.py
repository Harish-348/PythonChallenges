# Write a Python program that generates a random DNA sequence of length 20 using the
# characters A , T , C , and G . Use a list comprehension to create the sequence.
# Define a simple repeating DNA pattern
import random
n=20
bases="ATGC"
dna_sequence=[random.choice(bases) for i in range(n)]
print(dna_sequence)
