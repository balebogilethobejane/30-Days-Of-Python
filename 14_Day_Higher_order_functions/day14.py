#Day 14
#Level 1
#1. Explain the difference between map, filter, and reduce.
"""map is a function that takes in a function and iterable as parameters.
It transform every item in an iterable"""
#map
numbers_str = ['2', '4', '6'] 
num_str = ['1', '3','5'] 
total_map = map(lambda x, y: int(x) + int(y), numbers_str, num_str)
print(list(total_map))

#filter
"""filter is a function that also takes both function and iterable as parameters:
Can only return an iterable.
it select specif items"""
numbers_str = [1, 2, 3, 4, 5] 
total_filter = filter(lambda a: a % 2 == 0, numbers_str)
print(list(total_filter))

#reduce
"""reduce is a function that combines list of items into a single value.
it takes in function and iterable."""
from functools import reduce
numbers_str = ['1', '2', '3', '4', '5'] 
total_reduce = reduce(lambda a, b: int(a) + int(b), numbers_str)
print(total_reduce)

#2. Explain the difference between higher order function, closure and decorator
#higher_order function
"""Higher order function are functions that can take one or more function as parameter,
also return another function as output. or A function that works well with other functions"""
def higher_order_function(func, lst):
    summation = func(lst)
    return summation
def sum_of_number(nums):
    return sum(nums)

#closure
"""A closure is a function that remembers the varible, even after the outer function is executed.
A function that remembers variables from its surrounding environment."""
def add_num():
    num = 5
    def add(n):
        return n + num
    return add(6)
print(add_num())

#decorator
"""decorator is a design pattern that allows adding functionality to an existing function without modifying it.
a special way to modify function using the special syntax @"""
def decorators(func):
    def wrapper():
        print("I am testing before")
        func()
        print("After everything.")
    return wrapper
@decorators
def greetings():
    print('Hello')
greetings()

#3. Define a call function before map, filter or reduce, see examples.
#a. Map
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
def change_name_upper(name):
    return name.upper()
upper_names = map(change_name_upper, names)
print(list(upper_names))

#b. Filter
numbers = [1, 2, 3, 4, 5] 
def is_odd(num):
    if num % 2 != 0:
        return True
    return False

odd_number = filter(is_odd, numbers)
print(list(odd_number))

#c. reduce
numbers_str = ['1', '2', '3', '4', '5']
def add_two_num(a, b):
    return int(a) + int(b)

single_value = reduce(add_two_num, numbers_str)
print(single_value)

#4. using loops to print each countries
countries =  [
    "United States",
    "China",
    "Japan",
    "Germany",
    "United Kingdom",
    "France",
    "India",
    "Italy",
    "Canada",
    "South Korea",
    "Russia",
    "Australia",
    "Brazil",
    "Spain",
    "Mexico",
    "Indonesia",
    "Netherlands",
    "Saudi Arabia",
    "Switzerland",
    "Turkey",
    "Ethiopia"
]
for country in countries:
    print(country)

#5. Use for to print each name in the names list.
name_lst = ["Aggy", "Lee", "Thato","Anele", "Mpho", "lebo", "Leo"]
for name in name_lst:
    print(name)

#6. Use for to print each number in the numbers list.
number_lst = [0,1,2,3,4,5,6,7,8,9,10,11]
for num in number_lst:
    print(num)

#Level 2
#1. Use map to create a new list by changing each country to uppercase in the countries list
countries_upper = map(lambda country: country.upper(), countries)
print(list(countries_upper))
#2. Use map to create a new list by changing each number to its square in the numbers list
squared_number = map(lambda num: num ** 2, number_lst)
print(list(squared_number))
#3. Use map to change each name to uppercase in the names list
upper_name = map(lambda name: name.upper(), name_lst)
print(list(upper_name))

#4. Use filter to filter out countries containing 'land'.
land_countries = filter(lambda land: 'land' in land, countries)
print(list(land_countries))
#5. Use filter to filter out countries having exactly six characters.
len_char_country = filter(lambda a: len(a) == 6, countries)
print(list(len_char_country))
#6. Use filter to filter out countries containing six letters and more in the country list.
len_more_country = filter(lambda long: len(long) >= 6, countries)
print(list(len_more_country))
#7. Use filter to filter out countries starting with an 'E'
start_with = filter(lambda a: a.startswith('E'), countries)
print(list(start_with))

#8. Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
lst_1 =  [1,2,3,4,5]
call_back = reduce(lambda x, y: x * y, map(lambda x: x ** 3, filter(lambda x: x % 2 != 0, lst_1)))
print((call_back))

lst_2 =  [1,2,3,4,5]
call_back = reduce(lambda x, y: x + y,filter(lambda x: x % 2 != 0, map(lambda x: x ** 3, lst_1)))
print((call_back))

#9. Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.
def get_string_lists(lst):
    return isinstance(lst,str)
string_lst = [1, "hello", 2.5, "world", 3, True, "Python"]
string_iterable = filter(get_string_lists, string_lst)
print(list(string_iterable))

#10. Use reduce to sum all the numbers in the numbers list.
sum_num = [0,1,2,3,4,5,6,7,8,9,10,11]
total_num = reduce(lambda x, y: x + y, sum_num)
print(total_num)

#11. Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
country_lst = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway','Iceland']
country_string = reduce(lambda x, y: x + "," + 'and' + y,"are north European countries", country_lst)
print(country_string)

#12.Declare a function called categorize_countries that returns a list of countries with some common pattern (you can find the countries list in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).
def categorize_countries():
    pass

#13. Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter.
#14. Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.js list in the data folder.
#15. Declare a get_last_ten_countries function that returns the last ten countries in the countries list.