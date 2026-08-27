"""
Project: 30 Days Of Python challenge
Author (Original): Asabeneh Yetayeh (https://github.com/Asabeneh/30-Days-Of-Python)
Day: 11 - Functions (https://github.com/Asabeneh/30-Days-Of-Python/blob/master/11_Day_Functions/11_functions.md)
Challenger: KataTNT
"""

## Exercises: Level 1
# 1. Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add_two_numbers(n1: int | float, n2: int | float):
    return n1 + n2

print(add_two_numbers(1.6, 5))

# 2. Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
from math import pi
def area_of_circle(r):
    area = r * r * pi
    return area

print(area_of_circle(2))

# 3. Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
def add_all_nums(*nums):
    total = 0
    for num in nums:
        if not isinstance(num, (int, float)):
            print(f"Argument '{num}' must be number type.")
            return
        else:
            total += num
    return total 

print(add_all_nums('hello', 2))
print(add_all_nums(3, 5, 6, 7, 1))

# 4. Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to_fahrenheit.
def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

print(convert_celsius_to_fahrenheit(30))

# 5. Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
# Note: At Southern Hemisphere
def check_season(month: int):
    if month in [9, 10, 11]:
        return 'Spring'
    elif month in [12, 1, 2]:
        return 'Summer'
    elif month in [3, 4, 5]:
        return 'Autumn'
    elif month in [6, 7, 8]:
        return 'Winter'
    else:
        print(f'Month {month} is invalid.')
        return

print(check_season(3))

# 6. Write a function called calculate_slope which return the slope of a linear equation
def calculate_slope():
    return 

# 7. Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
from math import sqrt
def solve_quadratic_eqn(a, b, c):
    delta = b * b - 4 * a * c
    if delta < 0:
        print('The equation has no solution.')
    elif delta == 0:
        x = -b / 2 * a
        print(f'The equation has a double root.\nx = {x}')

    else:
        x1 = -b + sqrt(delta) / 2 * a
        x2 = -b - sqrt(delta) / 2 * a
        print(f'The equation has two distinct roots.\nx1 = {x1}\nx2 = {x2}')

solve_quadratic_eqn(2, 3, 1)

# 8. Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
def print_list(array: list):
    for element in array:
        print(element)

print(print_list([1, 2, 3]))

# 9. Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
def reverse_list(array: list):
    reversed_list = []
    index = len(array)-1
    while index >= 0:
        reversed_list.append(list[index])
        index -= 1
    return reversed_list

print(reverse_list([1, 2, 3, 4, 5]))
print(reverse_list(["A", "B", "C"])) 

# 10. Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
def capitalize_list_items(array: list):
    capitalized_list = []
    for element in array:
        capitalized_list.append(element.title())
    return capitalized_list

print(capitalize_list_items(["ha noi", "ho chi minh", "da nang"]))

# 11. Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
def add_item(array: list, item):
    res = array
    res.append(item)
    return res

food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk'];
print(add_item(food_stuff, 'Meat'))
numbers = [2, 3, 7, 9];
print(add_item(numbers, 5))

# 12. Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
def remove_item(array: list, item):
    res = array
    res.remove(item)
    return res

food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_stuff, 'Mango'))
numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))

# 13. Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
def sum_of_numbers(number):
    total = 0
    for n in range(number + 1):
        total += n
    return total 

print(sum_of_numbers(5))
print(sum_of_numbers(10))
print(sum_of_numbers(100))

# 14. Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
def sum_of_odds(number):
    total = 0
    for n in range(number + 1):
        if n % 2 != 0:
            total += n
    return total 

print(sum_of_odds(5))
print(sum_of_odds(10))
print(sum_of_odds(100))

# 15. Declare a function named sum_of_evens. It takes a number parameter and it adds all the even numbers in that range.
def sum_of_evens(number):
    total = 0
    for n in range(number + 1):
        if n % 2 == 0:
            total += n
    return total 

print(sum_of_evens(5))
print(sum_of_evens(10))
print(sum_of_evens(100))

