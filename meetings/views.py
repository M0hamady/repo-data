from django.shortcuts import render

# Create your views here.
from django.utils.datetime_safe import datetime
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from meetings.models import Meeting
from meetings.serializers import MeetingSerializers


@api_view(['GET','POST'])
@permission_classes((AllowAny,))
def meeting(request):
    if request.method == 'GET':
        list_of_search = [k for k, v in request.data.items()]
        print(list_of_search)
        if 'today' and 'is_accepted' and 'is_succeded' in list_of_search:
            day = datetime.today()
            date_today = str(day.year) + '-' + str(day.month) + '-' + str(day.day)
            users = Meeting.objects.filter(meet_at=date_today,is_accepted=request.data['is_accepted'],is_succeded=request.data['is_succeded'])
        elif 'today' and 'is_accepted' in list_of_search:
            day = datetime.today()
            date_today = str(day.year) + '-' + str(day.month) + '-' + str(day.day)
            users = Meeting.objects.filter(meet_at=date_today,is_accepted=request.data['is_accepted'])
        elif 'today' and 'is_success' in list_of_search:
            day = datetime.today()
            date_today = str(day.year) + '-' + str(day.month) + '-' + str(day.day)
            users = Meeting.objects.filter(meet_at=date_today, is_success=request.data['is_success'])
        elif 'is_accepted' in list_of_search:
            users = Meeting.objects.filter(is_accepted=request.data['is_accepted'])
        elif 'last_ip' in list_of_search:
            # users = Meeting.objects.filter(last_ip=True)
            pass
        elif 'today' in list_of_search:
            day = datetime.today()
            date_today= str(day.year)+'-'+ str(day.month)+'-' + str(day.day)
            print(date_today, 55)
            users = Meeting.objects.filter(meet_at = date_today)
        elif 'is_success' in list_of_search:
            users = Meeting.objects.filter(is_success=request.data['is_success'])
        else:users =Meeting.objects.all().order_by('-created_at')
        serializer = MeetingSerializers(users,many=True)
        # print(serializer.data)
        return Response(serializer.data)
    elif request.method == "POST":
        list_of_search = [k for k, v in request.data.items()]
        if ('time' in list_of_search):
             time = request.data['time']
        if ('date' in list_of_search):
             date = request.data['date']
        if ('ip' in list_of_search):
            ip = request.data['ip']
        if ('name' in list_of_search):
            name = request.data['name']
        if ('location' in list_of_search):
            location = request.data['location']
        if ('number' in list_of_search):
            number = request.data['number']
        if ('order' in list_of_search):
            proj = request.data['order']
            # it will get id of meeting and then make update to meeting in project


        user= Meeting.objects.create(
            location = location,
            number = number,
            name = name,
            last_ip = ip,
            is_success=False,
            meet_at =date,
            meet_time =time,
        )
        # if user.is_valid():
        print(user)
        user.save()
        # except:return Response({'done':False})
        # users = Meeting.objects.all()
        # serializer = MeetingSerializers(users, many=True)
        return Response({'done':True})
@api_view(['PUT'])
@permission_classes((AllowAny,))
def meeting_Update(request,id):
    if request.method == 'PUT':
        list_of_search = [k for k, v in request.data.items()]
        if 'succeded' in list_of_search :
            meet = Meeting.objects.get(id=id)
            if meet.is_success == True and request.data['succeded'] == 'False':
                print('false success')
                meet.is_success ="False"
                meet.save()
            elif meet.is_success == False and request.data['succeded']  :
                print('true success')
                meet.is_success =True
                meet.save()
            print(meet,'succc')
            return Response({'done':True})
        elif 'is_accepted' in list_of_search :
            meet = Meeting.objects.get(id=id)
            print(request.data['is_accepted'], 5555555, meet.is_accepted)
            if meet.is_accepted == True and request.data['is_accepted'] == 'False':
                print('false accepted')
                meet.is_accepted =False
                meet.save()
            elif meet.is_accepted == False and request.data['is_accepted'] =='True':
                print('true is_accepted')
                meet.is_accepted =True
                meet.save()
            print(meet,'acc')
            return Response({'done':True})
        else:return Response({'done':False})


@api_view(['GET'])
@permission_classes((AllowAny,))
def get_exact_meating(request,id):
    if request.method == 'GET':
        meet = Meeting.objects.get(id=id)
        serializer = MeetingSerializers(meet,many=False)
        return Response(serializer.data)

