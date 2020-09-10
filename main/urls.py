from django.urls import path
from main import views

urlpatterns = [
    path('students/' , views.StudentList.as_view(), name = 'student_list'),
    path('student/<int:pk>' , views.Student , name = 'get_student'),
    path('create_student/' , views.StudentCreate.as_view() , name = 'create_student'),
    path('student_update/<int:pk>' , views.StudentUpdate.as_view() , name = 'student_update'),
    #path('update_attendance/' , views.UpdateAttendance.as_view() , name = 'update_attendance'),

    path('teachers/' , views.TeacherList.as_view(),name = 'teacher_list'),
    path('teacher/<int:pk>' , views.TeacherInfo , name = 'get_teacher'),
    path('create_teacher' , views.TeacherCreate.as_view()),
    path('update_teacher/<int:pk>' , views.TeacherUpdate.as_view()),   

    path('division_students/<int:pk>' , views.DivisionStudents , name = 'div_kids'),     
    
    path('' , views.index , name = 'home')
]