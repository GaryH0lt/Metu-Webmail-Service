import requests
import wget
import zipfile
import os
import time
try:
    selenium.__version__
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.by import By

except:
    os.system("pip install selenium==4.2.0 && pip install webdriver-manager")
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
url = 'https://chromedriver.storage.googleapis.com/LATEST_RELEASE'
response = requests.get(url)
version_number = response.text
download_url = "https://chromedriver.storage.googleapis.com/" + version_number +"/chromedriver_win32.zip"
latest_driver_zip = wget.download(download_url,'chromedriver.zip')
with zipfile.ZipFile(latest_driver_zip, 'r') as zip_ref:
    zip_ref.extractall()
os.remove(latest_driver_zip)
driver.get("https://www.hocamclass.com/single-project")
time.sleep(3)
mailcalismasi = driver.find_element(By.CSS_SELECTOR,"#comp-l5qf2gr7 > a > div").click()
time.sleep(2)
to_inf = driver.find_element(By.CSS_SELECTOR,"#comp-l5ptop14 > p > span > span > a").text
subject_inf = driver.find_element(By.CSS_SELECTOR,"#comp-l5ptpu8a > p > span > span").text
body_inf = driver.find_element(By.CSS_SELECTOR,"#comp-l5ptq8n3 > p > span > span").text
username=""
password=""
driver.get("https://webmail.metu.edu.tr")
time.sleep(2)
username_area=driver.find_element(By.NAME,"_user")
username_area.send_keys(username)
password_area=driver.find_element(By.NAME,"_pass")
password_area.send_keys(password)
driver.find_element(By.CSS_SELECTOR,"#rcmloginsubmit").click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR,"#rcmbtn106").click()
time.sleep(2)
to_slot=driver.find_element(By.CSS_SELECTOR,"#compose_to > div > div > ul > li > input[type=text]")
to_slot.send_keys(to_inf)
subject_slot=driver.find_element(By.CSS_SELECTOR,"#compose-subject")
subject_slot.send_keys(subject_inf)
body_slot=driver.find_element(By.CSS_SELECTOR,"#composebody")
body_slot.send_keys(body_inf)
driver.find_element(By.CSS_SELECTOR,"#rcmbtn110").click()
print("Mesajınız başarıyla gönderilmiştir.")
x = input("")
