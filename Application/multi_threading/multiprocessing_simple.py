import time
import multiprocessing

def f(n) :
    # 获取当前线程的名字
    name = multiprocessing.current_process().name
    print(name,'start')
    print('worker', n)
    return None

def test_Process():
    numList = []
    for i in range(5):
        p = multiprocessing.Process(target=f, args=(i,))
        numList.append(p)
        p.start()
        p.join()
        print("end",numList)

def run(fn):
  #fn: 函数参数是数据列表的一个元素
  time.sleep(1)
  return fn*fn


def test_Pool():
    testFL = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("shunxu:")
    s = time.time()
    for fn in testFL:
        run(fn)

    e1 = time.time()
    print(
    "顺序执行时间：", int(e1 - s))

    print('concurrent:'  )# 创建多个进程，并行执行
    pool = multiprocessing.Pool(5)#创建拥有5个进程数量的进程池
    #testFL:要处理的数据列表，run：处理testFL列表中数据的函数
    rl = pool.map(run,testFL)
    pool.close()  # 关闭进程池，不再接受新的进程
    pool.join()  # 主进程阻塞等待子进程的退出
    e2 = time.time()
    print("并行执行时间：", int(e2 - e1))
    print(rl)



if __name__ == "__main__":
    test_Pool()
