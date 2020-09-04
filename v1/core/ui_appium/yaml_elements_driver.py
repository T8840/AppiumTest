# -*- coding: utf-8 -*-
"""
    :author: ATao
    :tag: 思考是个好东西！
    :description: 
"""

from core.ui_appium.driver import Driver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from utils.operateYaml import readYaml,get_dict_value
from core.log import getLogger

logger = getLogger()

class YamlElementsDriver(Driver):
    def __init__(self,driver:WebDriver,configs):
        super(YamlElementsDriver,self).__init__(driver,configs)
        self.yaml_data = readYaml(self.configs.YAML_ELEMENTS_PATH)


    def get_elements_info(self, element_name):
        elements_info = get_dict_value(self.yaml_data, target_key=element_name)[0]
        logger.info('从YAML中获取到元素信息：%s' % elements_info)
        return elements_info

    def op_element(self, element_name: str) ->None:
        """
        传入yaml中定义的元素名称：
        """
        element_info = self.get_elements_info(element_name)
        logger.info('开始执行操作：%s,%s' % (element_info[0], element_info[1]))
        if element_info[0] == 'id':
            self.driver.find_element(value=element_info[1]).click()
        if element_info[0] == 'xpath':
            self.driver.find_element(by=By.XPATH,value=element_info[1]).click()

        # if element_info:
        #     if element_name[2] == 'click':
        #         logger.info('开始执行操作：%s,%s'%(element_info[0],element_info[1]))
        #         self.driver.find_element_(by=element_info[0], value=element_info[1])
        #     return True
        # else:
        #     logger.error("查找元素出现问题了")
        #     raise Exception
            # return False


    # def elements_by(self,element_info:list) ->dict:
    #     elements = {
    #         common.find_element_by_id: lambda: self.driver.find_element_by_id(element_info["element_info"]),
    #         common.find_elements_by_id: lambda: self.driver.find_elements_by_id(element_info["element_info"]),
    #         common.find_element_by_xpath: lambda: self.driver.find_element_by_xpath(element_info["element_info"]),
    #         common.find_element_by_name: lambda: self.driver.find_element_by_name(element_info['name']),
    #         common.find_elements_by_name: lambda: self.driver.find_elements_by_name(element_info['name'])[element_info['index']],
    #         common.find_element_by_class_name: lambda: self.driver.find_element_by_class_name(element_info['element_info']),
    #         common.find_elements_by_class_name: lambda: self.driver.find_elements_by_class_name(element_info['element_info'])[
    #             element_info['index']]
    #     }
    #     return elements[element_info["find_type"]]()


    # def find_element(self,element_info:list) -> bool:
    #     try:
    #         WebDriverWait(self.driver, common.WAIT_TIME).until(lambda x: self.elements_by(element_info))
    #         return True
    #     except SeleniumException.TimeoutException:
    #         return False
    #     except SeleniumException.NoSuchElementException:
    #         logger.error("找不到数据")
    #         return False
