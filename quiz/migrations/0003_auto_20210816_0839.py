# Generated by Django 3.2.6 on 2021-08-16 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='q_attempted',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='student',
            name='student_score',
            field=models.IntegerField(default=0),
        ),
    ]
