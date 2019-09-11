
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='解析命令行参数')
    # 依次添加每一个参数
    parser.add_argument('echo')
    parser.add_argument('num')
    parser.add_argument('-v','--verbose',action='store_const',const=52)
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()
    print(vars(args))