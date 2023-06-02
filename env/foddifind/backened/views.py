from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from .models import *
from rest_framework.response import Response
from .serializer import *
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate, login
from rest_framework import status


# Create your views here.
class ContactView(APIView):
    serializer_class = ContactSerializer

    def get(self, request):
        detail = [
            {
                "fullname": detail.fullname,
                "address": detail.address,
                "city": detail.city,
            }
            for detail in contactDetail.objects.all()
        ]
        return Response(detail)

    def post(self, request):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


class BioDataView(APIView):
    serializer_class = BioDataSerialiser

    def get(self, request):
        detail = [
            {
                "height": detail.height,
                "weight": detail.weight,
                "age": detail.age,
                "gender": detail.gender,
                "vegetarian": detail.vegetarian,
                "activity_level": detail.activity_level,
                "body_goal": detail.body_goal,
            }
            for detail in BioData.objects.all()
        ]
        return Response(detail)

    def post(self, request):
        serializer = BioDataSerialiser(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


class LoginUser(APIView):
    permission_classes = [AllowAny]
    serializer_class = LoginUserSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data["username"]
            password = serializer.validated_data["password"]
            user = authenticate(request, username=username, password=password)

            if user is not None:
                # User credentials are correct
                return Response(serializer.data)
            else:
                # User credentials are invalid
                return Response({"error": "Invalid username or password"}, status=401)

        return Response(serializer.errors, status=400)


class SignUpView(APIView):
    def post(self, request):
        serializer = SignUpSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
