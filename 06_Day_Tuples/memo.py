# Exercises: Level 1
# 1. Create an empty tuple
empty_tuple = ()
print("Empty tuple:", empty_tuple)

# 2. Create a tuple containing names of your sisters and your brothers
sisters = ('Alice', 'Emily')
brothers = ('Bob', 'Charlie')
print("Sisters:", sisters)
print("Brothers:", brothers)

# 3. Join brothers and sisters tuples and assign it to siblings
siblings = brothers + sisters
print("Siblings:", siblings)

# 4. How many siblings do you have?
num_siblings = len(siblings)
print("Number of siblings:", num_siblings)

# 5. Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family_members = ('David', 'Eve') + siblings
print("Family members:", family_members)


# Exercises: Level 2
# 1. Unpack siblings and parents from family_members
parents = family_members[:2]
siblings_unpacked = family_members[2:]
print("Parents:", parents)
print("Siblings (unpacked):", siblings_unpacked)

# 2. Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('apple', 'banana', 'orange')
vegetables = ('carrot', 'broccoli', 'spinach')
animal_products = ('milk', 'egg', 'meat')
food_stuff_tp = fruits + vegetables + animal_products
print("Food stuff tuple:", food_stuff_tp)

# 3. Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
print("Food stuff list:", food_stuff_lt)

# 4. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
#    (We'll use the list, as it's more easily modifiable if needed)
list_len = len(food_stuff_lt)
if list_len % 2 == 0:
    middle_items = food_stuff_lt[list_len // 2 - 1:list_len // 2 + 1]
else:
    middle_items = [food_stuff_lt[list_len // 2]]
print("Middle item(s):", middle_items)

# 5. Slice out the first three items and the last three items from food_staff_lt list
first_three = food_stuff_lt[:3]
last_three = food_stuff_lt[-3:]
print("First three items:", first_three)
print("Last three items:", last_three)

# 6. Delete the food_staff_tp tuple completely
del food_stuff_tp
# Trying to access food_stuff_tp now would raise a NameError

# 7. Check if an item exists in tuple:
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')

# 8. Check if 'Estonia' is a nordic country
print("'Estonia' is a Nordic country:", 'Estonia' in nordic_countries)

# 9. Check if 'Iceland' is a nordic country
print("'Iceland' is a Nordic country:", 'Iceland' in nordic_countries)