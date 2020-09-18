from django.db import models
from django.core.validators import (
    MinValueValidator ,
    MaxValueValidator 
)
# Create your models here.

class Branch(models.Model):
    b_name = models.CharField(max_length = 256)

    def __str__(self):
        return self.b_name

class Class(models.Model):
    c_name = models.CharField(max_length=256)
    branch = models.ForeignKey('Branch' , on_delete=models.CASCADE)

    def __str__(self):
        return self.c_name
    
class Subject(models.Model):
    sub_name = models.CharField(max_length=100)

    def __str__(self):
        return self.sub_name
    
class Student(models.Model):
    s_name = models.CharField(max_length=256)
    classroom = models.ForeignKey('Class' , on_delete = models.CASCADE,default=None)

    def __str__(self):
        return self.s_name

class Teacher(models.Model):
    t_name = models.CharField(max_length=100)
    subject = models.ForeignKey('Subject' , on_delete=models.CASCADE , default=None)
    classroom = models.ForeignKey('Class' , on_delete=models.CASCADE ,default=None)
    branch = models.OneToOneField(Branch , on_delete=models.CASCADE , default=None)

    def __str__(self):
        return self.t_name

class Attendance(models.Model):
    student = models.OneToOneField(
        Student ,
        on_delete=models.CASCADE ,
        primary_key=True
    )
    #percentage = models.PositiveIntegerField(validators = [MinValueValidator(0) ,  MaxValueValidator(100)])
    #count = models.PositiveIntegerField(validators = [MinValueValidator(0)])
    attended_classes = models.IntegerField( default= 0,validators = [MinValueValidator(0) ])
    total_classes = models.IntegerField(default=0, validators=[MinValueValidator(0)])   

    def __str__(self):
        return "{} - {} %".format(self.student , self.attended_classes/self.total_classes*100)

class Marks(models.Model):

    def something():
        return 'a string'

    student = models.OneToOneField(
        Student ,
        on_delete=models.CASCADE,
        primary_key=True
    )   
    marks_scored = models.IntegerField(validators = [MinValueValidator(0)])
    total_marks = models.IntegerField(validators = [MinValueValidator(0)])
    student_performance = models.CharField(default = something , max_length=100)


    def __str__(self):
        return "{} - {}".format(self.student ,self.subject , self.marks_scored)
