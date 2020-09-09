from django.urls import path
from main import views

urlpatterns = [
    path('students/' , views.StudentList.as_view()),
    path('student/<int:pk>' , views.Student , name = 'get_student'),
    path('create_student/' , views.StudentCreate.as_view()),
    path('student_update/<int:pk>' , views.StudentUpdate.as_view()),
    #path('update_attendance/' , views.UpdateAttendance.as_view()),

    path('teachers/' , views.TeacherList.as_view()),
    path('teacher/<int:pk>' , views.TeacherInfo , name = 'get_teacher'),
    path('create_teacher' , views.TeacherCreate.as_view()),
    path('update_teacher/<int:pk>' , views.TeacherUpdate.as_view()),        
    
    path('' , views.index)
]