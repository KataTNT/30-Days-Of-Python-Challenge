"""
Project: 30 Days Of Python challenge
Author (Original): Asabeneh Yetayeh (https://github.com/Asabeneh/30-Days-Of-Python)
Day: 10 - Loops (https://github.com/Asabeneh/30-Days-Of-Python/blob/master/10_Day_Loops/10_loops.md)
Challenger: KataTNT
"""

## Exercises: Level 1
# 1. Iterate 0 to 10 using for loop, do the same using while loop.
for a in range (10):
    print(a)

b = 0
while b < 10:
    print(b)
    b += 1
# 2. Iterate 10 to 0 using for loop, do the same using while loop.
for c in range(10, 0, -1):
    print(c)

d = 10
while d > 0:
    print(d)
    d -= 1

"""
3. Write a loop that makes seven calls to print(), so we get on the output the following triangle:
#
##
###
####
#####
######
#######
"""


for e in range(1,8):
    print('#' * e)

"""
4. Use nested loops to create the following:
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
"""
for _ in range(8):
    res = '# ' * 8
    print(res[:-1])

"""
5. Print the following pattern:
0 x 0 = 0
1 x 1 = 1
2 x 2 = 4
3 x 3 = 9
4 x 4 = 16
5 x 5 = 25
6 x 6 = 36
7 x 7 = 49
8 x 8 = 64
9 x 9 = 81
10 x 10 = 100
"""
for f in range(11):
    print(f'{f} x {f} = {f * f}')

# 6. Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
programing_languages = ['Python', 'Numpy','Pandas','Django', 'Flask']
for item in programing_languages:
    print(item)

# 7. Use for loop to iterate from 0 to 100 and print only even numbers
for h in range(101):
    if h % 2 == 0:
        print(h)

# 8. Use for loop to iterate from 0 to 100 and print only odd numbers
for i in range(101):
    if i % 2 != 0:
        print(i)

## Exercises: Level 2
# 1. Use for loop to iterate from 0 to 100 and print the sum of all numbers.
sum_all = 0
for j in range(101):
    sum_all += j
print(f'The sum of all numbers is {sum_all}.') 

# 2. Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
sum_evens, sum_odds = 0, 0
for k in range(101):
    if k % 2 == 0:
        sum_evens += k
    else:
        sum_odds += k
print(f'The sum of all evens is {sum_evens}. And the sum of all odds is {sum_odds}.')

## Exercises: Level 3
# 1. Go to the data folder and use the countries_data.json file. Loop through the countries and extract all the countries containing the word land.
import json
with open("./data/countries_data.json", mode="r", encoding="utf-8") as file:
    countries_data = json.load(file)
extract_countries = []

for country in countries_data:
    if "land" in country["name"]:
        extract_countries.append(country["name"])
print(extract_countries)

# 2. This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
fruit = ['banana', 'orange', 'mango', 'lemon']
reversed_fruit = []
index = len(fruit) - 1
while index >= 0:
    reversed_fruit.append(fruit[index])
    index -= 1
print(fruit, '==reverse==>', reversed_fruit)

# 3. Go to the data folder and use the countries_data.json file.
#   i. What are the total number of languages in the data
counted_language = set()
count = 0
for country in countries_data:
    for language in country["languages"]:
        if language in counted_language:
            continue
        else:
            counted_language.add(language)
            count += 1
print('Total languages:', count)

#   ii. Find the 10 most spoken languages from the data
# https://github.com/KataTNT/30-Days-Of-Python-Challenge/blob/main/11_functions_excercises.py#L392

#   iii. Find the 10 most populated countries in the world
# https://github.com/KataTNT/30-Days-Of-Python-Challenge/blob/main/11_functions_excercises.py#L411