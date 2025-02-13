import statistics
import stat

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
print (first ,last,middle)

#11
it_companies.append("IT Companies")
print(it_companies)

#12
it_companies.insert( 3,"IT Companies")
print(it_companies)

#13
it_companies[1] = it_companies[1].upper()
print(it_companies)

#14
joined_companies = '#;&nbsp; '.join(it_companies)
print(joined_companies)

#15
if "Apple" in it_companies:
    print ("Apple is in the list")
else:
    print("Not in the list")

#16
it_companies.sort()
print(it_companies)


#17
it_companies.reverse()
print(it_companies)

#18
print(it_companies[0:3])

#19
print(it_companies[4:7])

#20
print(it_companies[4:5])

#21
it_companies.remove("Oracle")
print(it_companies)

#22
it_companies.remove("IBM")
print(it_companies)

#23
it_companies.pop()
print(it_companies)

#24
it_companies.clear()
print(it_companies)

#25
it_companies.clear()
print(it_companies)

#26
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

#26
full_stack = front_end + back_end
print(full_stack)

### Exercises: Level 2
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

print(max(ages))
print(min(ages) + max(ages))
print(sum(ages) /len(ages))
print (max(ages) - min(ages))
