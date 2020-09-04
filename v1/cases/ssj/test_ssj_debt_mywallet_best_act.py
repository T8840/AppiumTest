# -*- coding: utf-8 -*-
"""
    :author: zyr
    :description:
    奖励记录 get
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

    @allure.feature('test_search')
    @allure.story('test_story')
    @allure.severity('normal')
    def test_ssj_debt_mywallet_best_act(self):
        text = self.debt_page.get_debt_mywallet_best_act()
        assert text == '精品活动'

    def teardown(self):
        App.quit()