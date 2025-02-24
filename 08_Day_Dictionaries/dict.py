## 💻 Exercises: Day 8

#1
dog = {}

#2
dog ={
    'name':'Simba',
    'color': 'Black an White',
    'breed': "pitbull",
    'legs': 'black',
     'age': '16'
    }

#3
student = {
       'first_name': 'Lebo',
       'last_name': 'Thobejane',
       'gender':'female',
       'age': 23,
       'marital_status' : 'not married',
       'adress' : 'rayton',
       'skills': ['python','java','react'],
       'country': 'South Africa'


}

#4
print (len(student))

#5
value = student['skills']
print(type(value))

#6
value.append("sql")

print(value)

#7
keys = student.keys()
print(keys)

#8
values = student.values()
print(keys)


#9
print(student.items())

#10
print(student.popitem())

#11
del student
