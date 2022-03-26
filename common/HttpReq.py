#封装请求，让代码更简洁，更具有可读性，并且更好维护
import requests
from  common.logger import write_log
class HttpReq(object):
    """利用requests封装get请求和post请求需要传递的参数"""
    def __init__(self):
        self.headers = {"Content-Type": "application/json",
                        # "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36" 伪装user-agent
                        }

    @staticmethod
    def http_request(url,data, http_method, headers=None, cookies=None, auth=None, file=None):
        try:
            if http_method.upper() == "GET":
                res = requests.get(url, data=data, headers=headers, cookies=cookies, auth=auth, files=file)
                return res
            elif http_method.upper() == "POST":
                res = requests.post(url, data=data, headers=headers, cookies=cookies, auth=auth, files=file)
                return res
            else:
                # print("输入的请求方法不对")
                write_log.info("输入的请求方法不对")

        except Exception as e:
            # print("请求报错了:{0}".format(e))
            write_log.error("请求报错了:{0}".format(e))
            raise e


ETReq = HttpReq()
