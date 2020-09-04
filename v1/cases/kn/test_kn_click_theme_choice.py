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
        self.create_card_page=App.start().to_create_card_page()

    @allure.feature('test_search')
    @allure.story('test_story')
    @allure.severity('normal')
    def test_click_theme_choice(self):
        self.create_card_page.click_theme_choice()

    def teardown(self):
        App.quit()
