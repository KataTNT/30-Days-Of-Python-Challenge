"""
Project: 30 Days Of Python challenge
Author (Original): Asabeneh Yetayeh (https://github.com/Asabeneh/30-Days-Of-Python)
Day: 20 - PIP (https://github.com/Asabeneh/30-Days-Of-Python/blob/master/20_Day_Python_package_manager/20_python_package_manager.md)
Challenger: KataTNT
"""

import os
from dotenv import load_dotenv
import requests
import statistics as stats
import json
from pprint import pprint
from bs4 import BeautifulSoup
import re

## Exercises:
# 2. Read the cats API and cats_api = "https://api.thecatapi.com/v1/breeds":
def get_cat_breeds_data(output_file=None):
    load_dotenv()
    api_key = os.getenv("THECATAPI_KEY")
    url = "https://api.thecatapi.com/v1/breeds"
    
    headers = {
        "x-api-key": api_key
    }

    try:
        with requests.Session() as session:
            response = session.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            content = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch URL: {e}")
        return

    if output_file:
        try:
            with open(output_file, "w", encoding="utf-8") as file:
                json.dump(content, file, ensure_ascii=False, indent=4)
                print(f"Data successfully saved to '{output_file}'.")
        except IOError as e:
            print(f"Failed to write JSON file: {e}")
    else:
        return content

# Direct call API
#first_cat = get_cat_breeds_data()[0]
#print(first_cat)

# Save response as a JSON file for rate limiting
FILE_PATH = "output/cat_breeds.json"
if not os.path.isfile(FILE_PATH):
    print("File does not exists. Creating file ...")
    get_cat_breeds_data(output_file=FILE_PATH)
else:
    print(f"File '{FILE_PATH}' already exists.")

# ii. Find the min, max, mean, median, standard deviation of cats" weight in metric units.
# iii. Find the min, max, mean, median, standard deviation of cats" lifespan in years.
def calculate_cat_statistics(cat_breeds_data: dict, property: str):
    if property not in ["life_span", "weight.metric", "height.metric"]:
        print("Invalid property!")
        return
    properties = []
    for breed in cat_breeds_data:
        try:
            if "." not in property:
                e_parts = breed[property].split("-")
                e_min, e_max = map(int, e_parts)
                properties.extend([e_min, e_max])
            elif len(property.split(".")) == 2:
                parent_path, child_path = property.split(".")
                if isinstance(breed[parent_path], dict) and len(breed[parent_path]) == 2:
                    e_parts = breed[parent_path][child_path].split("-")
                    e_min, e_max = map(float, e_parts)
                    properties.extend([e_min, e_max])
        except (ValueError, AttributeError):
            pass
    property_stats = {
        "min": min(properties),
        "max": max(properties),
        "mean": stats.mean(properties),
        "median": stats.median(properties),
        "standard deviation": round(stats.stdev(properties), 3)
    }
    print(f"- {property} stats:", property_stats)

# Loading data from JSON file
with open(FILE_PATH, "r", encoding="utf-8") as file:
    print(f"\nLoading data from file '{FILE_PATH}'.")
    cat_breeds_data = json.load(file)

calculate_cat_statistics(cat_breeds_data, "weight.metric")
calculate_cat_statistics(cat_breeds_data, "life_span")

# iii. Create a frequency table of country and breed of cats
def cat_breeds_freq_dist(cat_breeds_data: dict, property: str):
    count_table = {}
    for breed in cat_breeds_data:
        if breed[property] not in count_table:
            count_table[breed[property]] = 1
        else:
            count_table[breed[property]] += 1
    result = []
    cat_breeds_count = len(cat_breeds_data)
    for k, v in count_table.items():
        result.append((k, round(v / cat_breeds_count * 100, 2)))
    result.sort(key=lambda x: x[1], reverse=True)
    return result

print("\nFrequency table of country of cats:")
pprint(cat_breeds_freq_dist(cat_breeds_data, "country_code"))
print("\nFrequency table of breed of cats:")
pprint(cat_breeds_freq_dist(cat_breeds_data, "breed_group"))

# 4. UCI is one of the most common places to get data sets for data science and machine learning. 
# Read the content of UCL (https://archive.ics.uci.edu/ml/datasets.php). Without additional libraries it will be difficult, so you may try it with BeautifulSoup4
def get_data_uci(output_file=None, data_take=None):
    if data_take is None:
        url = "https://archive.ics.uci.edu/ml/datasets"
    else:
        url = "https://archive.ics.uci.edu/datasets?skip=0&take=" + str(data_take)

    headers = {
        "User-Agent": "ScrapeBot/1.0 (https://github.com/KataTNT/30-Days-Of-Python-Challenge; tnt.kata1894@gmail.com) python-requests/2.34.2"
    }

    try:
        with requests.Session() as session:
            response = session.get(url, headers=headers, timeout=10)
            response.raise_for_status()
        content = response.content
        soup = BeautifulSoup(content, "html.parser")
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch URL: {e}")
        return

    data = []
    section = soup.select_one(".flex .flex-col .gap-1")
    rows = section.find_all("div", attrs={"role": "row"})
    for index, row in enumerate(rows):
        title = row.find("h2", class_="text-primary").getText(strip=True)
        description = row.find("p", class_="mr-8").getText(strip=True)
        properties = row.find_all("span", class_="truncate")
        tasks, ds_chars, instances, features = [ 
            re.sub(r"<.*?>", "", str(item)).strip() for item in properties
        ]
        
        tasks = [task.strip(',') for task in tasks.split()]
        ds_chars = [ds_char.strip(',') for ds_char in ds_chars.split()]
        instances = instances[:-10]
        features = features[:-9]

        data.append({
            "Dataset Title": title,
            "Overview": {
                "Description": description,
                "Associated Tasks": tasks,
                "Dataset Characteristics": ds_chars,
                "Instances": instances,
                "Features": features
            }
        })

    if output_file:
        try:
            with open(output_file, "w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
                print(f"Data successfully saved to '{output_file}'.")
        except IOError as e:
            print(f"Failed to write JSON file: {e}")
    else:
        return data

get_data_uci(output_file="output/uci-dataset.json", data_take=50)