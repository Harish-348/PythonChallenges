# You are given a list of student names and their scores. Use a dictionary comprehension to
# map each student's name to their grade based on the following criteria:
# Score >= 90: Grade = 'A'
# 80 <= Score < 90: Grade = 'B'
# 70 <= Score < 80: Grade = 'C'
# Score < 70: Grade = 'F'

students = [("Alice", 85), ("Bob", 92), ("Charlie", 67)]

grades = {name: ('A' if score >= 90 else 
                 'B' if score >= 80 else 
                 'C' if score >= 70 else 'F') 
          for name, score in students}

print(grades)
