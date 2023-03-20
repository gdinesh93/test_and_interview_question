import time

import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://opensource-demo.orangehrmlive.com/")
time.sleep(5)
driver.find_element(By.XPATH,'//*[@name="username"]').send_keys("Admin")
driver.find_element(By.XPATH,'//*[@name="password"]').send_keys("admin123")
driver.find_element(By.XPATH,'//*[@type="submit"]').click()
requests.get("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewAdminModule")
