"""
钱包页-立即提现-添加账户-添加银行卡-确认添加  selenium重写
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
        self.debt_page.click_add_account()
        # print("成功进入添加银行卡页面")
    @allure.feature('test_search')
    @allure.story('test_story')
    @allure.severity('normal')
    def test_ssj_debt_mywallet_wd_add_card(self):
        self.debt_page.add_card_comfirm()
        # 能查找到元素就表示成功

    def teardown(self):
        App.quit()