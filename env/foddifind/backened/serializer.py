from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = contactDetail
        fields = "fullname address city".split()


class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "username email password".split()


class BioDataSerialiser(serializers.ModelSerializer):
    class Meta:
        model = BioData
        fields = "height weight age gender vegetarian activity_level body_goal".split()


class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
