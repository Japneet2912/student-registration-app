# Generated by Django 3.2.23 on 2024-01-09 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='details1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stu_name', models.CharField(max_length=200)),
                ('stu_class', models.CharField(max_length=200)),
                ('stu_rollno', models.CharField(max_length=200)),
                ('stu_activity', models.CharField(max_length=200)),
                ('date', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='details',
        ),
    ]
