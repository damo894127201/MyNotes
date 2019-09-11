# _*_coding:utf-8 _*_

import tensorflow as tf

def main(args):
    print('第一个参数是: ',args[0])
    print('第二个参数是: ',args[1])
    print('第三个参数是：',args[2])

if __name__ == '__main__':
    tf.app.run()