#添加学院信息
import unittest
import requests
import json
from config.ProjectConfig import ETConfig
from testcase.data.DepartmentData import ADD_DATA
from ddt import ddt,data,unpack
from common.wrapers import *
#这里竟然可以只导入一个对象
from common.HttpReq import ETReq

@ddt
class AddDepartmentTest(unittest.TestCase):
    """添加学院信息"""

    def setUp(self):
        print("{0}执行前，清除数据库".format(self._testMethodName))
        self.url =ETConfig.url
    def tearDown(self):
        print("{0}执行后，清除数据库".format(self._testMethodName))

    @data(ADD_DATA['test_add_department_001'], ADD_DATA['test_add_department_002'],ADD_DATA['test_add_department_006'],ADD_DATA['test_add_department_007'],ADD_DATA['test_add_department_008'],ADD_DATA['test_add_department_009'],ADD_DATA['test_add_department_0010'])
    # @data(ADD_DATA)
    @unpack
    @write_case_log()
    def test_add_department_1(self,req_data,res_key,res_value,status_code,des):
        print(self._testMethodName+des)
        r=ETReq.post(url=self.url,data=json.dumps(req_data))
        print("响应文本为:"+r.text)
        response=json.loads(r.text)
        self.assertEqual(response[res_key]['count'],res_value)
        self.assertEqual(r.status_code,status_code)
        print("{}执行成功".format(self._testMethodName))

    @data(ADD_DATA['test_add_department_003'],ADD_DATA['test_add_department_004'], ADD_DATA['test_add_department_005'],ADD_DATA['test_add_department_0011'],ADD_DATA['test_add_department_0012'],ADD_DATA['test_add_department_0013'],ADD_DATA['test_add_department_004'])
    @unpack
    @write_case_log()
    def test_add_department_2(self, req_data, res_key, res_value, status_code, des):
        print(self._testMethodName + des)
        r = ETReq.post(url=self.url, data=json.dumps(req_data))

        print("响应文本为:" + r.text)
        response = json.loads(r.text)
        self.assertEqual(response[res_key][0], res_value)
        self.assertEqual(r.status_code, status_code)
        print("{}执行成功".format(self._testMethodName))



if __name__ == '__main__':
    unittest.main()
    suite=unittest.TestSuite()
    suite.addTest(AddDepartmentTest("test_add_department_1"))
    suite.addTest(AddDepartmentTest("test_add_department_2"))
    # runner=unittest.TextTestResult()
    # test_result=runner.run(suite)
    with open("1.txt", 'w+') as f: # 这种方法会关闭文件
      runner = unittest.TextTestRunner(stream=f, verbosity=1)
      testresult = runner.run(suite)