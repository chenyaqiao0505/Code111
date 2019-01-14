#coding=utf-8
#只做串口通讯
import sys,threading,time
import serial
import binascii,encodings
import re
import os
from struct import *
#from myutil import *
#name: SerialTest.py

#锁,避免串口资源冲突
mylock = threading.RLock()

class ComThread:
    def __init__(self, Port=0):
        self.l_serial = None
        self.alive = False
        self.waitEnd = None
        self.port = Port
        # print(11111)
        # print(self.port)

        #数据
        self.snddata = ''
        self.rcvdata = ''

    def waiting(self):
        if not self.waitEnd is None:
            self.waitEnd.wait()
        print()

    def SetStopEvent(self):
        if not self.waitEnd is None:
            self.waitEnd.set()
        self.alive = False
        self.stop()

    def stop(self):
        self.thread_read.join()
        if self.l_serial.isOpen():
            self.l_serial.close()

        #点击开始按钮之后，输入‘func:test on’指令
    def start(self):
        self.l_serial = serial.Serial()
        self.l_serial.port = self.port
        print(self.port)
        self.l_serial.baudrate = 9600
        self.l_serial.timeout = 2  #秒
        self.l_serial.open()

        if self.l_serial.isOpen():
            self.waitEnd = threading.Event()
            self.alive = True
            print('open serial port %d ok!\n' %(self.port+1))
            self.thread_read = None
            self.thread_read = threading.Thread(target=self.FirstReader)
            self.thread_read.setDaemon(1)
            self.thread_read.start()

            self.thread_write = None
            self.thread_write = threading.Thread(target=self.FirstWriter)
            self.thread_write.setDaemon(1)
            self.thread_write.start()


            return True
        else:
            return False

    def restart(self):
        #停止一次线程,事先需要调用stop方法，开始输入指令、
        stop()
        SendST = 'func:test?\r\n'
        self.l_serial.write(SendMS.encode('utf-8'))
        #再次返回机器状态和模式状态
        #是否开启
        SendMS = 'func:test?\r\n'
        self.l_serial.write(SendMS.encode('utf-8'))
        time.sleep(0.05)
        n = self.l_serial.inWaiting()
        dataMS = self.l_serial.read(n)
        listMS.append(dataMS)
        strMS = listMS[0]

        #返回机器模式码
        SendMM='manu:edit:mode?\r\n'
        self.l_serial.write(SendMM.encode('utf-8'))
        time.sleep(0.05)
        n = self.l_serial.inWaiting()
        dataMM = self.l_serial.read(n)
        listMM.append(dataMS)
        strMM= listMM[0]
        #继续执行循环输出指令
        FirstWriter()


    def FirstReader(self):
        while self.alive:
            # 接收间隔
            time.sleep(0.1)
            try:
                # 获取接收到的数据长度
                n = self.l_serial.inWaiting()
            except Exception as ex:
                print(str(ex))

        self.waitEnd.set()
        self.alive = False



    def FirstWriter(self):

        while self.alive:
            # 接收间隔
            time.sleep(0.1)
            #print("循环")
            listNM=[]
            listMS=[]
            listMM=[]
            listMT=[]
            try:
                # print('aaa')
                SendMN='*IDN?\r\n'
                if SendMN!='':
                    self.l_serial.write(SendMN.encode('utf-8'))
                time.sleep(0.05)
                n = self.l_serial.inWaiting()
                if n < 31:
                    time.sleep(0.1)
                    n = self.l_serial.inWaiting()
                    dataNM = self.l_serial.read(n)
                    listNM.append(dataNM)
                    strNM=listNM[1]
                else:
                    dataNM = self.l_serial.read(n)
                    listNM.append(dataNM)
                    strNM = listNM[1]

                #是否开启
                SendMS = 'func:test?\r\n'
                self.l_serial.write(SendMS.encode('utf-8'))
                time.sleep(0.05)
                n = self.l_serial.inWaiting()
                dataMS = self.l_serial.read(n)
                listMS.append(dataMS)
                strMS = listMS[0]
                return strMS

                #返回机器模式码
                SendMM='manu:edit:mode?\r\n'
                self.l_serial.write(SendMM.encode('utf-8'))
                time.sleep(0.05)
                n = self.l_serial.inWaiting()
                dataMM = self.l_serial.read(n)
                listMM.append(dataMS)
                strMM= listMM[0]

                #返回机器测量结果
                SendMT='meas?\r\n'
                self.l_serial.write(SendMT.encode('utf-8'))
                time.sleep(0.1)
                n = self.l_serial.inWaiting()
                dataMT = self.l_serial.read(n)
                listMT.append(dataMT)
                strMT = listMT[0]

                # if command!='':
                #     self.l_serial.write(command.encode('utf-8'))
                #     command=''

                MA = (strNM,strMS,strMM,strMT)
                return MA

            except Exception as ex:
                print(str(ex))
        self.waitEnd.set()
        self.alive = False


# 测试用部分
# if __name__ == '__main__':
#     com = 2
#     rt = ComThread(int(com)-1)
#     try:
#         if rt.start():
#             rt.waiting()
#             rt.stop()
#         else:
#             pass
#     except Exception as se:
#         print(str(se))
#
#     if rt.alive:
#         rt.stop()
#     os.system("pause")
#
#     print('')
#     print('End OK .')
#     del rt
