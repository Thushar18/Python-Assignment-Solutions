# 1. Create a Dictionary with at least 5 key-value pairs (Student ID and Name)
students = {
    101: "Ankush",
    102: "Bhaskar",
    103: "Chandu",
    104: "Dinesh",
    105: "Esha"
}

# 1.1 Adding a new value to dictionary
students[106] = "Eshwar"
print("After adding Eshwar:", students)

# 1.2 Updating a value in dictionary
students[104] = "Dharma"
print("After updating Dinesh to Dharma:", students)

# 1.3 Accessing a value in dictionary using key
student_id = 103
if student_id in students:
    print(f"Student ID {student_id} is:", students[student_id])
else:
    print("Student ID not found.")

# 1.4 Create a nested dictionary (dictionary of dictionaries)
nested_students = {
    201: {"name": "Rita", "age": 20},
    202: {"name": "Jonas", "age": 22},
    203: {"name": "Lucky", "age": 21}
}
print("Nested Dictionary:", nested_students)

# 1.5 Access values of nested dictionary
student_nested_id = 202
if student_nested_id in nested_students:
    print("Accessing nested dictionary:")
    print("Name:", nested_students[student_nested_id]["name"])
    print("Age:", nested_students[student_nested_id]["age"])

# 1.6 Print all keys in a dictionary
print("Keys in 'students' dictionary:")
for key in students:
    print(key)

# 1.7 Delete a value from dictionary
del students[102]
print("After deleting Student ID 102 (Bhaskar):", students)
