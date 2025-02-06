#day 9. 
#level 1
#1. getting user input, checking whether they are old enough to drive or not
age = int(input('Enter your age: '))
if age >= 18:
    print('You are old enough to drive.')
elif age < 18:
    missing_years = 18 - age
    print(f'You need {missing_years} more years to learn to drive')

#2. comparing the values of ages
my_age = 25
your_age = int(input('Enter your age: '))
diff = abs(your_age - my_age)
if your_age > my_age:
    if diff == 1:
        print(f'You are {diff} year older than me')
    else:
        print(f'You are {diff} years older than me')
elif your_age >= my_age:
    print('We are the same age')
else:
    print(f'You are {diff} younger than me')

#3. Get two numbers from the user using input prompt.
a = int(input('Enter number one: '))
b = int(input('Enter number two: '))
if a > b:
    print(f"{a} is greater than {b}")
elif a < b:
    print(f'{a} is smaller than {b}')
else:
    print(f'{a} is equal to {b}')

#Level 2
#1. Code that gives grade to students according to their scores
