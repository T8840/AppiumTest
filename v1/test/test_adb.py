# -*- coding: utf-8 -*-
"""
    :author: ATao
"""

from v1.core.android.adb import ADB
adb = ADB(serialno=ADB().devices(state="device")[0][0])

def test_install():
    adb.install_app(filepath=r"D:\com.xueqiu.android_12.6.1_257.apk")
#   product_MymoneyDev_v12.48.0.0_20200320_1723
def test_uninstall():
    adb.uninstall_app(package='com.xueqiu.android')

def test_push():
    adb.push(local = r"D:\AppiumBootstrap.jar",remote=r'/data/log/')

def test_activity():
    pass
test_push()
# test_install()
# test_uninstall()