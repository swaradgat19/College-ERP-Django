from django.urls import path
from main import views

urlpatterns = [
    path('students/' , views.StudentList.as_view(), name = 'student_list'),
    path('student/<int:pk>' , views.Student , name = 'get_student'),
    path('create_student/' , views.StudentCreate.as_view() , name = 'create_student'),
    path('student_update/<int:pk>' , views.StudentUpdate.as_view() , name = 'student_update'),
    path('update_attendance/<int:pk>' , views.UpdateAttendance.as_view() , name = 'update_attendance'),

    path('teachers/' , views.TeacherList.as_view(),name = 'teacher_list'),
    path('teacher/<int:pk>' , views.TeacherInfo , name = 'get_teacher'),
    path('create_teacher' , views.TeacherCreate.as_view() , name = 'create_teacher'),
    path('update_teacher/<int:pk>' , views.TeacherUpdate.as_view()),   
    path('attendance_list/<int:pk>' , views.Attendance_list),
    path('whos_attendance' , views.whos_attendance.as_view(), name = 'whos_attendance'),
    
    path('create_division' , views.create_div.as_view() , name = 'create_div'),
    path('create_branch' , views.create_branch.as_view() , name = 'create_branch'),
    path('create_subject' , views.create_subject.as_view() , name = 'create_subject'),

    path('update_marks/<int:pk>' , views.UpdateMarks.as_view() , name = 'update_marks'),
    path('whos_marks' , views.whos_marks , name = 'whos_marks'),


    path('division_students/<int:pk>' , views.DivisionStudents , name = 'div_kids'),     
    path('' , views.index , name = 'home')
]   