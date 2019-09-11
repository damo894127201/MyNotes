# _*_coding:utf-8 _*_
import logging

logger = logging.getLogger() # 获取日志器logger
logger.setLevel(level=0) # 设置logger的level

# 在代码中需要输出相应级别的日志的地方，设置如下代码
# 以下都是日志记录的level
logging.debug('debug_msg')
logging.info('info_msg')
logging.warning('warning_msg')
logging.error('error_msg')
logging.critical('critical_msg')