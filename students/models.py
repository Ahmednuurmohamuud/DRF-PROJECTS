from django.db import models

# Create your models here.


class student(models.Model):
    student_Id = models.CharField(max_length=10)
    name = models.CharField(max_length=10)
    age = models.IntegerField()
    def __str__(self):
        return self.name