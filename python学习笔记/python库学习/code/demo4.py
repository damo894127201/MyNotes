# _*_coding:utf-8 _*_

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('echo',help='这里是参数echo的说明',type=int) # 添加位置参数和其说明
args = parser.parse_args()
print('参数echo的数据类型是：',type(args.echo))