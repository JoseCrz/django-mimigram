""" Mimigram Views """

# Django
from django.http import HttpResponse, JsonResponse

# Utilities
from datetime import datetime

def hello_world(request):
    """ Basic Hello World """
    return HttpResponse('Hello from Django Unchained!')

def  time(request):
    now = datetime.now().strftime('%b %dth, %Y - %H:%M')
    return HttpResponse('Current server time: {now}'.format(now = now))

def numbers(request):
    numbers = request.GET['numbers']
    print(numbers)
    return HttpResponse(str(numbers))