
import argparse

parser = argparse.ArgumentParser(description='这是当前模块功能的介绍',usage='这是模块用法的介绍')
parser.add_argument('argv1') # 添加位置参数
parser.add_argument('-d','-del',action='store_true') # 添加选项参数
args = parser.parse_args()
print(args.argv1,args.d)