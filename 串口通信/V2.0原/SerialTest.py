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
        global t1, t2, t3, t4
        self.l_serial = None
        self.alive = False
        self.waitEnd = None
        self.port = Port
        self.t1=''
        self.t2=''
        self.t3=''
        self.t4=''
        self.control=0
        self.acw=0
        self.dcw=0
        self.ir=0
        self.gb=0
        self.getIRConf=0
        self.IRConfig=[]
        self.setIRConfig=0
        self.setValuesIR = ""

        #数据
        self.snddata = ''
        self.rcvdata = ''
        for i in range(5):
            self.IRConfig.append('')

    def waiting(self):
        if not self.waitEnd is None:
            self.waitEnd.wait()
        print()

    def getValueOfID(self):
        return self.t1

    def getValueOfMode(self):
        return self.t2

    def getValueOfStatus(self):
        #print(self.t3)
        return self.t3

    def getValueOfMeas(self):
        return self.t4
#返回了IRConfig
    def getValueOfConfig(self):
        return self.IRConfig
#配置setIRConfig为values,setIRConfig为状态码
    def setIRValueOfConfig(self,Values):
        self.setValuesIR = Values
        #print(Values, self.setValuesIR)
        self.setIRConfig=1


    def setValue(self):
        pass

    def TestOn(self):
        self.control=1

    def setModul(self, mode):
        if mode==1:
            self.acw=1
        elif mode==2:
            self.dcw=1
        elif mode==3:
            self.ir=1
            self.getIRConf=1
        else:
            self.gb=1

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
        #初始化串口
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
            read=''
            time.sleep(0.1)
            try:
                SendMN='*IDN?\r\n'
                if SendMN!='':
                    self.l_serial.write(SendMN.encode('utf-8'))
                time.sleep(0.05)
                n = self.l_serial.inWaiting()
                if n < 31:
                    time.sleep(0.1)
                    n = self.l_serial.inWaiting()
                    self.t1 = self.l_serial.read(n)
                else:
                    self.t1 = self.l_serial.read(n)

                #是否开启
                SendMS = 'func:test?\r\n'
                self.l_serial.write(SendMS.encode('utf-8'))
                time.sleep(0.05)
                n = self.l_serial.inWaiting()
                self.t3 = self.l_serial.read(n)

                #返回机器模式码
                SendMM='manu:edit:mode?\r\n'
                self.l_serial.write(SendMM.encode('utf-8'))
                time.sleep(0.05)
                n = self.l_serial.inWaiting()
                self.t2 = self.l_serial.read(n)

                #返回机器测量结果
                SendMT='meas?\r\n'
                self.l_serial.write(SendMT.encode('utf-8'))
                time.sleep(0.1)
                n = self.l_serial.inWaiting()
                self.t4 = self.l_serial.read(n)

                if self.control==1:
                    SendMT="func:test on\r\n"
                    self.l_serial.write(SendMT.encode('utf-8'))
                    self.control=0

                if self.acw==1:
                    SendMT="manu:edit:mode acw\r\n"
                    self.l_serial.write(SendMT.encode('utf-8'))
                    self.acw=0

                if self.dcw==1:
                    SendMT="manu:edit:mode dcw\r\n"
                    self.l_serial.write(SendMT.encode('utf-8'))
                    self.dcw=0
                if self.ir==1:
                    SendMT="manu:edit:mode ir\r\n"
                    self.l_serial.write(SendMT.encode('utf-8'))
                    self.ir=0
                if self.gb==1:
                    SendMT="manu:edit:mode gb\r\n"
                    self.l_serial.write(SendMT.encode('utf-8'))
                    self.gb=0

                if self.getIRConf==1:
                    reList=[]
                    SendMT="MANU:IR:VOLTage? \r\n"
                    self.l_serial.write(SendMT.encode('utf-8'))
                    time.sleep(0.2)
                    n = self.l_serial.inWaiting()
                    read=self.l_serial.read(n)
                    #test=str(read)

                    #print(test.replace('\r',''))
                    reList.append(read)

                    SendMT="MANU:IR:RHISet? \r\n"
                    self.l_serial.write(SendMT.encode('utf-8'))
                    time.sleep(0.2)
                    n = self.l_serial.inWaiting()
                    read=self.l_serial.read(n)
                    reList.append(read)
                    #self.IRConfig = self.IRConfig +'RHISet:,'+ read


                    SendMT="MANU:IR:RLOSet? \r\n"
                    self.l_serial.write(SendMT.encode('utf-8'))
                    time.sleep(0.2)
                    n = self.l_serial.inWaiting()
                    read=self.l_serial.read(n)
                    reList.append(read)
                    #self.IRConfig = self.IRConfig +'RLOSet:,'+ read

                    SendMT="MANU:IR:TTIMe? \r\n"
                    self.l_serial.write(SendMT.encode('utf-8'))
                    time.sleep(0.2)
                    n = self.l_serial.inWaiting()
                    read=self.l_serial.read(n)
                    reList.append(read)
                    #self.IRConfig = self.IRConfig +'TTIMe:,'+ read

                    SendMT="MANU:IR:REF? \r\n"
                    self.l_serial.write(SendMT.encode('utf-8'))
                    time.sleep(0.2)
                    n = self.l_serial.inWaiting()
                    read=self.l_serial.read(n)
                    reList.append(read)
                    #self.IRConfig = self.IRConfig +'REF:,'+ read
                    self.IRConfig=reList

                    self.getIRConf=0

                if self.setIRConfig==1:
                    # 设置
                    print(self.setValuesIR)
                    # VOLTage  0.05-1
                    SendMT='MANU:IR:VOLTage '+ self.setValuesIR[0] + '\r\n'
                    print(SendMT)
                    self.l_serial.write(SendMT.encode('utf-8'))
                    time.sleep(0.2)


                    SendMT='MANU:IR:RHISet ' + self.setValuesIR[1] + '\r\n'
                    self.l_serial.write(SendMT.encode('utf-8'))
                    time.sleep(0.2)


                    SendMT='MANU:IR:RLOSet '+ self.setValuesIR[2] + '\r\n'
                    self.l_serial.write(SendMT.encode('utf-8'))
                    time.sleep(0.2)


                    SendMT='MANU:IR:TTIMe '+ self.setValuesIR[3] + '\r\n'
                    self.l_serial.write(SendMT.encode('utf-8'))
                    time.sleep(0.2)


                    SendMT='MANU:IR:REF '+ self.setValuesIR[4] + '\r\n'
                    self.l_serial.write(SendMT.encode('utf-8'))
                    time.sleep(0.2)

                    # 刷新
                    self.getIRConf=1
                    # 恢复
                    self.setIRConfig=0

            except Exception as ex:
                print(str(ex))
        self.waitEnd.set()
        self.alive = False

# 测试用部分
#if __name__ == '__main__':
     #com = 2
     #rt = ComThread(int(com)-1)
     #try:
         #if rt.start():
             #rt.waiting()
             #rt.stop()
         #else:
             #pass
     #except Exception as se:
         #print(str(se))

     #if rt.alive:
         #rt.stop()
     #os.system("pause")

     #print('')
     #print('End OK .')
     #del rt
