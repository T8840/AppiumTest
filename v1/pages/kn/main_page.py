# -*- coding: utf-8 -*-
"""
    :author: ATao
    :description: 对象库层
                    由此main_page页面进行分转到不同子页面
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from core.ui_appium.driver import Driver
from .invest_page import InvestPage
from .debt_page import DebtPage
from .create_card_page import CreateCardPage
import time

class MainPage(Driver):

    _debt_icon_locator = (By.ID, "com.mymoney.sms:id/img_applyLoan")
    _invest_icon_locator = (By.ID, "com.mymoney:id/main_top_nav_button_second")
    _enter_create_card = (By.ID, "com.mymoney.sms:id/apply_card_img")

    def to_invest_page(self):
        """前往投资页面"""

        self.find_element_and_click(self._invest_icon_locator)
        return InvestPage(self.driver)

    def to_debt_page(self):
        """前往贷款页面"""
        time.sleep(3)
        self.find_element_and_click(self._debt_icon_locator)
        time.sleep(3)
        return DebtPage(self.driver)

    def to_create_card_page(self):
        """前往办卡页面"""
        self.find_element_and_click(self._enter_create_card)
        time.sleep(3)
        return CreateCardPage(self.driver)
