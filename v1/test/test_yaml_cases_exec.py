# -*- coding: utf-8 -*-
"""
    :author: ATao
    :tag: 思考是个好东西！
    :description: 
"""
from utils.operateYaml import readYaml
import pytest
yaml_data = readYaml('../cases/ssj_cases.yaml')

#
# class GetData():
#   def __init__(self,file_name):
#       '''
#       获取filename.yaml 配置文件的所有数据
#       '''
#       self.desc = []
#       self.method = []
#       self.url = []
#       self.data = []
#       self.header = []
#       self.assert_code = []
#       self.assert_text = []
#       self.assert_in_text = []
#       self.assert_body_has = []
#       param = readYaml('./test_example.yaml')
#       for i in range(0, len(param)):
#           self.method.append(param[i]['method'])
#           self.url.append(param[i]['url'])
#           self.header.append(param[i]['header'])
#           if 'desc' in param[i]:
#               self.desc.append(param[i]['desc'])
#           else:
#               self.desc.append(None)
#           if 'data' in param[i]:
#               self.data.append(param[i]['data'])
#           else:
#               self.data.append(None)
#           if 'assert_code' in param[i]:
#               self.assert_code.append(param[i]['assert_code'])
#           else:
#               self.assert_code.append(None)
#           if 'assert_text' in param[i]:
#               self.assert_text.append(param[i]['assert_text'])
#           else:
#               self.assert_text.append(None)
#           if 'assert_body_has' in param[i]:
#               self.assert_body_has.append(param[i]['assert_body_has'])
#           else:
#               self.assert_body_has.append(None)
#               # 断言数据列表化
#           if 'assert_in_text' in param[i]:
#               text = param[i]['assert_in_text']
#               Ltext = list(text.split(' '))
#               self.assert_in_text.append(Ltext)
#           else:
#               self.assert_in_text.append(None)
#
#
# #urls 为读取到yaml文件中的所有url type:list 如何获取数据 查看 title1
# @pytest.mark.parametrize('url',urls)
# def test_home_page(self,url):
#     '''
#     :param url:
#     :return:
#     '''
#     request = Request.Request(res)
#
#     #获取测试数据在yaml文件中的索引 关于重复的url目前还没有解决 所以只支持不同的url
#     index=urls.index(url)
#     log.info('测试接口描述:'+str(descs[index])) #答应日志
#
#     response=request.send_request(methods[index],urls[index],params[index],headers[index])
#
#     assert test.assert_code(response['code'], assert_codes[index])
#     if assert_in_texts[index] is not None:
#         assert test.assert_in_text(response['body'],*assert_in_texts[index])



# 处理setup
def listToFuncName(param):
    if param[0] != 'start':
        return "测试用例Yaml文件setup参数list必须以\'start\'开头"
    else:
        _, *non_start = param
        func_name ="App.start()." +  ".".join( ["to_" + i + "()" for i in non_start] )
        return func_name

def test_case_setup():
    case_set_up = yaml_data[0].get("setup",False)
    print(type(case_set_up))
    # 得到case的setup为列表，需要将该列表映射为App.start().to_debt_page()方法
    listToFuncName(case_set_up)

def test_yaml_data():
    print(yaml_data)