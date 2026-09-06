"""
Project: 30 Days Of Python challenge
Author (Original): Asabeneh Yetayeh (https://github.com/Asabeneh/30-Days-Of-Python)
Day: 20 - PIP (https://github.com/Asabeneh/30-Days-Of-Python/blob/master/20_Day_Python_package_manager/20_python_package_manager.md
Challenger: KataTNT
"""

import os
from dotenv import load_dotenv
import requests
import statistics as stats
import json

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

# ii. Find the min, max, mean, median, standard deviation of cats" weight in metric units.
# iii. Find the min, max, mean, median, standard deviation of cats" lifespan in years.
def calculate_cat_statistics(cats_data: dict, type: str):
    if type not in ["life_span", "weight.metric", "height.metric"]:
        print("Invalid type!")
        return
    elements = []
    for cat in cats_data:
        try:
            if "." not in type:
                e_parts = cat[type].split("-")
                e_min, e_max = map(int, e_parts)
                elements.extend([e_min, e_max])
            elif len(type.split(".")) == 2:
                parent_path, child_path = type.split(".")
                if isinstance(cat[parent_path], dict) and len(cat[parent_path]) == 2:
                    e_parts = cat[parent_path][child_path].split("-")
                    e_min, e_max = map(float, e_parts)
                    elements.extend([e_min, e_max])
        except (ValueError, AttributeError):
            pass
    element_stats = {
        "min": min(elements),
        "max": max(elements),
        "mean": stats.mean(elements),
        "median": stats.median(elements),
        "standard deviation": round(stats.stdev(elements), 3)
    }
    print(f"- {type} stats:", element_stats)

# Direct call API
#first_cat = get_cat_breeds_data()[0]
#print(first_cat)

# Save response as a JSON file for rate limiting
FILE_PATH = "data/cat_breeds.json"
if not os.path.isfile(FILE_PATH):
    print("File does not exists. Creating file ...")
    get_cat_breeds_data(output_file=FILE_PATH)
else:
    print(f"File '{FILE_PATH}' already exists.")

with open(FILE_PATH, "r", encoding="utf-8") as file:
    print(f"\nLoading data from file '{FILE_PATH}'.")
    cat_breeds_data = json.load(file)

calculate_cat_statistics(cat_breeds_data, "weight.metric")
calculate_cat_statistics(cat_breeds_data, "life_span")

# iii. Create a frequency table of country and breed of cats