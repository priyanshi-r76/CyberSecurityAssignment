# Program to store student marks and find topper

students = {
    "Rahul": 85,
    "Priyanshi": 98,
    "Aman": 78,
    "Sneha": 95,
    "Karan": 88
}

topper = max(students, key=students.get)

average = sum(students.values()) / len(students)

print("Student Marks:")
print(students)

print("Topper:", topper)
print("Highest Marks:", students[topper])

print("Average Marks:", average)
