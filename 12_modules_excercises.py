"""
Project: 30 Days Of Python challenge
Author (Original): Asabeneh Yetayeh (https://github.com/Asabeneh/30-Days-Of-Python)
Day: 13 - List Comprehension (https://github.com/Asabeneh/30-Days-Of-Python/blob/master/12_Day_Modules/12_modules.md)
Challenger: KataTNT
"""

from random import randint
from string import ascii_letters, digits
# Excercise: Level 1
# 1. Write a function which generates a six digit/character random_user_id.
def random_user_id():
    user_id = ''
    for i in range(6):
        if randint(0, 1) == 0:
            digit_index = randint(0, 9)
            user_id += digits[digit_index]
        else:
            char_index = randint(0, 25)
            user_id += ascii_letters[char_index]
    return user_id

print(random_user_id())

# 2. Modify the previous task. Declare a function named user_id_gen_by_user. 
# It doesn’t take any parameters but it takes two inputs using input(). 
# One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.
def user_id_gen_by_user():
    num_char = int(input('Number of characters: '))
    num_id = int(input('Number of IDs: '))
    user_ids = []
    for x in range(num_id):
        user_id = ''
        for i in range(num_char):
            if randint(0, 1) == 0:
                digit_index = randint(0, 9)
                user_id += digits[digit_index]
            else:
                char_index = randint(0, 25)
                user_id += ascii_letters[char_index]
        user_ids.append(user_id)
    return user_ids

for uid in user_id_gen_by_user():
    print(uid)

# 3. Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
def rgb_color_gen():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return f'rgb({r},{g},{b})'

print(rgb_color_gen())

## Excercise: Level 2
# 1. Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. 
# Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).
def list_of_hexa_colors(number: int):
    hexa_colors = []
    alphabet_1st6 = ascii_letters[:6]
    for n in range(number):
        hexa_color = '#'
        for char in range(6):
            if randint(0, 1) == 0:
                digit_index = randint(0, 9)
                hexa_color += digits[digit_index]
            else:
                char_index = randint(0, 5)
                hexa_color += alphabet_1st6[char_index]
        hexa_colors.append(hexa_color)
    return hexa_colors

print(list_of_hexa_colors(5))

# 2. Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
def list_of_rgb_colors(number: int):
    rgb_colors = []
    for n in range(number):
        rgb_colors.append(rgb_color_gen())
    return rgb_colors

print(list_of_rgb_colors(3))

# 3. Write a function generate_colors which can generate any number of hexa or rgb colors.
def generate_colors(color_format, number):
    if color_format == 'hexa':
        return list_of_hexa_colors(number)
    elif color_format == 'rgb':
        return list_of_rgb_colors(number)

print(generate_colors('hexa', 3))
print(generate_colors('rgb', 5))

## Exercises: Level 3
# 1. Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list.
def shuffle_list(list: list):
    shuffled_list = []
    for item in list:
        shuffled_list.insert(randint(0, len(shuffled_list)), item)
    return shuffled_list

alphabet_list = list(ascii_letters[:25])
print(alphabet_list)

alphabet_shuffled_list = shuffle_list(alphabet_list)
print(alphabet_shuffled_list)
# 2. Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.
def random_unique_7_numbers():
    numbers = []
    index = 0
    while index < 7:
        number = randint(0, 9)
        if number not in numbers:
            numbers.append(number)
            index += 1
    return numbers

print(random_unique_7_numbers())