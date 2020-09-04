# -*- coding: utf-8 -*-
"""
    :author: ATao
    :description: 
"""


from selenium.webdriver.common.by import By
from core.ui_appium.driver import Driver
import time

class DebtPage(Driver):

    _icon_mine_locator=(By.XPATH,'//android.view.View[@content-desc="我的"]')
    _username_input_locator = (By.ID,"com.mymoney:id/username_eact")
    _first_product_locator=(By.XPATH,'//*[@id="app"]/section/div[1]/div[1]/div[1]')#####点击第一个卡片
    _enter_myloan_locator="com.mymoney.sms:id/right2_img"     #############右上角按钮统一为该id

    def getIconName(self):
        return self.driver.get_screenshot_as_file('.')

    def click_icon_mine_to_login(self):
        self.find_element(self._icon_mine_locator).click()
        self.find_element(self._username_input_locator)
        return self

    def get_current_price(self):
        return float(self.driver.find_element_by_id("current_price").text)

    def click_no_card_alert(self):
        self.driver.switch_to.context('WEBVIEW_com.mymoney.sms')
        self.driver.find_element_by_xpath('//*[@id="app"]/section/div[1]/div[1]/div[1]').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="app"]/section/div[1]/div[1]/div[3]/div[2]/div/div/div[3]/span[1]').click()
        time.sleep(3)
        return self

    def click_have_card_alert(self):
        self.driver.switch_to.context('WEBVIEW_com.mymoney.sms')
        self.driver.find_element_by_xpath('//*[@id="app"]/section/div[1]/div[1]/div[1]').click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="app"]/section/div[1]/div[1]/div[3]/div[2]/div/div/div[3]/span[2]').click()
        time.sleep(3)
        return self

    def click_no_card(self):
        self.driver.switch_to.context('WEBVIEW_com.mymoney.sms')
        self.driver.find_element_by_xpath('//*[@id="app"]/section/div[1]/div[1]/div[2]/div/div[1]/div/div[2]/span').click()
        time.sleep(3)
        return self

    def click_have_card(self):
        self.driver.switch_to.context('WEBVIEW_com.mymoney.sms')
        self.driver.find_element_by_xpath('//*[@id="app"]/section/div[1]/div[1]/div[2]/div/div[2]/div/div[2]/span').click()
        time.sleep(3)
        return self

    def click_act_card(self):
        print(self.driver.contexts)
        self.driver.switch_to.context('WEBVIEW_com.mymoney.sms')
        self.driver.find_element_by_xpath('//*[@id="app"]/section/div[1]/div[2]/div/div[1]/div').click()
        time.sleep(3)
        return self


    def click_cus_service(self):
        self.driver.switch_to.context('WEBVIEW_com.mymoney.sms')
        self.driver.find_element_by_xpath('//*[@id="app"]/section/div[2]/span[2]').click()
        time.sleep(3)
        return self

    def close_alert(self):
        self.driver.switch_to.context('WEBVIEW_com.mymoney.sms')
        self.driver.find_element_by_xpath('//*[@id="app"]/section/div[1]/div[1]/div[1]').click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="app"]/section/div[1]/div[1]/div[3]/div[2]/div/div/div[1]/span[2]').click()
        time.sleep(3)
        return self

    def my_loan_act(self):
        self.driver.find_element_by_id(self._enter_myloan_locator).click()
        time.sleep(1)
        self.driver.switch_to.context('WEBVIEW_com.mymoney.sms')
        self.driver.find_element_by_xpath('//*[@id="app"]/section/img').click()
        time.sleep(3)

    def my_loan_apply(self):
        self.driver.find_element_by_id(self._enter_myloan_locator).click()
        time.sleep(1)
        self.driver.switch_to.context('WEBVIEW_com.mymoney.sms')
        self.driver.find_element_by_xpath('//*[@id="app"]/section/div[1]/div').click()
        time.sleep(3)
        self.driver.switch_to.context('WEBVIEW_com.mymoney.sms')
        for i in range(3):
            self.driver.find_element_by_xpath('//*[@id="app"]/section/div[1]/div/div[%s]/div' % (str(3 - i)))
            time.sleep(1)
        self.driver.switch_to.context('NATIVE_APP')
        self.driver.find_element_by_id(self._enter_myloan_locator).click()########点击反馈
        time.sleep(1)

    def my_loan_prize(self):
        self.driver.find_element_by_id(self._enter_myloan_locator).click()
        time.sleep(1)
        self.driver.switch_to.context('WEBVIEW_com.mymoney.sms')
        self.driver.find_element_by_xpath('//*[@id="app"]/section/div[2]/div').click()
        time.sleep(3)

    def my_loan_money(self):
        self.driver.find_element_by_id(self._enter_myloan_locator).click()
        time.sleep(1)
        self.driver.switch_to.context('WEBVIEW_com.mymoney.sms')
        self.driver.find_element_by_xpath('//*[@id="app"]/section/div[3]/div').click()
        time.sleep(3)

