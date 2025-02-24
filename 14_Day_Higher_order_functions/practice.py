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