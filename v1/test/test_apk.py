# -*- coding: utf-8 -*-
"""
    :author: ATao
    :description: 
"""
from v1.core.android.apkparser.apk import APK
apk  = APK(filename=r"D:\product_MymoneyDev_v12.48.0.0_20200320_1723.apk")
# apk  = APK(filename=r"D:\com.xueqiu.android_12.6.1_257.apk")



def test_get_package():
    print(apk.get_package())

def test_get_androidversion_code():
    print(apk.get_androidversion_code())

def test_show():
    print(apk.show())
# test_get_package()
# test_get_androidversion_code()
test_show()