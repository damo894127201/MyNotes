
# _*_coding:utf-8 _*_
import logging

logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# 创建Logger对象
logger = logging.getLogger(__name__)

# 下面是日志记录
logger.info('This is a log info')
logger.debug('Debugging')
logger.warning('Warning exists')
logger.info('Finish')