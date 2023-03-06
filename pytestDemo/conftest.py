import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

@pytest.fixture()
def init_driver(request):
    service_obj = Service("C:/Users/HP/Downloads/chromedriver.exe")
    webd = webdriver.Chrome(service=service_obj)
    request.cls.driver=webd

