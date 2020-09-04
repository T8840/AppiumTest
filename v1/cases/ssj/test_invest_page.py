# -*- coding: utf-8 -*-
"""
    :author: ATao
    :description: 业务层
"""

from pages.ssj.app import App

class TestDemo:
    def setup(self):
        self.invest_page=App.start().to_invest_page()

    # @allure.feature('test_search')
    # @allure.story('test_story')
    # @allure.severity('normal')
    def test_invest_page_icon(self):
        self.invest_page.getIconName()



    def teardown(self):
        App.quit()

