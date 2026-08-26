###
# Project: 30 Days Of Python challenge
# Author (Original): Asabeneh Yetayeh (https://github.com/Asabeneh/30-Days-Of-Python)
# Day: 2 - Variables, Builtin Functions (https://github.com/Asabeneh/30-Days-Of-Python/blob/master/02_Day_Variables_builtin_functions/02_variables_builtin_functions.md)
# Challenger: KataTNT
###

# Excercise 1
# Day 2: 30 Days of python programming'
first_name = "Triet"
last_name = "Thai"
full_name = first_name + " " + last_name
country = "Viet Nam"
city = "Ho Chi Minh City"
age = "32"
year = "2026"
is_married = True
is_true = True
is_light_on = False
job_expertise, level = "DevOps", "Senior"

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(job_expertise))
print(type(level))

print(len(first_name))
print(max(len(first_name),len(last_name)))

# Excercise 2
num_one = 5
num_two = 4
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two
exp = num_one ** num_two
floor_division = num_one // num_two

print(f'num_one = {num_one}\nnum_two = {num_two}')
print(f'total = {total}\ndiff = {diff}\nproduct = {product}\ndivision = {division}\nremainder = {remainder}\nexp = {exp}\nfloor_division = {floor_division}')

import math
radius = 30
area_of_circle = radius * radius * math.pi
circum_of_circle = 2 * radius * math.pi
print('Area = ', area_of_circle)
print('Circumference = ', circum_of_circle)

radius = float(input("Input radius:"))
area_of_circle = radius * radius * math.pi
print('Area of circle = ', area_of_circle)

first_name = input("Fill first name:")
last_name = input("Fill last name:")
country = input("Fill country:")
age  = input("Fill age:")

print(first_name, last_name, country, age)