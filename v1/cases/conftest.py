# -*- coding: utf-8 -*-
"""
    :author: ATao
    :tag: 思考是个好东西！
    :description: Pytest hook Appium
    1.setup需要根据传入函数名字进行执行，需要与yaml_cases_driver对象进行配合
    2.执行失败时需要进行截图
    3.需要制定报告
    4.需要与testlink配合，获取testlink的标题/数据
        这里需要一个脚本，自动的将testlink数据转换为yaml文件，这里可以晚点做
"""

import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

#

# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     # 用例报错捕捉
#     Action = DriverClient().Action
#     outcome = yield
#     rep = outcome.get_result()
#     if rep.when == "call" and rep.failed:
#         f = Action.driver.get_screenshot_as_png()
#         allure.attach(f, '失败截图', allure.attachment_type.PNG)
#         logcat = Action.driver.get_log('logcat')
#         c = '\n'.join([i['message'] for i in logcat])
#         allure.attach(c, 'APPlog', allure.attachment_type.TEXT)
#         if Action.get_app_pid() != Action.apppid:
#             raise Exception('设备进程 ID 变化，可能发生崩溃')
#
#
# def pytest_runtest_call(item):
#     # 每条用例代码执行之前，非用例执行之前
#     allure.dynamic.description('用例开始时间:{}'.format(datetime.datetime.now()))
#     Action = DriverClient().Action
#     if Action.get_app_pid() != Action.apppid:
#         raise Exception('设备进程 ID 变化，可能发生崩溃')

def pytest_collect_file(parent, path):
    if path.ext == ".yaml" and path.basename.startswith("test"):
        return YamlFile(path,parent)


class YamlFile(pytest.File):
    def collect(self):
        import yaml  # we need a yaml parser, e.g. PyYAML
        raw = yaml.safe_load(self.fspath.open())
        for name, spec in raw.items():
            yield YamlTest( name, self, spec)


class YamlTest(pytest.Item):
    def __init__(self, name, parent, spec):
        super().__init__(name, parent)
        self.spec = spec
        self.locator = None

    def runtest(self):
        for name, value in sorted(self.spec.items()):
            # some custom test execution (dumb example follows)
            if name != value:
                raise YamlException(self, name, value)

        # # 运行用例
        # for self.locator in self.spec:
        #     self.locator['time'] = 5
        #     is_displayed = True
        #     if not self.locator.get('is_displayed'):
        #         is_displayed = False if str(self.locator.get('is_displayed')).lower() == 'false' else True
        #     try:
        #         if self.locator.get('element'):
        #             response = self.Action.__getattribute__(self.locator.get('method'))(yamldict(self.locator))
        #         else:
        #             response = self.Action.__getattribute__(self.locator.get('method'))()
        #         self.assert_response(response, self.locator)
        #     except Exception as E:
        #         if is_displayed:
        #             raise E
        #         pass

    def repr_failure(self, excinfo):
        """ called when self.runtest() raises an exception. """
        if isinstance(excinfo.value, YamlException):
            return '测试类名称：{} \n' \
                   '输入参数：{} \n' \
                   '错误信息：{}'.format(self.name, self.locator, excinfo.value.args)

    # def assert_response(self, response, locator):
    #     if locator.get('assert_text'):
    #         assert locator['assert_text'] in response
    #     elif locator.get('assert_element'):
    #         assert response

    def reportinfo(self):
        return self.fspath, 0, "测试用例CaseName: {}".format(self.name)


class YamlException(Exception):
    """ custom exception for error reporting. """
