# -*- coding: utf-8 -*-
"""
    :author: ATao
    :description: 
"""

import click
import pytest
import os

@click.group()
def appium_runner():
    print("hello world")

@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name',
              help='The person to greet.')
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo('Hello %s!' % name)



@click.command()
@click.option('--case_path', default='./test_allure.py', help='测试用例路径.')
@click.option('--allure_path', default='./report',help='生成测试报告路径')
@click.option('--allure_path_report', default='./allure_report',help='执行次数')
def testcase(case_path, allure_path, allure_path_report):
    """执行测试用例"""
    pytest.main(['-v',
                 '-s',
                 case_path,
                 '--alluredir',allure_path
                 ])
    os.system(f'allure generate --clean {allure_path} -o {allure_path_report}' )

appium_runner.add_command(hello)
appium_runner.add_command(testcase)


if __name__ == '__main__':
    appium_runner()