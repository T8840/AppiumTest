# -*- coding: utf-8 -*-
"""
    :author: ATao
    :description: 
"""
import pytest

# 方式一：fixture名字作为用例的参数
@pytest.fixture()
def fixtureFunc():
    return 'fixtureFunc'

def test_fixture(fixtureFunc):
    print('我调用了{}'.format(fixtureFunc))

class TestFixture(object):
    def test_fixture_class(self, fixtureFunc):
        print('在类中使用fixture "{}"'.format(fixtureFunc))

# 方式二：使用@pytest.mark.usefixtures('fixture')装饰器
@pytest.mark.usefixtures('fixtureFunc')
def test_fixture2():
    print('in test_fixture "{}"'.format(fixtureFunc))

@pytest.mark.usefixtures('fixtureFunc')
class TestFixtureTwo(object):
    def test_fixture_class(self):
        print('in class with the test_fixture_class "{}"'.format(fixtureFunc))

# 方式三：使用autouse参数
"""
scope参数可以是session， module，class，function； 默认为function
1.session 会话级别（通常这个级别会结合conftest.py文件使用，所以后面说到conftest.py文件的时候再说）
2.module 模块级别： 模块里所有的用例执行前执行一次module级别的fixture
3.class 类级别 ：每个类执行前都会执行一次class级别的fixture
4.function ：这个默认是默认的模式，函数级别的，每个测试用例执行前都会执行一次function级别的fixture
"""

@pytest.fixture(scope='class',autouse=True)
def class_fixture():
    print('\n-----------------')
    print('我是class fixture')
    print('-------------------')

@pytest.mark.usefixtures('class_fixture')
class TestFixture1(object):
    def test_2(self):
        print('\n我是class1里面的test2')
    def test_3(self):
        print('\n我是class1里面的test3')

@pytest.mark.usefixtures('class_fixture')
class TestFixture2(object):
    def test_4(self):
        print('\n我是class2里面的test4')
    def test_5(self):
        print('\n我是class2里面的test5')




if __name__=='__main__':
    pytest.main(['-v', '--setup-show','test_fixture.py'])
#
# if __name__ == '__main__':
#     pytest.main(["-s", "test_pytestreport.py", "--pytest_report", "Pytest_Report.html"])
