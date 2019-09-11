
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-v','--verbose',dest='ver') # 添加选项参数'-v'，并用dest来指定'-v'后跟着的值，赋给变量ver
args = parser.parse_args()
print(args.ver,type(args.ver)) # 获取参数值，并打印出来。这里的变量名args.ver是在dest里定义的
print(args)