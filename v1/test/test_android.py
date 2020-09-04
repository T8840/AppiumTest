# -*- coding: utf-8 -*-
"""
    :author: ATao
    :description: 
"""

from v1.core.android.android import Android
# class OpDevice(ADB):

def list_app():
    print(Android().list_app())

def install():
    Android().install_app(filepath=r"D:\com.xueqiu.android_12.6.1_257.apk")


def uninstall():
    Android().uninstall_app(package='com.mymoney.sms')

# list_app()
# install()
uninstall()
