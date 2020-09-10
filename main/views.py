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

'''class UpdateAttendance(UpdateView):
    model = models.Attendance
    template_name = 'main/update_attendance.html'
    fields = '__all__'
    success_url = '/students' '''

class TeacherCreate(CreateView):
    model = models.Teacher
    template_name = 'main/create_teacher.html'
    fields = '__all__'
    success_url = '/teachers'

class TeacherList(ListView):
    model = models.Teacher
    template_name = 'main/teacher_list.html'
    context_object_name = 'teachers'

class TeacherUpdate(UpdateView):
    model = models.Teacher
    template_name = 'main/create_teacher.html'
    success_url = '/teachers'

def TeacherInfo(request , pk):
    teacher = get_object_or_404(models.Teacher , pk = pk)
    context = {
        'teacher' : teacher
    }

    return render(request , 'main/teacher.html' , context)

def index(request):

    context = {}

    return render(request, 'main/index.html' , context)

'''class DivisionStudents(DetailView):
    #queryset = models.Student.objects.filter(classroom = 1)
    query_pk_and_slug
    context_object_name = 'students'
    template_name = 'main/division_students.html'

'''

class DivisionList(ListView):
    model = models.Class
    template_name = 'main/index.html'
    context_object_name = 'divisions'

def DivisionStudents(request , pk):
    queryset = models.Student.objects.filter(classroom=pk)

    context = {
        'students' : queryset
    }

    return render(request , 'main/division_students.html' , context)