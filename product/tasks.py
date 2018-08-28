import time

from celery import shared_task

from product.email_service import send_email


@shared_task
def trigger_email(subject, message):
	delay_time = 15*60
	time.sleep(delay_time)
	send_email(subject, message)