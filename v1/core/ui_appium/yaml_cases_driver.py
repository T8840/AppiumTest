# -*- coding: utf-8 -*-
"""
    :author: ATao
    :tag: 思考是个好东西！
    :description: yaml测试文件的核心处理层
"""

from utils.operateYaml import readYaml
from core.log import getLogger

logger = getLogger()

class YamlCasesDriver:
    def __init__(self,configs):
        self.yaml_data = readYaml(configs.YAML_CASES_PATH)

    def get_cases_info(self):
        case_infos = []
        for i in self.yaml_data:
            case_infos.append(tuple(i.values()))
        logger.info("已从Yaml Case文件中获得了测试用例信息！")
        return case_infos












