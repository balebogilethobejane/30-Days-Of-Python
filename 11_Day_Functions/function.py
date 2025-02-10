#Level1
#1. Declaring a function that takes two parameters and returns
def add_two_numbers(a, b):
    return a + b
print(add_two_numbers(9,15))

#2. a function that calculates the are of the circle
def area_of_circle(pi, r):
    return pi * r * r
print(area_of_circle(3.14, 30))

#3. Function that takes arbitrary number of arguments
def add_all_nums(*nums):
    total = 0
    for num in nums:
        if num:
            total += num
        else:
            print("Need to be number")
    return total
       
print(add_all_nums(1, 2, 3, 5))

#4. function that converts celsius to fahrenheit
def convert_celsius_to_fahrenheit(c):
    F = (c * 9/5) + 32
    return F
print(convert_celsius_to_fahrenheit(38))

#5. A function that takes in a month and return season
def check_season(months):
    autumn = ['September', 'October', 'November']
    winter = ['December', 'January','February']
    spring = ['March','April', 'May']
    summer = ['June', 'July', 'August']
    if months in autumn:
        return "Autumn"
    elif months in winter:
        return 'Winter'
    elif months in summer:
        return 'Summer'
    elif months in spring:
        return 'Spring'
    else:
        print("Invalid month")
print(check_season('May'))

#6.A function that calculates the slope and returns slope
def calculate_slope(x1, x2, y1, y2):
    slope = (y2 - y1) / (x2 - x1)
    return slope
print(calculate_slope(2, 4, 6, 8))

#7. function that calculates quadratic equation
def solve_quadratic_eqn(a, b, c):
    x1 = (-b +(b**2 - (4 * a * c))**0.5)/ (2 * a)
    x2 = (-b - (b**2 - (4 * a * c))** 0.5) / (2 * a)
    return x1, x2
print(solve_quadratic_eqn(1, -5, 6))

#8. A function that takes a list parameter and prints out each element
def print_list(*args):
    for arg in args:
        print(arg)
    return args
print(print_list('Khosi', 'Thato','Anele','Lee'))

#9. A function that returns a reversed list
def reverse_list(*arr):
    reverse_lst = []
    for i in arr:
        reverse_lst.append(i)
    lst = reverse_lst[::-1]
    return lst
print(reverse_list('E', 'D', 'C', 'B', 'A'))

# 10. A Function that takes a list as parameter and returns a capitalized list
