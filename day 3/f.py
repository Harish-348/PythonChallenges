# List Comprehension - DNA Complement
# Given a DNA sequence as a list of characters ( A , T , C , G ), use a list comprehension to
# generate its complementary strand. The complement rules are:
# A pairs with T
# T pairs with A
# C pairs with G
# G pairs with C

dna_sequence = ['A', 'T', 'G', 'C', 'A']

a= {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

b= [a[base] for base in dna_sequence]

print(b)
