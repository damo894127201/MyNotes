import argparse

parser = argparse.ArgumentParser()
parser.add_argument('args_1') # 添加位置参数
parser.add_argument('-ver','-v',action='store_true') # 添加选项参数，第一个完整的参数名，第二个是省略的参数名，两者等价
args = parser.parse_args()
print(args.args_1,args.ver)