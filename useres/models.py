import uuid

from django.conf import settings
from django.db import models
# from django.contrib.auth.models import AbstractUser

# Create your models here.
from rest_framework.authtoken.admin import User as User_inf

from project.models import Project, Step
from project.serializers import ProjectSerializers, SteptSerializers
# from useres.serializers import User_Serualizer

'''
visitor ip location info meeting phone 
client project name  meeting phone 
eng [projects] location ip phone [meeting] 
designer  [projects] location ip phone [meeting] 
manager *[projects] location ip phone *[meeting]  

'''

class User(models.Model):
    # name = models.CharField(max_length=120, null=True)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, related_name='auth_user',
        on_delete=models.CASCADE, verbose_name=("User")
    )
    password = models.CharField(max_length=654 ,default='12345' )
    uuid = models.CharField(unique=True, default=uuid.uuid1,max_length=255)
    ip =  models.CharField(max_length=120, null=True)
    phone =  models.CharField(max_length=120, null=True)
    location =  models.CharField(max_length=120, null=True)
    pic = models.ImageField(upload_to="useres/%y", null=True)
    # is_visitor = models.BooleanField(default=True)
    is_client = models.BooleanField(default=True)
    is_eng = models.BooleanField(default=False)
    is_designer = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
    is_accountant = models.BooleanField(default=False)



    def __str__(self):
        return self.user.username

    def inf(self):
        data =User_inf.objects.filter(id=self.user.id)
        return data.values()
    def name_inf(self):
        """ name information"""
        data =User_inf.objects.get(id=self.user.id)
        return data.username
    def projec(self):
        data =Project.objects.filter(owner=self.user)
        serialize =ProjectSerializers(data,many=True)
        return serialize.data
    def projec_step(self):
        try:
            # print(Project.objects.filter(owner=self.user)[::-1][0])
            data =Step.objects.filter(project__name=Project.objects.filter(owner=self.user)[::-1][0])
            serialize =SteptSerializers(data ,many =True)
            return serialize.data
        except: return []
    def numper_of_finished_projects(self):
        res = 0
        try:
            project = Project.objects.filter(owner=self.user )
            serialize =ProjectSerializers(project, many=True)
            if serialize.data :
                for i in serialize.data:
                    print(1, 'from i in for',i['finshed_percent'])
                    if int(i['finshed_percent']) > 99:
                            print(1,'from i in for')
                            res = res + 1
                return res
        except: return res


    def project_percent(self):

        try:
            data = Project.objects.filter(owner=self.user).reverse()[0]
            lenght = data.steps_count
            print(lenght, type(lenght))
            finshed_count = data.steps_countFinshed
            print(finshed_count, type(finshed_count))
            percent = finshed_count//lenght
            return  percent
        except:return 0