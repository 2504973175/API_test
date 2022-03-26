import unittest
from common.HttpReq import ETReq
from config.ProjectConfig import ETConfig
class QueryDepartment(unittest.TestCase):
    def setUp(self):
        pass
        self.url = ETConfig.url

    def test_query_department1(self):
        r=ETReq.get(url=self.url)
        print(r.status_code)
        print("响应文本为:"+r.text)

if __name__ == '__main__':
    # unittest.main()
    suite=unittest.TestSuite()
    suite.addTest(QueryDepartment("test_query_department1"))
    runner=unittest.TextTestResult()
    test_result=runner.run(suite)
