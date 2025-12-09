from django.contrib import admin
from django.urls import path, include
from home import views as home_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/', include('todo.urls')),
]
