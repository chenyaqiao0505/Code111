import pika

connection = pika.BlockingConnection(       #建立连接
    pika.ConnectionParameters(host='localhost')
    )

channel = connection.channel()  #声明一个管道

#声明QUEUE
channel.queue_declare(queue='hello2',durable=True)

channel.basic_publish(exchange='',
    routing_key='hello2',
    body='Hello World!',
    properties=pika.BasicProperties(delivery_mode=2,
                                    )
                      )

#routing_key   queue名字
#body               消息
print(" [x] Sent 'Hello World!3'")
connection.close()      #关闭连接