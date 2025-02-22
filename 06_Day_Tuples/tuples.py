
## 💻 Exercises: Day 6

### Exercises: Level 1

#1
tuple = ()

#2
sisters = ("Kabelo","Tshegofatso")
brothers = ("Omphile","Thato")

#3
siblings = sisters + brothers 
print(siblings)

#4
print(len(siblings))

#5
parents = ("Walter", "Sadi")
family_members = sisters + brothers + parents
print(family_members)

### Exercises: Level 2

fruits = ("apples","orange","mango")
vegetables = ("brocolli","cabbage","carrots")
animal_products = ("cheese","Ham","steak")

food_stuff_tp = fruits + vegetables + animal_products
food_stuff_ls = list(food_stuff_tp)

middle_items = food_stuff_ls [-4:-1]
first_three = food_stuff_ls [0:3]
last_three = food_stuff_ls [3:0]
print(last_three)
