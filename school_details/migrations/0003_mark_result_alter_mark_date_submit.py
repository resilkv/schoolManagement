# Generated by Django 4.0.3 on 2022-04-22 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_details', '0002_mark_date_submit'),
    ]

    operations = [
        migrations.AddField(
            model_name='mark',
            name='result',
            field=models.CharField(default=1, max_length=10),
        ),
        migrations.AlterField(
            model_name='mark',
            name='date_submit',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
