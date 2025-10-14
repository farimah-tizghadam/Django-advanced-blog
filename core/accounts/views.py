from django.http import HttpResponse
from .tasks import sending_email




def send_email(request):
    sending_email.delay()
    return HttpResponse("<h1>Done Sending</h1>")