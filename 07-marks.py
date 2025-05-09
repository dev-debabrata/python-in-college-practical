# 7. Print student with highest mark 
# Given student -> A,B,C,D,E
# Marks -> 25,26,38,44,29


students = ['A', 'B', 'C', 'D', 'E']
marks = [25, 26, 38, 44, 29]

max_mark = max(marks)
index = marks.index(max_mark)

print("Topper:", students[index], "with marks:", max_mark)
