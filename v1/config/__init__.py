# -*- coding: utf-8 -*-
"""
    :author: ATao
    :description: 配置文件
"""
from .default import Config
from .ssj import SsjConfig
from .kn import KnConfig
from .prod import ProdConfig


config = {
    'common': Config,
    'ssj': SsjConfig,
    'kn': KnConfig,
    'prod': ProdConfig
}