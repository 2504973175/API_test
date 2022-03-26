
#storm项目获取用户信息 DDT+Excel Excel有几条数据，就执行几次用例
import unittest
import requests
import json
from config.ProjectConfig import ETConfig
from testcase.data.DepartmentData import ADD_DATA
from ddt import ddt,data,unpack
from common.wrapers import *
#这里竟然可以只导入一个对象
from common.HttpReq import ETReq
from common.doExcel import DoExcel
from common.HttpReq import HttpReq
from common.is_json import IsJson
from common.logger import write_log
import warnings
@ddt
class GetUserTest(unittest.TestCase):
    test_data = DoExcel().get_data("D:/接口实战/接口自动化用例.xlsx", 'getuser')
    #只要哪一行有值，就会被读为一条用例
    @classmethod
    def setUpClass(cls):
       write_log.info("------------------")
    """获取用户信息"""
    def setUp(self):
        warnings.simplefilter('ignore',ResourceWarning)
    def tearDown(self):
        pass

    @write_case_log()
    @data(*test_data)
    def test_get_user_info(self,item):
        print("正在执行测试用例{0}".format(item['title']))
        r=HttpReq().http_request(url=item['url'],data=(item['data']),http_method=item['method'])

        # print("响应文本为:"+r.text)
        try:

            self.assertEqual(item['expected_code'], r.json()['code'])  # 预期结果和直接返回的状态码比较
            TestResult='PASS'
            # print("测试用例执行成功")
            write_log.info("测试用例执行成功")
        except AssertionError as e:
            TestResult='FAIL'
            # print("执行用例出错(0)".format(e))
            write_log.error("执行用例出错{0}".format(e))

            raise e
        finally:
            DoExcel().write_back("D:/接口实战/接口自动化用例.xlsx", 'getuser',item['case_id']+1,10,r.json()['code'])
            DoExcel().write_back("D:/接口实战/接口自动化用例.xlsx", 'getuser',item['case_id']+1,11,r.text)
            DoExcel().write_back("D:/接口实战/接口自动化用例.xlsx", 'getuser',item['case_id']+1,12,TestResult)#写入结果


        # r=IsJson(r)
        # self.assertEqual(item['expected'],r['code'])#结果和响应结果中的code边角




if __name__ == '__main__':
    # unittest.main()
    suite=unittest.TestSuite()
    suite.addTest(GetUserTest("test_get_user_info"))
    # suite.addTest(AddDepartmentTest("test_add_department_2"))
    runner=unittest.TextTestResult()
    test_result=runner.run(suite)





