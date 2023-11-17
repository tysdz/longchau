from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import re
import json
import time
from bs4 import BeautifulSoup

driver = webdriver.Chrome()

# driver.get("https://fptshop.com.vn/dien-thoai")
# time.sleep(5)

def write_to_json(data, file_path):
    with open(file_path, "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)

# def click_show_more(driver):
#     try:
#         show_more = driver.find_element(By.XPATH,
#                                         '//*[@id="root"]/main/div/div[3]/div[2]/div[2]/div/div[3]/a')
#         show_more.click()
#         return True
#     except:
#         return False

# while click_show_more(driver):
#     time.sleep(2)

# content = driver.page_source
# soup = BeautifulSoup(content, "html.parser")
# main = driver.find_element(By.XPATH,
#                            '//*[@id="root"]/main/div/div[3]/div[2]/div[2]/div/div[2]')
# # main = driver.find_element(By.XPATH, '//*[@id="layout-desktop"]/div[3]/div[2]/div/div[7]/div[5]')

# # Tìm tất cả các thẻ 'a' bên trong 'main'
# h3_xpath = main.find_elements(By.TAG_NAME, 'h3')
# html_links = []
# for h3 in h3_xpath:
#     a = h3.find_element(By.TAG_NAME, 'a')
#     # Lặp qua từng phần tử 'a' và lấy giá trị của thuộc tính 'href'
#     link = a.get_attribute('href')
#     html_links.append(link)

# write_to_json(html_links, "fpt_link.json")



data_list = []
with open("fpt_link.json", "r", encoding="utf-8") as json_file:
    html_links = json.load(json_file)
visited_links = set()
for link in html_links:
    if link not in visited_links:
        driver.get(link)
        time.sleep(3)

        visited_links.add(link)
        try:
            name = driver.find_element(By.XPATH,
                    '//*[@id="root"]/main/div/div[1]/div[2]/div[1]/h1').text
            print(name)
            # brand = name.split(" ")[0]
            price_xpaths = [
                '//*[@id="root"]/main/div/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]',
                '//*[@id="root"]/main/div/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div/div[2]'
            ]
            for price_xpath in price_xpaths:
                try:
                    price = driver.find_element(By.XPATH, price_xpath).text
                    break  # If successful, exit the loop
                except:
                    continue
            show_detail = driver.find_element(By.XPATH, '//*[@id="root"]/main/div/div[2]/div/div[1]/div[2]/div[1]/div/div/a')
#                     if show_detail.is_displayed:
            show_detail.click()
            time.sleep(3)
            
            brand = driver.find_element(By.XPATH,
                                        '//*[@id="data-0"]/ul/li[1]/div').text
            monitor_size = driver.find_element(By.XPATH, 
                                               '//*[@id="data-4"]/table[1]/tbody/tr[1]/td[2]').text
            monitor_technique = driver.find_element(By.XPATH,
                                                     '//*[@id="data-4"]/table[2]/tbody/tr/td[2]/ul/li').text
            monitor_resolution = driver.find_element(By.XPATH,
                                                      '//*[@id="data-4"]/table[4]/tbody/tr/td[2]/ul/li/a').text
        
            back_camera_xpaths = [
                '//*[@id="data-6"]/div[3]',
                '//*[@id="data-7"]/div[3]',
                '//*[@id="data-7"]/div[2]'
            ]
            for back_camera_xpath in back_camera_xpaths:
                try:
                    back_camera = driver.find_element(By.XPATH, back_camera_xpath).text
                    break  # If successful, exit the loop
                except:
                    back_camera = None
                    continue
            # back_video  = driver.find_element(By.XPATH,
            #                                   '//*[@id="data-6"]/table[1]/tbody/tr/td[2]').text
            back_video_xpaths = [
                '//*[@id="data-7"]/table[1]/tbody/tr/td[2]',
                '//*[@id="data-6"]/table[1]/tbody/tr/td[2]'
            ]
            for back_video_xpath in back_video_xpaths:
                try:
                    back_video = driver.find_element(By.XPATH, back_video_xpath).text
                    break  # If successful, exit the loop
                except:
                    back_video = None
                    continue
            # front_camera = driver.find_element(By.XPATH,
            #                                    '//*[@id="data-8"]/div[3]/div').text
            front_camera_xpaths = [
                '//*[@id="data-8"]/div[3]/div/table',
                '//*[@id="data-7"]/div[3]/div/table',
                '//*[@id="data-8"]/div[2]/div/table'
            ]
            for front_camera_xpath in front_camera_xpaths:
                try:
                    front_camera = driver.find_element(By.XPATH, front_camera_xpath).text
                    break  # If successful, exit the loop
                except:
                    front_camera = None
                    continue
            # front_video = driver.find_element(By.XPATH,
            #                                   '//*[@id="data-7"]/table[1]/tbody/tr/td[2]').text
            front_video_xpaths = [
                '//*[@id="data-8"]/table[1]/tbody/tr/td[2]',
                '//*[@id="data-7"]/table[1]/tbody/tr/td[2]'
            ]
            for front_video_xpath in front_video_xpaths:
                try:
                    front_video = driver.find_element(By.XPATH, front_video_xpath).text
                    break  # If successful, exit the loop
                except:
                    front_video = None
                    continue
            # gpu = driver.find_element(By.XPATH,
            #                           '//*[@id="productDetailV2"]/section/div[4]/div[2]/div[1]/div[1]/div[2]/div[2]/section/div/ul/li[4]/div/div[3]/div').text
            gpu_xpaths = [
                '//*[@id="data-5"]/table/tbody/tr/td[2]'
            ]
            for gpu_xpath in gpu_xpaths:
                try:
                    gpu = driver.find_element(By.XPATH, gpu_xpath).text
                    break  # If successful, exit the loop
                except:
                    gpu = None
                    continue
            # cpu = driver.find_element(By.XPATH,
            #                           '//*[@id="productDetailV2"]/section/div[4]/div[2]/div[1]/div[1]/div[2]/div[2]/section/div/ul/li[4]/div/div[2]/div').text
            cpu_xpaths = [
                '//*[@id="data-2"]/table/tbody/tr[2]/td[2]'
            ]
            for cpu_xpath in cpu_xpaths:
                try:
                    cpu = driver.find_element(By.XPATH, cpu_xpath).text
                    break  # If successful, exit the loop
                except:
                    cpu = None
                    continue
            # ram = driver.find_element(By.XPATH,
            #                           '//*[@id="data-3"]/table/tbody/tr[1]/td[2]').text
            ram_xpaths = [
                '//*[@id="data-3"]/table/tbody/tr[1]/td[2]',
                '//*[@id="data-3"]/table/tbody/tr/td[2]'
            ]
            for ram_xpath in ram_xpaths:
                try:
                    ram = driver.find_element(By.XPATH, ram_xpath).text
                    break  # If successful, exit the loop
                except:
                    ram = None
                    continue
            # rom = driver.find_element(By.XPATH,
            #                           '//*[@id="productDetailV2"]/section/div[4]/div[2]/div[1]/div[1]/div[2]/div[2]/section/div/ul/li[5]/div/div[2]/div').text
            rom_xpaths = [
                '//*[@id="data-6"]/table/tbody/tr[1]/td[2]',
                '//*[@id="data-5"]/table/tbody/tr[1]/td[2]',
                '//*[@id="data-5"]/table/tbody/tr/td[2]'
            ]
            for rom_xpath in rom_xpaths:
                try:
                    rom = driver.find_element(By.XPATH, rom_xpath).text
                    break  # If successful, exit the loop
                except:
                    rom = None
                    continue
            # battery = driver.find_element(By.XPATH,
            #                               '//*[@id="productDetailV2"]/section/div[4]/div[2]/div[1]/div[1]/div[2]/div[2]/section/div/ul/li[6]/div/div[1]/div').text
            battery_xpaths = [
                '//*[@id="data-12"]/table[1]/tbody/tr/td[2]',
                '//*[@id="data-13"]/table[1]/tbody/tr[2]/td[2]',
                '//*[@id="data-12"]/table[1]/tbody/tr[2]/td[2]',
                '//*[@id="data-11"]/table[1]/tbody/tr[2]/td[2]'
            ]
            for battery_xpath in battery_xpaths:
                try:
                    battery = driver.find_element(By.XPATH, battery_xpath).text
                    break  # If successful, exit the loop
                except:
                    battery = None
                    continue
            # charging_port = driver.find_element(By.XPATH,
            #                                     '//*[@id="productDetailV2"]/section/div[4]/div[2]/div[1]/div[1]/div[2]/div[2]/section/div/ul/li[6]/div/div[3]/div/a').text
            charging_port_xpaths = [
                '//*[@id="data-13"]/table[2]/tbody/tr/td[2]',
                '//*[@id="data-12"]/table[2]/tbody/tr/td[2]',
                '//*[@id="data-11"]/table[2]/tbody/tr/td[2]'
            ]
            for charging_port_xpath in charging_port_xpaths:
                try:
                    charging_port = driver.find_element(By.XPATH, charging_port_xpath).text
                    break  # If successful, exit the loop
                except:
                    charging_port = None
                    continue
            # os = driver.find_element(By.XPATH,
            #                          '//*[@id="productDetailV2"]/section/div[4]/div[2]/div[1]/div[1]/div[2]/div[2]/section/div/ul/li[7]/div/div[2]/div').text
            os_xpaths = [
                '//*[@id="data-14"]/table/tbody/tr[1]/td[2]',
                '//*[@id="data-13"]/table/tbody/tr[1]/td[2]',
                '//*[@id="data-12"]/table/tbody/tr[1]/td[2]',
                '//*[@id="data-11"]/table/tbody/tr[1]/td[2]'
            ]
            for os_xpath in os_xpaths:
                try:
                    os = driver.find_element(By.XPATH, os_xpath).text
                    break  # If successful, exit the loop
                except:
                    os = None
                    continue
            # chipset = driver.find_element(By.XPATH,
            #                               '//*[@id="data-13"]/table/tbody/tr[2]/td[2]').text
            chipset_xpaths = [
                '//*[@id="data-14"]/table/tbody/tr[2]/td[2]',
                '//*[@id="data-13"]/table/tbody/tr[2]/td[2]',
                '//*[@id="data-12"]/table/tbody/tr[2]/td[2]',
                '//*[@id="data-11"]/table/tbody/tr[2]/td[2]'
            ]
            for chipset_xpath in chipset_xpaths:
                try:
                    chipset = driver.find_element(By.XPATH, chipset_xpath).text
                    break  # If successful, exit the loop
                except:
                    chipset = None
                    continue
            data = {
                "Tên": name,
                "brand": brand,
                "price": price,
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
            write_to_json(data_list, "fpt1.json")
           
        except Exception as e:
            continue  # Bỏ qua trang không có thông tin