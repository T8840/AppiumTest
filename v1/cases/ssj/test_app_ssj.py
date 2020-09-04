# -*- coding: utf-8 -*-
"""
    :author: ATao
    :tag: 思考是个好东西！
    :description: 处理YamlCases 的方式一
        希望方式二可以使用Conftest插件来处理YamlCase
"""

import pytest
import time
from pages.ssj.app import App
from config import config
from core.ui_appium.yaml_cases_driver import YamlCasesDriver

configs = config['ssj']
cases_driver = YamlCasesDriver(configs)


def run_setup(router):
    """输入Yaml Case的test_setup，需要将该列表映射为App.start().to_debt_page()方法"""
    if router == []:
        raise YamlCaseSetupException()
    if router[0] != 'start':
        raise YamlCaseSetupException()
    else:
        _, *non_start = router
        func_name = "App.start()." + ".".join(["to_" + i + "()" for i in non_start])
        eval(func_name)

class YamlCaseSetupException(Exception):
    """ custom exception for error reporting. """
    def __init__(self, args=("测试用例Yaml文件setup参数list必须以\'start\'开头",)):
        self.args = args

@pytest.fixture()
def quitDriver():
    """teardown操作"""
    driver = App
    yield driver
    driver.quit()


@pytest.mark.usefixtures('quitDriver')
@pytest.mark.parametrize('testlink_testsuite_name, testlink_id, testlink_name, testlink_external_id,case_setup, case_teststeps, case_testdata, expect', cases_driver.get_cases_info())
class TestAppSsj:
    def test_cases(self,testlink_testsuite_name, testlink_id, testlink_name, testlink_external_id,case_setup,case_teststeps,case_testdata,expect):
        run_setup(case_setup)
        time.sleep(5)

if __name__ == '__main__':
    pytest.main(['-sv'])