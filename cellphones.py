from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import re
import json
import time
from bs4 import BeautifulSoup

driver = webdriver.Chrome()

# driver.get("https://cellphones.com.vn/mobile.html")
# time.sleep(5)

def write_to_json(data, file_path):
    with open(file_path, "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)

# def click_show_more(driver):
#     try:
#         show_more = driver.find_element(By.XPATH,
#                                         '//*[@id="layout-desktop"]/div[3]/div[2]/div/div[7]/div[5]/div/div[2]/a')
#         show_more.click()
#         return True
#     except:
#         return False

# while click_show_more(driver):
#     time.sleep(3)

# content = driver.page_source
# soup = BeautifulSoup(content, "html.parser")
# main = driver.find_element(By.XPATH,
#                            '//*[@id="layout-desktop"]/div[3]/div[2]/div/div[7]/div[5]/div/div[1]')
# # main = driver.find_element(By.XPATH, '//*[@id="layout-desktop"]/div[3]/div[2]/div/div[7]/div[5]')

# # Tìm tất cả các thẻ 'a' bên trong 'main'
# a_elements = main.find_elements(By.TAG_NAME, 'a')

# # Lặp qua từng phần tử 'a' và lấy giá trị của thuộc tính 'href'
# html_links = [a.get_attribute('href') for a in a_elements]

# write_to_json(html_links, "cellphone_link.json")




data_list = []
with open("cell1.json", "r", encoding="utf-8") as json_file:
    html_links = json.load(json_file)
visited_links = set()
for link in html_links:
    if link not in visited_links:
        driver.get(link)
        time.sleep(3)

        visited_links.add(link)
        try:
            name = driver.find_element(By.XPATH,
                    '//*[@id="productDetailV2"]/section/div[1]/div[1]/h1').text
            brand = name.split(" ")[0]
            price_xpaths = [
                '//*[@id="trade-price-tabs"]/div/div/div[2]/p',
                '//*[@id="trade-price-tabs"]/div/div/div[2]/p[1]',
                '//*[@id="productDetailV2"]/section/div[2]/div[2]/div[1]/div/p'
            ]
            for price_xpath in price_xpaths:
                try:
                    price = driver.find_element(By.XPATH, price_xpath).text
                    break  # If successful, exit the loop
                except:
                    continue 
                # lấy chi tiết
            max_attempts = 26 # Số lần thử tối đa
            current_attempt = 0
            while current_attempt < max_attempts:
                try:
                    show_detail = driver.find_element(By.XPATH, '//*[@id="productDetailV2"]/section/div[4]/div[2]/div[1]/div/button')
                    if show_detail.is_displayed:
                        show_detail.click()
                        time.sleep(2)

                        monitor_size = driver.find_element(By.XPATH, '//*[@id="productDetailV2"]/section/div[4]/div[2]/div[1]/div/div[2]/div[2]/section/div/ul/li[1]/div/div[1]/div').text
                        print(1)
                        monitor_technique = driver.find_element(By.XPATH, '//*[@id="productDetailV2"]/section/div[4]/div[2]/div[1]/div[1]/div[2]/div[2]/section/div/ul/li[1]/div/div[2]/div').text
                        print(2)
                        monitor_resolution = driver.find_element(By.XPATH, '//*[@id="productDetailV2"]/section/div[4]/div[2]/div[1]/div[1]/div[2]/div[2]/section/div/ul/li[1]/div/div[3]/div').text
                        print(3)
                        back_camera = driver.find_element(By.XPATH,'//*[@id="productDetailV2"]/section/div[4]/div[2]/div[1]/div[1]/div[2]/div[2]/section/div/ul/li[2]/div/div[1]/div' ).text
                        print(4)
                        back_video  = driver.find_element(By.XPATH,'//*[@id="productDetailV2"]/section/div[4]/div[2]/div[1]/div[1]/div[2]/div[2]/section/div/ul/li[2]/div/div[2]/div').text
                        print(5)
                        front_camera = driver.find_element(By.XPATH,'//*[@id="productDetailV2"]/section/div[4]/div[2]/div[1]/div[1]/div[2]/div[2]/section/div/ul/li[3]/div/div[1]/div').text
                        print(6)
                        front_video = driver.find_element(By.XPATH,'//*[@id="productDetailV2"]/section/div[4]/div[2]/div[1]/div[1]/div[2]/div[2]/section/div/ul/li[3]/div/div[2]/div').text
                        print(7)
                        gpu = driver.find_element(By.XPATH,'//*[@id="productDetailV2"]/section/div[4]/div[2]/div[1]/div[1]/div[2]/div[2]/section/div/ul/li[4]/div/div[3]/div').text
                        print(8)
                        cpu = driver.find_element(By.XPATH,'//*[@id="productDetailV2"]/section/div[4]/div[2]/div[1]/div[1]/div[2]/div[2]/section/div/ul/li[4]/div/div[2]/div').text
                        print(9)
                        ram = driver.find_element(By.XPATH,'//*[@id="productDetailV2"]/section/div[4]/div[2]/div[1]/div[1]/div[2]/div[2]/section/div/ul/li[5]/div/div[1]/div').text
                        print(10)
                        rom = driver.find_element(By.XPATH,'//*[@id="productDetailV2"]/section/div[4]/div[2]/div[1]/div[1]/div[2]/div[2]/section/div/ul/li[5]/div/div[2]/div').text
                        print(11)
                        battery = driver.find_element(By.XPATH,'//*[@id="productDetailV2"]/section/div[4]/div[2]/div[1]/div[1]/div[2]/div[2]/section/div/ul/li[6]/div/div[1]/div').text
                        print(12)
                        charging_port = driver.find_element(By.XPATH,'//*[@id="productDetailV2"]/section/div[4]/div[2]/div[1]/div[1]/div[2]/div[2]/section/div/ul/li[6]/div/div[3]/div/a').text
                        print(13)
                        os = driver.find_element(By.XPATH,'//*[@id="productDetailV2"]/section/div[4]/div[2]/div[1]/div[1]/div[2]/div[2]/section/div/ul/li[7]/div/div[2]/div').text
                        print(14)
                        chipset = driver.find_element(By.XPATH,'//*[@id="productDetailV2"]/section/div[4]/div[2]/div[1]/div[1]/div[2]/div[2]/section/div/ul/li[4]/div/div[1]/div').text
                        print(15)
                        break
                except:
                    driver.execute_script("window.scrollBy(0, 100);")
                    current_attempt += 1
                    time.sleep(0.2)

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
            write_to_json(data_list, "cellphone3.json")
            # show_detail = driver.find_element(By.XPATH,
            #                                 '//*[@id="productDetailV2"]/section/div[4]/div[2]/div[1]/div/button')
            # show_detail.click()
            # time.sleep(2)

            # size_screen = driver.find_element(By.XPATH,
            #                                 '//*[@id="productDetailV2"]/section/div[4]/div[2]/div[1]/div/div[2]/div[2]/section/div/ul/li[1]/div/div[1]/div').text
           
        except Exception as e:
            continue  # Bỏ qua trang không có thông tin
        






