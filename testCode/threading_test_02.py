# from multiprocessing import Process
# import time
#
# def start(name):
#     time.sleep(1)
#     print('hello', name,time.strftime('%H:%M:%S'))
#
# if __name__ == '__main__':
#     p = Process(target=start, args=('ZhangSan',))
#     p1 = Process(target=start, args=('LiSi',))
#     p.start()
#     p1.start()
#     p.join()


#
# from multiprocessing import Process, Queue
# def start(q):
#     q.put( 'hello')
#
# if __name__ == '__main__':
#     q = Queue()
#     p = Process(target=start, args=(q,))
#     p.start()
#     print(q.get())
#     p.join()


#manager实现进程通信
from multiprocessing import Process, Manager

def f(dic, list,i):
    dic['1'] = 1
    dic['2'] = 2
    dic['3'] = 3
    list.append(i)

if __name__ == '__main__':
    manager = Manager()
    dic = manager.dict()#通过manager生成一个字典
    list = manager.list(range(5))#通过manager生成一个列表
    p_list = []
    for i in range(10):
        p = Process(target=f, args=(dic, list,i))

        p.start()
        p_list.append(p)
    print(p_list)
    for res in p_list:
        res.join()

    print(dic)
    print(list)

# from multiprocessing import Process, Pool
# import time
#
#
# def Foo(i):
#     time.sleep(1)
#
#
# return i + 100
#
#
# def Bar(arg):
#     print('number::', arg)
#
#
# if __name__ == "__main__":
#     pool = Pool(3)  # 定义一个进程池，里面有3个进程
# for i in range(10):
#     pool.apply_async(func=Foo, args=(i,), callback=Bar)
# # pool.apply(func=Foo, args=(i,))
#
# pool.close()  # 关闭进程池
# pool.join()  # 进程池中进程执行完毕后再关闭,(必须先close在join)