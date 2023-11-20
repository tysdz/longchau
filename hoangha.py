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
                    if th == 'Kích thước màn hình':
                        monitor_size = td
                    # if th == 'Độ phân giải':
                    #     monitor_resolution = td
                    if th == 'Độ phân giải':
                        resolutions = td.split(', ')
                        if len(resolutions) == 1:
                            monitor_resolution = resolutions[0]
                        elif len(resolutions) == 2:
                            monitor_resolution = resolutions[0]
                            back_camera = resolutions[1]
                        elif len(resolutions) == 3:
                            monitor_resolution = resolutions[0]
                            back_camera = resolutions[1]
                            front_camera = resolutions[2]
                    # if th =='Độ phân giải camera sau':
                    #     back_camera=td
                    if th =='Quay phim':
                        video = td.split(', ')
                        if len(video) == 1 :
                            back_video = video[0]
                        if len(video) == 2:
                            front_video == video[1]
                            back_video = video[0]
                    # if th == 'Độ phân giải camera trước':
                    #     front_camera = td
                    # if th == 'Tính năng camera':
                    #     front_video = td
                    if th == 'Vi xử lý đồ họa (GPU)':
                        gpu = td
                    if th == 'Tốc độ CPU':
                        cpu = td
                    if th == 'RAM':
                        ram = td
                    if th == 'Bộ nhớ trong':
                        rom = td
                    if th == 'Dung lượng pin':
                        battery = td
                    if th == 'Hỗ trợ sạc tối đa:':
                        charging_port = td
                    if th == 'Hệ điều hành':
                        os = td
                    if th == 'Vi xử lý':
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
            write_to_json(data_list, "Hoangha.json")
           
        except Exception as e:
            continue  # Bỏ qua trang không có thông tin