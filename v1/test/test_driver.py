# -*- coding: utf-8 -*-
"""
    :author: ATao
    :description: 
"""

from core.ui_appium.yaml_elements_driver import YamlElementsDriver
from config import config
from appium import webdriver

configs = config['ssj']

driver = webdriver.Remote(configs.REMOTEHOST, configs.DESIRED_CAPS)
y = YamlElementsDriver(driver)