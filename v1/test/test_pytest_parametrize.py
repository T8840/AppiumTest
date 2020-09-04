# -*- coding: utf-8 -*-
"""
    :author: ATao
    :tag: 思考是个好东西！
    :description: 
"""

import pytest

data_1 = [
    (1, 2, 4),
    (4, 5, 9)
]


def add(a, b):
    return a + b


@pytest.mark.parametrize('a, b, expect', data_1)
class TestParametrize(object):

    def test_parametrize_1(self, a, b, expect):
        print('\n测试函数1测试数据为\n{}-{}'.format(a, b))
        assert add(a, b) == expect

    def test_parametrize_2(self, a, b, expect):
        print('\n测试函数2数据为\n{}-{}'.format(a, b))
        assert add(a, b) == expect


if __name__ == '__main__':
    pytest.main(['-sv'])