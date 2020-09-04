# -*- coding: utf-8 -*-
"""
    :author: ATao
    :description: 对象库层
                    由此main_page页面进行分转到不同子页面
"""
import inspect
from core.ui_appium.yaml_elements_driver import YamlElementsDriver
from .invest_page import InvestPage
from .debt_page import DebtPage

class MainPage(YamlElementsDriver):
    # 结合真实页面情况来显示，这里切换到家庭账本2

    def to_invest_page(self):
        """前往投资页面"""
    #     # inspect.stack()
        self.op_element('icon_invest')
        return InvestPage(self.driver,self.configs)

    def to_debt_page(self):
        """前往贷款页面"""
        # _debt_icon_locator = (By.ID, "com.mymoney:id/main_top_nav_button_first")
        # self.find_element_and_click(_debt_icon_locator)
        self.op_element('icon_debt')
        return DebtPage(self.driver,self.configs)

    def to_login_page(self):
        """前往登录页面"""
        pass