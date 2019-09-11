
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('echo',help='这里是参数echo的说明') # 添加位置参数和其说明
args = parser.parse_args()
print(args)