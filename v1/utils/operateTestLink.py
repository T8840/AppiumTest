# -*- coding: utf-8 -*-
"""
    :author: ATao
    :tag: 思考是个好东西！
    :description: 封装操作TestLink API
"""

import testlink
from config import config


class TestLinkProcess:
    common = config['common']
    conn_testlink = testlink.TestLinkHelper(common.TESTLINK_API_URL,common.TESTLINK_API_KEY) \
                            .connect(testlink.TestlinkAPIClient)

    @classmethod
    def get_project_info(cls) -> list:
        projects = cls.conn_testlink.getProjects()
        projects_info = []
        __subkey = ['id','name','prefix']
        for project in projects:
            projects_info.append({key: project[key] for key in __subkey})
        return projects_info

    @classmethod
    def get_test_plan_info(cls) ->list:
        test_plans = cls.conn_testlink.getProjectTestPlans(cls.get_project_info()[2].get('id'))
        return test_plans

    @classmethod
    def get_test_cases_by_test_plan(cls) ->list:
        test_suites = cls.conn_testlink.getFirstLevelTestSuitesForTestProject(cls.common.TESTLINK_TESTPROJECT_ID)
        test_cases = []
        for test_suite in test_suites:
            for case in cls.conn_testlink.getTestCasesForTestSuite(test_suite['id'], True, None):
                case.update({'testlink_testsuite_name':test_suite.get('name','')})
                test_cases.append(case)
        return test_cases

def extractCasesToYaml(yamlpath):
    """单条case数据格式->
    {'id': '2362', 'parent_id': '2361', 'node_type_id': '3', 'node_order': '15', 'node_table': 'testcases','name': '跑马灯-轮播正常', 'external_id': 'ZY-2'}
        希望转换为

    """
    from ruamel import yaml
    yamlpath_name = yamlpath + 'test_example.yaml'
    testlink_cases = []
    test_cases = sorted(TestLinkProcess.get_test_cases_by_test_plan() ,key=lambda k:k['id'])
    for case in test_cases:
        case = {k:v for k,v in case.items() if ('node' not in k and 'parent' not in k)}
        case.update({'testlink_id':case.pop('id'),'testlink_name':case.pop('name'),'testlink_external_id':case.pop('external_id')})
        case.update({'case_setup':[],'case_teststeps':[],'case_testdata':[],'expect':[]})
        testlink_cases.append(case)
    with open(yamlpath_name,'w',encoding='utf-8') as f:
        yaml.dump(testlink_cases,f,Dumper=yaml.RoundTripDumper,allow_unicode=True)

def uploadResultToTestLink():
    pass

if __name__ == "__main__":
    yamlpath = config['ssj'].YAML_CASES_DIR_PATH
    extractCasesToYaml(yamlpath)




