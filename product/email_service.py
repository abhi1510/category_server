from django.core.mail import send_mail
from django.conf import settings

from_email = settings.EMAIL_HOST_USER
# recepients = ['naveen.kumar1@timesinternet.in']
recepients = ['abhik.chy@gmail.com']


def send_email(subject, message):
    try:
        send_mail(subject, message, from_email, recepients, fail_silently=False)
    except:
    	# log error
        print('Error sending email')
