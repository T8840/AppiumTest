# -*- coding: utf-8 -*-
"""
    :author: ATao
    :description: 
"""

from selenium.webdriver.common.by import By
from core.ui_appium.driver import Driver

class InvestPage(Driver):


    _icon_locator=(By.ID,"")

    def getIconName(self):
        return self.driver.get_screenshot_as_file('.')

    # def search(self, keyword):
    #     self.find_element(self._input_locator).send_keys(keyword)
    #     self.find_element(self._name_locator).click()
    #     return self
    #
    # def get_current_price(self):
    #     return float(self.driver.find_element_by_id("current_price").text)

