import pika

RABBITMQ_QUEUE = "filtered_trades"

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

#channel.queue_declare(queue=RABBITMQ_QUEUE, durable=True)


def callback(ch, method, properties, body):
    print(f"New event is received: {body}")


channel.basic_consume(on_message_callback=callback, queue=RABBITMQ_QUEUE, auto_ack=True)

channel.start_consuming()