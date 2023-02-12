from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator

from  useres.models import  User as User_info
from rest_framework import serializers


class UserSerializers(serializers.ModelSerializer):
    info = serializers.ListField(source='inf')
    projects = serializers.ListField(source='projec')
    last_project_percent = serializers.IntegerField(source='project_percent')
    projec_steps = serializers.ListField(source='projec_step')
    numper_of_finished_project = serializers.IntegerField(source='numper_of_finished_projects')
    class Meta:
        model = User_info
        fields = "__all__"

class UserSerializersMin(serializers.ModelSerializer):
    info = serializers.ListField(source='inf')
    projects = serializers.ListField(source='projec')
    last_project_percent = serializers.IntegerField(source='project_percent')
    numper_of_finished_project = serializers.IntegerField(source='numper_of_finished_projects')

    class Meta:
        model = User_info
        fields = "__all__"
class AllUserSerializersMin(serializers.ModelSerializer):
    name = serializers.CharField(source='name_inf')
    # projects = serializers.ListField(source='projec')
    # last_project_percent = serializers.IntegerField(source='project_percent')
    # numper_of_finished_project = serializers.IntegerField(source='numper_of_finished_projects')

    class Meta:
        model = User_info
        fields = "__all__"

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    phone = serializers.CharField(write_only=True, required=True, )
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = User
        fields = ('username', 'password',
                  # 'password2','first_name', 'last_name',
                  'email', 'phone')
        # extra_kwargs = {
        #     'first_name': {'required': False},
        #     'last_name': {'required': False}
        # }

    # def validate(self, attrs):
    #     if attrs['password'] != attrs['password2']:
    #
    #         raise serializers.ValidationError({"password": "Password fields didn't match."})
    #     return attrs

    # def validate_firstname(self, name_val):
    #     if 'ann' not in name_val.lower():
    #         raise serializers.ValidationError("error message")

        # return name_val
    def validate_phone(self, num_val):
        if  num_val[0] != '0' or 0 and num_val[1] != "1"  and num_val[1] != '1' or '2' or '5' or '0':
            print('not valid phone')
            raise serializers.ValidationError("not valid phone")
        return num_val

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            # first_name=validated_data['first_name'],
            # last_name=validated_data['last_name']
        )

        user.set_password(validated_data['password'])
        user.save()
        user_information = User_info.objects.create(
            user = user,
            phone= validated_data['phone']
        )
        user_information.save()
        return user
class User_Serualizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class ChangeImagwSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_info
        fields = "__all__"