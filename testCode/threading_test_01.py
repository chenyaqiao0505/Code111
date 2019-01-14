# import threading
# import time
#
# '''直接调用'''
#
# def hello(name):
#     print("Hello %s"%name)
#     time.sleep(3)
#
# if __name__ == "__main__":
#     t1=threading.Thread(target=hello,args=("zhangsan",)) #生成线程实例
#     t2=threading.Thread(target=hello,args=("lisi",))
#
# t1.setName("aaa") #设置线程名
# t1.start() #启动线程
# t2.start()
# t2.join() #join 等待t2先执行完
# print("Hello")
# print(t1.getName()) #获取线程名



##设置setDaemon状态(True/False)的区别
# import threading, time
#
#
# def doThreadTest():
#     print('start thread time:', time.strftime('%H:%M:%S'))
#     time.sleep(10)
#     print('stop thread time:', time.strftime('%H:%M:%S'))
#
# threads = []
# for i in range(3):
#     thread = threading.Thread(target=doThreadTest)
#     # thread.setDaemon(True)
#     threads.append(thread)
#
# for t in threads:
#     t.start()
#
# for t in threads:
#     t.join(1)
# print('stop main thread')

# #多线程请求同一资源情况
# import threading
# import time
#
# num = 100
# def show():
#     global num
#     time.sleep(1)
#     num -= 1
#
# list = []
# for i in range(100):
#     t = threading.Thread(target=show)
#     t.start()
#     list.append(t)
#
# for t in list:
#     t.join()
# print(num)

import threading
import time

num = 100
lock = threading.Lock()

def show():
    global num
    time.sleep(1)
    lock.acquire()
    num -= 1
    lock.release()

list = []
for i in range(100):
    t = threading.Thread(target=show)
    t.start()
    list.append(t)

for t in list:
    t.join()

print(num)