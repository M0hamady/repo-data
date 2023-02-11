from rest_framework.authentication import BasicAuthentication,TokenAuthentication
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from django.utils.datetime_safe import datetime
from rest_framework.authtoken.admin import User
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from meets.models import Meeting
from project.models import Project, Step, Moshtarayet
from project.permisions import IsManagerUser, IsEngUser
from project.serializers import ProjectSerializers, SteptSerializers
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from  django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings

# first gitr all projects by date of creation
#
# @api_view(['GET','PUT'])
@api_view(['GET','POST','PUT'])
@authentication_classes([TokenAuthentication])
# @permission_classes((IsAuthenticated,))
@permission_classes([IsManagerUser])
def project(request):
    if request.method == 'GET':
        # print(request.headers)
        try:
            project = Project.objects.all().order_by('-created_at')
            serialize = ProjectSerializers(project, many= True)
        except: return ({'message':'ther is no data for project'})
        # serialize.data.popitem('test','test res')

        return Response(serialize.data)
    elif request.method == "POST":
        # print(request,55,request)
        list_of_search = [k for k, v in request.data.items()]
        if ('name' in list_of_search):
            name_ = request.data['name']
        if ('address' in list_of_search):
            address_ = request.data['address']
        if ('owner' in list_of_search):
            owner = Token.objects.get(key =str(request.data['owner']).split(' ')[0])
            print(str(request.data['owner']).split(' '),545454)
        print(list_of_search)
        project = Project.objects.create(
            name=name_,
            address=address_,
            owner = User.objects.get(auth_token=owner),
            creator = request.user,
        )
        project.save()
        if 'number' in list_of_search:
            number = request.data['number']
            for i in range(int(number)):
                # print(i)
                step = Step.objects.create(
                    name='un named yet',
                        project = project
                )
                step.save()
            print("done creation for step",id)
        if 'id' in list_of_search:
            id_meet = get_object_or_404(Meeting,id =request.data['id'])
        # meeting = Meeting.objects.get(id=id)
            if id_meet :
                print("create relation")
                id_meet.order.add(project)
                id_meet.save()
                print('saved')
        return Response({'done':True})
# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
# def projectUpdate(request,id):
#     if request.method == "PUT":
#         list_of_search = [k for k, v in request.data.items()]
#         if 'chang_civil' in list_of_search:
#             civil_eng = request.data['chang_civil']
#         if 'chang_designer' in list_of_search:
#             chang_designer = request.data['chang_designer']
#

@api_view(['GET','POST'])
@permission_classes((AllowAny,))
def step(request):
    if request.method == 'GET':
        step = Step.objects.all()
        serialize = SteptSerializers(step,many=True)
        return Response(serialize.data)

@api_view(['GET','POST'])
@permission_classes((AllowAny,))
def exac_step(request,id):
    if request.method == 'GET':
        step = Step.objects.filter(project =id)
        serialize = SteptSerializers(step,many=True)
        # print(step[0].moshtrayat)
        return Response(serialize.data)
    if request.method == 'POST':
        list_of_search = [k for k, v in request.data.items()]
        step = Step.objects.create(
             project=id
        )
        if ('name' in list_of_search):
            step.name = request.data['name']
        step.save()
@api_view(['GET','POST','PUT'])
@permission_classes((AllowAny,))
def exac_proj(request,id):
    if request.method == 'GET':
        try:
            proj = Project.objects.get(id =id)
        # print(proj.steps())
            serialize = ProjectSerializers(proj,many=False)
        except:
            return ({'message': 'ther is no data for that project'})
        return Response(serialize.data)
    elif request.method == 'POST':
        pass
    elif request.method == "PUT":
        ''' her we gwt each update id for user'''
        print('going to update')
        list_of_search = [k for k, v in request.data.items()]
        proj = Project.objects.get(id=id)
        if 'chang_civil' in list_of_search:
            civil_eng = request.data['chang_civil']
            try:
                proj.civil_eng =User.objects.get(id=civil_eng)
            except:return Response({'message':"we can nit find this user contact admin"})
        if 'chang_designer' in list_of_search:
            chang_designer = request.data['chang_designer']
            try:
                proj.designer_eng =User.objects.get(id=chang_designer)
            except: return Response({'message':"we can nit find this user contact admin "})
        proj.save()
        serialize = ProjectSerializers(proj, many=False)
        return Response(serialize.data)
@api_view(['GET','POST','PUT'])
@permission_classes((AllowAny,))
def moshtrayat(request,id):
    if request.method == 'GET':
        proj = Moshtarayet.objects.all()
        serialize = ProjectSerializers(proj,many=False)
        return Response(serialize.data)
    if request.method == 'POST':
        # id of ites step
        step = Step.objects.get(id =id)
        name = request.data['name']
        cost = int(request.data['cost'])

        moshtra = Moshtarayet.objects.create(
            name=name,
            cost=cost,
            step = step,
        )
        moshtra.save()

        return Response({'projectid':step.project.id})
    if request.method == 'PUT':
        list_of_search = [k for k, v in request.data.items()]
        if 'name' in list_of_search:
            name = request.data['name']
        if 'cost' in list_of_search:
            cost = int(request.data['cost'])

        moshtra = get_object_or_404(Moshtarayet, id = id)
        moshtra.name =name
        moshtra.cost = cost
        moshtra.save()
        print(moshtra.step.project.id,55555)

        return Response({'projectid':moshtra.step.project.id})

@api_view(['POST'])
@permission_classes((AllowAny,))
def add_step(request,id):
    if request.method == 'POST':
        list_of_search = [k for k, v in request.data.items()]
        # id of ites proj
        proj = Project.objects.get(id = id)
        if 'name' in list_of_search:
            name = request.data['name']
        if 'start_at' in list_of_search:
            start = request.data['start_at']
        if 'finished_at' in list_of_search:
            end = request.data['finished_at']
        step = Step.objects.create(
            name=name,
            start_at = start,
            finished_at= end,
            project = proj,
        )
        step.save()

        return Response({'projectid':step.project.id})


@csrf_exempt
@api_view(['GET','PUT'])
@permission_classes((AllowAny,))
def aStep(request,id):
    if request.method == 'GET':
        step = Step.objects.get(id=id)
        print(step)
        serialize = SteptSerializers(step, many=False)
        return Response(serialize.data)
    if request.method == 'PUT':
        print('going to update')
        step = Step.objects.get(id=id)
        print(step,5)
        list_of_search = [k for k, v in request.data.items()]
        if ('name' in list_of_search):
            name = request.data['name']
            step.name = name
        if ('start_at' in list_of_search):
            start = request.data['start_at']
            step.start_at = start
        if ('finished_at' in list_of_search):
            end = request.data['finished_at']
            step.finished_at =end
        if ('is_finished' in list_of_search):
            is_finished = request.data['is_finished']
            print('changed')
            if is_finished == 'false':
                is_finished = False
            else: is_finished = True
            step.is_finished =is_finished
        step.save()
    return Response({'done':True,'projectid':step.project.id})

@receiver(post_save,sender =settings.AUTH_USER_MODEL)
def TokenCreate(sender,instance, created, **kwargs):
    if created:
        Token.objects.create(user =instance)

@api_view(['GET','PUT'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def project_users(request,id):
    if request.method == 'GET':
        print(id,44444444)
        projects = Project.objects.filter(owner=User.objects.get(id=id))
        serialize = ProjectSerializers(projects, many=True)
        return Response(serialize.data)
    if request.method == 'PUT':
      pass
    # return Response({'done':True,'projectid':step.project.id})
