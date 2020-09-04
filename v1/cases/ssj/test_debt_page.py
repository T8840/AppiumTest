# -*- coding: utf-8 -*-
"""
    :author: ATao
    :description: 
"""

import pytest
import allure
from pages.ssj.app import App

class TestDemo:

    def setup(self):
        # self.debt_page=App.start().to_debt_page()
        self.debt_wallet_page=App.start().to_debt_page().to_wallet_page()


    # def test_click_my_wallet(self):
    #     self.debt_page.click_my_wallet()
    #     import time
    #     time.sleep(5)

    def test_debt_wallet_record_flow(self):
        self.debt_wallet_page.get_wallet_record_flow()
        import time
        time.sleep(5)

    def teardown(self):
        App.quit()
