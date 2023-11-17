from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import re
import json
import time

chrome_options = Options()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--window-size=1920x1080")
driver = webdriver.Chrome()

# Tìm tất cả các liên kết phù hợp với biểu thức chính quy
driver.get("https://nhathuoclongchau.com.vn/thuc-pham-chuc-nang/vien-uong-ho-tro-phu-nu-truoc-khi-mang-thai-promum-new-start-2-x15.html")  # Điều này chỉ để khởi tạo trình duyệt
time.sleep(2)

name = driver.find_element(By.XPATH,
                                    '//*[@id="__next"]/div[1]/div[2]/div[3]/div/div[1]/div[2]/div/div[2]/h1').text
unit = driver.find_element(By.XPATH,
                                    '//*[@id="__next"]/div[1]/div[2]/div[3]/div/div[1]/div[2]/div/div[5]/table/tbody/tr[1]/td[2]/div/span/p').text
category = driver.find_element(By.XPATH,
                                        '//*[@id="__next"]/div[1]/div[2]/div[3]/div/div[1]/div[2]/div/div[5]/table/tbody/tr[2]/td[2]/a/p').text
dosage_forms = driver.find_element(By.XPATH,
                                            '//*[@id="__next"]/div[1]/div[2]/div[3]/div/div[1]/div[2]/div/div[5]/table/tbody/tr[3]/td[2]/div').text
specification = driver.find_element(By.XPATH,
                                            '//*[@id="__next"]/div[1]/div[2]/div[3]/div/div[1]/div[2]/div/div[5]/table/tbody/tr[4]/td[2]/div').text
made_in = driver.find_element(By.XPATH,
                                    '//*[@id="__next"]/div[1]/div[2]/div[3]/div/div[1]/div[2]/div/div[5]/table/tbody/tr[5]/td[2]/div').text
producer = driver.find_element(By.XPATH,
                                        '//*[@id="__next"]/div[1]/div[2]/div[3]/div/div[1]/div[2]/div/div[5]/table/tbody/tr[6]/td[2]/div').text
country = driver.find_element(By.XPATH,
                                    '//*[@id="__next"]/div[1]/div[2]/div[3]/div/div[1]/div[2]/div/div[5]/table/tbody/tr[7]/td[2]/div').text
ingredient = driver.find_element(By.XPATH,
                                        '//*[@id="__next"]/div[1]/div[2]/div[3]/div/div[1]/div[2]/div/div[5]/table/tbody/tr[8]/td[2]').text
short_des = driver.find_element(By.XPATH,
                                        '//*[@id="__next"]/div[1]/div[2]/div[3]/div/div[1]/div[2]/div/div[5]/table/tbody/tr[9]/td[2]/div/p').text
        
print("Tên : " + name )
print("Đơn vị : " + unit )
print("Danh mục : " + category )
print("Dạng bào chế : " + dosage_forms )
print("Quy cách : " + specification )
print("Xuất xứ : " + made_in )
print("Nhà sản xuất : " + producer )
print("Nước sản xuất : " + country )
print("Thành phần : " + ingredient )
print("Mô tả ngắn : " + short_des )        

