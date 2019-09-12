from django.contrib import admin
from django.urls import path,include
from finder import urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('finder/',include(urls)),
]
