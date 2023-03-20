

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
#
driver=webdriver.Chrome(service=Service("C:\\Users\\HP\\Downloads\\chromedriver.exe"))
# driver.get("https://www.jqueryscript.net/demo/Drop-Down-Combo-Tree/")
# driver.maximize_window()
# driver.find_element(By.ID,"justAnInputBox").click()
# time.sleep(3)
# dr=driver.find_elements(By.XPATH,'//*[@class="comboTreeItemTitle"]')
#
# for i in dr:
#     print(i.text)
# from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.firefox import GeckoDriverManager
# from selenium.webdriver.chrome.service import Service
#
# driver=webdriver.Chrome(service=Service(""))
#
# driver=webdriver.Chrome(ChromeDriverManager().install())
#
# f=open(r"C:\Users\HP\PycharmProjects\selenium\pytestDemo\New Text Document.txt",'r')
# content=f.read()
# print(content)
# import re
#
# p=re.compile("\s(\w+\.JPG)",re.IGNORECASE)
# m=p.findall(content)
# print(m)
# print(len(m))
#
# s="\n".join(m)
# print(s)
# file=open("album.txt","a")
# file.write(s)
#
# driver.get("https://jqueryui.com/datepicker/")
# time.sleep(3)
# driver.maximize_window()
# frame=driver.find_element(By.XPATH,'//*[@class="demo-frame"]')
# act=ActionChains(driver)
# act.scroll_to_element(driver.find_element(By.XPATH,'//*[contains(text(),"Icon trigger")]')).perform()
#
# driver.switch_to.frame(frame)
# driver.find_element(By.XPATH,'//*[@id="datepicker"]').click()
# exp_month="March"
# exp_year="2024"
# dt=28
# date=driver.find_element(By.XPATH,'//*[@data-date="'+str(dt)+'"]')
# table=driver.find_element(By.XPATH,'//*[@class="ui-datepicker-title"]')
# while True:
#     month = driver.find_element(By.XPATH, '//*[@class="ui-datepicker-month"]').text
#     year = driver.find_element(By.XPATH, '//*[@class="ui-datepicker-year"]').text
#     date=driver.find_element(By.XPATH,'//*[@class="ui-datepicker-calendar"]//tr/td/a[contains(text(),"28")]')
#     if month==exp_month and year==exp_year:
#         date.click()
#         break
#
#     else:
#         driver.find_element(By.XPATH,'//*[contains(text(),"Next")]').click()
#
# time.sleep(3)
#
# act.drag_and_drop()
# act.drag_and_drop_by_offset()
# driver.swit
#
# ch_to.new_window('window')
# driver.switch_to.new_window('tab')

# driver.get("https://stackoverflow.com/")
# elements=driver.find_elements(By.XPATH,"//*[contains(@class,'ta-center pb64')]/div/div/img")
#
# for ele in elements:
#     print(ele.get_attribute("alt"))

driver.implicitly_wait(10)
mywait=WebDriverWait(driver,10)
mywait.until(expected_conditions.ele

# import re
#
# txt="Thousands of organizations around the globe use Stack Overflow for Teams"
#
# p=re.compile("(?<=around)\s(\w+)")
# m=p.finditer(txt)
#
# for i in m:
#     print(i.group(1))