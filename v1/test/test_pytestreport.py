# -*- coding: utf-8 -*-
"""
    :author: ATao
    :tag: 思考是个好东西！
    :description: 
"""
import pytest

def testTrue():
    assert True

def testFalse():
    assert False

def testError():
    1 / 0

@pytest.mark.skip(reason="misunderstood the API")
def testSkip():
    assert 1 == 1

@pytest.mark.xfail(reason="Xpass")
def testXPass():
    assert True

@pytest.mark.xfail(reason="Xfail")
def testXFail():
    assert False


if __name__ == '__main__':
    pytest.main(["-s", "test_pytestreport.py", "--pytest_report", "Pytest_Report.html"])
