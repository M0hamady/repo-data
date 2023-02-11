from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.utils.datetime_safe import datetime
from rest_framework import status, generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from useres.models import User as User_inf
from .models import Meeting
from .serializers import MeetingSerializers, CreateMeetingSerializer


@api_view(['GET','POST'])
@authentication_classes([TokenAuthentication])
def meeting(request):
    if request.method == 'GET':
        if request.user:
            try:
                if User_inf.objects.get(user = request.user).is_manager :
                    meets= Meeting.objects.all()
                    serialize= MeetingSerializers(meets,many=True, context={'request': request})
                    return Response(serialize.data)
            except User_inf.DoesNotExist:return Response({"detail": "Not Valid Call Admin."},status=status.HTTP_400_BAD_REQUEST)
        else:return Response({"detail": "Log in first."},status=status.HTTP_400_BAD_REQUEST)
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

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
def CreayeMeetingView(request):
    if request.user:
        # remember old state
        _mutable = request.data._mutable
        # set to mutable
        request.data._mutable = True
        # сhange the values you want
        print(request.user)
        request.data['created_by'] = request.user.id
        request.data['last_ip'] = request.META['REMOTE_ADDR']
        # set mutable flag back
        request.data._mutable = _mutable
        print(request.data)
        serializer = CreateMeetingSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer.validated_data)
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    return Response({'message':'required login'})


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
def get_exact_meating(request,id):
    if request.method == 'GET':
        meet = Meeting.objects.get(id=id)
        serializer = MeetingSerializers(meet,many=False)
        return Response(serializer.data)

@api_view(["GET", "PUT",'DELETE'])
@authentication_classes([TokenAuthentication])
def meetingeView(request,uuid):
    try:
        item = get_object_or_404(Meeting,created_by=request.user , uuid =uuid)
    except Meeting.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = MeetingSerializers(item,  context={'request': request})
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = MeetingSerializers(item, data=request.data, partial=True,context={'request': request})
        print(1)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    # 
    # elif request.method == "POST":
    #     serializer = MeetingSerializers(item, data=request.data, partial=True,context={'request': request})
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors)
    elif request.method =="DELETE":
        item.delete()
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET",])
@authentication_classes([TokenAuthentication])
def meetingseView(request):
    try:
        item = Meeting.objects.filter(created_by=request.user )
    except item.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = MeetingSerializers(item,many=True,  context={'request': request})
        return Response(serializer.data)

    return Response( status=status.HTTP_400_BAD_REQUEST)