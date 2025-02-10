#Exercises - Day 4

#1
text1= "Thirty"
text2 ="Days"
text3 = "of"
text4 = "Python"
space = " "
new_text = text1 + space + text2 +space + text3 + space + text4
#print(new_text)

#2
text1= "Coding"
text2 ="For"
text3 = "All"
space= " "
new_text = text1 + space + text2 +space + text3 
#print(new_text)

#3
company = "Coding For All"

#4
print(company)

#5
print(len(company))

#6
print(company.upper())

#7
print(company.lower())

#8
print(company.capitalize().title().swapcase())

#9
print(company[0:6])

#10
print("Coding" in "Coding For All")

#11
text= "Coding For All"
new_text = (text.replace("Coding For All","python"))
print(new_text)

#12
text= "Coding For All"
new_text = (text.replace("Coding","python"))
print(new_text)

#13
text = "Coding For All"
split_text = (text.split())
print(split_text)

#14
text = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" 
split_text = (text.split(","))
print(split_text)

#15
text = "Coding For All"
print(text[0])

#16
text = "Coding For All"
print(text[-1])

#17
text = "Coding For All"
print(text[10])

#18
text = "Python For Everyone"
acronym =  text.split()[0][0] + text.split()[1][0] + text.split()[2][0]
print(acronym)

#19
text = "Coding For All"
acronym =  text.split()[0][0] + text.split()[1][0] + text.split()[2][0]
print(acronym)


