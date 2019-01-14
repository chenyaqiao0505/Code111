import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=15672))
channel = connection.channel()

channel.queue_declare(queue='task_queue')

messages = ['python new_task.py First message.',
            'python new_task.py Second message..',
            'python new_task.py Third message...',
            'python new_task.py Fourth message....',
            'python new_task.py Fifth message.....',
            'python new_task.py Sixth message......']
for m in messages:
    channel.basic_publish(exchange='',
                          routing_key='task_queue',
                          body=m,
                          properties=pika.BasicProperties(
                              delivery_mode=2,  # make message persistent
                          ))
    print(" [x] Sent %r" % m)

connection.close()