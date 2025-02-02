# Concatenate strings
str1 = 'Thirty'
str2 = 'Days'
str3 = 'Of'
str4 = 'Python'
concatenated_string1 = f'{str1} {str2} {str3} {str4}'
print(concatenated_string1)

str5 = 'Coding'
str6 = 'For'
str7 = 'All'
concatenated_string2 = f'{str5} {str6} {str7}'
print(concatenated_string2)

# Declare a variable named company
company = "Coding For All"
print(company)

# Print the length of the company string
print(len(company))

# Change all characters to uppercase
print(company.upper())

# Change all characters to lowercase
print(company.lower())

# Use capitalize(), title(), swapcase() methods
print(company.capitalize())
print(company.title())
print(company.swapcase())

# Slice out the first word
print(company[7:])

# Check if the string contains a word
print('Coding' in company)

# Replace the word coding with Python
print(company.replace('Coding', 'Python'))

# Change Python for Everyone to Python for All
phrase = 'Python for Everyone'
print(phrase.replace('Everyone', 'All'))

# Split the string using space as the separator
print(company.split())

# Split the string at the comma
tech_companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(tech_companies.split(', '))

# Character at index 0
print(company[0])

# Last index of the string
print(company[-1])

# Character at index 10
print(company[10])

# Create an acronym
def acronym(phrase):
    return ''.join(word[0] for word in phrase.split()).upper()

print(acronym('Python For Everyone'))
print(acronym('Coding For All'))

# Position of the first occurrence of C
print(company.index('C'))

# Position of the first occurrence of F
print(company.index('F'))

# Position of the last occurrence of l
print('Coding For All People'.rfind('l'))

# Position of the first occurrence of the word 'because'
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.find('because'))

# Position of the last occurrence of the word 'because'
print(sentence.rindex('because'))

# Slice out the phrase 'because because because'
start = sentence.find('because')
end = sentence.rindex('because') + len('because')
print(sentence[start:end])

# Check if the string starts with a substring
print(company.startswith('Coding'))

# Check if the string ends with a substring
print(company.endswith('coding'))

# Remove trailing spaces
print('   Coding For All      '.strip())

# Check if variables are identifiers
print('30DaysOfPython'.isidentifier())
print('thirty_days_of_python'.isidentifier())

# Join list with a hash with space string
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(' # '.join(libraries))

# New line escape sequence
print("I am enjoying this challenge.\nI just wonder what is next.")

# Tab escape sequence
print("Name\t\tAge\tCountry\tCity")
print("Asabeneh\t250\tFinland\tHelsinki")

# String formatting
radius = 10
area = 3.14 * radius ** 2
print(f'The area of a circle with radius {radius} is {area} meters square.')

# String formatting for arithmetic operations
a, b = 8, 6
print(f'{a} + {b} = {a + b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')

print("🎉 CONGRATULATIONS ! 🎉")