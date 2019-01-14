from UdpClientForDOTestOk22 import  udpclient

w1 = udpclient()
class udpdevice:
    def __init__(self):
        self.a1 = []
        
    def CheckNum(self):
        i = 0
        DI = 0
        DO = 0
        while True:
            # The number of card
            msg = b'\xAA\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
            Result = w1.control(msg, True)
            if Result != None:
                reList = [hex(x) for x in bytes(Result)]
                # 字节串转16进制数组,再转整数
                DI = int(reList[1], 16)
                DO = int(reList[2], 16)
            i += 1
            if i == 4:
                break
            return DI+DO


    def Read(self,value):
      #读取写00情况
       #读取DI
        msg = b'\xAA\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        Result = w1.control(msg, True)
        # reList = [hex(x) for x in bytes(Result)]  # 数据库的处理
        #print(Result,"34543")
        #TK=[hex(x) for x in bytes(Result)]
        #print(TK,"output")
        
        resu = [] # 接收结果不正确的值
        r1 = []  # 接受结果的列表
        i = 0
        for x in bytes(Result):
            i +=1
            if i !=1 and i !=2:     #去掉前两位
                resu.append(x ^ value)
                a = x ^ value
                if a ==0:
                    r1.append('pass')
                else:
                    e1 = []
                    for j in range(8):
                        if a & 1 ==1:
                            e1.append(j)
                        a = a >> 1
                    r1.append(e1)
        return r1

    def control1(self):
        #发送控制命令
        i = 0
        output = []
        toutput = []
        msglist = [b'\xAA\x03\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
                   b'\xAA\x03\xAA\xAA\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
                   b'\xAA\x03\x55\x55\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
                   b'\xAA\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00']
        while True:
            if i == 0:
                Result = w1.control(msglist[i], False)
                output = w2.Read(0xFF)
                toutput = output
                print(i)
            if i == 1:    
                print(i)
                Result = w1.control(msglist[i], False)
                output = w2.Read(0xAA)                    
                if len(output) < len(toutput):
                    for l in range(len(output)):
                        if toutput[l] != output[l]:
                            toutput[l] = set(toutput[l]+output[l])                                
                    else:
                        for ll in range(len(output)):
                            if toutput[l] != output[l]:
                                toutput[ll] = set(toutput[ll]+output[ll])
            if i == 2:
                print(i)
                Result = w1.control(msglist[i], False)
                output = w2.Read(0x55)

                if len(output) < len(toutput):
                    for l in range(len(output)):
                        if toutput[l] != output[l]:
                            toutput[l] = set(toutput[l]+output[l])
                            
                    else:
                        for ll in range(len(output)):
                            if toutput[l] != output[l]:
                                toutput[ll] = set(toutput[ll]+output[ll])
            if i == 3:
                print(i)
                Result = w1.control(msglist[i], False)
                output = w2.Read(0x00)
                if len(output) < len(toutput):
                    for l in range(len(output)):
                        if toutput[l] != output[l]:
                            toutput[l] = set(toutput[l]+output[l])
                            
                    else:
                        for ll in range(len(output)):
                            if toutput[l] != output[l]:
                                toutput[ll] = set(toutput[ll]+output[ll])

            i += 1
            
            if i == 4:
                break
        return toutput

w2 = udpdevice()
