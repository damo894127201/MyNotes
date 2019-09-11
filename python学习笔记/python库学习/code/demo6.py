
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('number',type=int,default=0,nargs='+') # 添加位置参数和其说明
args = parser.parse_args()
# 求参数 number的和，number可能会输入多个值
print(sum(args.number))