# Generated by Django 4.0.3 on 2022-04-19 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_details', '0005_remove_teacher_teaching_in_teacher_teaching_in'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='teaching_in',
        ),
        migrations.AddField(
            model_name='teacher',
            name='teaching_in',
            field=models.ManyToManyField(to='school_details.grade'),
        ),
    ]
