# _*_coding:utf-8 _*_
import logging

logger = logging.getLogger('main.core') # 子模块的Logger，会复用主模块的Logger的配置

def run():
    logger.info('Core Info')
    logger.debug('Core Debug')
    logger.error('Core Error')