# -*- coding: utf-8 -*-
"""
    :author: ATao
    :description: 操作页面元素API的封装
"""

import os
from appium import webdriver
from time import sleep
from enum import Enum
from selenium.webdriver.common.by import By
import selenium.common.exceptions as SeleniumException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from core.log import getLogger
from config import config
logger = getLogger()
common = config['prod']

# 封装常用的标签
def elements_by(mOperate, cts):
    elements = {
        common.find_element_by_id : lambda :cts.find_element_by_id(mOperate["element_info"]),
        common.find_elements_by_id : lambda :cts.find_elements_by_id(mOperate["element_info"]),
        common.find_element_by_xpath: lambda :cts.find_element_by_xpath(mOperate["element_info"]),
        common.find_element_by_name: lambda :cts.find_element_by_name(mOperate['name']),
        common.find_elements_by_name: lambda :cts.find_elements_by_name(mOperate['name'])[mOperate['index']],
        common.find_element_by_class_name: lambda :cts.find_element_by_class_name(mOperate['element_info']),
        common.find_elements_by_class_name: lambda :cts.find_elements_by_class_name(mOperate['element_info'])[mOperate['index']]
    }
    return elements[mOperate["find_type"]]()


class Driver:
    _black_list = [
        (By.ID, "image_cancel"),
        (By.ID, "tips")
    ]

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find_element(self,opGroup:dict) -> bool:
        '''
       查找元素.mOperate是字典
       operate_type：对应的操作
       element_info：元素详情
       find_type: find类型
       '''
        try:
            WebDriverWait(self.driver, common.WAIT_TIME).until(lambda x: elements_by(opGroup, self.driver))
            return True
        except SeleniumException.TimeoutException:
            return False
        except SeleniumException.NoSuchElementException:
            logger.error("找不到数据")
            return False

    # def find_element(self, locator):
    #     logger.info(f"正在查找元素：{locator[1]}")
    #     try:
    #         return self.driver.find_element(*locator)
    #     except:
    #         self.handle_exception()
    #         # self.find_element(locator)
    #         return self.driver.find_element(*locator)

    def find_element_and_click(self, locator):
        logger.info(f"正在查找并点击元素：{locator[1]}")
        try:
            # 如果click也有异常，可以这样处理
            self.find_element(locator).click()
        except:
            self.handle_exception()
            self.find_element(locator).click()

    def handle_exception(self):
        print(":exception")
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

    # WebDriver.implicitly_wait(10)
    """
    给定控件的xpatch, id 或者name来查找控件

    :Args:
         - controlInfo: 控件的信息，可以是xpath,id或者其他属性

    :Return:
        如果找到控件，返回第一个

    :Usage:
        self.findElement(controlInfo)
    """

    def findElement(self, controlInfo):
        element = ""
        if (controlInfo.startswith("//")):
            element = self.driver.find_element_by_xpath(controlInfo)
        elif (":id/" in controlInfo or ":string/" in controlInfo):
            element = self.driver.find_element_by_id(controlInfo)
        else:
            # 剩下的字符串没有特点，无法区分，因此先尝试通过名称查找
            try:
                element = self.driver.find_element_by_name(controlInfo)
            except:
                try:
                    # 如果通过名称不能找到则通过class name查找
                    element = self.driver.find_element_by_class_name(controlInfo)
                except:
                    # 最后通过accessibility_id查找
                    element = self.driver.find_element_by_accessibility_id(controlInfo)

        return element

    """
    给定控件的xpatch, id 或者name来查找控件

    :Args:
         - controlInfo: 控件的信息，可以是xpath,id或者其他属性

    :Return:
        返回所有满足条件的控件，返回的类型是一个列表

    :Usage:
        self.findElements(controlInfo)
    """

    def findElements(self, controlInfo):
        elements = ""
        if (controlInfo.startswith("//")):
            elements = self.driver.find_elements_by_xpath(controlInfo)
        elif (":id/" in controlInfo):
            elements = self.driver.find_elements_by_id(controlInfo)
        else:
            elements = self.driver.find_elements_by_name(controlInfo)
            if (len(elements) == 0):
                try:
                    elements = self.driver.find_elements_by_class_name(controlInfo)
                except:
                    elements = self.driver.find_element_by_accessibility_id(controlInfo)
        return elements

    """
    在一个已知的控件中通过给定控件的xpatch, id 或者name来查找子控件

    :Args:
        - parentElement: 父控件，是一个已知的WebElement
        - childElementInfo: 子控件的信息，可以是xpath,id或者其他属性

    :Return:
        如果找到控件，返回第一个

    :Usage:
        self.findElement(controlInfo)
    """

    def findElementInParentElement(self, parentElement, childElementInfo):
        element = ""
        if (childElementInfo.startswith("//")):
            element = parentElement.find_element_by_xpath(childElementInfo)
        elif (":id/" in childElementInfo):
            element = parentElement.find_element_by_id(childElementInfo)
        else:
            # 剩下的字符串没有特点，无法区分，因此先尝试通过名称查找
            try:
                element = parentElement.find_element_by_name(childElementInfo)
            except:
                # 如果通过名称不能找到则通过class name查找
                element = parentElement.find_element_by_class_name(childElementInfo)

        return element

    """
    在一个已知的控件中通过给定控件的xpatch, id 或者name来查找子控件

    :Args:
        - parentElement: 父控件，是一个已知的WebElement
        - childElementInfo: 子控件的信息，可以是xpath,id或者其他属性

    :Return:
        如果找到控件，返回所有符合条件的控件

    :Usage:
        self.findElementsInParentElement(parentElement, controlInfo)
    """

    def findElementsInParentElement(self, parentElement, childElementInfo):
        elements = ""
        if (childElementInfo.startswith("//")):
            elements = parentElement.find_elements_by_xpath(childElementInfo)
        elif (":id/" in childElementInfo):
            elements = parentElement.find_elements_by_id(childElementInfo)
        else:
            # 剩下的字符串没有特点，无法区分，因此先尝试通过名称查找
            elements = parentElement.find_elements_by_name(childElementInfo)
            if (len(elements) == 0):
                # 如果通过名称不能找到则通过class name查找
                elements = parentElement.find_elements_by_class_name(childElementInfo)

        return elements

    """
    通过UIAutomator的uia_string来查找控件

    :Args:
        -uia_string: UiSelector相关的代码，参考http://developer.android.com/
        tools/help/uiautomator/UiSelector.html#fromParent%28com.android.uiautomator.core.UiSelector%29

    :Return:
        -找到的控件

    :usage:
        self.findElementByUIAutomator(new UiSelector().(android.widget.LinearLayout))
    """

    def findElementByUIAutomator(self, uia_string):
        return self.driver.find_element_by_android_uiautomator(uia_string)

    """
    滑动操作

    :Args:
         - x1,y1,x2,y2： 滑动操作的起点和终点的坐标

    :Usage:
        self.swipe(50, 50, 400, 400)
    """

    def flick(self, x1, y1, x2, y2):
        self.driver.flick(x1, y1, x2, y2)

    """
    滑动操作

    :Args:
         - x1,y1,x2,y2： 滑动操作的起点和终点的坐标
         - peroid: 多长时间内完成该操作,单位是毫秒

    :Usage:
        self.swipe(50, 50, 400, 400, 500)
    """

    def getSize(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return (x, y)

        # 屏幕向上滑动

    def swipe_up(self, t):
        l = self.getSize()
        x1 = int(l[0] * 0.5)  # x坐标
        y1 = int(l[1] * 0.75)  # 起始y坐标
        y2 = int(l[1] * 0.25)  # 终点y坐标
        self.driver.swipe(x1, y1, x1, y2, t)

    # 屏幕向下滑动
    def swipe_down(self, t):
        l = self.getSize()
        x1 = int(l[0] * 0.5)  # x坐标
        y1 = int(l[1] * 0.25)  # 起始y坐标
        y2 = int(l[1] * 0.75)  # 终点y坐标
        self.driver.swipe(x1, y1, x1, y2, t)

    # 屏幕向左滑动
    def swipe_left(self, t):
        l = self.getSize()
        x1 = int(l[0] * 0.75)
        y1 = int(l[1] * 0.5)
        x2 = int(l[0] * 0.05)
        self.driver.swipe(x1, y1, x2, y1, t)

    # 屏幕向右滑动
    def swipe_right(self, t):
        l = self.getSize()
        x1 = int(l[0] * 0.05)
        y1 = int(l[1] * 0.5)
        x2 = int(l[0] * 0.75)
        self.driver.swipe(x1, y1, x2, y1, t)

    def tap(self, x, y):
        self.driver.tap([(x, y)])

    """
    长按点击操作
    :Args:
     - x,y： 长按点的坐标
     - peroid: 多长时间内完成该操作,单位是毫秒

    :Usage:
        self.longPress(50, 50, 500)
    """

    def longPress(self, x, y, peroid):
        self.driver.tap([(x, y)], peroid)

    def pinch(self):
        self.driver.pinch()

    """
    点击某一个控件，如果改控件不存在则会抛出异常

    :Args:
         - elementInfo: 控件的信息，可以是xpath,id或者其他属性

    :Usage:
        self.clickElement(elementInfo)
    """

    def clickElement(self, elementInfo):
        element = self.findElement(elementInfo)
        element.click()

    """
    获取某个控件显示的文本，如果该控件不能找到则会抛出异常

    :Args:
         - elementInfo: 控件的信息，可以是xpath,id或者其他属性

    :Return:
        返回该控件显示的文本

    :Usage:
        self.getTextOfElement(elementInfo)

    """

    def getTextOfElement(self, elementInfo,period):
        for i in range(0, period):
            sleep(1)
            try:
                element = self.findElement(elementInfo)
                return element.text
            except:
                continue
        raise Exception("Cannot find %s in %d seconds" % (elementInfo, period))

    """
    清除文本框里面的文本

    :Usage:
        self.clearTextEdit(elementInfo)
    """

    def clearTextEdit(self, elementInfo):
        element = self.findElement(elementInfo)
        element.clear()

    """
    按返回键

    :Usage:
        self.pressBackKey()
    """

    def pressBackKey(self):
        # code码参考Android的官网的keycode
        self.driver.press_keycode(4)

    """
    等待某个控件显示

    :Args:
         - elementInfo: 控件的信息，可以是xpath,id或者其他属性
         - period：等待的秒数

    :Usage:
        self.waitForElement(elementInfo, 3)
    """

    def waitForElement(self, elementInfo, period):
        for i in range(0, period):
            sleep(1)
            try:
                self.findElement(elementInfo)
                return
            except:
                continue

        raise Exception("Cannot find %s in %d seconds" % (elementInfo, period))

    """
       等待某个控件显示并点击

       :Args:
            - elementInfo: 控件的信息，可以是xpath,id或者其他属性
            - period：等待的秒数

       :Usage:
           self.clickWaitForElement(elementInfo, 3)
       """
    def clickWaitForElement(self, elementInfo, period=2):
        for i in range(0, period):
            sleep(1)
            try:
                self.clickElement(elementInfo)
                return
            except:
                continue

        raise Exception("Cannot find %s in %d seconds" % (elementInfo, period))

    """
          等待某个控件显示并输入文本

          :Args:
               - elementInfo: 控件的信息，可以是xpath,id或者其他属性
               - period：等待的秒数

          :Usage:
              self.sendKeyOnElement(elementInfo,'username' 3)
    """

    def sendKeyOnElement(self,elementInfo, text,period):
        for i in range(0, period):
            sleep(1)
            try:
                self.findElement(elementInfo).send_keys(text)
                return
            except:
                continue

        raise Exception("Cannot find %s in %d seconds" % (elementInfo, period))

    # def etPageSource(self):
    #     self.driver.getPageSource()

    """
    等待某个控件不再显示

    :Args:
         - elementInfo: 控件的信息，可以是xpath,id或者其他属性
         - period：等待的秒数

    :Usage:
        self.waitForElementNotPresent(elementInfo, 3)
    """

    def waitForElementNotPresent(self, elementInfo, period):
        for i in range(0, period):
            sleep(1)
            # 不存在了则返回
            if (not self.checkElementIsShown(elementInfo)):
                return
            else:
                continue

        raise Exception("Cannot find %s in %d seconds" % (elementInfo, period))

    """
    判断某个控件是否显示

    :Args:
         - elementInfo: 控件的信息，可以是xpath,id或者其他属性
    :Return:
        True: 如果当前画面中期望的控件能被找到

    :Usage:
        self.checkElementIsShown(elementInfo)
    """

    def checkElementIsShown(self, elementInfo):
        try:
            self.findElement(elementInfo)
            return True
        except:
            return False

    """
    判断某个控件是否显示在另外一个控件中

    :Args:
        - parentElement: 父控件，是一个已知的WebElement
        - childElementInfo: 子控件的信息，可以是xpath,id或者其他属性
    :Return:
        True: 如果当前画面中期望的控件能被找到

    :Usage:
        self.checkElementShownInParentElement(elementInfo)
    """

    def checkElementShownInParentElement(self, parentElement, childElementInfo):
        try:
            self.findElementInParentElement(parentElement, childElementInfo)
            return True
        except:
            return False

    """
    判断某个控件是否被选中

    :Args:
         - elementInfo: 控件的信息，可以是xpath,id或者其他属性
    :Return:
        True: 如果当前画面中期望的控件能被选中

    :Usage:
        self.checkElementIsSelected(elementInfo)
    """

    def checkElementIsSelected(self, elementInfo):
        element = self.findElement(elementInfo)
        return element.is_selected()

    """
    判断某个开关控件是否被选中

    :Args:
         - elementInfo: 控件的信息，可以是xpath,id或者其他属性
    :Return:
        True: 如果当前画面中期望的控件能被选中

    :Usage:
        self.checkElementIsChecked(elementInfo)
    """

    def checkElementIsChecked(self, elementInfo):
        element = self.findElement(elementInfo)
        if (element.get_attribute("checked") == "false"):
            return False
        else:
            return True

    """
    判断摸个控件是否enabled
    :Args:
         - elementInfo: 控件的信息，可以是xpath,id或者其他属性
    :Return:
        True: 如果当前画面中期望的控件enabled

    :Usage:
        self.checkElementIsEnabled(elementInfo)
    """

    def checkElementIsEnabled(self, elementInfo):
        element = self.findElement(elementInfo)
        return element.get_attribute("enabled")

    def startAcitivity(self, app_package,app_activity):
        return self.driver.start_activity(app_package, app_activity, )

    """
    获取当前的Activity

    :Return:
        当前Activity的名称
    """

    def getCurrentActivity(self):
        return self.driver.current_activity

    """
       获取当前页面的resource

       :Return:
           当前当前页面的resource，返回xml格式
    """
    def getPageSource(self):
        return self.driver.page_source

    """
    等待某一个Activity显示
    备注：不确定是否适用于ios

    :Args:
        -activityName: 某acitivity的名称
        -period: 等待的时间，秒数
    """

    def waitForActivity(self, activityName, period):
        for i in range(0, period):
            sleep(1)
            try:
                if (activityName in self.getCurrentActivity()):
                    return
            except:
                continue

        raise Exception("Cannot find the activity %s in %d seconds" % (activityName, period))

    """
    保存当前手机的屏幕截图到电脑上指定位置

    :Args:
         - pathOnPC: 电脑上保存图片的位置

    :Usage:
        self.saveScreenshot("c:\test_POI1.jpg")
    """

    def saveScreenshot(self, pathOnPC):
        self.driver.save_screenshot(pathOnPC)

    def setNetwork(self, netType):
        pass

    """
    安装测试程序
    """

    def InstallApp(self,apkPath):
        self.driver.install_app(apkPath)

    """
    卸载测试程序
    """
    def UninstallApp(self,app_id):
        self.driver.remove_app(app_id)

    """
    启动测试程序
    """

    def launchApp(self):
        self.driver.launch_app()

    """
    关闭测试程序
    """

    def closeApp(self):
        self.driver.close_app()

    """
    获取测试设备的OS

    :Return: Android或者ios
    """

    def getDeviceOs(self):
        return self.desired_caps['platformName']

    """
    只打开wifi连接
    """

    def enableWifiOnly(self):
        if ((self.driver.network_connection & 0x2) == 2):
            return
        else:
            self.driver.set_network_connection(ConnectionType.WIFI_ONLY)

    """
    只打开数据连接
    """

    def enableDataOnly(self):
        if (int(self.driver.network_connection & 4) == 4):
            return
        else:
            self.driver.set_network_connection(ConnectionType.DATA_ONLY)

    """
    关闭所有网络连接
    """

    def disableAllConnection(self):
        self.driver.set_network_connection(ConnectionType.NO_CONNECTION)

    """
    获取context
    """

    def getContext(self):
        #self.driver.contexts
        return self.driver.current_context
        # self.driver.context()

    """
        获取contexts
    """
    def getContexts(self):
        return self.driver.contexts

    """
        切换context
    """
    def switchContext(self, contextName):
        self.driver.switch_to.context(contextName)

    def accpect(self):
        pass

    """
    打开所有的网络连接
    """

    def enableAllConnection(self):
        self.driver.set_network_connection(ConnectionType.ALL_NETWORK_ON)


"""
Connection types are specified here:
    https://code.google.com/p/selenium/source/browse/spec-draft.md?repo=mobile#120
    Value (Alias)      | Data | Wifi | Airplane Mode
    -------------------------------------------------
    0 (None)           | 0    | 0    | 0
    1 (Airplane Mode)  | 0    | 0    | 1
    2 (Wifi only)      | 0    | 1    | 0
    4 (Data only)      | 1    | 0    | 0
    6 (All network on) | 1    | 1    | 0
"""


class ConnectionType(Enum):
    NO_CONNECTION = 0
    AIRPLANE_MODE = 1
    WIFI_ONLY = 2
    DATA_ONLY = 4
    ALL_NETWORK_ON = 6
