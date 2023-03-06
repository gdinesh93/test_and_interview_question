import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(service=Service("C:\\Users\\HP\\Downloads\\chromedriver.exe"))
driver.get("https://www.youtube.com/")
driver.switch_to.new_window('tab')
window_ids = driver.window_handles

for i in window_ids:
    driver.switch_to.window(i)
    print(driver.title)
    if not driver.title:


        driver.close()

time.sleep(5)
