from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse , HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from main import models
#from main import forms
from django.views.generic import (
    ListView,
    DetailView,
    FormView,
    UpdateView,
    CreateView
)
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .decorators import unauthenticated_user,allowed_users
# Create your views here.
@unauthenticated_user
def registerPage(request):
    form = UserCreationForm()

    if request.method == 'POST' :
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user )

            return redirect('login')
    
    context = {'form':form}
    return render(request, 'main/register.html', context)
@unauthenticated_user    
def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR Password in incorrect')
        

    context = {}
    return render(request, 'main/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

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

class StudentCreate(LoginRequiredMixin, CreateView):
    model = models.Student
    template_name = 'main/create_student.html'
    fields = '__all__'
    success_url = '/students'

class StudentUpdate(LoginRequiredMixin , UpdateView):
    model = models.Student
    template_name = 'main/create_student.html'
    fields = '__all__'
    success_url = '/students'

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
    fields = '__all__'
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

class create_div(CreateView):
    model = models.Class
    template_name = 'main/create_div.html'
    fields = '__all__'
    success_url = '/'

class create_branch(CreateView):
    model = models.Branch
    template_name = 'main/create_branch.html'
    fields = '__all__'
    success_url = '/'
'''
def UpdateAttendance(request , pk):

    student = get_object_or_404(models.Student , pk =pk)
    attendance = models.Attendance.objects.filter(student=student) # Gets the attendance of that student

    attendance_form = forms.Attendance_Form()

    if request.method == 'POST':
        attendance_form = forms.Attendance_Form(request.POST)
        if attendance_form.is_valid():
            attendance_form.save()
            return HttpResponseRedirect('/')

    context = {
        'form' : attendance_form,
        'student' : student,
        'attendance' : attendance
    }
    '''

    #return render(request , 'main/update_attendance.html' , context)


class UpdateAttendance(UpdateView):
    model = models.Attendance
    template_name = 'main/update_attendance.html'
    fields = '__all__'
    success_url = '/'


def Attendance_list(request , pk):

    student  = get_object_or_404(models.Student , pk = pk)
    attendance = models.Attendance.objects.filter(student=pk)

    context = {
        'attendance' : attendance,
        'student' : student
    }


    return render(request , 'main/attendance_list.html' , context)

class create_subject(CreateView):
    model = models.Subject
    template_name = 'main/create_subject.html'
    success_url = '/'
    fields = '__all__'

class whos_attendance(ListView):

    model = models.Student
    context_object_name = 'student'
    template_name = 'main/whos_attendance.html' 


def whose_attendance(request):

    student = models.Student.objects.all()
    attendance = models.Attendance.objects.all()

    context = {
        'student' : student ,
        'attendance' : attendance
    }

    return render(request , 'main/whos_attendance.html' , context)

class UpdateMarks(UpdateView):
    model = models.Marks
    fields = '__all__'
    template_name = 'main/update_marks.html'
    success_url = '/'

def whos_marks(request):
    student = models.Student.objects.all()
    marks = models.Marks.objects.all()

    context = {
        'student' : student,
        'marks' : marks
    }

    return render(request , 'main/whos_marks.html' , context)