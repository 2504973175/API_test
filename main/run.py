import unittest
import platform
import os.path
from common.logger import write_log
from config.ProjectConfig import ETConfig
from common.HTMLTestRunnerCNs import HTMLTestRunner
from common.send_email import sendEmail
class RunCase(object):
    report_dir=ETConfig.Report_DIR
    #执行用例函数
    def run_case(self):
        # 运行测试用例并生成html测试报告
        with open('{}//et_result.html'.format(self.report_dir), 'wb') as fp:

            try:
                write_log.info("RunCase执行用例--开始")
                suite = unittest.TestSuite()
                tests = unittest.defaultTestLoader.discover('..\\testcase', pattern='*Storm.py')
                suite.addTest(tests)
                runner = HTMLTestRunner(stream=fp, title=u'自动化测试报告', description=u'运行环境：{}'.format(platform.platform()),
                                        tester="istester")
                runner.run(suite)
                write_log.info("RunCase执行用例--结束")
            except Exception as e:
                write_log.error("RunCase执行用例，生成报告失败：{}".format(e))


if __name__ == '__main__':
    test = RunCase()#创建对象
    test.run_case()#调用测试用例执行函数
    sendEmail().send_mail()
    #调用发送邮件函数