## Exercises: Level 2
# 1. Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
def evens_and_odds(number: int):
    if number <= 0:
        print('Accept only positive integer!')
        return
    else:
        odds = 0
        evens = 0
        for n in range(1, number):
            if n % 2 != 0:
                odds += 1
            else:
                evens += 1
        print('The number of odds are ', odds)
        print('The number of evens are ', evens)

evens_and_odds(100)

# 2. Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
def factorial(number: int):
    if number < 0:
        print('Accept only positive integer!')
        return
    elif number == 0:
        return 1
    else:
        res = 1
        for n in range(1, number + 1):
            res *= n
        return res

print(factorial(0))
print(factorial(5))

# 3. Call your function is_empty, it takes a parameter and it checks if it is empty or not
def is_empty(param):
    if param == '' or param is None:
        print('It is empty.')
    else:
        print('It is not empty.')

is_empty('')
is_empty('Bingo')

# 4. Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).
import statistics
# calculate_mean
def calculate_mean(array: list):
    total = 0
    for element in array:
        total += element
    return total  / len(array)

list_mean = [3, 13, 2, 34, 11, 17, 27, 47, 1]
print(list_mean, '| Mean = ', calculate_mean(list_mean), '| Mean (statstics) = ', statistics.mean(list_mean))

# calculate_median
def calculate_median(array: list):
    temp = sorted(array)
    median_index = len(temp) // 2
    if len(temp) % 2 != 0:
        return temp[median_index]
    else:
        return (temp[median_index - 1] + temp[median_index]) / 2

list_median_1 = [3, 13, 2, 34, 11, 17, 27, 47, 1]
print(list_median_1, '| Median = ', calculate_median(list_median_1), '| Median (statstics) = ', statistics.median(list_median_1))


list_median_2 = [3, 13, 2, 34, 11, 17, 27, 47, 1, 8]
print(list_median_2, '| Median = ', calculate_median(list_median_2), '| Median (statstics) = ', statistics.median(list_median_2))

# calculate_mode
def calculate_mode(array: list):
    mode = None
    count_table = {}
    for element in array:
        if not element in count_table:
            count_table[element] = 1
        else:
            count_table[element] += 1
    for element, count in count_table.items():
        if count == max(count_table.values()):
            mode = element
            return mode

list_mode = [1, 2, 3, 2, 5, 6, 3, 4, 1, 3, 2]
print(list_mode, '| Mode = ', calculate_mode(list_mode), '| Mode (statistics) = ', statistics.mode(list_mode))

# calculate_range
def calculate_range(array: list):
    sorted_array = sorted(array)
    return max(sorted_array) - min(sorted_array)

list_range = [5, 8, 2, 4, 3, 10]
print(list_range, '| Range =', calculate_range(list_range))
# calculate_variance
def calculate_variance(array: list):
    mean = calculate_mean(array)
    x = {}
    for xi in array:
        x[xi] = (xi - mean) ** 2
    total = 0
    for i, ss in x.items():
        total += ss
    return total / (len(array) - 1)

list_variance = [10, 34, 23, 54, 9]
print(list_variance, '| Variance =', calculate_variance(list_variance), '| Variance (statistics) =', statistics.variance(list_variance) )

# calculate_std
def calculate_std(array: list):
    variance = calculate_variance(array)
    return sqrt(variance)

list_standard_deviation = [5, 8, 2, 4, 3, 10]
print(list_standard_deviation, '| Standard Deviation = ', calculate_std(list_standard_deviation), '| Standard Deviation (statistics) = ', statistics.stdev(list_standard_deviation))

# 5. Write a function called greet which takes a default argument, name. If no argument is supplied it should print "Hello, Guest!", otherwise it should greet the person by name.
def greet(name = "Guest"):
    print(f'Hello, {name}!')

greet()
greet("Alice")

# 6. Create a function called show_args to take an arbitrary number of named arguments and print their names and values.
def show_args(**args):
    res = 'Received: '
    for name, value in args.items():
        res += f'{name}: {value}, '
    res = res[:-2]
    print(res)

