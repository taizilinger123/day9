# _*_coding:utf-8_*_
__author__ = 'Alex Li'
import pika,time
#new---Python File创建一个新的python文件
connection = pika.BlockingConnection(pika.ConnectionParameters(
    'localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello2',durable=True)

def callback(ch, method, properties, body): #回调函数
    print("--->",ch,method,properties)
    time.sleep(30)
    print(" [x] Received %r" % body)
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1) #处理完这一条再给我发下一条
channel.basic_consume(#消费消息
                      callback, #如果收到消息，就调用CALLBACK函数来处理消息
                      queue='hello2',
                      #no_ack=True  #不确认
                     )

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()