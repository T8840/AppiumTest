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
    def test_act_recommand(self):
        self.create_card_page.act_recommand()

    def teardown(self):
        App.quit()
