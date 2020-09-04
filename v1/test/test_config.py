# -*- coding: utf-8 -*-
"""
    :author: ATao
    :description: 
"""

from v1.config import config

if __name__ == "__main__":
    configs = config['ssj']
    print(configs.DESIRED_CAPS["appPackage"])