# -*- coding: utf-8 -*-
"""
    :author: ATao
    :description: 
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class Config:
    # 日志配置：LOG_PATH请设置绝对路径
    LOG_PATH = 'E:/uitcloudserver/v1/log/'
    LOG_FILENAME = 'fastapi.log'
    LOG_LEVEL = 'info'

    # TestLink
    TESTLINK_API_URL = "http://172.22.23.148:81/lib/api/xmlrpc/v1/xmlrpc.php"
    TESTLINK_API_KEY = "1392b3a156167f136c15b10880645d72"
    TESTLINK_TESTPROJECT_ID = '2348'

    # 查找元素方法配置
    NAME = "name"
    ID = "id"
    XPATH = "xpath"
    INDEX = "index"
    find_element_by_id = "by_id"
    find_elements_by_id = "by_ids"
    find_element_by_name = "by_name"
    find_elements_by_name = "by_names"
    find_element_by_link_text = "by_link_text"
    find_elements_by_link_text = "by_link_texts"
    find_element_by_xpath = "by_xpath"
    find_elements_by_xpath = "by_xpaths"
    find_element_by_class_name = "class_name"
    find_elements_by_class_name = "class_names"
    SELENIUM = "selenium"
    APPIUM = "appium"
    ANDROID = "android"
    IOS = "ios"
    IE = "ie"
    FOXFIRE = "foxfire"
    CHROME = "chrome"
    CLICK = "click"
    DRIVER = ""
    TAP = "tap"
    SWIPELEFT = "swipeLeft"
    SELENIUM_APPIUM = "appium"
    SEND_KEYS = "send_keys"
    FIND_STR = "find_str"
    WAIT_TIME = 5
    # selenium
    SEND_CODE = "send_code"  # 输入验证码

    # 本地存储记录所有的case情况的路径
    REPORT_INFO_PATH = "d:/info.txt"
    REPORT_INIT = "d:/init.txt"
    REPORT_COLLECT_PATH = "d:/collect.txt"
    CRASH_LOG_PATH = "d:/crash.txt"  # 存放crash的json文件名
    # my server
    HOST = '192.168.1.38'
    PORT = 8088

    PROTOCOL = "http://"  # 协议
    APACHE_PATH = "D:/app/Apache2.2/htdocs/appium/log/"  # apapche器的地址，开发可以在这个上面下载异常日志
    SCREEN_IMG_PATH = "D:/app/Apache2.2/htdocs/appium/img/"  # 截图地址


    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///user.db'

    ENABLE_SENTRY = False
    SENTRY_DSN = ''

    REDIS_HOST = 'localhost'
    REDIS_PORT = 6379
    REDIS_DB = 0
    REDIS_PASSWORD = 'redis'

    REQUEST_STATS_WINDOW = 60

    BROKER_URL = 'redis://localhost:6379/0'
    CELERY_RESULT_BACKEND = 'redis://localhost:6379/1'
    CELERY_TASK_SERIALIZER = 'msgpack'
    CELERY_RESULT_SERIALIZER = 'json'
    CELERY_TASK_RESULT_EXPIRES = 60 * 60
    CELERY_ACCEPT_CONTENT = ['json', 'msgpack']

    RATELIMIT_HEADERS_ENABLED = True

    CACHE_KEY_PREFIX = 'fastapi::'
    CACHE_TYPE = 'redis'
    CACHE_REDIS_URL = 'redis://localhost:16379/0'
    CACHE_DEFAULT_TIMEOUT = 60 * 60
