from django.urls import path

from .views import search, listen

urlpatterns = [
    path(r'search', search, name='text-search'),
    path(r'listen', listen, name='voice-search')
]
