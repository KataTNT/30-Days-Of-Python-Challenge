'''
Project: 30 Days Of Python challenge
Author (Original): Asabeneh Yetayeh (https://github.com/Asabeneh/30-Days-Of-Python)
Day: 22 - Web Scraping (https://github.com/Asabeneh/30-Days-Of-Python/blob/master/22_Day_Web_scraping/22_web_scraping.md)
Challenger: KataTNT
'''

import requests
from bs4 import BeautifulSoup
from pathlib import Path
import json
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

## Exercises:
# 1. Scrape the following website and store the data as json file(url = 'http://www.bu.edu/president/boston-university-facts-stats/').
def scrape_bu_stats(url: str, output_path: Path) -> None:
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    try:
        with requests.Session() as session:
            response = session.get(url, headers=headers, timeout=10)
            response.raise_for_status()
    except requests.exceptions.RequestException as e:
        logger.error(f"Failed to fetch URL: {e}")
        return
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, "html.parser")
    stats_content = soup.find("div", class_="facts-stats-content")

    if not stats_content:
        logger.error("Could not find 'facts-stats-content' container on the page.")
        return
    
    data = {}
    groups = [group.get_text(strip=True) for group in stats_content.find_all("h4", class_="stat-group-title")]
    for section in stats_content.find_all("section", class_="stat-section"):
        title_tag = section.find("h4", class_="stat-group-title")
        if not title_tag:
            continue
        group = title_tag.get_text(strip=True)
        groups.remove(group)

        data[group] = {}

        for item in section.find_all("li"):
            label_tag = item.find("span", class_="stat-label")
            figure_tag = item.find("span", class_="stat-figure")
            if label_tag and figure_tag:
                label = label_tag.get_text(strip=True)
                figure = figure_tag.get_text(strip=True)
                data[group][label] = figure

    stat_lists = stats_content.find_all("div", class_="bu-stat-list")
    for index, stat_list in enumerate(stat_lists):
        data[groups[index]] = {}

        for article in stat_list.find_all("article", class_="bu-stat-single"):
            title_tag = article.find("h3", class_="bu-stat-title")
            value_tag = article.find("span", class_="bu-stat-value-field")
            if title_tag and value_tag:
                title = title_tag.get_text(strip=True)
                value = value_tag.get_text(strip=True)
                data[groups[index]][title] = value

    output_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        with open(output_path, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        logger.info(f"Data successfully saved to {output_path}")
    except IOError as e:
        logger.error(f"Failed to write JSON file: {e}")

BU_URL = "http://www.bu.edu/president/boston-university-facts-stats/"
OUTPUT_FILE = Path('./output/bu-edu.json')
scrape_bu_stats(BU_URL, OUTPUT_FILE)