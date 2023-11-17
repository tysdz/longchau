from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import re
import json
import time
from bs4 import BeautifulSoup

driver = webdriver.Chrome()

# driver.get("https://viettelstore.vn/dien-thoai")
# time.sleep(5)

def write_to_json(data, file_path):
    with open(file_path, "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)

# def click_show_more(driver):
#     try:
#         show_more = driver.find_element(By.XPATH,
#                                         '//*[@id="div_Danh_Sach_San_Pham_loadMore_btn"]/a')
#         show_more.click()
#         return True
#     except:
#         return False

# while click_show_more(driver):
#     time.sleep(3)

# content = driver.page_source
# soup = BeautifulSoup(content, "html.parser")
# divs = driver.find_elements(By.XPATH,
#                            '//div[@class="product-info"]')
# html_links = [ ]
# # main = driver.find_element(By.XPATH, '//*[@id="layout-desktop"]/div[3]/div[2]/div/div[7]/div[5]')
# for div in divs:
# # Tìm tất cả các thẻ 'a' bên trong 'main'
#     a_elements = div.find_elements(By.TAG_NAME, 'a')

# # # Lặp qua từng phần tử 'a' và lấy giá trị của thuộc tính 'href'
# #     html_links = [a[0].get_attribute('href') for a in a_elements]
#     if a_elements:
#         # Lấy href của 'a' đầu tiên trong 'div'
#         html_links.append(a_elements[0].get_attribute('href'))
# write_to_json(html_links, "Viettelstore_link.json")

data_list = []
with open("Viettelstore_link.json", "r", encoding="utf-8") as json_file:
    html_links = json.load(json_file)
visited_links = set()
for link in html_links:
    if link not in visited_links:
        driver.get(link)
        time.sleep(8)

        visited_links.add(link)
        try:
            name = driver.find_element(By.XPATH,
                    '//*[@id="thongtin"]/div/div[1]/h1').text
            print(name)
            
            show_detail = driver.find_element(By.XPATH, '//*[@id="navcau-hinh"]')
#                     if show_detail.is_displayed:
            show_detail.click()
            time.sleep(8)
            cuon = driver.find_element(By.XPATH, '//*[@id="pop-digital"]/div[3]/div/div[2]')

            # Perform click-and-hold on the 'cuon' element
            ActionChains(driver).click_and_hold(cuon).perform()
            
            # Drag the element down by 20 pixels
            ActionChains(driver).move_by_offset(0, 50).perform()
            time.sleep(2)

            parameter = driver.find_element(By.XPATH,'//*[@id="panel-cau-hinh"]/table/tbody/tr[13]/td[2]').text
            
            data = {
                "Tên": name, 
                "Chi tiết": parameter  
            }
            
            data_list.append(data)
            write_to_json(data_list, "viettelStore.json")
           
        except Exception as e:
            continue  # Bỏ qua trang không có thông tin