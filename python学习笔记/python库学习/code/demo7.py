
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('number',type=int,default=0,choices=[0,1,2]) # 添加位置参数和其说明
args = parser.parse_args()
print(args.number)