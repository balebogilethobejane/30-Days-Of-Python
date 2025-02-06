#Day 8.
#1. empty dict 
dog = {}
print(dog)

#2. add value, key on dict
dog = {'name': 'Sam dal', 'color': 'white', 'breed': 'Husky', 'legs': 'straigh buffy short', 'age':2 }
print(dog)

#3. student dictionary
students = {'first_name':'Khosi', 'last_name': 'Dlomo', 'gender': 'Female', 'age': 27, 'marital status':'Single', 'skills':['Python','CSS','CPP','C#'],'country':'South Africa', 'city': 'JHB'}
print(students)

#4. length of the dict
print(len(students))

#5. get value and check the datatype 
val = students.values()
print(val)
print(type(students.items()))
print(type(val))

#6. modify the skills
students['skills'] = 'HTML'
students['skills'] = 'Java'
print(students)

#7. get dict keys and  8. values
print(students.keys())
print(students.values())

#9.conversion of dict
print(students.items())

#10. deleting one item
print(students.popitem())

#11. deleting a dictionary
del students