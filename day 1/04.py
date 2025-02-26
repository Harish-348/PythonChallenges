# dict contains names as keys and values as scrores .you need to return the name and the score of the highest scorer

d={"Harish":99,"siddu":98,"pavan":98,"harry":98.5}


highest_name = None
highest_score = float('-inf')

for k,v in d.items():
    if v > highest_score:
        highest_name =k
        highest_score = v

print(highest_name, highest_score)