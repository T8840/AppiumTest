# -*- coding: utf-8 -*-
"""
    :author: ATao
    :description: 启动文件
"""

import click
import pytest
import os
import arrow

@click.group()
def appium_runner():
    print("欢迎使用！")

@click.command()
def airtest():
    """Simple program that greets NAME for a total of COUNT times."""
    click.echo('脚本正在开发中，请耐心等待！')


now = (arrow.now()).format('YYYY-MM-DD-HH-mm-ss')
@click.command()
@click.option('--case_path', default='./cases/', help='默认测试用例路径为cases.如果使用该参数，请在后面加入ssj或kn，其他情况不支持') # 修改为case目录中的所有
@click.option('--report_path', default=f'./report/pytest_report/{now}.html',help='生成的html测试报告路径')
def appiumtest(case_path,report_path):
    """执行测试用例"""
    test_case_path = ""
    if case_path == './cases/':
        test_case_path = './cases/'

    elif case_path == 'ssj':
        test_case_path = './cases/ssj/'

    elif case_path == 'kn':
        test_case_path = './cases/kn/'

    elif case_path == 'demo':
        test_case_path = './cases/ssj/test_invest_page.py'

    else:
        print("--case_path后目前只支持参数ssj与kn，请重新输入")
    pytest.main(['-s',
                 test_case_path,
                 '--pytest_report', report_path
                 ])

#############################################################################################
############################# 使用allure来生成测试报告###########################################
##############################################################################################
# @click.command()
# @click.option('--case_path', default='./cases/', help='默认测试用例路径为cases.如果使用该参数，请在后面加入ssj或kn，其他情况不支持') # 修改为case目录中的所有
# @click.option('--allure_path', default=f'./report/pytest_report/{now}',help='生成的xml测试报告路径')
# @click.option('--allure_path_report', default=f'./report/allure_report/{now}',help='生成的allure测试报告路径')
# def appiumtest(case_path,allure_path, allure_path_report):
#     """执行测试用例"""
#     test_case_path = ""
#     if case_path == './cases/':
#         test_case_path = './cases/'
#         pytest.main(['-v',
#                      '-s',
#                      test_case_path,
#                      '--alluredir', allure_path
#                      ])
#     elif case_path == 'ssj':
#         test_case_path = './cases/ssj/'
#         pytest.main(['-v',
#                      '-s',
#                      test_case_path,
#                      '--alluredir',allure_path
#                      ])
#     elif case_path == 'kn':
#         test_case_path = './cases/kn/'
#         pytest.main(['-v',
#                      '-s',
#                      test_case_path,
#                      '--alluredir', allure_path
#                      ])
#     else:
#         print("--case_path后目前只支持参数ssj与kn，请重新输入")
#     os.system(f'allure generate --clean {allure_path} -o {allure_path_report}' )

appium_runner.add_command(airtest)
appium_runner.add_command(appiumtest)


if __name__ == '__main__':
    appium_runner()