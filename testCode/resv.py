import SerialTest2
import os

if __name__ == '__main__':

    SerialTest2.com = 2
    rt = SerialTest2.ComThread(int(SerialTest2.com)-1)
    try:
        if rt.start():
            rt.waiting()
            rt.stop()
        else:
            pass
    except Exception as se:
        print(str(se))

    if rt.alive:
        rt.stop()
    os.system("pause")

    print('')
    print('End OK .')
    del rt
