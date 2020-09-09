from django.contrib import admin
from main import models

# Register your models here.

admin.site.register([
    models.Branch,
    models.Class,
    models.Subject,
    models.Student,
    models.Teacher,
    models.Attendance,
    models.Marks
])
