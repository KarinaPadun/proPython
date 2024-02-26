from django.urls import path
from .views import courses_view  
from .views import CoursesListView, CourseDetailView, EnrollCourseView

app_name = "courses"

urlpatterns = [
    path('', CoursesListView.as_view(), name='courses_list'),
    path('courses/', courses_view, name='courses'),
    path('<int:pk>/', CourseDetailView.as_view(), name='course_detail'),
    path('enroll/', EnrollCourseView.as_view(), name='enroll_course'),
]
