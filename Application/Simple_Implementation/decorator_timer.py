# -*- coding: utf-8 -*-

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.clock()
        func(*args, **kwargs)

        end_time = time.clock()
        print("函数运行时间：" + str(end_time-start_time))
    return wrapper

@timer
def main():
    print('>>>>开始计算函数运行时间')
    for i in range(1, 1000):
        for j in range(i):
            print(j)


if __name__ == '__main__':
    main()