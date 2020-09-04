# -*- coding: utf-8 -*-
"""
    :author: zyr
    :description:
    提现金额-余额  待测试
"""

import pytest
import allure
import yaml
from pages.ssj.app import App

class TestDemo:

    def setup(self):
        self.debt_page=App.start().to_debt_page()
        self.debt_page.click_icon_mine_to_login()
        self.debt_page.click_my_wallet()
        # self.debt_page.click_withdraw_button()
        # print("成功进入提现页面")
    @allure.feature('test_search')
    @allure.story('test_story')
    @allure.severity('normal')
    def test_ssj_debt_mywallet_wd_amount(self):
        text = self.debt_page.find_wd_withdraw_amount()
        # assert '金额' in text

    def teardown(self):
        App.quit()