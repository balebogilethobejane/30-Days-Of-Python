#DAy 13:
#1. Filtering negative and zeros in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negative_filter = [i for i in numbers if i <= 0]
print(negative_filter)

#extra exercise
num_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_num = [i for i in num_lst if i % 2 == 0]
print(even_num)

#2. flatten the list into one dimensional list
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
one_dimensional_lst = [number for row in list_of_lists for num in row for number in num]
print(one_dimensional_lst)

list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [ number for row in list_of_lists for number in row]
print(flattened_list)  

#3. Using lst comprehension to create a list of tuples:
tuple_num = [(i, 1, i, i ** i, i ** 3, i ** 4, i ** 5) for i in range(11)]
print(tuple_num)

#4. Flatten a list to a new list
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flatten_countries = [[villa.upper(), villa[:3].upper(), capital.upper()] for city in countries for (villa,capital) in city]
print(flatten_countries)

#5. converting a lst into a dict
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
dictionary_ = [{'country' :country[0][0].upper(), 'city': country[0][1].upper()} for country in countries]
print(dictionary_)

#6. list to a list of concatenated strings
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
string_names = [name + " " + surname for fullname in names for (name,surname) in fullname]
print(string_names)

#7. A lambda function that solves a slope or y-intercept of linear
slopes_gradient = lambda x1, x2, y1, y2: (y2 - y1) / (x2 - x1) if x2 != x1 else None 
m = slopes_gradient(1,2,3,6,)
print(m)