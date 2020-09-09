from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from main import models
from main import forms
from django.views.generic import (
    ListView,
    DetailView,
    FormView,
    UpdateView,
    CreateView
)
# Create your views here.

class StudentList(ListView):
    model = models.Student
    template_name = 'student_list'
    context_object_name = 'students' 

def Student(request,pk):
    #student = models.Student.objects(pk = pk)

    student = get_object_or_404(models.Student , pk = pk)

    context = {
        'Students' : student
        }

    return render(request , 'main/student.html' , context)

class StudentCreate(CreateView):
    model = models.Student
    template_name = 'main/create_student.html'
    fields = '__all__'
    success_url = '/students'

class StudentUpdate(UpdateView):
    model = models.Student
    template_name = 'main/create_student.html'
    fields = '__all__'
    success_url = '/students'

class UpdateAttendance(UpdateView):
    model = models.Attendance
    template_name = 'main/update_attendance.html'
    fields = '__all__'
    success_url = '/students'


    