from django.urls import path

from .views import search, upload

urlpatterns = [
    path(r'search', search, name='text-search'),
    path(r'upload', upload, name='image-search'),
    # path(r'listen', listen, name='voice-search')
]
