from celery import shared_task
from time import sleep
from django.http import JsonResponse


@shared_task
def sending_email():
    sleep(3)
    print('done sending email')