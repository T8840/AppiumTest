# -*- coding: utf-8 -*-
"""
    :author: ATao
    :description: 
"""

import sys
import os
import logbook
import logbook.more
from config import config

def logFormate(record,handler):
    formate = "[{date}] [{level}] [{filename}] [{func_name}] [{lineno}] {msg}".format(
        date = record.time,                              # 日志时间
        level = record.level_name,                       # 日志等级
        filename = os.path.split(record.filename)[-1],   # 文件名
        func_name = record.func_name,                    # 函数名
        lineno = record.lineno,                          # 行号
        msg = record.message                             # 日志内容
    )
    return formate


def initLogger(filename,fileLogFlag=True,stdOutFlag=False):

    BASE_DIR = os.path.abspath(os.path.join(os.path.dirname("__file__"),os.path.pardir))
    BASE_DIR = os.path.abspath(os.path.join(BASE_DIR,os.path.pardir))
    LOG_DIR = os.path.join(BASE_DIR,'log')
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)

    logbook.set_datetime_format('local')

    logger = logbook.Logger(filename)
    logger.handlers = []

    if fileLogFlag:#日志输出到文件
        logFile = logbook.TimedRotatingFileHandler(os.path.join(LOG_DIR, '%s.log' % 'log'),date_format='%Y-%m-%d', bubble=True, encoding='utf-8')
        logFile.formatter = logFormate
        logger.handlers.append(logFile)

    if stdOutFlag:#日志打印到屏幕
        logStd = logbook.more.ColorizedStderrHandler(bubble=True)
        logStd.formatter = logFormate
        logger.handlers.append(logStd)

    return logger


class Logger:
    common = config['common']
    logger = initLogger(common.LOG_PATH, True, True)


def getLogger():
    return Logger.logger


def setLogger(logger):
    Logger.logger = logger