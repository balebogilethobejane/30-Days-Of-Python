#1. concatenate
a,b,c,d = 'Thirty','Days','Of','Python'
print(a + b +c + d)

#2. Concatenate strings
m, n, o = 'Coding', 'For', 'All'
print(m + n + o)

#3. Declaring a variable name
company = 'Coding For All'

#4. printing variable:
print(company)

#5. lenght
print(len(company))

#6. Uppercase 
print(company.upper())

#7. lowercase
print(company.lower())

#8. capitalize(), title(), swapcase() methods
print(f'Capitilize: {company.capitalize()}')
print(f'Title: {company.title()}')
print(f'Swapcase: {company.swapcase()}')

#9. slicing
print(company[7:])#company[7:]

#10. index method
# print(company.find('Coding')) #find()
# print(company.index('Coding'))#index()
print('Coding' in company)

#11. replace
print(company.replace('Coding','Python'))

#12. replacing
string = 'Python for Everyone'
print(string.replace('Everyone','All'))

#13. Spliting
print(company.split())

#14. split at comma
lsts = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(lsts.split(','))

#15. indexing
print(company[0])

#16. last index
print(company[-1])

#17. index10
print(company[10])

#18. Acronym
print(''.join(string[0]).upper().split())

#19. abbreviation
new_com = company.split( )
print(''.join(company[0]).upper().split())

#20. indexing 
print(company.index('C'))

#21. index
print(company.find('F'))

#22. rfind
print(company.rfind('l'))

#23. find or index
sentences = 'You cannot end a sentence with because because because is a conjunction'
print(sentences.find('because'))

#24. rindex
print(sentences.rindex('because'))

#25. slice phrase
start = sentences.find('because')
end = sentences.rindex('because') + len('because')
print(sentences[start:end])

#26. position
print(sentences.find('because'))

#27. slice
print(sentences[start:end])

#28. substing
print(string.startswith('Coding'))

#29. end with
print(string.endswith('Coding'))

#30.remove right and left space
new_ = ' Coding For All '
print(new_.rstrip().lstrip())

#31. isidentifier()
first_ = '30DaysOfPython'
second_ = 'thirty_days_of_python'
print(first_.isidentifier())
print(second_.isidentifier())

#32. join list
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(' # '.join(libraries))

#33. new line to escape
new_line = 'I am enjoying this challenge.\nI just wonder what is next.'
print(new_line)

#34. tap escape
tab_escape = 'Name\tAge\tCountry\tCity'
scape = 'Asabeneh\t27\tFinland\tHelsinki'
print(tab_escape)
print(scape)

#35. format string
radius = 10
area = 3.14 * radius ** 2
outcome = 'The area of a circle with radius {} is {} meters square'.format(radius, area)
print(outcome)

#36 formart strings
num1 = 8
num2 = 6
total = num1 + num2
diff = num1 - num2
product = num1 * num2
division = num1 / num2
remainder = num1 % num2
floor_ = num1 // num2
exp = num1 ** num2
print('{} + {} = {}'. format(num1, num2, total))
print('{} + {} = {}'. format(num1, num2, diff))
print('{} + {} = {}'. format(num1, num2, product))
print('{} + {} = {:.2f}'. format(num1, num2, division))
print('{} + {} = {}'. format(num1, num2, remainder))
print('{} + {} = {}'. format(num1, num2, floor_))
print('{} + {} = {}'. format(num1, num2, exp))