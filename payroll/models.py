from tkinter import CASCADE
from django.db import models
from employee import *
from employee.models import *


class PayRoll(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date_of_joining = models.DateField()
    salary = models.FloatField()
