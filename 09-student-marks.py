# 9. Write a program to input the names and Marks of 8 students and display it. 
#     Change the Marks of 2 students and print the max Marks among the students


students = {}
for i in range(8):
    name = input(f"Enter name of student {i+1}: ")
    mark = int(input(f"Enter marks of {name}: "))
    students[name] = mark

# Change marks of 2 students
students["Alice"] = 90 
students["Bob"] = 85   

print("Updated student marks:", students)
print("Max marks:", max(students.values()))
