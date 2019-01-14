from UdpClient import  udpclient
import time
import threading 


w1 = udpclient()
class udpdevicedo:
    def __init__(self):
        self.DeviceOnline = 0     #0在线
        self.DINumList = 0
        self.alive = 1
        self.thread_lock = 0  #开始键是否点击 点了1  没点0
        self.thread_read = threading.Thread(target=self.MonitorDevice)
        self.thread_read.setDaemon(1)
        self.thread_read.start()
        
        self.controllingDevice = 0 #control执行完标志 初始化为0 表示没执行control

    def MonitorDevice(self):
        while self.alive:
            try:
                if self.controllingDevice == 0:
                    self.DINumList = self.CheckNum()
                    if len(self.DINumList) != 0:
                        self.DeviceOnline = 1
            except Exception as ex:
                self.DeviceOnline = 0
            time.sleep(1)
            
    def StartThread(self):
        self.controllingDevice = 1
        print('startthread')
        
    def CheckNum(self):
        i = 0
        DI = 0
        DO = 0
        Numlist = []
        msg = b'\xAA\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        Result = w1.control(msg, True)
        if Result != None:
            reList = [hex(x) for x in bytes(Result)]
            # 字节串转16进制数组,再转整数
            DI = int(reList[1], 16)
            DO = int(reList[2], 16)
            Numlist.append(DI)
            Numlist.append(DO)
        else:
            print('请检查板卡是否插好~！')
        return Numlist

    def Read(self,value):
        msg = b'\xAA\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        Result = w1.control(msg, True)
        resu = [] # 接收结果不正确的值
        r1 = []  # 接受结果的列表
        i = 0
        ss = self.CheckNum()
        for x in bytes(Result):
            i +=1
            if i !=1 and i !=2 and i <= ss[1]*2:     #去掉前两位
                resu.append(x ^ value)
                a = x ^ value
                if a == 0:
                    r1.append([])   
                else:
                    e1 = []
                    for j in range(8):
                        if a & 1 == 1:
                            e1.append(8-j)
                        a = a >> 1
                    r1.append(e1)
        r2 = []     #结果前后移位
        leng = int(len(r1)/2)
        for i in range(leng):
            r2.append(r1[i*2+1])
            r2.append(r1[i*2])
        return r2

    def control1(self):
        i = 0
        output = []
        toutput = []
        msglist = [b'\xAA\x03\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
                   b'\xAA\x03\xAA\xAA\xAA\xAA\xAA\xAA\xAA\xAA\xAA\xAA\xAA\xAA\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
                   b'\xAA\x03\x55\x55\x55\x55\x55\x55\x55\x55\x55\x55\x55\x55\x55\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
                   b'\xAA\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00']
        
        Result = w1.control(msglist[0], False)
        output0 = self.Read(0xFF)
        Result = w1.control(msglist[1], False)
        output1 = self.Read(0xAA)             

        Result = w1.control(msglist[2], False)
        output2 = self.Read(0x55)
        
        Result = w1.control(msglist[3], False)
        output3 = self.Read(0x00)
        for i in range(len(output0)):
            output3[i] = list(set(output0[i]+output1[i]+output2[i]+output3[i]))
        self.controllingDevice = 0
        return output3
