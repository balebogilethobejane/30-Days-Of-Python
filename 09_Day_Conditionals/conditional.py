# #day 9. 
# #level 1
# #1. getting user input, checking whether they are old enough to drive or not
# age = int(input('Enter your age: '))
# if age >= 18:
#     print('You are old enough to drive.')
# elif age < 18:
#     missing_years = 18 - age
#     print(f'You need {missing_years} more years to learn to drive')

# #2. comparing the values of ages
# my_age = 25
# your_age = int(input('Enter your age: '))
# diff = abs(your_age - my_age)
# if your_age > my_age:
#     if diff == 1:
#         print(f'You are {diff} year older than me')
#     else:
#         print(f'You are {diff} years older than me')
# elif your_age >= my_age:
#     print('We are the same age')
# else:
#     print(f'You are {diff} younger than me')

# #3. Get two numbers from the user using input prompt.
# a = int(input('Enter number one: '))
# b = int(input('Enter number two: '))
# if a > b:
#     print(f"{a} is greater than {b}")
# elif a < b:
#     print(f'{a} is smaller than {b}')
# else:
#     print(f'{a} is equal to {b}')

# #Level 2
# #1. Code that gives grade to students according to their scores
# grades = int(input('What is your grade: '))
# if 80 <= grades <= 100:
#     print('A')
# elif 70 <= grades <= 89:
#     print('B')
# elif 60 <= grades <= 69:
#     print('C')
# elif 50 <= grades <= 59:
#     print('D')
# else:
#     print('F')

# #2. checking seasons
# autumn = ['September', 'October', 'November']
# winter = ['December', 'January','February']
# spring = ['March','April', 'May']
# summer = ['June', 'July', 'August']

# season = input('Enter the month: ')
# if season in autumn:
#     print('The season is Autumn')
# elif season in winter:
#     print('The season is Winter')
# elif season in spring:
#     print('The season is Spring')
# else:
#     print('The season is Summer')

# #3. If a fruit doesn't exist in the list add the fruit to the list and print the modified list. 
# fruits = ['banana', 'orange', 'mango', 'lemon']
# food = input('Enter a fruit: ')
# if food not in fruits:
#     fruits.append(food)
#     print(fruits)
# else:
#     print('That fruit already exist in the list')

#Level 3
#1. modifying dictionary
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

#checking if skills in dict
if 'skills' in person:
    lst_ = person['skills']
    length = len(lst_) // 2
    print(lst_[length])

if 'skills' in person:
    if 'Python' in person['skills']:
        print('Python exist')
    else:
        print('Python doe not exist')

if 'skills' in person:
    skill = person['skills']
    if set(skill) == {'JavaScript', 'React'}:
        print('We got a Front end developer')

    elif set(skill) =={'Node', 'MongoDB', 'Python'}:
        print('We got a back end developer') 

    elif set(skill) == {'React', 'Node', 'MongoDB'}:
        print('We got a fullstack developer.')

    else:
        print('unknown title')
    
#and logigal operator
if person['is_marred'] and person['country'] == 'Finland':
    print(f'{person["first_name"]} {person["last_name"]} lives in {person["country"]}. He is Married')


