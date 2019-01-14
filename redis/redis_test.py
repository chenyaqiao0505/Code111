import redis
import time
r = redis.Redis(host='127.0.0.1', port=6379,db=2)
# for i,j,k in zip(range(50),range(50,100),range(100,150)):
r.lpush('name',2)
r.lpush('name',3,4,5,6,7,'q','w','e','r','t','p')
    # r.hget('name','i')
# print(r.lpop('name'))
# print(r.llen('name'))

list = []
for i in range(r.llen('name')):
    list.append(r.lpop('name').decode())

print(list)
