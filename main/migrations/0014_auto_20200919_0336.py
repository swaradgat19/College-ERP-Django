# Generated by Django 3.1 on 2020-09-18 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_marks_student_performance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marks',
            name='student_performance',
            field=models.CharField(default='', max_length=100),
        ),
    ]
