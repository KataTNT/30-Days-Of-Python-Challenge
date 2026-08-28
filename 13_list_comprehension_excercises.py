"""
Project: 30 Days Of Python challenge
Author (Original): Asabeneh Yetayeh (https://github.com/Asabeneh/30-Days-Of-Python)
Day: 13 - List Comprehension (https://github.com/Asabeneh/30-Days-Of-Python/blob/master/13_Day_List_comprehension/13_list_comprehension.md)
Challenger: KataTNT
"""

# 1. Filter only negative and zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

e1 = [ number for number in numbers if number < 0]
print(e1)

# 2. Flatten the following list of lists of lists (two dimension) to a one dimensional list
list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

e2 = [ number for row in list_of_lists for number in row]
print(e2)

# 3. Using list comprehension create the following list of tuples:
import pprint
e3 = [ (i, i ** 0, i ** 1, i ** 2, i ** 3, i ** 4, i ** 5 ) for i in range(11)]
pprint.pprint(e3)

# 4. Flatten the following list to a new list:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

e4 = [ [country.upper(), country[:3].upper(), city.upper()] for row in countries for country, city in row ]
print(e4)

# 5. Change the following list to a list of dictionaries:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

e5 = [ {'country': country, 'city': city } for row in countries for country, city in row ]
print(e5)

# 6. Change the following list of lists to a list of concatenated strings:
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]

e6 = [ i + ' ' + j for row in names for i, j in row ]
print(e6)