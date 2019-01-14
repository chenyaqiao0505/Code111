import time
import requests
class Timeit(object):
    def __init__(self,func):
        self._wrapped = func

    def __call__(self, *args, **kwargs):
        start_time = time.time()
        result = self._wrapped(*args, **kwargs)
        print('现在是%s' %(time.time() - start_time))
        return result

@Timeit
def func():
    time.sleep(1)
    print( 'invoking function func')

if __name__ == '__main__':
    func()