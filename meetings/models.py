from django.db import models

from project.models import Project
from useres.models import User

'''
meeting 
time location request_meet attendant   is succeded 

'''
# Create your models here.
class Meeting(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    location =models.CharField(max_length=150,null=True)
    number =models.CharField(max_length=150,null=True)
    name =models.CharField(max_length=150,null=True)
    is_success = models.BooleanField(default=False)
    is_accepted=models.BooleanField(default=False)
    last_ip =models.CharField(max_length=150,null=True)
    meet_at = models.DateField(auto_now=False,null=True)
    meet_time = models.TimeField(auto_now=False,null=True)
    orders = models.ManyToManyField(Project)


    def __str__(self):
        return self.name

# class Meeting_attendant(models.Model):
#     attendaand = models.ManyToManyField(User)
#     meating = models.ManyToManyField(Meeting)
#
#     def __str__(self):
#         return self.attendaand