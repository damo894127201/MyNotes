
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-v','--verbose',required=True) # 添加选项参数'-v'，且设置参数为必须
args = parser.parse_args()
print(args.verbose,type(args.verbose)) # 获取参数值，并打印出来
print(args)