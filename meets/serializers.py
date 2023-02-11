from datetime import date

from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Meeting


class MeetingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Meeting
        fields = "__all__"

class CreateMeetingSerializer(serializers.ModelSerializer):
    print(1)
    meet_at = serializers.DateField(required=True,help_text = "Enter only 10 characters", )
    bartment_space = serializers.CharField(required=True,help_text = "Enter only 10 characters")
    created_by =   serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='id')
    location = serializers.CharField(required=True,help_text = "Enter only 10 characters")
    order = serializers.ListSerializer(child=serializers.DateField(),required=False,help_text = "Enter only 10 characters")
    class Meta:
        model = Meeting
        fields = "__all__"

    def validate(self, data):
        """
        Check that start is before finish.
        """
        today = date.today()
        if data['meet_at'] <= today:
            print(1)
            raise serializers.ValidationError("how can we make meeting in past")
        return data
    # def create(self, validated_data):
    #     print(55)
    #     validated_data['created_by'] = serializers.data['created_by']
    #     return Meeting.objects.create(**validated_data)
