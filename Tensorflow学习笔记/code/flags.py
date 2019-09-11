# _*_coding:utf-8 _*_

import tensorflow as tf

flags = tf.app.flags
FLAGS = flags.FLAGS

# 定义我们的参数
tf.app.flags.DEFINE_integer('data',10,'这是数据') # data是我们定义的参数
tf.app.flags.DEFINE_boolean('istrain',True,'是否训练') # istrain是我们定义的参数

# 定义主函数
def main(args):
    print('data: {}'.format(FLAGS.data))
    print('istrain: {}'.format(FLAGS.istrain))
    
if __name__ == '__main__':
    tf.app.run() # 该函数指明了，程序所需要的参数的具体值，需要从命令行中获取