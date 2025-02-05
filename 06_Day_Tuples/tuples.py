#Level1:
#1. Empty tuple
my_tuple = ()
print(my_tuple)

#2. tuple with values:
sisters = ('Thobie', 'Thandeka', 'Nthabi')
brothers = ('Sbo', 'Sbo', 'Sbu')
print(sisters)
print(brothers)

#3. joining tuples
siblings = sisters + brothers
print(siblings)

#4. length of siblings tuple
total_siblings = len(siblings)
print(total_siblings)

#5. Modifying the tuple
lst_tuple = list(siblings)
lst_tuple.append('Sphola')
lst_tuple.append('Pale')
family_members = tuple(lst_tuple)
print(family_members)

#..................
#Level 2
#1. unpacking the tuple
unp_fam =  list(family_members)
a, b, c, d, e, f, *rents = unp_fam
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(*siblings)

#2. multiple tuples join all three 
fruits = ('Mango', 'Banana', 'Guava', 'Peach')
Vegetable = ('carrot', 'beetroot', 'potato', 'onion')
animal = ('Lion', 'Jaguar', 'panther', 'panda')
food_stuff_tp = fruits + Vegetable + animal
print(food_stuff_tp)

#3. conversion tuples to list
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

#4.slicing
num_food_stuff_lt = len(food_stuff_lt)
if num_food_stuff_lt % 2 == 0:
    mid_ = food_stuff_lt[num_food_stuff_lt // 2 - 1: num_food_stuff_lt // 2 + 1]
else:
    mid_ = food_stuff_lt[num_food_stuff_lt // 2]
print(mid_)

#5. slice 1st and last 
first_ = food_stuff_tp[0:3]
last_ = food_stuff_tp[-3:]
print(first_)
print(last_)

#6. delete the tuple
del food_stuff_tp

#7. exist in  tuple
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)