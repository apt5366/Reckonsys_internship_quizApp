# Generated by Django 3.2.6 on 2021-08-17 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_alter_question_right_choice'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='choice_seq',
            field=models.IntegerField(default=1),
        ),
    ]
