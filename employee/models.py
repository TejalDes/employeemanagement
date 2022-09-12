from django.db import models


class Employee(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    birth_date = models.DateField()
    address = models.CharField(max_length=80)
    phone = models.PositiveIntegerField()
    email = models.EmailField(max_length=50)
    emp_id = models.PositiveSmallIntegerField()  # try working with uid or primary key
