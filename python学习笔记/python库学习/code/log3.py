# _*_coding:utf-8 _*_

import logging

logger = logging.getLogger() # 获取日志器logger
logger.setLevel(level=0) # 设置logger的level

LOG_FORMAT = "%(asctime)s %(name)s %(levelname)s %(pathname)s %(message)s "#配置输出日志格式
DATE_FORMAT = '%Y-%m-%d  %H:%M:%S %a ' #配置输出时间的格式，注意月份和天数不要搞乱了

logging.basicConfig(level=logging.DEBUG,# 设置输出的日志级别，大于等于DEBUG级别的日志记录都会输出
                   format= LOG_FORMAT,
                    datefmt=DATE_FORMAT,
                    filename = "./code/test.log" # 设置日志输出的文件名及其路径
                   )

logging.debug('msg1')
logging.info('msg2')
logging.warning('msg3')
logging.error('msg4')
logging.critical('msg5')