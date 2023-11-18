from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import re
import json
import time
from bs4 import BeautifulSoup

driver = webdriver.Chrome()

# driver.get("https://didongviet.vn/dien-thoai.html")
# time.sleep(5)

def write_to_json(data, file_path):
    with open(file_path, "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)

# def click_show_more(driver):
#     try:
#         show_more = driver.find_element(By.XPATH,
#                                         '//*[@id="__next"]/main/div[2]/div/main/div/div/div[4]/button')
#         show_more.click()
#         return True
#     except:
#         return False

# while click_show_more(driver):
#     time.sleep(2)

# content = driver.page_source
# soup = BeautifulSoup(content, "html.parser")
# main = driver.find_element(By.XPATH,
#                            '//*[@id="__next"]/main/div[2]/div/main/div/div/div[3]/div/div[3]/div')
# # Tìm tất cả các thẻ 'a' bên trong 'main'
# a_elements = main.find_elements(By.TAG_NAME, 'a')

# # Lặp qua từng phần tử 'a' và lấy giá trị của thuộc tính 'href'
# html_links = [a.get_attribute('href') for a in a_elements]
# write_to_json(html_links, "didongviet_link.json")



data_list = []
with open("didongviet_link.json", "r", encoding="utf-8") as json_file:
    html_links = json.load(json_file)
visited_links = set()
for link in html_links:
    if link not in visited_links:
        driver.get(link)
        time.sleep(2)

        visited_links.add(link)
        try:
            name = driver.find_element(By.XPATH,
                    '//*[@id="blockPrice"]/div/h1').text
            print(name)
            brand = name.split(" ")[0]
            price_xpaths = [
                '//*[@id="blockPrice"]/div/div[5]/div[1]/div/p',
                '//*[@id="blockPrice"]/div/div[5]/div[1]/div/p'
            ]
            for price_xpath in price_xpaths:
                try:
                    price = driver.find_element(By.XPATH, price_xpath).text
                    break  # If successful, exit the loop
                except:
                    continue
            show_detail = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div[2]/main/div/div/div[5]/div[2]/div/div/div/button')
#                     if show_detail.is_displayed:
            show_detail.click()
            time.sleep(2)
            
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
            div1 = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div[2]/main/div/div/div[5]/div[2]/div/div/div/div[2]/div[1]')
            div_show1s = div1.find_elements(By.XPATH, './/*[contains(@class, "flex justify-between items-start odd:bg-white even:bg-gray-100 p-2 w-full")]')
            for div_show1 in div_show1s:
                p = div_show1.find_elements(By.TAG_NAME, "p")
                
                if p[0].text == 'Công nghệ màn hình':
                    monitor_technique = p[1].text
                if p[0].text == 'Màn hình rộng':
                    monitor_size = p[1].text
                if p[0].text == 'Độ phân giải':
                    monitor_resolution = p[1].text
            
            div1 = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div[2]/main/div/div/div[5]/div[2]/div/div/div/div[2]/div[2]')
            div_show1s = div1.find_elements(By.XPATH, './/*[contains(@class, "flex justify-between items-start odd:bg-white even:bg-gray-100 p-2 w-full")]')
            for div_show1 in div_show1s:
                p = div_show1.find_elements(By.TAG_NAME, "p")
                
                if p[0].text =='Độ phân giải':
                    back_camera=p[1].text
                if p[0].text =='Quay phim':
                    back_video = p[1].text
            
            div1 = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div[2]/main/div/div/div[5]/div[2]/div/div/div/div[2]/div[3]')
            div_show1s = div1.find_elements(By.XPATH, './/*[contains(@class, "flex justify-between items-start odd:bg-white even:bg-gray-100 p-2 w-full")]')
            for div_show1 in div_show1s:
                p = div_show1.find_elements(By.TAG_NAME, "p")
                
                if p[0].text =='Độ phân giải':
                    front_camera=p[1].text
                if p[0].text =='Video Call':
                    front_video = p[1].text
            
            div1 = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div[2]/main/div/div/div[5]/div[2]/div/div/div/div[2]/div[4]')
            div_show1s = div1.find_elements(By.XPATH, './/*[contains(@class, "flex justify-between items-start odd:bg-white even:bg-gray-100 p-2 w-full")]')
            for div_show1 in div_show1s:
                p = div_show1.find_elements(By.TAG_NAME, "p")
                
                if p[0].text =='Chip đồ họa (GPU)':
                    gpu=p[1].text
                if p[0].text =='Chip xử lý (CPU)':
                    cpu = p[1].text
                if p[0].text =='Hệ điều hành':
                    os = p[1].text

            div1 = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div[2]/main/div/div/div[5]/div[2]/div/div/div/div[2]/div[5]')
            div_show1s = div1.find_elements(By.XPATH, './/*[contains(@class, "flex justify-between items-start odd:bg-white even:bg-gray-100 p-2 w-full")]')
            for div_show1 in div_show1s:
                p = div_show1.find_elements(By.TAG_NAME, "p")
                
                if p[0].text =='RAM':
                    ram =p[1].text
                if p[0].text =='Bộ nhớ trong':
                    rom = p[1].text

            div1 = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div[2]/main/div/div/div[5]/div[2]/div/div/div/div[2]/div[7]')
            div_show1s = div1.find_elements(By.XPATH, './/*[contains(@class, "flex justify-between items-start odd:bg-white even:bg-gray-100 p-2 w-full")]')
            for div_show1 in div_show1s:
                p = div_show1.find_elements(By.TAG_NAME, "p")
                
                if p[0].text =='Dung lượng pin':
                    battery =p[1].text
                if p[0].text =='Công nghệ pin':
                    charging_port = p[1].text

                # if th == 'Độ phân giải camera trước':
                #     front_camera = td
                # if th == 'Tính năng camera':
                #     front_video = td
                # if th == 'Chip đồ họa':
                #     gpu = td
                # if th == 'Chip xử lý':
                #     cpu = td
                # if th == 'RAM':
                #     ram = td
                # if th == 'Bộ nhớ trong':
                #     rom = td
                # if th == 'Dung lượng pin':
                #     battery = td
                # if th == 'Công nghệ pin':
                #     charging_port = td
                # if th == 'Hệ điều hành':
                #     os = td
                # if th == 'Chip xử lý':
                #     chipset = td
              
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
                # "chipset":chipset  
            }
            
            data_list.append(data)
            write_to_json(data_list, "didongviet.json")
           
        except Exception as e:
            continue  # Bỏ qua trang không có thông tin