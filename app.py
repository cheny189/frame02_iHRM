"""
封装数据
"""
# 封装接口URL前缀
import os
import logging
import logging.handlers
BASE_URL = "http://182.92.81.159"

FILE_PATH = os.path.abspath(__file__)
PRO_PATH = os.path.dirname(FILE_PATH)
# 代码变体
# a = os.getcwd()
print("动态获取的项目绝对路径", PRO_PATH)
TOKEN =None
USER_ID =None


def my_log_config():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    to_1 = logging.StreamHandler()  # 默认到控制台
    to_2 = logging.handlers.TimedRotatingFileHandler(PRO_PATH + "/log/mylog.log",
                                                     when="h",
                                                     interval=12,
                                                     backupCount=10,
                                                     encoding="utf-8")
    # 4. 指定输出格式
    formatter = logging.Formatter(
        "%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s")

    # 5. 组合: 输出格式与输出目标和日志对象相组合
    to_1.setFormatter(formatter)
    to_2.setFormatter(formatter)
    logger.addHandler(to_1)
    logger.addHandler(to_2)


# my_log_config()
# logging.info("hello")
