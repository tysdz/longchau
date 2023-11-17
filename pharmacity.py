from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import re
import json
import time
from bs4 import BeautifulSoup

driver = webdriver.Chrome()

def write_to_json(data, file_path):
    with open(file_path, "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)

data_list = []
# html_links = []
# for page_id in range(1, 179):
#     page_url = f"https://www.pharmacity.vn/duoc-pham?page={page_id}"
#     driver.get(page_url)
#     time.sleep(3)

#     max_attempts = 6 # Số lần thử tối đa
#     current_attempt = 0
#     while current_attempt < max_attempts:
#         driver.execute_script("window.scrollBy(0, 530);")
#         current_attempt += 1
#         time.sleep(1)

#     links = driver.find_elements(By.XPATH, '//a[@href]')
#     matching_links = [link.get_attribute("href") for link in links if re.match(r'https://www\.pharmacity\.vn/.+', link.get_attribute("href"))]
#     html_links.extend([link for link in matching_links if link.endswith(".html")])
#     # html_links = [link for link in matching_links if link.endswith(".html")]
#     # write_to_json(html_links, "pharmacity.json")

# write_to_json(html_links, "pharmacity_link.json")
# ###################################################
with open("phama_link.json", "r", encoding="utf-8") as json_file:
    links = json.load(json_file)
visited_links = set()
for link in links:
    if link not in visited_links:
        driver.get(link)
        time.sleep(2)
        visited_links.add(link)
        try:
            name = driver.find_element(By.XPATH,
                                       '//*[@id="__next"]/main/div[1]/div/div[1]/div[2]/div/div[2]/div/div[1]/h1').text
            mo_ta = driver.find_element(By.XPATH,
                                        '//*[@id="__next"]/main/div[1]/div/div[1]/div[2]/div/div[2]/div/div[2]/div[1]/div[2]').text
            data = {
                "Tên":name,
                "Chi tiết":mo_ta
            }

            data_list.append(data)

            write_to_json(data_list, "pharmacity2.json")
        except Exception as e:
            continue