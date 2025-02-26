# Given a sentence, use a dictionary comprehension to count the frequency of each word in
# the sentence.

sentence = "the quick brown fox jumps over the lazy dog"
l=sentence.split()
# print(l)
count_frequency={i:l.count(i) for i in l}
print(count_frequency)