# my_age = 22
# my_height = 5.6
# complex_number = 4 +8j

# #4
# base = int(input('base: '))
# height = int(input('height: '))
# area_triangle = 0.5 * base * height
# print(f'The area of a triangle is {area_triangle}')

# #5
# a = int(input('side a: '))
# b = int(input('side b: '))
# c = int(input('side c: '))

# perimeter = a + b + c
# print(f'The perimeter of the triangle is: {perimeter}')

# #6 
# length = float(input('length: '))
# width = float(input('width: '))
# area = length * width
# perimeter_rectangle = 2 * (length + width)
# print(f'The area of a rectangle is: {area}')
# print(f'The perimeter of a rectangle is: {perimeter_rectangle}')

# #7
# radius = float(input('Radius: '))
# pi = 3.14
# area_of_circle = pi * radius * radius
# circumference = 2 * pi * radius

# print(area_of_circle)
# print(circumference)

#8
y = '2x - 2'
y1 =0
x2=0
x_int = 2/2
y_int = 2*(0) - 2

m = (y_int - y1) / (x2 - x_int)
print(m)

#9
x_1, y_1 = 2 ,2
x_2, y_2 = 6, 10

M = (y_2 - y_1) / (x_2 - x_1)
print(M)

#10
print(m > M)
print(m < M)
print(m == M)
print(m >= M)
print(m <= M)

#11
y= 'x^2 +6x + 9'
#for x values
y1 = 0
x1 = -3
y_ = (-3 ** 2) + (6 * -3) + 9
print(y_)

#12
py = len('python')
dr = len('dragon')
pyt = 'python'
dra = 'dragon'

print(py > dr)

#13
print('on' in pyt and 'on' in dra) 

#14
sentence = 'I hope this course is not full of jargon'
print('jargon' in sentence)

#15
print('on' not in pyt and 'on' not in dra) 

#16
length = len('python')
print(length)
float_length = float(length)
print(float_length)
string_length = str(float_length)
print(string_length)

#17
number = int(input("Number: "))
if number % 2 == 0:
    print('Even')
else:
    print("Odd")

#18
num1 = 7
num2 = 3
if num1 // num2 == int(2.7):
    print(True)
else:
    print(False)

#19
a = 10
b = '10'
if type(b) == type(a):
    print('Equal')
else:
    print("Not equal")

#20
numb = '9.8'
if int(float(numb)) == 10:
    print(True)
else:
    print(False)

#21
hours = int(input("Enter hours: "))
rate_per_hour = int(input('Enter rate per hour: '))
weekly_earnings = hours * rate_per_hour
print(f"Your weeklyt hours are: {weekly_earnings}")

#22
years = int(input("Enter the number of years you have lived: "))
seconds = years * 3600
print(f'You have lived for {seconds} seconds.')

#23
for row in range(1, 6):
    for col in range(1, 6):
        if col == 1:
            print(row, end=" ")
        elif col == 2:
            print(1, end=' ')
        elif col > 2:
            num = col - 2
            print(row ** num, end=' ')
    print() 