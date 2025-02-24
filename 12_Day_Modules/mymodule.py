#Exercises
import random
import string
#Level 1.
#1. function that generates six digit/ character random_user_id
def random_user_id():
    id_char = string.ascii_letters + string.digits
    user_id = ''.join(random.choice(id_char) for i in range(7)) 
    return user_id
print(random_user_id())

#2. modifying the previous task.
def user_id_gen_by_user():
    num_char = int(input("Enter number of Characters: "))
    num_ID = int(input("Enter number of ID: "))
    user_id_gen = string.ascii_letters + string.digits
    lst_id = []
    for i in range(num_ID):
        current_id = ''
        for n in range(num_char):
            user_id = random.choice(user_id_gen)
            current_id += user_id
        lst_id.append(current_id)
    return lst_id
print(user_id_gen_by_user())

#3. A function that generates rgb colors(3values ranging from 0 to 255 each)
def rgb_color_gen():
    minimun = 0
    maximum = 255
    r = random.randint(minimun, maximum)
    g = random.randint(minimun, maximum)
    b = random.randint(minimun, maximum)
    return (r,g,b)
print(rgb_color_gen())

LEVEL 2:
1. A function that returns number of hexadecimal colors in an array.
def list_of_hexa_colors():
    hexa_digit = list(string.digits)
    hexa_alpha = list(string.ascii_letters)[:6]
    hexa_char = hexa_digit + hexa_alpha
    hexa = []

    for _ in range(6):
        hexa.append(random.choice(hexa_char))
    hexa_decimal = '#' + ''.join(hexa)
    return hexa_decimal
print(list_of_hexa_colors())

#2. a function that returns any number of rgb colors in an array
def list_of_rgb_colors():
    mini = 0
    maxi = 255
    r = random.randint(mini, maxi)
    g = random.randint(mini, maxi)
    b = random.randint(mini, maxi)
    rgb = (r, g, b)
    return rgb
print(list_of_rgb_colors())

#3. A function that generates any number of hexa or rgb colors:
def generate_colors(colors, num):
    hexa_lst = []
    rgb_lst = []
    for _ in range(num):
        if colors == "hexa":
            hexa_lst.append(list_of_hexa_colors())
        
    for _ in range(num):
        if colors == "rgb":
            ls=list_of_rgb_colors()
            newls=f"rgb{(ls)}"
            rgb_lst.append(newls)           
    
    return rgb_lst if colors=="rgb" else hexa_lst 
print(generate_colors('hexa', 3))
print(generate_colors('rgb', 3))

#LEVEL 3
#1. a function that takes a list as a parameter and returns a shuffled list
def shuffle_list(lst):
    if not lst:
        return
    else:
        random.shuffle(lst)
    return lst
print(shuffle_list([1,2,3,4,5,6,7]))

#2. A function that returns an array of seven random numbers in a range of 0-9, Numbers must be uniques:
def random_unique_number():
    num_arr = []
    for i in range(0, 10):
        random.shuffle(i)
