from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pytest
#
# driver=None
# def setup(module):
#     global driver
#     service_obj = Service("C:/Users/HP/Downloads/chromedriver.exe")
#     driver = webdriver.Chrome(service=service_obj)
#
# def teardown(module):
#     print("executing the teardown")
#
# def test1():
#     driver.get("https://mail.google.com/mail/")
#     assert driver.title=="Gmail"

driver=None
@pytest.fixture()
def init_driver():
    global driver
    service_obj = Service("C:/Users/HP/Downloads/chromedriver.exe")
    driver = webdriver.Chrome(service=service_obj)
    yield
    print("executing the teardown")

def test1(init_driver):
    driver.get("https://mail.google.com/mail/")
    assert driver.title=="Gmail"

@pytest.mark.usefixtures("init_driver")
def test2():
    driver.get("https://www.saucedemo.com/")
    assert driver.title=="Swag Labs"