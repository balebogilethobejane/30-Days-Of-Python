## 💻 Exercises: Day 7

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#1
print(len(it_companies))

#2
it_companies.add("Twitter")
print(it_companies)

#3
IT_COMPANIES ={ "BBD","MTN","Telkom"}
it_companies.update(IT_COMPANIES)
print(it_companies)

#4
it_companies.remove('BBD')
print(it_companies)

#5
#This method is different from the remove() method, because the remove() method will raise an error if the specified item does not exist, and the discard() method will not.

### Exercises: Level 2
C = A.union(B)  
print(C)

print(A.intersection(B))

print(A.issubset(B))

print(A.isdisjoint(B))

CEE = A.union(B)
DEE = B .union(A)
print(CEE)
print(DEE)

print(A.symmetric_difference(B))

del A
del B

### Exercises: Level 3
age_set = set(age)
print(age_set)
print(len(age)< len(age_set))

sentence = "I am a teacher and I love to inspire and teach people"
words = sentence.split()
unique_words =set(words)
print(len(unique_words))
