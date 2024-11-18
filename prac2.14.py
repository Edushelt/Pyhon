students = [("alice", 85), ("Bob", 75), ("Charlie", 90)]

# Sort by the second element in each tuple (the score)
sorted_students = sorted(students, key=lambda x: x[1])

print(sorted_students)