# -*- coding: utf-8 -*-
"""
    :author: zT
    :description:
"""


from selenium.webdriver.common.by import By
from core.ui_appium.driver import Driver
import time

class CreateCardPage(Driver):

    def check_banner(self):
        # size=self.driver.get_window_size()
        # self.driver.tap([(size["width"]*0.5, size["height"]*0.14)])
        self.driver.switch_to.context('WEBVIEW_com.mymoney.sms')
        self.driver.find_element_by_xpath('//*[@id="app"]/div/section[1]/div/div[1]/div').click()
        time.sleep(3)
        return self

    def check_recommand(self):
        self.driver.switch_to.context('WEBVIEW_com.mymoney.sms')
        time.sleep(1)
        _refer2 = """//*[@id="app"]/div/header/section[2]/div[2]/div[2]/div[1]/div[2]"""
        self.driver.find_element_by_xpath(_refer2).click()
        time.sleep(3)
        return self

    def click_hot_bank(self):
        _view_more = '//*[@id="app"]/div/section[2]/div[2]/div[1]'
        for i in range(1,9):
            _hot_bank_btn='//*[@id="app"]/div/section[2]/ul/li[%s]/div'%(str(i))
            self.driver.switch_to.context('WEBVIEW_com.mymoney.sms')
            if i ==7:
                self.driver.find_element_by_xpath(_view_more).click()
                time.sleep(1)
                self.driver.find_element_by_xpath(_hot_bank_btn).click()
                time.sleep(3)
                self.driver.keyevent(4)
                time.sleep(1)
            else:
                self.driver.find_element_by_xpath(_hot_bank_btn).click()
                time.sleep(3)
                self.driver.keyevent(4)
                time.sleep(1)
            return self

    def click_theme_choice(self):
        _theme_chocie_list = ['//*[@id="app"]/div/section[3]/div[2]/div[1]',
                              '//*[@id="app"]/div/section[3]/div[2]/div[2]/div[1]',
                              '//*[@id="app"]/div/section[3]/div[2]/div[2]/div[2]',
                              '//*[@id="app"]/div/section[3]/div[3]/div[1]',
                              '//*[@id="app"]/div/section[3]/div[3]/div[2]/div[1]',
                              '//*[@id="app"]/div/section[3]/div[3]/div[2]/div[2]']
        for i in _theme_chocie_list:
            self.driver.switch_to.context('WEBVIEW_com.mymoney.sms')
            self.driver.find_element_by_xpath(i).click()
            time.sleep(1)
            self.driver.keyevent(4)
            time.sleep(1)
        return self

    def card_divided(self):
        for i in range(6):
            _card_btn='//*[@id="app"]/div/section[4]/ul/li[%s]'%(str(i+1))
            self.driver.switch_to.context('WEBVIEW_com.mymoney.sms')
            self.driver.find_element_by_xpath(_card_btn).click()
            time.sleep(1)
            self.driver.keyevent(4)
            time.sleep(1)
        return self
    def act_recommand(self):
        for i in range(3):
            _act_btn = '//*[@id="app"]/div/section[5]/ul/li[%s]' % (str(i + 1))
            self.driver.switch_to.context('WEBVIEW_com.mymoney.sms')
            self.driver.find_element_by_xpath(_act_btn).click()
            time.sleep(1)
            self.driver.keyevent(4)
            time.sleep(1)
        return self

    def hot_recommand(self):
        for i in range(4):
            _act_btn = '//*[@id="app"]/div/section[6]/div[2]/div[%s]' % (str(i + 1))
            self.driver.switch_to.context('WEBVIEW_com.mymoney.sms')
            self.driver.find_element_by_xpath(_act_btn).click()
            time.sleep(1)
            self.driver.keyevent(4)
            time.sleep(1)
        return self

    def hot_rank(self):
        for i in range(15):
            _act_btn = '//*[@id="app"]/div/section[7]/div[2]/div[%s]/a' % (str(i + 1))
            self.driver.switch_to.context('WEBVIEW_com.mymoney.sms')
            self.driver.find_element_by_xpath(_act_btn).click()
            time.sleep(3)
            self.driver.keyevent(4)
            time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div').click()
        time.sleep(3)
        return self