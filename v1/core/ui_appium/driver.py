# -*- coding: utf-8 -*-
"""
    :author: ATao
    :description: 操作页面元素API的封装
"""

import os
from appium import webdriver

from enum import Enum
from selenium.webdriver.common.by import By
import selenium.common.exceptions as SeleniumException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from core.log import getLogger
from config import config


logger = getLogger()

# class Singleton(object):
#     """单例模式
#     """
#     Action = None
#     def __new__(cls, *args, **kw):
#         if not hasattr(cls, '_instance'):
#             host = "http://localhost:4723/wd/hub"
#             desired_caps = {'appActivity': '.SplashActivity',
#                             'appPackage': 'com.sina.weibo',
#                             'autoGrantPermissions': True,
#                             'autoLaunch': False,
#                             'automationName': 'UiAutomator2',
#                             'deviceName': udid,
#                             'noReset': True,
#                             'platformName': 'Android',
#                             'platformVersion': '9.0',
#                             'udid': udid}
#
#             driver = webdriver.Remote(host, desired_caps)
#             # Action = ElementActions(driver, ADB, Parameterdict=desired_caps)
#             orig = super(Singleton, cls)
#             cls._instance = orig.__new__(cls, *args, **kw)
#             # cls._instance.Action = Action
#         return cls._instance



class Driver:
    _black_list = [
        (By.ID, "image_cancel"),
        (By.ID, "tips")
    ]
    common = config['common']

    def __init__(self, driver: WebDriver,configs):
        self.driver = driver
        self.configs = configs

    def find_element(self, locator):
        logger.info(f"正在查找元素：{locator[1]}")
        try:
            return self.driver.find_element(*locator)
        except:
            self.handle_exception()
            # self.find_element(locator)
            return self.driver.find_element(*locator)

    def find_element_and_click(self, locator):
        logger.info(f"正在查找并点击元素：{locator[1]}")
        try:
            # 如果click也有异常，可以这样处理
            self.find_element(locator).click()
        except:
            self.handle_exception()
            self.find_element(locator).click()

    def handle_exception(self):
        """触发异常时先检查是否有黑名单中元素存在并处理"""
        print("Warn：触发exception！")
        logger.error("Warn：触发exception！")
        # WebDriver.implicitly_wait(0)
        for locator in self._black_list:
            print(locator)
            elements = self.driver.find_elements(*locator)
            if len(elements) >= 1:
                # todo: 不是所有的弹框处理都是要点击弹框，可根据业务需要自行封装
                elements[0].click()
            else:
                print("%s not found" % str(locator))

