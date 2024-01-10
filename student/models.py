from django.db import models

# Create your models here.



# class details(models.Model):
#     stu_name = models.CharField(max_length = 200)
#     stu_class = models.CharField(max_length = 200)
#     stu_rollno = models.CharField(max_length = 200)
#     stu_activity = models.CharField(max_length = 200)
#     date = models.DateField()


class details1(models.Model):
    stu_name = models.CharField(max_length = 200)
    stu_class = models.CharField(max_length = 200)
    stu_rollno = models.CharField(max_length = 200)
    stu_activity = models.CharField(max_length = 200)
    date = models.DateField()

    def __str__(self):
        return self.stu_name

