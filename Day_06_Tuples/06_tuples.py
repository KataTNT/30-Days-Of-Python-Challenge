"""
Project: 30 Days Of Python challenge
Author (Original): Asabeneh Yetayeh (https://github.com/Asabeneh/30-Days-Of-Python)
Day: 06 - Tuples (https://github.com/Asabeneh/30-Days-Of-Python/blob/master/06_Day_Tuples/06_tuples.md)
Challenger: KataTNT
"""

## Exercises: Level 1
# 1. Create an empty tuple
empty = ()

# 2. Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
brothers = ("Kunkka", "Rikimaru", "Kardel", "Tiny")
sisters = ("Shendelzare", "Traxex", "Luna", "Lina", "Alleria", "Lanaya")

# 3. Join brothers and sisters tuples and assign it to siblings
siblings = brothers + sisters

# 4. How many siblings do you have?
print(f"I have {len(siblings)} siblings.")

# 5. Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family_members = siblings + ("Kael", "Rylai")
print("Family members:", family_members)

## Exercises: Level 2
# 1. Unpack siblings and parents from family_members
parents, siblings = family_members[-2:], family_members[:-2]
print("Parents:", parents)
print("Siblings:", siblings)

# 2. Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ("banana", "orange", "mango", "lemon")
vegetables = ("tomato", "pottato", "cabbage", "onion", "carrot")
animal_products = ("milk", "egg", "beef", "pork")
food_stuff_tp = fruits + vegetables + animal_products

# 3. Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
print("food_stuff_lt 's type:", type(food_stuff_lt))

# 4. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
print("Middle item from food_stuff_tp:", food_stuff_tp[len(food_stuff_lt) // 2])
print("Middle item from food_stuff_lt:", food_stuff_lt[len(food_stuff_lt) // 2])

# 5. Slice out the first three items and the last three items from food_stuff_lt list
print(f"First 3 items from food_stuff_lt: {food_stuff_lt[:3]}\nLast 3 items from food_stuff_lt: {food_stuff_lt[-3:]}")

# 6. Delete the food_stuff_tp tuple completely
del food_stuff_tp

# 7. Check if an item exists in tuple:
nordic_countries = ("Denmark", "Finland","Iceland", "Norway", "Sweden")

# Check if 'Estonia' is a nordic country
print("'Estonia' is a nordic country:", "Estonia" in nordic_countries)

# Check if 'Iceland' is a nordic country
print("'Iceland' is a nordic country:", "Iceland" in nordic_countries)