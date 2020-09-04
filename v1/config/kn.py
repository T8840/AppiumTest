# -*- coding: utf-8 -*-
"""
    :author: ATao
    :description: 
"""

from .default import Config

class KnConfig(Config):
    LOG_LEVEL = 'debug'
    REMOTEHOST = "http://localhost:4723/wd/hub"
    DESIRED_CAPS = {
        "platformName":"android",
        "deviceName" : "Huawei",
        "appPackage" :"com.mymoney.sms",
        "appActivity" : ".ui.SplashActivity",
        "autoGrantPermissions" : "true",
        # "udid" : "emulator-5556",
        "noSign": True,
        "noReset": True,
        "chromedriverExecutableDir" :"/Users/seveniruby/projects/chromedriver/2.20/",
        "showChromedriverLog" : True
    }
    FILE_BROWSER_SHARE_URL = 'http://10.201.5.161:7777/share/exQb26Kq'