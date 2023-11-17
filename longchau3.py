from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Khởi tạo trình duyệt
driver = webdriver.Chrome()

# Mở trang web chứa bảng
driver.get("https://nhathuoclongchau.com.vn/thuc-pham-chuc-nang/vien-uong-bo-sung-canxi-giam-nguy-co-loang-xuong-calcium-premium-jpanwell-120-v.html")  # Thay URL bằng URL thực tế
time.sleep(5)
# Xác định bảng bằng XPath hoặc các phương thức khác tùy vào trang web
name = driver.find_element(By.XPATH,
                '//*[@id="__next"]/div[1]/div[2]/div[3]/div/div[1]/div[2]/div/div[2]/h1').text
table = driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div[2]/div[3]/div/div[1]/div[2]/div/div[5]/table')  # Thay XPath bằng XPath thực tế

# Lấy tất cả các hàng (tr) trong bảng
rows = table.find_elements(By.TAG_NAME, "tr")
parameter = []
# Lặp qua từng hàng
for row in rows:
    # Lấy tất cả các ô dữ liệu (td) trong hàng
    cells = row.find_elements(By.TAG_NAME, "td")
    
    # Trích xuất và in dữ liệu của hai ô dữ liệu
    if len(cells) >= 2:
        
        parameter.append(cells[0].text + ": " + cells[1].text)
        data = {
                        "Tên":name,
                        "Chi tiết":parameter  
                    } 
        
print(data)
# Đóng trình duyệt
driver.quit()
