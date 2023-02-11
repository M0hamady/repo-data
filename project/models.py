from django.db import models
# Create your models here.
from rest_framework.authtoken.admin import User
# from  useres.models import User as User_inf

'''
project is finished -created at - cost - finished at - 
owner - eng - designer - mohaseb - imges order
address 
connected to steps

'''
class Project(models.Model):
    name = models.CharField(max_length=150,null=True)
    created_at = models.DateTimeField(auto_now=True)
    is_finished = models.BooleanField(default=False)
    finished_at = models.DateTimeField(auto_now=False,null=True)
    address = models.CharField(max_length=300, null=True)
    cost = models.FloatField(null=True)
    worker =models.ManyToManyField('useres.User')
    owner = models.ForeignKey(User,on_delete=models.DO_NOTHING, related_name='owner',default=1)
    creator = models.ForeignKey(User,on_delete=models.DO_NOTHING, related_name='creator')
    manger = models.ForeignKey(User,on_delete=models.DO_NOTHING, blank=True,
        null=True, related_name='manager')
    civil_eng = models.ForeignKey(User,on_delete=models.DO_NOTHING, blank=True,
        null=True, related_name='civil_eng')
    designer_eng = models.ForeignKey(User,on_delete=models.DO_NOTHING, blank=True,
        null=True, related_name='designer')

    # owner =/

    # meeting
    # owner = models.Many()
    # civil_eng = models.ForeignKey()
    # designer = models.ForeignKey()
    # manager = models.ForeignKey()
    def __str__(self):
        return self.name

    @property
    def steps_count(self):
        return Step.objects.filter(project__id =self.id).count()
    def steps_countFinshed(self):
        return Step.objects.filter(project__id =self.id , is_finished =True).count()
    def steps(self):
        obj = Step.objects.filter(project__id =self.id).values()
        return obj
    def meetings(self):
        from meets.models import Meeting
        obj = Meeting.objects.filter(order__id =self.id).values()
        return obj
    def moshtryat(self):
        obj = Step.objects.filter(project__id =self.id).values()
        res = []
        for i in obj:
            # print(i['id'])
            moshtrayat = Moshtarayet.objects.filter(step__id=i['id']).values()
            if moshtrayat :
                for i in moshtrayat:
                    res.append(i)
        return res
    def costes(self):
        obj = Step.objects.filter(project__id =self.id).values()
        res = 0
        for i in obj:
            # print(i['id'])

            moshtrayat = Moshtarayet.objects.filter(step__id=i['id']).values()
            if moshtrayat :
                for i in moshtrayat:
                    res = res +i['cost']
        return res
    @property
    def finshed_oercent(self):
        obj = Step.objects.filter(project__id=self.id).count()
        objFinshed = Step.objects.filter(project__id=self.id,is_finished=True).count()
        percent = objFinshed / obj *100
        return percent
    def moshtryat_detail(self):
        obj = Step.objects.filter(project__id =self.id).values()
        res = []
        for i in obj:
            # print(i['id'])
            moshtrayat = Moshtarayet.objects.filter(step__id=i['id']).values()
            if moshtrayat :
                res.append({'moshtrayat':moshtrayat,'step_name':i['name']})
        return res
    def owner_name(self):
        return self.owner.username

class Step(models.Model):
    name = models.CharField( null= True,max_length=150)
    cost = models.FloatField(null=True)
    show_to_owner = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    start_at = models.DateField(auto_now=False,null=True)
    finished_at = models.DateTimeField(auto_now=False,null=True)
    is_finished =models.BooleanField(default=False)
    project =models.ForeignKey(Project,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    def moshtrayat_count(self):
        return Moshtarayet.objects.filter(step__id =self.id).count()

    def moshtrayat(self):
        data = Moshtarayet.objects.filter(step__id=self.id).values()
        return data
    @property
    def all_cost(self):
        data = Moshtarayet.objects.filter(step__id=self.id).values()
        costs = 0
        for i in data:
            costs = costs + int(i['cost'])
            # print(i['cost'])
        return costs



class Images_step(models.Model):
    step = models.ForeignKey(Step,on_delete=models.CASCADE)
    uuid = models.CharField(max_length=120, null=True)
    # img= models.ImageField(null=True,upload_to="steps/images")
class Moshtarayet(models.Model):
    name = models.CharField( null= True,max_length=150)
    cost = models.FloatField(null=True)
    created_at = models.DateTimeField(auto_now=True)
    step = models.ForeignKey(Step,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
