# -*- coding: utf-8 -*-
"""
    :author: zyr
    :description:
    公告栏  get
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
        # print("成功进入贷款页面")
    @allure.feature('test_search')
    @allure.story('test_story')
    @allure.severity('normal')
    def test_ssj_debt_mywallet_notice(self):
        text = self.debt_page.find_notice()
        assert text != ""

    def teardown(self):
        App.quit()