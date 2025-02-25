# find the vowels in the sentence
s="my name is harishi"
count=0
for char in s:
    if char in "aeiouAEIOU":
        count+=1
print(count)