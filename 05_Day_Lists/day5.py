## 💻 Exercises: Day 5

### Exercises: Level 1

#1
list = []

#2
list = [ 1,2,3,4,5,6]

#3
print(len(list))

#6
first_item =(list[0])
last_item =(list[-1])
middle_item =list[len(list) // 2]
print(last_item)
print(first_item)
print(middle_item)

#7
it_companies =['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle' , 'Amazon']

#8
print(it_companies)

#9
print(len(it_companies))

#10
first =(it_companies[0])
last=(it_companies[-1])
middle = it_companies[len(list) // 2]
print (f'first item : {first}, last item : {last}, middle item :{middle}')

#11
it_companies.append('IT company')
print(it_companies)

#12
it_companies.insert(3,'IT company')
print(it_companies)

#13
company_to_leave = 'IMB'
modified_it_companies = [company.upper() if company != company_to_leave else company for company in it_companies]

print(modified_it_companies)

#14
joined_companies = '#;&nbsp; '.join(it_companies)

print(joined_companies)

#15
company_to_check = 'IBM'
if any(company == company_to_check for company in it_companies):
    print(f"{company_to_check} exists in the list.")
else:
    print(f"{company_to_check} does not exist in the list.")

#16
it_companies.sort()
print(it_companies)

#17
it_companies.sort(reverse = )
print(it_companies)
