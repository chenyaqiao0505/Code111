from RedisHelper import RedisHelper
import time
#发布
obj = RedisHelper()
for i in range(100):
    for j in range(100):
        obj.publish('mytopic%s'%i,'hello%s'%j)#发布
        # time.sleep(0.1)