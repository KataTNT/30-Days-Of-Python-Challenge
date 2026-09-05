"""
Project: 30 Days Of Python challenge
Author (Original): Asabeneh Yetayeh (https://github.com/Asabeneh/30-Days-Of-Python)
Day: 25 - Pandas (https://github.com/Asabeneh/30-Days-Of-Python/blob/master/25_Day_Pandas/25_pandas.md)
Challenger: KataTNT
"""

import pandas as pd
# 1. Read the hacker_news.csv file from data directory
df = pd.read_csv("data/hacker_news.csv")

# 2. Get the first five rows
print("\n--- First 5 rows:")
print(df.head())

# 3. Get the last five rows
print("\n--- Last 5 rows:")
print(df.tail())

# 4. Get the title column as pandas series
print("\n--- Get the title column as pandas series")
title = df["title"]
print(title)

# 5. Count the number of rows and columns
rows, columns = df.shape
print(f"\n--- Rows: {rows}, Columes: {columns}")

# - Filter the titles which contain python
print("\n--- Titles contain 'python'")
filtered_title_by_python = title[title.str.contains("python")]
print(filtered_title_by_python)

# - Filter the titles which contain JavaScript
print("\n--- Titles contain 'JavaScript'")
filtered_title_by_js = title[title.str.contains("JavaScript")]
print(filtered_title_by_js)

# - Explore the data and make sense of it
print("\n--- Top authors:")
print(df["author"].value_counts().head())
