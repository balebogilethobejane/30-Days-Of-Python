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

