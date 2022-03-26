import os
class ProjectConfig(object):
#封装配置
    version="v1.0"
    url="http://10.100.42.12:8099/api/departments/"
# 替换为你本地的接口项目路径（注意不是自动化项目路径）
    PROJECT_DIR = "C:\\Users\\010702\\PycharmProjects\\easytest\\接口环境\\"
    # 自动化测试项目目录
    TEST_DIR = "D:\APItest"
    Log_DIR="D:\\APItest\\log"
    Report_DIR="D:\\APItest\\report"
#邮件配置信息
    EMAIL_CONFIG={"EMAIL_SERVER":"smtp.qq.com",#服务器
                  "EMAIL_USER":"2504973175@qq.com",
                  "EMAIL_PWD":"hiisrspixxpmdhje",#授权码
                  "EMAIL_SENDER":"2504973175@qq.com",
                  "EMAIL_RECEIVER":"2504973175@qq.com"
                  }
ETConfig=ProjectConfig()


