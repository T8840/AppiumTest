# -*- coding: utf-8 -*-
"""
    :author: ATao
    :tag: 思考是个好东西！
    :description: 
"""

import time
from core.ui_appium.yaml_elements_driver  import YamlElementsDriver

class DebtMyWalletPage(YamlElementsDriver):
    def get_wallet_title_text(self):
        pass

    def get_wallet_record_flow(self):
        self.op_element('debt_wallet_record_flow')


    # def get_wallet_title_text(self):
    #     _id_wallet_title = (By.ID,"com.mymoney:id/sui_toolbar_back_title")
    #     # self.find_element(_id_wallet_title).get_attribute("text")
    #     return self.find_element(_id_wallet_title).get_attribute("text")

    # def get_wallet_record_flow(self):
    #     _id_wallet_flow_text = (By.XPATH,"//android.widget.TextView[@text='奖励记录']")
    #     self.find_element(_id_wallet_flow_text).click()
    #     return self
    #
    # def get_wallet_record_flow_title_text(self):
    #     _id_record_flow_title = (By.ID,"com.mymoney:id/sui_toolbar_back_title")
    #     return self.find_element(_id_record_flow_title).get_attribute("text")
    #
    # def get_debt_mywallet_best_act(self):
    #     self.switchContext('WEBVIEW_com.mymoney')
    #     text = self.driver.find_element_by_xpath('//div[@class="active-list-container"]/h2').get_attribute('innerHTML')
    #     return text
