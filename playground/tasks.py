from time import sleep
from celery import shared_task

@shared_task()
def notify_customers(message):
    print('Sending 10k emails...')
    sleep(10)
    print(message)
    print('Emails were successfully sent.')
