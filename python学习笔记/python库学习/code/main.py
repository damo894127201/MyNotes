# _*_coding:utf-8 _*_

import logging
import core # 子模块

logger = logging.getLogger('main')
logger.setLevel(level=logging.DEBUG)

# Handler
handler = logging.FileHandler('./code/common.log')
handler.setLevel(logging.INFO)

# Formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)

logger.info('Main Info')
logger.debug('Main Debug')
logger.error('Main Error')
core.run() # 调用子模块方法，同时开始记录子模块日志信息