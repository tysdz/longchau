from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://cellphones.com.vn/iphone-15-pro-max.html")
time.sleep(4)

name = driver.find_element(By.XPATH, '//*[@id="productDetailV2"]/section/div[1]/div[1]/h1').text

# Sử dụng JavaScript để cuộn xuống và hiển thị phần tử show_detail
max_attempts = 30 # Số lần thử tối đa
current_attempt = 0
while current_attempt < max_attempts:
    try:
        show_detail = driver.find_element(By.XPATH, '//*[@id="productDetailV2"]/section/div[4]/div[2]/div[1]/div/button')
        if show_detail.is_displayed:
            show_detail.click()
            time.sleep(2)

            size_screen = driver.find_element(By.XPATH, '//*[@id="productDetailV2"]/section/div[4]/div[2]/div[1]/div/div[2]/div[2]/section/div/ul/li[1]/div/div[1]/div').text
            break
    except:
        driver.execute_script("window.scrollBy(0, 100);")
        current_attempt += 1
        time.sleep(0.5)


# driver.execute_script("window.scrollBy(0, 2500);")
# time.sleep(10)


print(name)
print(size_screen)
