#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:loyo
# datetime:2021/8/15 9:32 下午
# software: PyCharm
import allure
import pytest
import yaml
from selenium import webdriver



def pytest_collection_modifyitems(items):
    # 修改ids名称中的中文编码，正常显示中文
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')
    


@pytest.fixture()
def remote_driver():
    option = webdriver.ChromeOptions()
    option.debugger_address = '127.0.0.1:1994'
    remote_driver = webdriver.Chrome(options=option)
    remote_driver.implicitly_wait(5)
    yield  remote_driver
    remote_driver.quit()

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

@pytest.fixture()
def cookies_driver(driver):
    driver.get('https://work.weixin.qq.com/')
    with open('data/data.yaml') as f:
        cookies = yaml.safe_load(f)
    with allure.step("cookies写入当前driver"):
        for cooke in cookies:
            driver.add_cookie(cooke)
        return driver
    
  