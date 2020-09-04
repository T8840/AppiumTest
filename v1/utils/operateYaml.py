import os
import json
from ruamel.yaml import YAML

def get_dict_value(in_dict, target_key, results=[]):
    """获取嵌套字典的key值"""
    for key in in_dict.keys():
        data = in_dict[key]
        if isinstance(data, dict):
            get_dict_value(data, target_key, results=results)
        if key == target_key and isinstance(data, dict) != True:
            results.append(in_dict[key])
    return results

def readYaml(file) -> dict:
    """Read file and return json data or dict
    Read file and return all its content as json format or dict
    Arg:
        file: File name, including its path
    """

    if not os.path.isfile(file):
        print("File: " + file + ' not found!')
        return None

    fname, fext = os.path.splitext(file)

    with open(file) as data:
        if fext == ".yaml":
            yaml = YAML(typ='safe')
            return yaml.load(data)
        else:
            return json.load(data)

# 支持在哪个文件中使用，自动获取该文件的名称
