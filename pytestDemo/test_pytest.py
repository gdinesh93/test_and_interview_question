from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pytest



def test1():
    service_obj=Service("C:/Users/HP/Downloads/chromedriver.exe")
    driver=webdriver.Chrome(service=service_obj)
    driver.get("https://chromedriver.chromium.org/downloads")
    print(driver.title)
    assert driver.title=="ChromeDriver - WebDriver for Chrome - Downloads"
@pytest.mark.open
def test2():
    service_obj = Service("C:/Users/HP/Downloads/chromedriver.exe")
    driver = webdriver.Chrome(service=service_obj)
    driver.get("https://mail.google.com/mail/")
    print(driver.title)
    assert driver.title == "Gmail"
@pytest.mark.open
def test3():
    service_obj = Service("C:/Users/HP/Downloads/chromedriver.exe")
    driver = webdriver.Chrome(service=service_obj)
    driver.get("https://www.saucedemo.com/")
    print(driver.title)
    assert driver.title == "Swag Labs"
@pytest.mark.open
def test4():
    service_obj = Service("C:/Users/HP/Downloads/chromedriver.exe")
    driver = webdriver.Chrome(service=service_obj)
    driver.get("https://demo.opencart.com/")
    print(driver.title)
    assert driver.title == "Your Store"
