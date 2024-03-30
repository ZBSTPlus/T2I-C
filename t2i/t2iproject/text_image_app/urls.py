from django.urls import path
from .views import *
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index, name='index'),
    path('download_image/', download_image, name='download_image'),

]
