""" Mimigram Views """

# Django
from django.http import HttpResponse, JsonResponse
import json

# Utilities
from datetime import datetime

def hello_world(request):
    """ Basic Hello World """
    return HttpResponse('Hello from Django Unchained!')

def  time(request):
    now = datetime.now().strftime('%b %dth, %Y - %H:%M')
    return HttpResponse('Current server time: {now}'.format(now = now))

def sort_numbers(request):
    """ Sorts numbers & returns a json response """
    numbers = request.GET['numbers'].split(',')
    numbers_list = [int(i) for i in numbers]
    sorted_number_list = sorted(numbers_list)

    data = {
        'status': 'ok',
        'numbers': sorted_number_list,
        'message': 'Integers sorted'
    }

    return HttpResponse(json.dumps(data, indent=4), content_type='application/json')

def entrance(response, name, age):
    if age < 18:
        message = 'Sorry {} you cannot access'.format(name)
    else:
        message = 'Welcome aboard, {}!'.format(name)

    return HttpResponse(message)