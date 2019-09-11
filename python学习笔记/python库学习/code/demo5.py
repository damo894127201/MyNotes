
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('file',help='这里是参数echo的说明',type=argparse.FileType('r',encoding='utf-8')) # 添加位置参数和其说明
args = parser.parse_args()
print('参数echo的数据类型是：',type(args.file))
print()
# 读取文件
for line in args.file:
    print(line)