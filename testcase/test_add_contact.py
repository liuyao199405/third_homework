#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:loyo
# datetime:2021/8/15 9:49 下午
# software: PyCharm
import time
import allure
import pytest
import yaml


@pytest.mark.skip
@allure.feature("保存cookies")
class TestSaveCookies:
    @allure.title("保存cookies")
    @allure.story("保存cookies")
    def test_save_cookies(self, remote_driver):
        remote_driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
        with open("data/data.yml", "w") as f:
            yaml.safe_dump(remote_driver.get_cookies(), f)

@allure.feature('企业微信web测试')
class TestAddContacts:
    @allure.title('添加联系人')
    @allure.story('添加联系人')
    def test_add_contcats(self,cookies_driver):
        cookies_driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
        cookies_driver.refresh()
        
        # 打开通讯录
        cookies_driver.find_element_by_id('menu_contacts').click()
        time.sleep(2)
        
        # 点击添加成员按钮
        with allure.step('点击添加成员按钮'):
            add_btn = cookies_driver.find_element_by_xpath('//div[@class="ww_operationBar"]/a[contains(@class,"js_add_member")]')
            add_btn.click()
            time.sleep(4)
            
        # 填入成员信息
        with allure.step('填入成员信息'):
            user_name = "测试人员1"
            cookies_driver.find_element_by_id("username").send_keys(user_name)
            cookies_driver.find_element_by_id("memberAdd_english_name").send_keys("1号")
            cookies_driver.find_element_by_id("memberAdd_acctid").send_keys("Cs01")
            cookies_driver.find_element_by_id("memberAdd_phone").send_keys("13004445461")
            cookies_driver.find_element_by_id("memberAdd_title").send_keys("普通职员")
            time.sleep(2)
            
            # 保存信息
            cookies_driver.find_element_by_css_selector(
                '.js_member_editor_form > div:nth-child(1) .js_btn_save').click()

            # 断言通讯录是否添加成功e
            with allure.step("断言添加结果"):
                user_list = cookies_driver.find_elements_by_css_selector(f'[title="{user_name}"]')
                assert len(user_list) >= 1, "成员添加失败"
            
        
        