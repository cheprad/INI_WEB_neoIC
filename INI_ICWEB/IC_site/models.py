from django.db import models

# Create your models here.
class Userscore(models.Model) :
    Userscore = models.IntegerField(max_length=5)
    ExamsDone = models.CharField(max_length=255)