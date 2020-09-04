# -*- coding: utf-8 -*-
"""
    :author: ATao
    :tag: 思考是个好东西！
    :description: 
"""
from utils.operateYaml import readYaml

pages_name =[]
elements_info = dict()
yaml_data = readYaml('./elements.yaml')


def get_dict_value(in_dict, target_key, results=[]):
    for key in in_dict.keys():  # 迭代当前的字典层级
        data = in_dict[key]  # 将当前字典层级的第一个元素的值赋值给data
        # 如果当前data属于dict类型, 进行回归
        if isinstance(data, dict):
            get_dict_value(data, target_key, results=results)
        # 如果当前键与目标键相等, 并且判断是否要筛选
        if key == target_key and isinstance(data, dict) != True:
            results.append(in_dict[key])
    return results

def get_elements_info(element_name):
    pages_name = yaml_data.keys()
    print(get_dict_value(yaml_data,element_name)[0])

def test_info():
    get_elements_info('invest')