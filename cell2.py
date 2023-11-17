from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import re
import json
import time
from bs4 import BeautifulSoup

driver = webdriver.Chrome()

driver.get("https://cellphones.com.vn/mobile/apple.html")
time.sleep(5)
################# phần crawl link #########################
def write_to_json(data, file_path):
    with open(file_path, "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)

GROUP_PRODUCTS = ["Apple", "Samsung", "Xiaomi", "Oppo", "Nokia", "Realme", "Vsmart", "ASUS", "Vivo", "OnePlus",
                      "POCOPhone", "Nubia"]
html_links = []
def click_show_more(driver):
                try:
                    show_more = driver.find_element(By.XPATH,
                                                    '//*[@id="layout-desktop"]/div[3]/div[2]/div/div[4]/div[5]/div/div[2]/a')
                    show_more.click()
                    return True
                except:
                    return False
                
def crawl(self):
        for group in self.GROUP_PRODUCTS:
            # Chrome driver
            driver = webdriver.Chrome("C:/Windows/chromedriver.exe")
            driver.get("https://cellphones.com.vn/mobile/" + group + ".html")

            content = driver.page_source
            soup = BeautifulSoup(content, "html.parser")

            while click_show_more(driver):
                time.sleep(5)

            content = driver.page_source
            soup = BeautifulSoup(content, "html.parser")

            links = driver.find_elements(By.XPATH, '//*[@href]')
            matching_links = [link.get_attribute("href") for link in links]
            html_links.extend([link for link in matching_links if link.endswith(".html")])

write_to_json(html_links, "cellphone_link.json")




# data_list = []
# content = driver.page_source
# soup = BeautifulSoup(content, "html.parser")

# links = driver.find_elements(By.XPATH, '//*[@href]')
# matching_links = [link.get_attribute("href") for link in links]
# html_links.extend([link for link in matching_links if link.endswith(".html")])
# # print(html_links)
# visited_links = set()
# for link in html_links:
#     if link not in visited_links:
#         driver.get(link)
#         time.sleep(7)

#         visited_links.add(link)
#         try:
#             name = driver.find_element(By.XPATH,
#                     '//*[@id="productDetailV2"]/section/div[1]/div[1]/h1').text
            
#             # max_attempts = 7 # Số lần thử tối đa
#             # current_attempt = 0
#             # while current_attempt < max_attempts:
#             #     driver.execute_script("window.scrollBy(0, 400);")
#             #     current_attempt += 1
#             #     time.sleep(2)
            
#             show_detail = driver.find_element(By.XPATH,
#                                             '//*[@id="productDetailV2"]/section/div[4]/div[2]/div[1]/div/button')
#             show_detail.click()
#             time.sleep(2)

#             size_screen = driver.find_element(By.XPATH,
#                                             '//*[@id="productDetailV2"]/section/div[4]/div[2]/div[1]/div/div[2]/div[2]/section/div/ul/li[1]/div/div[1]/div').text
           
#         except Exception as e:
#             continue  # Bỏ qua trang không có thông tin
        
# data = {
#     "Tên":name,
#     "Kích thước màn hình":size_screen
# }
# data_list.append(data)




