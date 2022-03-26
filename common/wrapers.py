import unittest
from functools import wraps
from common.logger import write_log
def write_case_log():
    """
    记录用例运行日志
    :return:
    """
    def wraper_func(func):
        @wraps(func) #不懂
        def inner_func(*args, **kwargs):
            write_log.info('{}开始执行'.format(func.__name__))
            func(*args, **kwargs)
            write_log.info('{}执行中'.format(args))
            write_log.info('{}结束执行'.format(func.__name__))
        return inner_func
    return wraper_func