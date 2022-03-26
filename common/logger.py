import logging
import os
from logging import handlers
from config.ProjectConfig import ETConfig

def logger():
    # os.makedirs("{}logs".format(ETConfig.Log_DIR), exist_ok=True)#os.makedirs() 方法用于递归创建目录。
    log = logging.getLogger("{}\\et.log".format(ETConfig.Log_DIR))
    format_str = logging.Formatter('%(asctime)s [%(module)s] %(levelname)s [%(lineno)d] %(message)s', '%Y-%m-%d %H:%M:%S')
    # 按天录入日志，最多保存7天的日志
    handler = handlers.TimedRotatingFileHandler(filename=("{}/et.log".format(ETConfig.Log_DIR)), when='D', backupCount=7, encoding='utf-8')
    log.addHandler(handler)
    log.setLevel(logging.INFO)
    handler.setFormatter(format_str)
    return log

write_log = logger()
write_log.info("你好")