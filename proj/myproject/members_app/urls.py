from django.urls import path
from .views import input_view, output_view, session_view


urlpatterns = [
    path('input/', input_view, name='input'),
    path('output/', output_view, name='output'),
    path('session/', session_view, name='session'),
]
