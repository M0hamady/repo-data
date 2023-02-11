from rest_framework import serializers

from .models import Websiteindex, Montagat


class Website_Serualizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Websiteindex
        fields = "__all__"
class Montagat_Serualizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Montagat
        fields = "__all__"