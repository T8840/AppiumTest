# -*- coding: utf-8 -*-
"""
    :author: ATao
    :tag: 思考是个好东西！
    :description: 
"""
import time
from .debt_my_wallet_page import DebtMyWalletPage
from core.ui_appium.yaml_elements_driver  import YamlElementsDriver

class DebtMinePage(YamlElementsDriver):

    def to_debt_my_wallet(self):
        """路由"""
        time.sleep(5)
        self.op_element('icon_debt_my_wallet')
        return DebtMyWalletPage(self.driver, self.configs)
