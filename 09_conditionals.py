"""
Project: 30 Days Of Python challenge
Author (Original): Asabeneh Yetayeh (https://github.com/Asabeneh/30-Days-Of-Python)
Day: 9 - Conditionals (https://github.com/Asabeneh/30-Days-Of-Python/blob/master/09_Day_Conditionals/09_conditionals.md)
Challenger: KataTNT
"""

## Exercises: Level 1
# 1. Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years.
your_age = int(input('Enter your age: '))

if your_age >= 18:
    print('You are old enough to learn to drive.')
else:
    print(f'You need {18 - your_age} more years to learn to drive.')

# 2. Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input.
# You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age.
my_age = 32
age_gap = your_age - my_age

if age_gap == 0:
    print('You are the same age as me.')
elif age_gap == 1:
    print('You are 1 year older than me.')
elif age_gap == -1:
    print('You are 1 year younger than me.')
elif age_gap > 1:
    print(f'You are {abs(age_gap)} years older than me.')
else:
    print(f'You are {abs(age_gap)} years younger than me.')

# 3. Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:
a = int(input('Enter number one: '))
b = int(input('Enter number two: '))

if a > b:
    print(f'{a} is greater than {b}.')
elif a == b:
    print(f'{a} is equal {b}.')
else:
    print(f'{a} is less than {b}.')

## Exercises: Level 2
# 1. Write a code which gives grade to students according to theirs scores:
score = int(input('Enter your score: '))
if score >= 90 and score <= 100:
    print('Grade A')
elif score >= 80:
    print('Grade B')
elif score >= 70:
    print('Grade C')
elif score >= 60:
    print('Grade D')
else:
    print('Grade F')

# 2. Get the month from user input then check if the season is Autumn, Winter, Spring or Summer. 
# If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring. June, July or August, the season is Summer.
month = input('Enter the month: ')
if month in ['September', 'October', 'November']:
    print('Autumn')
elif month in ['December', 'January', 'February']:
    print('Winter')
elif month in ['March', 'April', 'May']:
    print('Spring')
elif month in ['June', 'July', 'August']:
    print('Summer')
else:
    print(f'Month {month} is invalid.')

# 3. The following list contains some fruits. If a fruit doesn't exist in the list, add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list').
fruits = ['banana', 'orange', 'mango', 'lemon']

new_fruit = input('Enter a new fruit: ')
if new_fruit in fruits:
    print('That fruit already exist in the list.')
else:
    fruits.append(new_fruit)
    print(fruits)

## Exercises: Level 3
# Here we have a person dictionary. Feel free to modify it!
person = {
    'first_name': 'Triet',
    'last_name': 'Thai',
    'age': 32,
    'country': 'Viet Nam',
    'is_married': True,
    'skills': ['CI/CD', 'Docker', 'IaC', 'Kubernetes', 'Python', 'MongoDB', 'PostgreSQL'],
    'address': {
        'city': 'Ho Chi Minh City',
        'zipcode': '70000'
    }
}

# 1. Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
if 'skills' in person.keys():
    print(person["skills"][len(person["skills"])//2])

    # 2. Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
    if 'Python' in person["skills"]:
        print(True)

# 3. If a person skills has only JavaScript and React, print('He is a front end developer'), 
#    if the person skills has Node, Python, MongoDB, print('He is a backend developer'), 
#    if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), 
#    else print('unknown title') - for more accurate results more conditions can be nested!
available_skills = set(person["skills"])
frontend_skills = {'JavaScript', 'React'}
backend_skills = {'Node', 'Python', 'MongoDB'}
fullstack_skills = {'React', 'Node', 'MongoDB'}

if frontend_skills == available_skills:
    print('This person is a front end developer.')
elif backend_skills.issubset(available_skills):
    print('This person is a backend developer.')
elif fullstack_skills.issubset(available_skills):
    print('This person is a fullstack developer.')
else:
    print('Unknown title.')

# 4. If the person is married and if he lives in Finland, print the information in the following format
if person["is_married"] and person["country"] == 'Finland':
    print(f'{person["first_name"]} {person["last_name"]} lives in Finland and is married.')
else:
    print(f'{person["first_name"]} {person["last_name"]} lives in {person["country"]} and is married.')