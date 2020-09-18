# Generated by Django 3.1 on 2020-09-15 04:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_remove_attendance_percentage'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='branch',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='main.branch'),
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='subject',
        ),
        migrations.AddField(
            model_name='teacher',
            name='subject',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='main.subject'),
        ),
    ]
