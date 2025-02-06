# 1. Create an empty dictionary called dog
dog = {}

# 2. Add name, color, breed, legs, age to the dog dictionary
dog['name'] = 'Buddy'
dog['color'] = 'Golden'
dog['breed'] = 'Labrador'
dog['legs'] = 4
dog['age'] = 3

# 3. Create a student dictionary and add keys
student = {
    'first_name': 'John',
    'last_name': 'Doe',
    'gender': 'Male',
    'age': 20,
    'marital_status': 'Single',
    'skills': ['Python', 'Java'],
    'country': 'USA',
    'city': 'New York',
    'address': '123 Main Street'
}

# 4. Get the length of the student dictionary
student_length = len(student)
print("Length of student dictionary:", student_length)

# 5. Get the value of skills and check the data type
skills_value = student['skills']
print("Skills:", skills_value)
print("Data type of skills:", type(skills_value))

# 6. Modify the skills values by adding one or two skills
student['skills'].append('JavaScript')
student['skills'].append('HTML')
print("Updated skills:", student['skills'])

# 7. Get the dictionary keys as a list
student_keys = list(student.keys())
print("Student dictionary keys:", student_keys)

# 8. Get the dictionary values as a list
student_values = list(student.values())
print("Student dictionary values:", student_values)

# 9. Change the dictionary to a list of tuples using items() method
student_items = list(student.items())
print("Student dictionary as list of tuples:", student_items)

# 10. Delete one of the items in the dictionary
del student['address']
print("Student dictionary after deleting address:", student)

# 11. Delete one of the dictionaries
del dog
