## 💻 Exercises: Day 9

### Exercises: Level 1

#1
age = int(input("How old are you ?"))
if age > 18:
    print("You are old enough to drive")
else:
    print("You need 3 more yars to learn to drive")

#2
my_age = 24
your_age = int(input("How old are you?"))
if my_age <your_age :
    print("You are older")
else:
    print("You are younger")


#3
number_1= int(input("Enter number one ?"))
number_2= int(input("Enter number two ?"))
if number_1 > number_2:
 print(f"{number_1} greater than {number_2}")



### Exercises: Level 2

#1

student_grade = int(input("What is you grade?"))

if student_grade <= 80 and student_grade <= 100:
   print("You got an A")

elif student_grade >= 70 and student_grade < 89:
   print("You got an B")

elif student_grade >= 60 and student_grade < 69:
   print("You got an C")

elif student_grade >= 50 and student_grade < 59:
   print("You got an D")

elif student_grade <49:
    print("You got an F")
else:
   print("You got an F")



month = input("Enter a month")

if month == "September" or "October" or "November":
   print("The season is Spring")
elif month == "December" or "January" or "February":
   print("The season is Summer")
elif month == "March" or "April" or "May":
   print("The season is Autumn")
elif month == "June" or "July" or "August":
   print("The season is Autumn")


#2
fruits = ['banana', 'orange', 'mango', 'lemon']

fruit = input('What is your favourite fruit ?')

if fruit != fruits:
   fruits.append(fruit)
   print(fruits)


### Exercises: Level 3

person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

if 'skills' in person:
    skills_list =person['skills']
    middle_skill = len(skills_list)//2
    print(middle_skill)


if 'skills' in person:
   skills_list =person['skills']
   if 'Python' in skills_list:
      print('Python is in the list')
   else :
      print('python not in the list')

if 'skills' in person:
   skills =person['skills']
   if 'JavaScript' in skills and 'React' in skills:
      print("He is a frontend developer")
   elif 'Node' in skills and 'Python' in skills and 'MongoDB' in skills:
      print("He is a backend developer")
   elif 'Node' in skills and 'React' in skills and 'MongoDB' in skills:
      print("He is a fullstack developer")
else:
      print("Unknown title")

if person ['is_marred'] and person['country'] == 'Finland':
   print (f"{person['first_name']}{person['last_name']} lives in {person['country']}. He is married")
   