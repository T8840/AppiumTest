
from .default import Config

class SsjConfig(Config):
    LOG_LEVEL = 'debug'
    REMOTEHOST = "http://localhost:4723/wd/hub"
    DESIRED_CAPS = {
        "platformName":"android",
        "deviceName" : "Huawei",
        "appPackage" :"com.mymoney",
        "appActivity" : "com.mymoney.biz.splash.SplashScreenActivity",
        "autoGrantPermissions" : "true",
        # "udid" : "emulator-5556",
        "noSign": True,
        "noReset": True,
        "chromedriverExecutableDir" :"/Users/seveniruby/projects/chromedriver/2.20/",
        "showChromedriverLog" : True
    }
    FILE_BROWSER_SHARE_URL = 'http://10.201.5.161:7777/share/QCAGQuaC'

    # YAML配置
    YAML_ELEMENTS_PATH = 'E:/uitcloudserver/v1/pages/ssj/ssj_elements.yaml'
    YAML_CASES_DIR_PATH = 'E:/uitcloudserver/v1/cases/ssj/'
    YAML_CASES_PATH = 'E:/uitcloudserver/v1/cases/ssj/test_ssj_cases.yaml'

