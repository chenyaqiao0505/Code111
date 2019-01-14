from gevent import monkey; monkey.patch_all()
import gevent
import time


def foo():
    print('11')
    time.sleep(3)
    print('22')

def bar():
    print('33')
    print('44')

gevent.joinall([
gevent.spawn(foo),
gevent.spawn(bar),
])