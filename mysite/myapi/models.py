from django.db import models

# Create your models here.
class Employee(models.Model):

    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female')
    ]

    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128, blank=True)
    email_id = models.CharField(max_length=256)
    phone_num = models.CharField(max_length=16)
    employee_gender = models.CharField(choices=GENDER_CHOICES, max_length=1)
    employee_address = models.TextField()
    employee_job = models.ManyToManyField('AvailableJobs', blank=1)
    date_f_birth = models.DateField()


class AvailableJobs(models.Model):

    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name