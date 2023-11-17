from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import re
import json
import time
from bs4 import BeautifulSoup

# # Khởi tạo trình duyệt
# driver = webdriver.Chrome()

# # Tìm tất cả các liên kết phù hợp với biểu thức chính quy
# driver.get("https://nhathuoclongchau.com.vn/trang-thiet-bi-y-te")
# time.sleep(5)

# # Hàm để bấm nút "show more"
# def click_show_more(driver):
#     try:
#         show_more = driver.find_element(By.XPATH, '//*[@id="category-page__products-section"]/div[2]/button')
#         show_more.click()
#         return True
#     except:
#         return False

# Hàm để ghi dữ liệu vào tệp JSON
def write_to_json(data, file_path):
    with open(file_path, "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)

# Mở tệp JSON trước khi bắt đầu thu thập dữ liệu
# data_list = []  # List chứa dữ liệu

# # Chờ cho nút "show more" xuất hiện và bấm nó
# while click_show_more(driver):
#     time.sleep(3)

# content = driver.page_source
# soup = BeautifulSoup(content, "html.parser")

# links = driver.find_elements(By.XPATH, '//*[@href]')
# matching_links = [link.get_attribute("href") for link in links if re.match(r'https://nhathuoclongchau\.com\.vn/trang-thiet-bi-y-te/.+', link.get_attribute("href"))]
# html_links = [link for link in matching_links if link.endswith(".html")]

with open("longchau-trang-thiet-bi-y-te.json", "r", encoding="utf-8") as json_file:
    links = json.load(json_file)
html_links = []
for link in links:
    if link not in html_links:
        html_links.append(link)

write_to_json(html_links,"longchau-trang-thiet-bi-y-te.json")





















# visited_links = set()  # Set to keep track of visited links

# for link in html_links:
#     if link not in visited_links:
#         driver.get(link)
#         time.sleep(2)
#         # Process the page as needed
#         visited_links.add(link)  # Add the visited link to the set
#         try:
#             name = driver.find_element(By.XPATH,
#                 '//*[@id="__next"]/div[1]/div[2]/div[3]/div/div[1]/div[2]/div/div[2]/h1').text
#             table = driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div[2]/div[3]/div/div[1]/div[2]/div/div[5]/table')  # Thay XPath bằng XPath thực tế

#             # Lấy tất cả các hàng (tr) trong bảng
#             rows = table.find_elements(By.TAG_NAME, "tr")
#             parameter = []
#             for row in rows:
#             # Lấy tất cả các ô dữ liệu (td) trong hàng
#                 cells = row.find_elements(By.TAG_NAME, "td")
            
#             # Trích xuất và in dữ liệu của hai ô dữ liệu
#                 if len(cells) >= 2:
#                     parameter.append(cells[0].text + ": " + cells[1].text)
            
#             data = {
#                 "Tên": name, 
#                 "Chi tiết": parameter  
#             }
            
#             data_list.append(data)
            
#             # Ghi dữ liệu vào tệp JSON sau mỗi lần thu thập từ một trang
#             write_to_json(data_list, "trang-thiet-bi-y-te.json")

#         except Exception as e:
#             continue  # Bỏ qua trang không có thông tin

# print("Dữ liệu đã được lưu vào thuc-pham-chuc-nang.json")
