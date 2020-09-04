# -*- coding: utf-8 -*-
"""
    :author: ATao
    :description: 
"""

from core.ui_appium.yaml_elements_driver  import YamlElementsDriver
import time
from .debt_mine_page import DebtMinePage

class DebtPage(YamlElementsDriver):

    # _icon_mine_locator=(By.XPATH,'//android.view.View[@content-desc="我的"]')
    # # _username_input_locator = (By.ID,"com.mymoney:id/recently_used_login_way_tv") #未登录情况
    # _content_desc_my_wallet = (By.XPATH,'//android.view.View[@content-desc="我的钱包"]')
    def to_debt_mine_page(self):
        """路由"""
        time.sleep(6)
        self.op_element('icon_mine')
        return DebtMinePage(self.driver,self.configs)

    def getIconName(self):
        return self.driver.get_screenshot_as_file('.')

    def click_my_wallet(self):
        self.op_element('my_wallet')
        time.sleep(2)
        return self


    #
    # def get_withdrawable_amount(self):
    #     self.switchContext('WEBVIEW_com.mymoney')
    #     text = self.driver.find_element_by_xpath('//span[@class="icon-tips"]/..').get_attribute('innerHTML')
    #     return text
    #
    # def withdrawable_close(self):
    #     self.switchContext('WEBVIEW_com.mymoney')
    #     self.driver.find_element_by_xpath('//span[@class="icon-tips"]').click()
    #     time.sleep(3)
    #     self.driver.find_element_by_xpath('//div[@class="ssui-dialog"]//div[@class="ssui-dialog__ft"]/a').click()
    #     time.sleep(2)
    #
    #
    # def find_notice(self):
    #     self.switchContext('WEBVIEW_com.mymoney')
    #     text = self.driver.find_element_by_xpath('//div[@class="notice-content"]//div[@class="text-wrap"]/div[@class="text"]/div[@class="text-inner"]').get_attribute("innerHTML")
    #     return text
    #
    # def click_withdraw_button(self):
    #     self.switchContext('WEBVIEW_com.mymoney')
    #     self.driver.find_element_by_xpath('//div[@class="btn"]/a').click()
    #     return self
    #
    # def find_withdraw_button_text(self):
    #     self.switchContext('WEBVIEW_com.mymoney')
    #     self.driver.find_element_by_xpath('//div[@class="btn"]/a').click()
    #     time.sleep(2)
    #     _id_title = (By.ID, "com.mymoney:id/sui_toolbar_back_title")
    #     self.switchContext('NATIVE_APP')
    #     time.sleep(1)
    #     return self.find_element(_id_title).get_attribute("text")
    #
    # def find_wd_withdraw_amount(self):
    #     self.switchContext('WEBVIEW_com.mymoney')
    #     self.driver.find_element_by_xpath('//div[@class="btn"]/a').click()
    #     time.sleep(2)
    #     print(self.getContext())
    #     time.sleep(3)
    #     self.driver.find_elements_by_xpath('//*[@id="app"]//div[@class="withdraw-container"]')
    #     # print(text)
    #     # return text
    #
    # def click_add_account(self):
    #     _xpath_add_account = (
    #     By.XPATH, "//android.view.View[contains(@content-desc,'元')]/following-sibling::android.view.View[1]")
    #     self.find_element(_xpath_add_account).click()
    #
    # def find_add_account_button(self):
    #     _id_title = (By.ID,"com.mymoney:id/sui_toolbar_back_title")
    #     self.click_add_account()
    #     time.sleep(2)
    #     return self.find_element(_id_title).get_attribute("text")
    #
    # def find_add_card(self):
    #     _xpath_add_card_button = (By.XPATH,"//android.view.View[@content-desc='添加银行卡']")
    #     self.find_element(_xpath_add_card_button).click()
    #     time.sleep(2)
    #     _xpath_comfirm_add_buttom = (By.XPATH,"//android.view.View[@content-desc='确认添加']")
    #     self.find_element(_xpath_comfirm_add_buttom)
    #
    # def add_card_comfirm(self):
    #     self.find_add_card() #到达了正确的地方
    #     time.sleep(4)
    #     #查找四个正确的元素   "//android.view.View[contains(@text, 'xxx')]"
    #     _xpath_name = (By.XPATH,'//android.widget.EditText[contains(@text,"输入您的真实姓名")]')
    #     _xpath_idNumber = (By.XPATH,'//android.widget.EditText[contains(@text,"输入身份证号")]')
    #     _xpath_cardNumber = (By.XPATH,'//android.widget.EditText[contains(@text,"输入您的银行卡号")]')
    #     _xpath_phone = (By.XPATH,'//android.widget.EditText[contains(@text,"输入银行卡绑定的手机号")]')
    #
    #     self.find_element(_xpath_name).send_keys("zyr")
    #     self.find_element(_xpath_idNumber).send_keys("361127200306065733")
    #     self.find_element(_xpath_cardNumber).send_keys("6216612000010874123")
    #     self.find_element(_xpath_phone).send_keys("18166041111")
    #     time.sleep(1)
    #
    #     _xpath_confirm_button = (By.XPATH,"	//android.webkit.WebView[@content-desc='支付方式列表']/android.view.View/android.view.View[10]")
    #     self.find_element(_xpath_confirm_button).click()
    #
    #     #会弹出是否添加银行卡的确认信息，点击确认
    #     _xpath_add_comfirm = (By.XPATH,'//android.widget.Button[@content-desc="确认"]')
    #     self.find_element(_xpath_add_comfirm).click()
    #     time.sleep(1)
    #     #点击确认，弹出错误提示弹窗

if __name__ == "__main__":
    pass
