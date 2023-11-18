from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import re
import json
import time
from bs4 import BeautifulSoup

driver = webdriver.Chrome()

# driver.get("https://didongthongminh.vn/dien-thoai")
# time.sleep(5)

def write_to_json(data, file_path):
    with open(file_path, "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)

# def click_show_more(driver):
#     try:
#         show_more = driver.find_element(By.XPATH,
#                                         '//*[@id="load_more_button"]')
#         show_more.click()
#         return True
#     except:
#         return False

# while click_show_more(driver):
#     time.sleep(1.5)

# content = driver.page_source
# soup = BeautifulSoup(content, "html.parser")
# main = driver.find_element(By.XPATH,
#                             '//*[@id="box_product"]')
# html_links= []
# # for main_xpath in main_xpaths:
# #     main = driver.find_element(By.XPATH, main_xpath)
# # Tìm tất cả các thẻ 'a' bên trong 'main'
# a_elements = main.find_elements(By.TAG_NAME, 'a')

# # Lặp qua từng phần tử 'a' và lấy giá trị của thuộc tính 'href'
# html_links = [a.get_attribute('href') for a in a_elements]
# write_to_json(html_links, "didongthongminh_link.json")



data_list = []
with open("didongthongminh_link.json", "r", encoding="utf-8") as json_file:
    html_links = json.load(json_file)
visited_links = set()
for link in html_links:
    if link not in visited_links:
        driver.get(link)
        time.sleep(2)

        visited_links.add(link)
        try:
            name = driver.find_element(By.XPATH,
                    '//*[@id="main_container"]/div/div[2]/div[1]/h1').text
            print(name)
            brand = name.split(" ")[0]
            price_xpaths = [
                '//*[@id="main_container"]/div/div[2]/section[1]/aside[2]/div[1]/div[1]/div[2]/div[2]/span[2]',
                '//*[@id="main_container"]/div/div[2]/section[1]/aside[2]/div[1]/div[1]/p[2]/span[1]'
                ]
            for price_xpath in price_xpaths:
                try:
                    price = driver.find_element(By.XPATH, price_xpath).text
                    break  # If successful, exit the loop
                except:
                    continue
            
            show_detail = driver.find_element(By.XPATH, '//*[@id="load_more_charactestic"]')
#                     if show_detail.is_displayed:
            show_detail.click()
            time.sleep(2)
            # max_attempts = 10 # Số lần thử tối đa
            # current_attempt = 0
            # while current_attempt < max_attempts:
            #     driver.execute_script("window.scrollBy(0, 100);")
            #     current_attempt += 1
            #     time.sleep(0.5)

            table = driver.find_element(By.XPATH, '//*[@id="charactestic_detail"]/div/div/div[2]/table')
            # Lấy tất cả các hàng (tr) trong bảng
            rows = table.find_elements(By.TAG_NAME, "tr")
            monitor_technique = ''
            monitor_size = ''
            monitor_resolution = ''
            back_camera = ''
            back_video = ''
            front_camera = ''
            front_video = ''
            gpu = ''
            cpu = ''
            ram = ''
            rom = ''
            battery = ''
            charging_port = ''
            os = ''
            chipset = ''

            for tr in rows:
                try:
                    th = tr.find_elements(By.TAG_NAME, 'td')[0].text
                    td = tr.find_elements(By.TAG_NAME, 'td')[1].text
                    if th == 'Công nghệ màn hình':
                        monitor_technique = td
                    if th == 'Màn hình rộng':
                        monitor_size = td
                    if th == 'Độ phân giải':
                        monitor_resolution = td
                    if th =='Độ phân giải camera sau':
                        back_camera=td
                    if th =='Quay phim':
                        back_video = td
                    if th == 'Độ phân giải camera trước':
                        front_camera = td
                    if th == 'Tính năng camera':
                        front_video = td
                    if th == 'Chip đồ họa':
                        gpu = td
                    if th == 'Chip xử lý':
                        cpu = td
                    if th == 'RAM':
                        ram = td
                    if th == 'Bộ nhớ trong':
                        rom = td
                    if th == 'Dung lượng pin':
                        battery = td
                    if th == 'Công nghệ pin':
                        charging_port = td
                    if th == 'Hệ điều hành':
                        os = td
                    if th == 'Chip xử lý':
                        chipset = td
                except:
                    x=0
              
            data = {
                "name":name,
                "brand": brand,
                "price":price,
                "monitor_technique":monitor_technique,
                "monitor_size":monitor_size,
                "monitor_resolution":monitor_resolution,
                "back_camera":back_camera,
                "back_video":back_video,
                "front_camera":front_camera,
                "front_video":front_video,
                "gpu":gpu,
                "cpu":cpu ,
                "ram": ram,
                "rom":rom ,
                "battery":battery ,
                "charging_port":charging_port ,
                "os":os ,
                "chipset":chipset  
            }
            
            data_list.append(data)
            write_to_json(data_list, "didongthongminh2.json")
        
        except Exception as e:
            continue  # Bỏ qua trang không có thông tin