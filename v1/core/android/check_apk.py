# -*- coding: utf-8 -*-
"""
    :author: ATao
    :description: 从File Browser下载Apk应用
                校验手机上是否存在该Apk，并校验版本是否一致
                一致，直接跳过
                不一致，会进行下载，安装，并删除
"""

import requests
import json
import os
import re

from core.android.apkparser.apk import APK
from core.android.adb import ADB
from core.log import getLogger

logger = getLogger()

class CheckAppPackage:

    def __init__(self, filebrowse_share_url,package_name):
        self.share_url = filebrowse_share_url
        self.apk_name =''
        self.package_name = package_name
        self.filename = r"download.apk"

    def check(self):
        """检查手机中是否已包含下载应用版本
           只有下载版本与手机版本在匹配一致才不会安装
           匹配不一致或app中没有该应用时都会进行安装
        """
        apk = APK(filename=self.filename)
        adb = ADB(serialno=ADB().devices(state="device")[0][0])

        cmd = f'dumpsys package {self.package_name}'
        result = adb.shell(cmd=cmd)
        pattern = "versionCode=(\d*) "
        download_apk_version_code = apk.get_androidversion_code()
        try:
            if re.search(pattern,result) and (re.search(pattern,result).group(1) == download_apk_version_code):
                logger.info("手机已安装与下载版本一致的应用，开始执行测试用例！")
                return True
            else:
                logger.info("手机还没有安装与下载版本一致的应用，开始进行安装应用！")
                adb.install_app(self.filename)
                self.check()
        except Exception as e:
            print(e)


    def __get_apk_path(self):
        _api_url = self.share_url.split('share')
        _api_url.insert(1, 'api/public/share')
        _request_url = ''.join(_api_url)
        _r = requests.get(_request_url, timeout=600, verify=False)
        data = json.loads(_r.text)['path'].split("/")[-1]
        self.apk_name = data
        return data

    def __download_apk(self):
        if os.path.exists(self.filename):
            self.__remove_download_apk()
        _api_url = self.share_url.split('share')
        _api_url.insert(1, 'api/public/dl')
        _request_url = ''.join(_api_url) + '/'+ self.__get_apk_path()
        install_name = "download.apk"
        with open(install_name, "wb") as f:
            _r = requests.get(_request_url, timeout=6000, verify=False)
            f.write(_r.content)
            logger.info("已经下载APK应用成功：%s"%self.apk_name)
            # print("已经下载APK应用成功：%s"%self.apk_name)


    def __remove_download_apk(self):
        """在安装完或或不需安装时调用该方法删除已下载到本地的应用"""
        os.remove(self.filename)
        logger.info("已经移除本地下载的应用！")

    def __enter__(self):
        self.__download_apk()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__remove_download_apk()

if __name__ == "__main__":
    filebrowse_share_url = 'http://10.201.5.161:7777/share/QCAGQuaC'
    package_name = "com.mymoney"

    with CheckAppPackage(filebrowse_share_url,package_name) as D:
        D.check()

