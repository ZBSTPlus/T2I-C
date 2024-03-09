from django.urls import path
from text_converter.views import text_to_image

urlpatterns = [
    path('text-to-image/', text_to_image, name='text_to_image'),
]
