from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import json
import time
from bs4 import BeautifulSoup

def write_to_json(data, file_path):
    with open(file_path, "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)

driver = webdriver.Chrome()

data_list = []
with open("Viettelstore_link.json", "r", encoding="utf-8") as json_file:
    html_links = json.load(json_file)

visited_links = set()
for link in html_links:
    if link not in visited_links:
        name = ""
        brand= ""
        monitor_technique = ""
        kich_thuoc_man_hinh = ""
        monitor_resolution = ""
        cam_sau = ""
        vid_sau = ""
        cam_truoc = ""
        gpu = ""
        cpu = ""
        ram = ""
        rom = ""
        pin = ""
        cong_sac = ""
        he_dieu_hanh = ""
        chip = ""
        price= ""
        error = ""
        driver.get(link)
        time.sleep(8)
        visited_links.add(link)
        try:

            parameter = set()
            name = driver.find_element(By.XPATH, '//*[@id="thongtin"]/div/div[1]/h1').text
            print(name)
            try:
                os = driver.find_element(By.XPATH, '//*[@id="dacdiem"]/div[2]/div/div[2]/table/tbody/tr[3]/td[2]').text
            except:
                continue
            
            he_dieu_hanh = driver.find_element(By.XPATH, '//*[@id="dacdiem"]/div[2]/div/div[2]/table/tbody/tr[9]/td[2]').text
            vid_sau = driver.find_element(By.XPATH, '//*[@id="dacdiem"]/div[2]/div/div[2]/table/tbody/tr[11]/td[2]').text
            try:
                price = driver.find_element(By.XPATH, '//*[@id="thongtin"]/div/div[1]/div[2]/div/div[1]/span[2]').text
            except:
                price = driver.find_element(By.XPATH, '//*[@id="thongtin"]/div/div[1]/div[2]/div/div[1]/span[1]').text

            

            brand = name.split()[0]
            show_detail = driver.find_element(By.XPATH, '//*[@id="navcau-hinh"]')
            show_detail.click()
            time.sleep(4)
            
            table = driver.find_element(By.XPATH, '//*[@id="panel-cau-hinh"]/table')
            
            cuon = driver.find_element(By.XPATH, '//*[@id="pop-digital"]/div[3]/div/div[2]')

            loopp = 6
            while(loopp >0 ):
                rows = table.find_elements(By.TAG_NAME, "tr")    
                for row in rows:
                # Lấy tất cả các ô dữ liệu (td) trong hàng
                    cells = row.find_elements(By.TAG_NAME, "td")
                    
                
                # Trích xuất và in dữ liệu của hai ô dữ liệu
                    if len(cells) > 1:
                        parameter.add(cells[0].text + ": " + cells[1].text)
                        

                # Perform click-and-hold on the 'cuon' element
                ActionChains(driver).click_and_hold(cuon).perform()
                
                # Drag the element down by 20 pixels
                ActionChains(driver).move_by_offset(0, 70).perform()
                ActionChains(driver).release().perform()
                time.sleep(0.5)
                loopp -= 1
            
            # table = driver.find_element(By.XPATH, '//*[@id="panel-cau-hinh"]/table')

            # # Lấy tất cả các hàng (tr) trong bảng
            # rows = table.find_elements(By.TAG_NAME, "tr")
            # parameter = []
            # for row in rows:
            # # Lấy tất cả các ô dữ liệu (td) trong hàng
            #     cells = row.find_elements(By.TAG_NAME, "td")
            
            # # Trích xuất và in dữ liệu của hai ô dữ liệu
            #     if len(cells) > 1:
            #         parameter.append(cells[0].text + ": " + cells[1].text)

            # parameter = driver.find_element(By.XPATH,'//*[@id="panel-cau-hinh"]/table/tbody/tr[13]/td[2]').text

            for item in parameter:
                if 'RAM' in item:
                    ram = item.split(':')[-1].strip()
                if 'Bộ nhớ trong' in item:
                    rom = item.split(':')[-1].strip()
                if 'Loại màn hình' in item:
                    monitor_technique = item.split(':')[-1].strip()
                if 'Kích thước' in item:
                    kich_thuoc_man_hinh = item.split(':')[-1].strip()
                if 'Độ phân giải' in item:
                    monitor_resolution = item.split(':')[-1].strip()
                if 'Camera sau' in item:
                    cam_sau = item.split(':')[-1].strip()
                if 'Camera trước' in item:
                    cam_truoc = item.split(':')[-1].strip()
                if 'Chip đồ họa (GPU)' in item:
                    gpu = item.split(':')[-1].strip()
                if 'Số nhân CPU' in item:
                    cpu = item.split(':')[-1].strip()
                if 'RAM' in item:
                    ram = item.split(':')[-1].strip()
                if 'Bộ nhớ trong' in item:
                    rom = item.split(':')[-1].strip()
                # if 'Loại pin' in item:
                #     cong_sac = item.split(':')[-1].strip()
                if 'Dung lượng Pin' in item:
                    pin = item.split(':')[-1].strip()
                if 'Kết nối USB' in item:
                    cong_sac = item.split(':')[-1].strip()
                if 'Chipset' in item:
                    chip = item.split(':')[-1].strip()
                if 'Loại màn hình' in item:
                    monitor_technique = item.split(':')[-1].strip()
                if 'Loại màn hình' in item:
                    monitor_technique = item.split(':')[-1].strip()
                
                    
            #print(ram)
            data = {
                "name":name,
                "brand": brand,
                "monitor technique": monitor_technique,
                "monitor_size": kich_thuoc_man_hinh,
                "monitor_resolution": monitor_resolution,
                "back_camera": cam_sau,
                "back_video": vid_sau,
                "front_camera": cam_truoc,
                "gpu": gpu,
                "cpu":cpu,
                "ram":ram,
                "rom":rom,
                "battery":pin,
                "charging_port":cong_sac,
                "os":he_dieu_hanh,
                "chipset":chip,
                "price":price,
                "link":link,
                "error":""
            }
            print(data)
            data_list.append(data)
            write_to_json(data_list, "viettelStore.json")

        except Exception as e:
            print("loi")
            continue  # Ignore pages without information

driver.quit()