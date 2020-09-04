# -*- coding: utf-8 -*-
"""
    :author: zyr
    :description:
首先确保你的随手记主页面存在贷款这个Tab
"""

import pytest
import allure
import yaml
from pages.ssj.app import App

class TestDemo:

    def setup(self):
        self.debt_page=App.start().to_debt_page()
        self.debt_page.click_icon_mine_to_login()
        # print("成功进入贷款页面")
    @allure.feature('test_search')
    @allure.story('test_story')
    @allure.severity('normal')
    def test_ssj_to_my_wallet_page(self):
        self.debt_page.click_my_wallet()
        text = self.debt_page.get_wallet_title_text()
        assert text == "我的钱包"

    def teardown(self):
        App.quit()