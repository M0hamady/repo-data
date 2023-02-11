from django.conf import settings
from django.db import models
import uuid
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
    bartment_space =models.CharField(max_length=9,null=True)
    is_success = models.BooleanField(default=False)
    is_accepted=models.BooleanField(default=False)
    uuid = models.CharField(unique=True, default=uuid.uuid4,max_length=255)
    last_ip =models.CharField(max_length=150,null=True)
    meet_at = models.DateField(auto_now=False,null=True)
    meet_time = models.TimeField(auto_now=False,null=True)
    order = models.ManyToManyField(Project)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='meet_user',
        on_delete=models.SET_NULL, verbose_name=("User") , null=True
    )


    def __str__(self):
        return self.created_by.username

# class Meeting_attendant(models.Model):
#     attendaand = models.ManyToManyField(User)
#     meating = models.ManyToManyField(Meeting)
#
#     def __str__(self):
#         return self.attendaand