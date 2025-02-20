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

#2. 