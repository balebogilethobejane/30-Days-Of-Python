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
def capitalize_list_items(*lst):
    capital_lst = []
    for i in lst:
        capital_lst.append(i.capitalize())
    return capital_lst
print(capitalize_list_items("mr","mrs","miss", 'doc'))

#11. Declaring a function tha takes a list and an item parameters, returning a list with the items addedd at the end.
def add_items(lst_, n):
    my_lst = lst_[:]
    my_lst.append(n)
    return my_lst
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_items(food_staff, 'Meat')) 

#12. Declaring a function that takes a list and an item parameters and returning a list with removed item
def remove_item(lst, item):
    new_lst = lst[:]
    new_lst.remove(item)
    return new_lst
numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3)) 

#13. Declaring a function that takes a number parameter and adds all the numbers in that range
def sum_of_numbers(n):
    y=0
    for i in range(1,n+1):
        y += i
    return y
print(sum_of_numbers(10))

#14. Declaring a function that takes a number parameter and adds all the odd numbers in that range 
def sum_of_odds(n):
    num = 0
    for i in range(n+1):
        if i % 2 != 0:
            num += i
    return num
print(sum_of_odds(10))

#15. Declaring a function that takes a number parameter and adds all the even numbers in that - range
def sum_of_even(n):
    num = 0
    if n <= 0:
        for i in range(n, 0):
            if i % 2 == 0:
                num += i
        return num
    else:
        for i in range(1, n +1):
            if i % 2 == 0:
                num += i
        return num
print(sum_of_even(-10))

#Level 2
#1. declaring a function that takes positive int, and counts the number of even numbers and odd numbers
def even_and_odd(n):
    even = 0
    odd = 0
    if n < 0:
        return
    else:
        for num in range(n+1):
            if num % 2 == 0:
                even += 1
            elif num % 2 != 0:
                odd += 1
        return f"The number of evens are {even} \nThe number of odds are {odd}"
print(even_and_odd(100))

#2. Factorial function that takes in a whole number and return a factorial of that number
def factorial(number):
    if number == 1 or number == 0:
        return
    y = 1
    for i in range(1, number +1):
        y *= i
    return y
print(factorial(5))

#3. declaring a function that checks if it is empty or not
def is_empty(n):
    if not n:
        return False
    else:
        return True
print(is_empty([]))   

#4. Different functions that take lists, They should calculate mean, median,mode, range, variance, std
#mean
def calculate_mean(lst):
    if not lst:
        return False
    else: 
        sum_num = sum(lst)
        length_of_lst = len(lst)
        mean = sum_num / length_of_lst
    return mean
print(calculate_mean([1, 2, 2, 3, 4, 5]))

#median
def calculate_median(lsts):
    if not lsts:
        return False
    sorted_lst = sorted(lsts)
    length_lst = len(sorted_lst)

    if length_lst % 2 == 0:
        mid_1 = sorted_lst[length_lst // 2 -1]
        mid_2 = sorted_lst[length_lst // 2]
        median = (mid_1 + mid_2) / 2
    else:
        median = sorted_lst[length_lst // 2]
    return median
print(calculate_median([1, 2, 2, 3, 4, 5,6]))

#Mode
def calculate_mode(lst):
    if not lst:
        return False
    more_count = 0
    mode = []
    for num in lst:
        count = 0
        for num2 in lst:
            if num == num2:
                count += 1
        if count > more_count:
            mode = [num]
            more_count = count
        elif count == more_count and num not in mode:
            mode.append(num)
    if more_count == 1 and len(lst) > 1:
        return "No mode"
    return mode
print(calculate_mode([1, 2, 2, 3, 3, 3, 3, 4, 5, 6]))

#Range
def calculate_range(lst):
    if not lst:
        return True
    min_num = min(lst)
    max_num = max(lst)
    range_num = max_num - min_num
    return range_num
print(calculate_range([1, 2, 2, 3, 4, 5,10]))

#variance
def calculate_variance(lst):
    if not lst:
        return False
    mn = calculate_mean(lst)
    sqr_diff = []
    for i in lst:
        sqr_diff.append((i - mn) **2)
    sum_sqr_diff = sum(sqr_diff)
    variance = sum_sqr_diff / (len(lst) - 1)
    return round(variance,2)
print(calculate_variance([1, 2, 2, 3, 4, 5,10]))

#Standard Deviation
def calculate_std(lst):
    if not lst:
        return False
    varience = calculate_variance(lst)
    
    std = varience ** 0.5
    return round(std, 2)
print(calculate_std([1, 2, 2, 3, 4, 5,10]))

#LEVEL 3
#1. function that check if numbers are prime numbers
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
print(is_prime(5))

#2. function that checks all unique item
def unique_items(unique_lst):
    
    return sorted(set(unique_lst))
print(unique_items([1, 2, 2, 3, 4, 4, 5]))