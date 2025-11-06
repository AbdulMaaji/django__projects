from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render


def credits(request):
    content = "Abdul Ma\'aji"

    return HttpResponse(content, content_type="text/plain")


def about(reguest):
    content = "<html><body><h1>Hello World!</h1></body></html>"

    return HttpResponse(content, content_type="text/html")


def version_info(request):
    import django
    import sys

    info = {
        "python_version": sys.version,
        "django_version": django.get_version(),
    }

    return JsonResponse(info)


def blog_home(request):
    posts = [
        {
            'title':  'First Post',
            'author': 'Amina',
            'content': 'Welcome to my blog!'
        },
        {
            'title': 'Second Post',
            'author': 'Yusuf',
            'content': 'Learning Django is fun!'
        },
        {
            'title': 'Third post',
            'author': 'Zahra',
            'content': 'Templates are cool!'
        },
    ]

    return render(request, 'blog/home.html', {'posts': posts})
