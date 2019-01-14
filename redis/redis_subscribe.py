from RedisHelper import RedisHelper

obj = RedisHelper()#订阅
i = 0
while True:
    redis_sub = obj.subscribe('mytopic%s'%i)  # 调用订阅方法
    msg= redis_sub.parse_response()
    print(msg)
    i += 1