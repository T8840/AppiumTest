# -*- coding: utf-8 -*-
"""
    :author: zT
    :description:
"""

import pytest
import allure
import yaml
from pages.kn.app import App

class TestDemo:
    # search_data = yaml.safe_load(open("search.yaml", "r"))
    # print(search_data)

    def setup(self):
        self.debt_page=App.start().to_debt_page()

    @allure.feature('test_search')
    @allure.story('test_story')
    @allure.severity('normal')
    def test_click_no_card_alert(self):
        self.debt_page.click_no_card_alert()

    def teardown(self):
        App.quit()