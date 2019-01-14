import pika
import time
#建立连接
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

#建立管道，指定
#如果确认queue已经被声明了，也可以不写。但是你不知道生产者还是消费者先运行。如果生产者先运行的话，消费者这里的声明是没用的。
channel.queue_declare(queue='hello2',durable=True)


def callback(ch, method, properties, body):
    time.sleep(4)
    print(" [x] Received %r" % body )
    ch.basic_ack(delivery_tag=method.delivery_tag)

# ch    管道内存对象
# method    消息发给谁
# properties  暂无
# body    消息内容


channel.basic_qos(prefetch_count=1)#处理完这条再处理下一条
#开始消费消息
channel.basic_consume(callback,
        queue='hello2',
        no_ack=True)

#callback   如果收到消息，就调用callback函数来处理消息。回调函数
#queue    消息名称
#no_ack=True    不管该条消息有没有处理完成，都不会给生产者发确认消息
print(' [*] Waiting for messages. To exit press CTRL+C')

# 开始收消息
channel.start_consuming()
