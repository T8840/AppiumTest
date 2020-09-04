# -*- coding: utf-8 -*-
"""
    :author: ATao
    :description: 
"""

import sys
import pytest
import allure
import os

@pytest.fixture(scope='function')
def login():
    print("登录")

@allure.feature('加入购物车')
def test_1(login):
    """将苹果加入购物车"""
    print("测试用例1")

@allure.feature('加入购物车')
def test_2():
    """将橘子加入购物车"""
    print("测试用例2")


def m_run(case_path, allure_path, test_count, allure_report_path):
    pytest.main(['-v',
                 '-s',
                 case_path,
                 '--alluredir',allure_path,
                 '--count', str(test_count),
                 '--repeat-scope=function',
                 '--disable-warnings',
                 '--capture=no',
                 ])

if __name__ == "__main__":
    pytest.main(['-v','-s','-q','test_allure.py','--alluredir','report'])