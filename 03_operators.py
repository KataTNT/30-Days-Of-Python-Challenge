'''
Project: 30 Days Of Python challenge
Author (Original): Asabeneh Yetayeh (https://github.com/Asabeneh/30-Days-Of-Python)
Day: 03 - Operators (https://github.com/Asabeneh/30-Days-Of-Python/blob/master/03_Day_Operators/03_operators.md)
Challenger: KataTNT
'''

## Exercises
# 1. Declare your age as integer variable
age = 32

# 2. Declare your height as a float variable
height = 1.79

# 3. Declare a variable that store a complex number
z = 1 + 1j
print(z)
print(type(z))

# 4. Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
base = int(input('Enter base: '))
height = int(input('Enter height: '))
area_triangle = 0.5 * base * height
print(' The area of the triangle is', area_triangle)

# 5. Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
a = int(input('Enter side a: '))
b = int(input('Enter side b: '))
c = int(input('Enter side c: '))
perimeter_triangle = a + b + c
print('The perimeter of the triangle is', perimeter_triangle)

# 6. Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
length = int(input('Enter length: '))
width = int(input('Enter width: '))
area_rectangle = length * width
perimeter_rectangle = 2 * (length + width)
print('The area of the rectangle is', area_rectangle)
print('The perimeter of the rectangle is', perimeter_rectangle)

# 7. Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
radius = int(input('Enter radius: '))
pi = 3.14
area_circle = pi * radius * radius
circumference = 2 * pi * radius
print('The area of the circle is', area_circle)
print('The circumference of the circle is', circumference)

# 8. Calculate the slope, x-intercept and y-intercept of y = 2x -2

# 9. Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)

# 10. Compare the slopes in tasks 8 and 9.

# 11. Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.

# 12. Find the length of 'python' and 'dragon' and make a falsy comparison statement.
print('12 =>', len('python') > 6 and len('dragon') > 6 )

# 13. Use and operator to check if 'on' is found in both 'python' and 'dragon'
print('13 =>', 'on' in 'dragon' and 'on' in 'python')

# 14. I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence
print('14 =>', 'jargon' in 'I hope this course is not full of jargon')

# 15. There is no 'on' in both dragon and python
print('15 =>', 'on' not in 'dragon' and 'on' not in 'python')

# 16. Find the length of the text python and convert the value to float and convert it to string
print('16 =>', str(float(len('python'))))

# 17. Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
print("17 => 'x % 2 == 0'")

# 18. Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
print('18 =>', 7 // 3 == int(2.7))

# 19. Check if type of '10' is equal to type of 10
print('19 =>', type('10') == type(10))

# 20. Check if int('9.8') is equal to 10
# print(int('9.8') == 10) => ValueError: invalid literal for int() with base 10: '9.8'
print('20 =>', int(9.8) == 10)

# 21. Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hours = int(input('Enter hours: '))
rate_per_hour = int(input('Enter rate per hour: '))
print('Your weekly earning is', hours * rate_per_hour)

# 22. Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
live_years = int(input('Enter number of years you have lived: '))
second_can_lives = 60 * 60 * 24 * (365 * live_years)
print(f'You have lived for {second_can_lives} seconds.')

# 23. Write a Python script that displays the following table
print(1, 1 ** 0, 1 ** 1, 1 ** 2, 1 ** 3)
print(2, 2 ** 0, 2 ** 1, 2 ** 2, 2 ** 3)
print(3, 3 ** 0, 3 ** 1, 3 ** 2, 3 ** 3)
print(4, 4 ** 0, 4 ** 1, 4 ** 2, 4 ** 3)
print(5, 5 ** 0, 5 ** 1, 5 ** 2, 5 ** 3)