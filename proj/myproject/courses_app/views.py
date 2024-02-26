from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .models import Courses
from members_app.models import UserEnrollment
from django.contrib.auth.mixins import LoginRequiredMixin

@login_required
def courses_view(request):
    return render(request, 'courses_app/courses.html')

class CoursesListView(ListView):
    model = Courses
    template_name = 'courses_app/courses_list.html'
    context_object_name = 'courses'

class CourseDetailView(DetailView):
    model = Courses
    template_name = 'courses_app/course_detail.html'
    context_object_name = 'course'

class EnrollCourseView(LoginRequiredMixin, CreateView):
    model = UserEnrollment
    template_name = 'courses_app/enroll_course.html'
    fields = ['course']
    success_url = '/courses/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
