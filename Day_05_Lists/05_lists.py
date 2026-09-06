'''
Project: 30 Days Of Python challenge
Author (Original): Asabeneh Yetayeh (https://github.com/Asabeneh/30-Days-Of-Python)
Day: 05 - Lists (https://github.com/Asabeneh/30-Days-Of-Python/blob/master/05_Day_Lists/05_lists.md)
Challenger: KataTNT
'''

## Exercises: Level 1
# 1. Declare an empty list
empty = []

# 2. Declare a list with more than 5 items
numbers = [1, 2, 3, 4, 5]

# 3. Find the length of your list
print('Length of list:', len(numbers))

# 4. Get the first item, the middle item and the last item of the list
print(f'First item: {numbers[0]}, Middle item: {numbers[len(numbers) // 2]}, Last item: {numbers[-1]}')

# 5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ['Ken', 18, 170, True, 'Tokyo, Japan']

# 6. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# 7. Print the list using print()
print(it_companies)

# 8. Print the number of companies in the list
print('Number of companies:', len(it_companies))

# 9. Print the first, middle and last company
print(f'First company: {it_companies[0]}, Middle company: {it_companies[len(it_companies) // 2]}, Last company: {it_companies[-1]}')

# 10. Print the list after modifying one of the companies
it_companies[1] = 'Google LLC'
print(it_companies)

# 11. Add an IT company to it_companies
it_companies.append('FPT')

# 12. Insert an IT company in the middle of the companies list
it_companies.insert(len(it_companies) // 2, 'Viettel')

# 13. Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[1] = it_companies[1].upper()

# 14. Join the it_companies with a string '#;  '
print('#;  '.join(it_companies))

# 15. Check if a certain company exists in the it_companies list.
print('GOOGLE' in it_companies)

# 16. Sort the list using sort() method
it_companies.sort()

# 17. Reverse the list in descending order using reverse() method
it_companies.reverse()

# 18. Slice out the first 3 companies from the list
print(it_companies[:3])

# 19. Slice out the last 3 companies from the list
print(it_companies[-3:])

# 20. Slice out the middle IT company or companies from the list
print(it_companies[len(it_companies) // 2])

# 21. Remove the first IT company from the list
it_companies.pop(0)

# 22. Remove the middle IT company or companies from the list
it_companies.pop(len(it_companies) // 2)

# 23. Remove the last IT company from the list
it_companies.pop(-1)

# 24. Remove all IT companies from the list
it_companies.clear

# 25. Destroy the IT companies list
del it_companies

# 26. Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
fe_joined_be = front_end + back_end
print(fe_joined_be)

# 27. After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.
full_stack = fe_joined_be.copy()
insert_index = full_stack.index('Redux') + 1
full_stack[insert_index:insert_index] = ['Python', 'SQL'] 
print(full_stack)

## Exercises: Level 2
# 1. The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# - Sort the list and find the min and max age
ages.sort()
min_age, max_age = ages[0], ages[-1]
print(f'Min: {min_age}\nMax: {max_age}')

# - Add the min age and the max age again to the list
ages.extend([min_age, max_age])
print(ages)

# - Find the median age (one middle item or two middle items divided by two)
ages.sort()
ages_count = len(ages)
middle_index = ages_count // 2
if ages_count % 2 == 0:
    median_age = (ages[middle_index - 1] + ages[middle_index]) / 2
else:
    median_age = ages[middle_index]
print(f'Median: {median_age}')

# - Find the average age (sum of all items divided by their number )
average_age = sum(ages) / ages_count
print(f'Average: {average_age}')

# - Find the range of the ages (max minus min)
print('Range:', max(ages) - min(ages))

# - Compare the value of (min - average) and (max - average), use abs() method
print('(min - average) <= (max - average):', abs(min(ages) - average_age) <= abs(max(ages) - average_age))

# 2. Find the middle country(ies) in the countries list
countries = [ 'Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cabo Verde', 'Cambodia', 'Cameroon', 'Canada', 'Central African Republic', 'Chad', 'Chile', 'China', 'Colombia', 'Comoros', 'Congo, Democratic Republic of the', 'Congo, Republic of the', 'Costa Rica', "Côte d'Ivoire", 'Croatia', 'Cuba', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'East Timor (Timor-Leste)', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Eswatini', 'Ethiopia', 'Fiji', 'Finland', 'France', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Greece', 'Grenada', 'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Korea, North', 'Korea, South', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Mauritania', 'Mauritius', 'Mexico', 'Micronesia', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'North Macedonia', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Palestine', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar', 'Romania', 'Russia', 'Rwanda', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Vincent and the Grenadines', 'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'South Sudan', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Sweden', 'Switzerland', 'Syria', 'Tajikistan', 'Tanzania', 'Thailand', 'Togo', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Vatican City', 'Venezuela', 'Vietnam', 'Yemen', 'Zambia', 'Zimbabwe']
countries_count = len(countries)
middle_index = countries_count // 2
print('Middle country:', countries[middle_index])

# 3. Divide the countries list into two equal lists if it is even if not one more country for the first half.
first_half, second_half = [], []
if countries_count % 2 == 0:
    first_half, second_half = countries[:middle_index], countries[middle_index:]
else:
    first_half, second_half = countries[:middle_index + 1], countries[middle_index + 1:]
print(f'First half: {len(first_half)}\nSecond half: {len(second_half)}')

# 4. ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
first_country, second_country, third_country, *rest = countries
print(f'1st country: {first_country}\n2nd country: {second_country}\n3rd country: {third_country}\nRemaining country: {rest}')