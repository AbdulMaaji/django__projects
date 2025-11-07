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


def news(request):
    data = {
        'news': [
            "RiffMates now has a news page!",
            "RiffMates has it's first web page",
        ],
    }
    # Render the previous/news folder template at /news/
    return render(request, 'news/news2.html', data)


def news_test(request):
    """Render the new news2.html (the React-styled version) at /news-test/"""
    data = {
        'news': [
            "RiffMates now has a news page!",
            "RiffMates has it's first web page",
        ],
    }
    return render(request, 'news_test.html', data)
