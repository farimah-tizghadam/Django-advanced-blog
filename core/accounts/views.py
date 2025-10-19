from django.http import HttpResponse, JsonResponse
from .tasks import sending_email
from django.core.cache import cache
from django.views.decorators.cache import cache_page
import requests


def send_email(request):
    sending_email.delay()
    return HttpResponse("<h1>Done Sending</h1>")

# without using decorator
"""def test(request):
    if cache.get("test_delay_api") is None:
        response = requests.get('https://790fa2f6-ba9d-40be-8c7a-27479edfaa33.mock.pstmn.io/test/delay/5')
        cache.set('test_delay_api', response.json())
    return JsonResponse(cache.get('test_delay_api'))"""

#using decorator
@cache_page(60)
def test(request):
    response = requests.get('https://790fa2f6-ba9d-40be-8c7a-27479edfaa33.mock.pstmn.io/test/delay/5')
    return JsonResponse(response.json())