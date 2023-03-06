import random
import re
import string
import time

# def email_generator():
#     p = ''
#     for i in range(8):
#         x = random.choice(string.ascii_lowercase + string.digits)
#         p = p + x
#     return p + "@gmail.com"
#
# print(email_generator())
#
# def lname_generator():
#     p=random.choice(["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis",
#     "Miller", "Wilson", "Moore", "Taylor", "Anderson"])
#     print(p)
#
# lname_generator()
# import sys
#
# sys.path.append()
# from

#
# def email_generator():
#     p = ''
#     for i in range(8):
#         x = random.choice(string.ascii_lowercase + string.digits)
#         p = p + x
#     return p + "@gmail.com"
#
#
# def password_generator():
#     p = ""
#     for i in range(8):
#         x = random.choice(string.ascii_letters + string.digits)
#         p = p + x
#     return p
#
#
# def fnamegenerator():
#     p = random.choice(["Ava", "Ethan", "Mia", "Liam", "Sophia",
#                        "Jackson", "Isabella", "Noah", "Charlotte", "William", "Harper"])
#     return p
#
#
# def lnamegenerator():
#     p = random.choice(["Smith", "Johnson", "Williams", "Jones",
#                        "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor", "Anderson"])
#     return p
#
#
# def gendergenerator():
#     p = random.choice(["Male", 'Female'])
#     return p
# email=email_generator()
# fname=fnamegenerator()
# lname=lnamegenerator()
# pswd=password_generator()
# gender=gendergenerator()
#
# p=map(str,(email,fname,lname,pswd,gender))
#
# print(p)
# text="The customer has been successfully added"
#
# p=re.compile("customer")
# m=p.findall(text)
# print(m)
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
driver=webdriver.Chrome(service=Service("C:\\Users\\HP\\Downloads\\chromedriver.exe"))
textbox_email_id='Email'
textbox_password_id="Password"
button_login_xpath="//*[contains(text(),'Log in')]"
link_logout_xpath="//*[contains(text(),'Logout')]"
driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
driver.find_element(By.ID,textbox_email_id).clear()
driver.find_element(By.ID,textbox_email_id).send_keys("admin@yourstore.com")
driver.find_element(By.ID,textbox_password_id).clear()

driver.find_element(By.ID,textbox_password_id).send_keys("admin")
driver.find_element(By.XPATH,button_login_xpath).click()
time.sleep(3)

lnk_customer_menu_xpath = '//p[contains(text(),"Promotions")]/preceding::p[contains(text(),"Customers")]'
lnk_customer_menu_list_xpath = '//*[@href="/Admin/Customer/List"]/p[contains(text(),"Customers")]'

driver.find_element(By.XPATH,lnk_customer_menu_xpath).click()
driver.find_element(By.XPATH,lnk_customer_menu_list_xpath).click()
act=ActionChains(driver)
ele=driver.find_element(By.XPATH,'//*[text()="nopCommerce"]')
act.scroll_to_element(ele).perform()
time.sleep(5)
