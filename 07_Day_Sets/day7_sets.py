#Level 1
#1. length
# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
print(len(it_companies))

#2. Adding to a set
it_companies.add('Twitter')
print(it_companies)

#3. Multiple insert
it_companies.update(['BBD', 'BCX', 'CyberX'])
print(it_companies)

#4. remove one item
it_companies.remove('BCX')
print(it_companies)

#5. differencer between remove and discard
'''remove() method raises an error if the item or set is not found.
While discard() method does not raise any error'''

#level 2
#1. join A and B
print(A.union(B))

#2. intersection
print(A.intersection(B))

#3. subsets
print(A.issubset(B))

#4. disjoint
print(A.isdisjoint(B))

#5. joining vise versa
print(A | B)
print(B | A)

#6. symmetric diff
print(A.symmetric_difference(B))

#7. delete sets
del it_companies
del A
del B

#Level 3:
#1. conversion list to set
set_age = set(age)
set_len = len(set_age)
lst_len = len(age)
print(lst_len > set_len)

#2. explaination:
'''1. String is a text inside double or single quote.
2. list is a collection of unordered changeable items.
3. tuples are collection of immutable, unordered items.
4. sets are a collection of ordered, unique items'''

#3. split method
sente = 'I am a teacher and I love to inspire and teach people'
splits_sentence = sente.split()
unique_words = set(splits_sentence)
print(unique_words)
words = len(unique_words)
print(words)
