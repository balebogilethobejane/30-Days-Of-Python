#Exercises Day5
#Level1
#1. declaring an empty list
my_list = []
print(my_list)

#2 Dclaring a list with more than 5 items
lst1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(lst1)

#3. the length of list 
print(len(lst1))
print(len(my_list))

#4. getting the 1st, mid and last item
print(lst1[0]) #1st item
print(lst1[-1]) #last item
l = len(lst1) // 2
if l % 2 == 1:
    print(lst1[l])
else:
    print(lst1[l -1])

#5. Mixed_data types
mixed_data_type = ['Khosi', '27', '5.6', 'single', 'midrand']
print(mixed_data_type)

#6.variable named it_companies
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
#7. 
print(it_companies)

#8. Number of companies
print(len(it_companies))

#9. 1st, mid, last company
print(it_companies[0])
print(it_companies[-1])
it = len(it_companies) // 2
if it % 2 == 1:
    print(it_companies[it])
else:
    print(it_companies[it - 1])

#10. modify
it_companies[1] = 'BBD'
print(it_companies)

#11. Adding IT to it_company
print(it_companies.append('IT Company'))

#12. insert an IT company in the mid
if it % 2 == 1:
    new_ = it_companies[it]
print(it_companies.insert(new_, 'IT Compony'))

#13. change to uppercase
it_companies[2] = 'Microsoft'.upper()
print(it_companies)

#14. joining
for i in it_companies:
    print(it_companies.append('#'.join(i)))

#15. checking if exist in the list
print('IBM' in it_companies)

#16. sorting the list
new_it_sort_lst = sorted(it_companies)
print(new_it_sort_lst)

print(it_companies.sort())

#17. reverse the list
print(it_companies.sort(reverse=True))

#18. slicing the first 3 company
slices = it_companies[:2]
print(it_companies)

#19. last slicing
print(it_companies[-3:-1])

#20. slice mid.
mid = len(it_companies) // 2
if mid % 2 == 1:
    mid_ = it_companies[mid]
print(mid)

#21.remove the 1st 
print(it_companies.pop(0))

#22. remove mid
print(it_companies.pop(2))

#23. remove last
print(it_companies.pop(-1))

#24.remove all items
print(it_companies.clear())

#25. destroy the list
del(it_companies)

#26. join two list
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
new_list = front_end + back_end

#27.copying
full_stack = new_list.copy()
full_stack.append('Python','SQL')
print(full_stack)

#Level 2 
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

#sorting a list and finding the max and min
print(ages.sort())
maxi = max(ages)
mini = min(ages)
print(maxi)
print(mini)

#adding min and max ages to a list
sorted_list = ages.sort()

#median
median = len(sorted_list) // 2

#average 
divis = len(sorted_list)
all_items = sum(ages)
average = all_items / divis

#range
rang = max(ages) - min(ages)
print(rang)

#compare
print(compare = abs(mini - average))
print(val = abs(maxi - average))

# 2. mid country
countries = ['Afghanistan','Albania','Algeria','Andorra','Angola','Antigua and Barbuda','Argentina','Armenia','Australia','Austria','Azerbaijan',
             'Bahamas','Bahrain','Bangladesh','Barbados','Belarus','Belgium','Belize','Benin','Bhutan','Bolivia','Bosnia and Herzegovina','Botswana','Brazil','Brunei','Bulgaria','Burkina Faso','Burundi',
             'Cambodia','Cameroon','Canada','Cape Verde','Central African Republic','Chad','Chile','China','Colombi','Comoros','Congo (Brazzaville)','Congo','Costa Rica',"Cote d'Ivoire",'Croatia','Cuba','Cyprus',
             'Czech Republic', 'Denmark','Djibouti','Dominica','Dominican Republic','East Timor (Timor Timur)','Ecuador','Egypt','El Salvador','Equatorial Guinea','Eritrea','Estonia','Ethiopia','Fiji',
             'Finland','France','Gabon','Gambia, The','Georgia','Germany','Ghana','Greece','Grenada','Guatemala','Guinea','Guinea-Bissau','Guyana','Haiti','Honduras','Hungary','Iceland','India','Indonesia',
             'Iran','Iraq','Ireland','Israel','Italy','Jamaica','Japan','Jordan','Kazakhstan','Kenya','Kiribati','Korea, North','Korea, South','Kuwait','Kyrgyzstan','Laos','Latvia','Lebanon','Lesotho',
             'Liberia','Libya','Liechtenstein','Lithuania','Luxembourg','Macedonia','Madagascar','Malawi','Malaysia','Maldives','Mali','Malta','Marshall Islands','Mauritania','Mauritius','Mexico','Micronesia',
             'Moldova','Monaco','Mongolia','Morocco','Mozambique','Myanmar','Namibia','Nauru','Nepal','Netherlands','New Zealand','Nicaragua','Niger','Nigeria','Norway','Oman','Pakistan','Palau','Panama',
             'Papua New Guinea','Paraguay','Peru','Philippines','Poland','Portugal','Qatar','Romania','Russia','Rwanda','Saint Kitts and Nevis','Saint Lucia','Saint Vincent','Samoa','San Marino',
             'Sao Tome and Principe','Saudi Arabia','Senegal','Serbia and Montenegro','Seychelles','Sierra Leone','Singapore','Slovakia','Slovenia','Solomon Islands','Somalia','South Africa','Spain',
             'Sri Lanka','Sudan','Suriname','Swaziland','Sweden','Switzerland','Syria','Taiwan','Tajikistan','Tanzania','Thailand','Togo','Tonga','Trinidad and Tobago', 'Tunisia','Turkey','Turkmenistan',
             'Tuvalu','Uganda','Ukraine','United Arab Emirates','United Kingdom','United States','Uruguay','Uzbekistan','Vanuatu','Vatican City','Venezuela','Vietnam', 'Yemen','Zambia','Zimbabwe']

#3. half
lst_1 = []
lst_2 = []
equal_list = len(countries) // 2
if equal_list % 2 == 0:
    lst_1[equal_list]
    lst_2[equal_list - 1]

#unpacking
lst_ = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
asia, russ, state, * scandic = lst_