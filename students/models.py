from django.db import models


# Create your models here.
from groups.models import Group


class Student(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    surname = models.CharField(max_length=255, null=False, blank=False)
    avg_mark = models.IntegerField()
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=False)
