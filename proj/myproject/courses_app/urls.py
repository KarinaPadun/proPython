from django.urls import path
from .views import courses_view  

app_name = "courses"

urlpatterns = [
    path('courses/', courses_view, name='courses'),
]
