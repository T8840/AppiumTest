# -*- coding: utf-8 -*-
"""
    :author: ATao
    :description: 配置文件
"""

from appium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from config import config
from core.android.check_apk import CheckAppPackage
from .main_page import MainPage


class App:
    """继承Driver对象与其操作元素的通用方法"""
    driver: WebDriver = None
    configs = config['kn']

    @classmethod
    def check_app(cls):
        """检查手机是否安装"""
        """从File Browser下载Apk应用
                校验手机上是否存在该Apk，并校验版本是否一致
                一致，直接跳过
                不一致，会进行下载，安装，并删除"""
        filebrowse_share_url = cls.configs.FILE_BROWSER_SHARE_URL
        package_name = cls.configs.DESIRED_CAPS["appPackage"]
        with CheckAppPackage(filebrowse_share_url, package_name) as D:
            D.check()


    @classmethod
    def start(cls):
        """启动函数"""
        cls.check_app()
        desired_caps = {}
        desired_caps = cls.configs.DESIRED_CAPS
        remoteHost = cls.configs.REMOTEHOST
        cls.driver = webdriver.Remote(remoteHost, desired_caps)
        cls.driver.implicitly_wait(10)

        # 完成页面初始化操作
        _agree_permission_locator = (By.ID, "com.mymoney.sms:id/sui_dialog_positive_btn")
        _next_page_locator = (By.ID, "com.mymoney.sms:id/next_page_bt")
        _skip_locator = (By.ID,"com.mymoney.sms:id/skip_tv")
        _close_sms_dia_locator = (By.ID, "com.mymoney.sms:id/close_btn")

        cls.driver.find_element(*_agree_permission_locator).click()
        cls.driver.find_element(*_next_page_locator).click()
        cls.driver.find_element(*_skip_locator).click()
        cls.driver.find_element(*_close_sms_dia_locator).click()
        return MainPage(cls.driver)

    @classmethod
    def quit(cls):
        cls.driver.quit()