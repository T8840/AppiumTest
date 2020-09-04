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
from core.log import getLogger
from .main_page import MainPage
import time
logger = getLogger()

class App:
    """继承Driver对象与其操作元素的通用方法"""
    driver: WebDriver = None
    configs = config['ssj']

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
        # cls.check_app()
        desired_caps = {}
        desired_caps = cls.configs.DESIRED_CAPS
        remoteHost = cls.configs.REMOTEHOST
        cls.driver = webdriver.Remote(remoteHost, desired_caps)
        cls.driver.implicitly_wait(10)

        # 完成页面初始化操作，由于在参数中配置了 noRset选项，所以在编写过程中，并不会做初始化操作，下面这一部分是的元素可能定位不到，编写用例时候可以注释
        # logger.info("正在完成APP初始化操作！")
        # _agree_permission_locator = (By.ID, "com.mymoney:id/confirmBtn")
        # _permision_toast_locator = (By.ID, "com.android.packageinstaller:id/permission_allow_button")
        # _next_page_locator = (By.ID, "com.mymoney:id/next_btn")
        # _start_sui_locator = (By.ID, "com.mymoney:id/begin_btn")
        #
        # cls.driver.find_element(*_agree_permission_locator).click()
        # cls.driver.find_element(*_next_page_locator).click()
        # cls.driver.find_element(*_next_page_locator).click()
        # cls.driver.find_element(*_start_sui_locator).click()
        logger.info("已完成APP初始化操作，开始进入主页面！")
        time.sleep(5)
        return MainPage(cls.driver,cls.configs)

    @classmethod
    def quit(cls):
        cls.driver.quit()