show_args(name="Alice", age=30, city="New York")
show_args(name="Bob", pet="Fluffy, the bunny")

## Exercises: Level 3
# 1. Write a function called is_prime, which checks if a number is prime.
def is_prime(n: int):
    if not isinstance(n, int):
        print('Input n is not an integer!')
        return
    if n < 2:
        return False
    if n == 2:
        return True
    else:
        i = 2
        is_prime = True
        while i <= sqrt(n) + 1:
            if n % i == 0:
                is_prime = False
                break
            else:
                i += 1
        return is_prime

prime_list = []
for i in range(100):
    if is_prime(i):
        prime_list.append(i)

print(prime_list)

# 2. Write a functions which checks if all items are unique in the list.
def check_list_unique(array: list):
    temp = sorted(array)
    for i in range(len(array)):
        if i == len(array) - 1:
            return True
        if temp[i] == temp[i + 1]:
            return False
    return True

list_unique_numbers = [1, 2, 5, 8, 9, 10, 3, 6, 7, 4]
print(check_list_unique(list_unique_numbers))
            
list_not_unique = ["tokyo", "london", "paris", "new york", "paris"]
print(check_list_unique(list_not_unique))

# 3. Write a function which checks if all the items of the list are of the same data type.
def check_list_same_type(array: list):
    first_type = type(array[0])
    for i in array:
        if type(i) == first_type:
            continue
        else:
            return False
    return True

list_numbers = [1, 2, 5, 8, 9, 10, 3, 6, 7, 4]
print(list_numbers, check_list_same_type(list_numbers))

list_string = list('abcdef')
print(list_string, check_list_same_type(list_string))

list_multi_types = [1, 2, 'a', 3, 'c', ('rose', 'pink') ]
print(list_multi_types, check_list_same_type(list_multi_types))    


# 4. Write a function which check if provided variable is a valid python variable
import string
import keyword
def is_valid_var(var):
    valid_1st_char = string.ascii_letters + '_'
    valid_char = valid_1st_char + string.digits
    if var[0] not in valid_1st_char:
        return False
    for c in var:
        if c not in valid_char:
            return False
    if keyword.iskeyword(var):
        return False
    return True

print('_hello', is_valid_var('_hello'))
print('2hello', is_valid_var('2hello'))
print('hEll0_w0rld', is_valid_var('hEll0_w0rld'))
print('import', is_valid_var('import'))

# 5. Go to the data folder and access the countries-data.py file.
# - Create a function called the most_spoken_languages in the world. It should return 10 or 20 most spoken languages in the world in descending order.
import json
file = open("./data/countries-data.py", mode="r", encoding="utf-8")
countries_data = json.load(file)
def most_spoken_languages(countries_data, top_n=10):
    all_languages = []
    for country in countries_data:
        all_languages.extend(country.get("languages", []))
    all_languages_unique = set()
    for language in all_languages:
        all_languages_unique.add(language)
    languages_counted = []
    for language in all_languages_unique:
        languages_counted.append({"language": language,"countries_count": all_languages.count(language)})
    languages_counted.sort(key=lambda x: x["countries_count"], reverse=True)
    top_languages = languages_counted[:top_n]
    print(f'Top {top_n} most spoken languages:\n#\tLanguage - Countries')
    for rank, language in enumerate(top_languages, start=1):
        print(f'{rank}\t{language["language"]} - {language["countries_count"]}')
    
most_spoken_languages(countries_data)

# - Create a function called the most_populated_countries. It should return 10 or 20 most populated countries in descending order.
def most_populated_countries(countries_data, top_n=10):
    population_data = []
    for country in countries_data:
        population_data.append({"name": country["name"], "population": country["population"]})
    population_data.sort(key=lambda x: x["population"], reverse=True)
    top_countries = population_data[:top_n]
    print(f'Top {top_n} most populated countries:\n#\tCountry - Population')
    for rank, country in enumerate(top_countries, start=1):
        print(f'{rank}\t{country["name"]} - {country["population"]}')

most_populated_countries(countries_data, 20)