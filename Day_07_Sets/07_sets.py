'''
Project: 30 Days Of Python challenge
Author (Original): Asabeneh Yetayeh (https://github.com/Asabeneh/30-Days-Of-Python)
Day: 07 - Sets (https://github.com/Asabeneh/30-Days-Of-Python/blob/master/07_Day_Sets/07_sets.md)
Challenger: KataTNT
'''

# Sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

## Exercises: Level 1
# 1. Find the length of the set it_companies
print(len(it_companies))

# 2. Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(it_companies)

# 3. Insert multiple IT companies at once to the set it_companies
it_companies = it_companies | {'FPT', 'VNG', 'Viettel'}
print(it_companies)

# 4. Remove one of the companies from the set it_companies
it_companies.remove('FPT')
print(it_companies)

# 5. What is the difference between remove and discard
print("The 'remove()' method will raise a 'KeyError' if the element is not found while the 'discard()' method will not.")

## Exercises: Level 2
# 1. Join A and B
print('Join A and B:', A | B)

# 2. Find A intersection B
print('A intersection B:', A.intersection(B))
print('or', A & B)

# 3. Is A subset of B
print('Is A subset of B? =>', A.issubset(B))
print('or', A <= B)

# 4. Are A and B disjoint sets
print('Are A and B disjoint sets? =>', A.isdisjoint(B))

# 5. Join A with B and B with A
print('Join A with B:', A | B)
print('Join B with A:', B | A)

# 6. What is the symmetric difference between A and B
print('The symmetric difference between A and B:', A.symmetric_difference(B))
print('or', A ^ B)

# 7. Delete the sets completely
del it_companies
try:
    print(it_companies)
except NameError:
    print("The set is completely deleted.")

## Exercises: Level 3
# 1. Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age_set = set(age)

print(f'The length of "age" list ({len(age)}) is bigger than the length of "age" set ({len(age_set)}) if there are duplicate items.')

# 2. Explain the difference between the following data types: string, list, tuple and set


# 3. I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
sentence = 'I am a teacher and I love to inspire and teach people'
unique_words = set(sentence.split())
print(unique_words)
