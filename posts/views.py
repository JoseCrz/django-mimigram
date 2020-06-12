from django.http import HttpResponse
from datetime import datetime

posts = [
    {
        'name': 'My Dog.',
        'user': 'Yésica Cortes',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/id/237/200/200'
    },
    {
        'name': 'Khe.',
        'user': 'Pink Woman',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/id/84/200/200'
    },
    {
        'name': 'Nautural web.',
        'user': 'Pancho Villa',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/id/784/200/200'
    },
]

# Create your views here.
def list_post(response):
    content = []
    for post in posts:
        content.append("""
          <p><b>{name}</b></p>
          <p>{user} - {timestamp}</p>
          <img src="{picture}"/>
        """.format(**post))

    return HttpResponse('<br>'.join(content))