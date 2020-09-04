# -*- coding: utf-8 -*-
"""
    :author: zyr
    :description:
    奖励记录-是安卓的原生元素，可以直接通过appium定位 get
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
    def test_ssj_to_mywallet_record_flow(self):
        self.debt_page.get_wallet_record_flow()
        text = self.debt_page.get_wallet_record_flow_title_text()
        assert text == "奖励记录"

    def teardown(self):
        App.quit()