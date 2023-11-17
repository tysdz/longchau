from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import re
import json
import time
from bs4 import BeautifulSoup

# chrome_options = Options()
# chrome_options.add_argument("--incognito")
# chrome_options.add_argument("--window-size=1920x1080")
driver = webdriver.Chrome()

# Tìm tất cả các liên kết phù hợp với biểu thức chính quy
driver.get("https://nhathuoclongchau.com.vn/thuc-pham-chuc-nang")  # Điều này chỉ để khởi tạo trình duyệt
time.sleep(5)

# Hàm để bấm nút "show more"
def click_show_more(driver):
    try:
        show_more = driver.find_element(By.XPATH, '//*[@id="category-page__products-section"]/div[2]/button')
        show_more.click()
        return True
    except:
        return False

# Chờ cho nút "show more" xuất hiện và bấm nó
while click_show_more(driver):
    time.sleep(3)

content = driver.page_source
soup = BeautifulSoup(content, "html.parser")
# Tìm tất cả các liên kết phù hợp với biểu thức chính quy
# list_product = soup.find_all("div", attrs = {"class": "link"})
# for item in list_product:
links = driver.find_elements(By.XPATH, '//*[@href]')
matching_links = [link.get_attribute("href") for link in links if re.match(r'https://nhathuoclongchau\.com\.vn/thuc-pham-chuc-nang/.+', link.get_attribute("href"))]
html_links = [link for link in matching_links if link.endswith(".html")]
print(html_links)
    # Lặp qua các liên kết và thu thập thông tin
    # Lặp qua các liên kết và thu thập thông tin
visited_links = set()  # Set to keep track of visited links
data_list = []
for link in html_links:
        if link not in visited_links:
            driver.get(link)
            time.sleep(2)
            # Process the page as needed
            visited_links.add(link)  # Add the visited link to the set
            try:
                name = driver.find_element(By.XPATH,
                                            '//*[@id="__next"]/div[1]/div[2]/div[3]/div/div[1]/div[2]/div/div[1]/h1').text
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
                
                # print("Tên : " + name )
                # print("Đơn vị : " + unit )
                # print("Danh mục : " + category )
                # print("Dạng bào chế : " + dosage_forms )
                # print("Quy cách : " + specification )
                # print("Xuất xứ : " + made_in )
                # print("Nhà sản xuất : " + producer )
                # print("Nước sản xuất : " + country )
                # print("Thành phần : " + ingredient )
                # print("Mô tả ngắn : " + short_des )

            except Exception as e:
                continue  # Bỏ qua trang không có thông tin

            data = {
                    "Tên": name,
                    "Đơn vị": unit,
                    "Danh mục": category,
                    "Dạng bào chế": dosage_forms,
                    "Quy cách": specification,
                    "Xuất xứ": made_in,
                    "Nhà sản xuất": producer,
                    "Nước sản xuất": country,
                    "Thành phần": ingredient,
                    "Mô tả ngắn": short_des
                }
                
            data_list.append(data)

with open("scraped_data.json", "w", encoding="utf-8") as json_file:
    json.dump(data_list, json_file, ensure_ascii=False, indent=4)

print("Dữ liệu đã được lưu vào scraped_data.json")
