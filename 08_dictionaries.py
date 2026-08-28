'''
Project: 30 Days Of Python challenge
Author (Original): Asabeneh Yetayeh (https://github.com/Asabeneh/30-Days-Of-Python)
Day: 08 - Dictionaries (https://github.com/Asabeneh/30-Days-Of-Python/blob/master/08_Day_Dictionaries/08_dictionaries.md)
Challenger: KataTNT
'''

## Excercises:
# 1. Create an empty dictionary called dog
dog = {}

# 2. Add name, color, breed, legs, age to the dog dictionary
dog['name'] = 'Fat'
dog['color'] = 'Black and White'
dog['breed'] = 'Phu Quoc Ridgeback'
dog['legs'] = 4
dog['age'] = 5

print(dog)

# 3. Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {
    'first_name': 'Ken',
    'last_name': 'Kaneki',
    'gender': 'Man',
    'age': 18,
    'is_married': False,
    'skills': ['Reading'],
    'country': 'Japan',
    'city': 'Tokyo',
    'address': 'District 20'
}

# 4. Get the length of the student dictionary
print(len(student))

# 5. Get the value of skills and check the data type, it should be a list
print(type(student['skills']))

# 6. Modify the skills values by adding one or two skills
student['skills'].append('Pain Tolerance')

print(student['skills'])

# 7. Get the dictionary keys as a list
print(list(student.keys()))

# 8. Get the dictionary values as a list
print(list(student.values()))

# 9. Change the dictionary to a list of tuples using items() method
print(list(student.items()))

# 10. Delete one of the items in the dictionary
student.pop('address')
print(student)

# 11. Delete one of the dictionaries
student.clear()
print(student)