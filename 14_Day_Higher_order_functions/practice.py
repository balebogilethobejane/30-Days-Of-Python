def sum_numbers(nums):
    return sum(nums)
def higher_order_functions(f, lst):
    summation = f(lst)
    return summation
result = higher_order_functions(sum_numbers, [1, 2, 3, 4, 5])
print(result)

#function that return a function as a value
def square(x):
    return x ** 2
def cube(x):
    return x ** 3
def absolute(x):
    if x > 0:
        return x
    else:
        return -(x)
def higher_order_funct(type):
    if type == "square":
        return square
    elif type == 'cube':
        return cube
    elif type == 'absolute':
        return absolute

result = higher_order_funct('square')
print(result(3))       # 9
result = higher_order_funct('cube')
print(result(3))       # 27
result = higher_order_funct('absolute')
print(result(-3))

#closure
def outer():
    x = 10
    def inner(y):
        return x + y
    return inner
closure = outer()
print(closure(5))  # 15

#decorator
def decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@decorator
def greet():
    print("Hello!")
greet()


'''These decorator functions are higher order functions
that take functions as parameters'''

# First Decorator
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

# Second decorator
def split_string_decorator(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string

    return wrapper

@split_string_decorator
@uppercase_decorator     # order with decorators is important in this case - .upper() function does not work with lists
def greeting():
    return 'Welcome to Python'
print(greeting())   # WELCOME TO PYTHON

def decorator_with_parameters(function):
    def wrapper_accepting_parameters(para1, para2, para3):
        function(para1, para2, para3)
        print("I live in {}".format(para3))
    return wrapper_accepting_parameters

@decorator_with_parameters
def print_full_name(first_name, last_name, country):
    print("I am {} {}. I love to teach.".format(
        first_name, last_name, country))

print_full_name("Asabeneh", "Yetayeh",'Finland')

#multiple decorators to a single function
def uppercase_decorators(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
def split_string_decorator(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string
    return wrapper

@split_string_decorator
@uppercase_decorators
def greeting():
    return "Welcome to Python"
print(greeting())

def decorator_with_parameters(function):
    def wrapper_accepting_parameters(para1, para2, para3):
        function(para1, para2, para3)
        print("I live in {}".format(para3))
    return wrapper_accepting_parameters

@decorator_with_parameters
def print_full_name(first_name, last_name, country):
    print("I am {} {}. I love to teach.".format(
        first_name, last_name, country))
print_full_name("Asabeneh", "Yetayeh",'Finland')

names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
def change_to_upper(name):
    return name.upper()
names_upper_cased = map(change_to_upper, names)
print(list(names_upper_cased))  

#OR The lambda way
names_upper_cased = map(lambda name: name.upper(), names)
print(list(names_upper_cased))  

#I have a list of strings that represent numbers: ['1', '2', '3', '4', '5']. How can I convert each of these strings into an integer so that I have a list of integers instead?"
numbers_str = ['1', '2', '3', '4', '5']  # iterable
numbers_int = map(int, numbers_str) #int is a built in function
print(list(numbers_int)) 

#filter
numbers = [1, 2, 3, 4, 5] 
def is_odd(n):
    if n % 2 != 0:
        return True
    return False
odd_numbers = filter(is_odd, numbers)
print(list(odd_numbers))

#lambda
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
long_names = filter(lambda name: len(name) > 7, names)
print(list(long_names))

odd_numbers = filter(lambda n: n % 2 == 0, numbers)
print(list(odd_numbers))

from functools import reduce
numbers_str = ['1', '2', '3', '4', '5'] 
total = reduce(lambda a, b: int(a) + int(b), numbers_str)
print(total)