from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import re
import json
import time
from bs4 import BeautifulSoup

driver = webdriver.Chrome()

# driver.get("https://hoanghamobile.com/dien-thoai-di-dong")
# time.sleep(5)

def write_to_json(data, file_path):
    with open(file_path, "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)

# def click_show_more(driver):
#     try:
#         show_more = driver.find_element(By.XPATH,
#                                         '//*[@id="page-pager"]/a')
#         show_more.click()
#         return True
#     except:
#         return False

# while click_show_more(driver):
#     time.sleep(3)

# content = driver.page_source
# soup = BeautifulSoup(content, "html.parser")
# # main = driver.find_element(By.XPATH,
# #                             '//*[@id="page_5"]/div')
# main_xpaths = [
#     '/html/body/section[5]/div/div[1]/div',
#     '//*[@id="page_2"]/div',
#     '//*[@id="page_3"]/div',
#     '//*[@id="page_4"]/div',
#     '//*[@id="page_5"]/div',
#     '//*[@id="page_6"]/div',
#     '//*[@id="page_7"]/div',
#     '//*[@id="page_8"]/div',
#     '//*[@id="page_9"]/div',
#     '//*[@id="page_10"]/div'
#     ]
# html_links= []
# for main_xpath in main_xpaths:
#     main = driver.find_element(By.XPATH, main_xpath)
#     # Tìm tất cả các thẻ 'a' bên trong 'main'
#     a_elements = main.find_elements(By.TAG_NAME, 'a')

#     # Lặp qua từng phần tử 'a' và lấy giá trị của thuộc tính 'href'
#     html_links.extend([a.get_attribute('href') for a in a_elements])

# write_to_json(html_links, "Hoangha_link1.json")



data_list = []
with open("Hoangha_unique_links.json", "r", encoding="utf-8") as json_file:
    html_links = json.load(json_file)
visited_links = set()
for link in html_links:
    if link not in visited_links:
        driver.get(link)
        time.sleep(3)

        visited_links.add(link)
        try:
            name = driver.find_element(By.XPATH,
                    '/html/body/section[2]/div/div/div[1]/h1').text
            print(name)
            brand = name.split(" ")[4]
            price = driver.find_element(By.XPATH,
                                        '/html/body/section[2]/div/div/div[2]/div[2]/p[1]/strong').text
            
            show_detail = driver.find_element(By.XPATH, '/html/body/section[3]/div/div/div[2]/div/div[1]/a')
#                     if show_detail.is_displayed:
            show_detail.click()
            time.sleep(3)
            # max_attempts = 10 # Số lần thử tối đa
            # current_attempt = 0
            # while current_attempt < max_attempts:
            #     driver.execute_script("window.scrollBy(0, 100);")
            #     current_attempt += 1
            #     time.sleep(0.5)

            table = driver.find_element(By.XPATH, '//*[@id="popup-modal"]/table')
            # Lấy tất cả các hàng (tr) trong bảng
            rows = table.find_elements(By.TAG_NAME, "tr")
            parameter = []
            for row in rows:
            # Lấy tất cả các ô dữ liệu (td) trong hàng
                cells = row.find_elements(By.TAG_NAME, "td")


            # Trích xuất và in dữ liệu của hai ô dữ liệu
                if len(cells) > 1:
                    parameter.append(cells[0].text + ": " + cells[1].text)
            
            data = {
                "Tên": name,
                "brand": brand,
                "price": price, 
                "Chi tiết": parameter  
            }
            
            data_list.append(data)
            write_to_json(data_list, "Hoangha.json")
           
        except Exception as e:
            continue  # Bỏ qua trang không có thông tin