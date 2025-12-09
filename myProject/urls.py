from django.contrib import admin
from django.urls import path, include
from home import views as home_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('credits/', home_views.credits, name='credits'),
    path('about/', home_views.about, name='about'),
    path('version-info/', home_views.version_info, name='version_info'),
    path('news/', home_views.news, name='news'),
    path('news-test/', home_views.news_test, name='news_test'),
    path('blog/', home_views.blog_home, name='blog_home'),
    path('todo/', include('todo.urls')),
    path('bands/', include('bands.urls')),
]
