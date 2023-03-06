import pytest

# @pytest.mark.parametrize("s1",["madam","lol","peak","toot"])
# def test_01(s1):
#     str1=s1
#     str2=""
#     for i in str1:
#         str2=i+str2
#     assert str2==str1, " "+str1+"not palindrome"

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
#
# @pytest.mark.parametrize("name,pswd",[("standard_user","secret_sauce"),
#                                       ("locked_out_user","secret_sauce"),("problem_user","secret_sauce"),
#                                       ("performance_glitch_user","secret_sauce")])
# def test_swaglabs(name,pswd):
#     service_obj = Service("C:/Users/HP/Downloads/chromedriver.exe")
#     driver = webdriver.Chrome(service=service_obj)
#     driver.get("https://www.saucedemo.com/")
#     driver.implicitly_wait(10)
    # driver.find_element(By.ID, "user-name").send_keys(name)
    # driver.find_element(By.ID, "password").send_keys(pswd)
    # driver.find_element(By.ID, "login-button").click()
    # if driver.current_url == "https://www.saucedemo.com/inventory.html":
    #     assert True
    # else:
    #     assert False

@pytest.mark.parametrize("i",range(50))
def test_num(i):
    if i==20 or i==30:
        assert True