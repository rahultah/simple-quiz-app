# Generated by Django 3.0.4 on 2020-05-10 17:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0002_auto_20200510_2230'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='questions',
            options={},
        ),
        migrations.RemoveField(
            model_name='questions',
            name='catagory',
        ),
    ]
