"""
添加收款账户,selenium重写
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
        self.debt_page.click_withdraw_button()

        # print("成功进入提现页面")
    @allure.feature('test_search')
    @allure.story('test_story')
    @allure.severity('normal')
    def test_ssj_debt_mywallet_add_account(self):
        text = self.debt_page.find_add_account_button()
        assert text == "支付方式列表"

    def teardown(self):
        App.quit()