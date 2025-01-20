from django.contrib import admin
from django.urls import path
from task1.views import platform, games, cart, sign_up_by_django, sign_up_by_html

urlpatterns = [
    path('', platform, name='platform'),
    path('games/', games, name='games'),
    path('cart/', cart, name='cart'),
    path('html_sign_up/', sign_up_by_html, name='sign_up_by_html'),
    path('django_sign_up/', sign_up_by_django, name='sign_up_by_django'),
]


