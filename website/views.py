from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from website.models import Websiteindex, Montagat
from website.serializers import Website_Serualizer, Montagat_Serualizer


class Website_index(viewsets.ModelViewSet):
    queryset = Websiteindex.objects.all()
    serializer_class =Website_Serualizer

class MontagatView(viewsets.ModelViewSet):
    queryset = Montagat.objects.all()
    serializer_class =Montagat_Serualizer
