from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User, Group
from rest_framework.permissions import AllowAny
from django.contrib.auth.hashers import make_password
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class Register(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response({'error' : 'Username and password are required'}, status=status.HTTP_400_BAD_REQUEST)
        
        if User.objects.filter(username=username).exists():
            return Response({'error' : 'Username already exists'}, status=400)
        
        user = User.objects.create(
            username=username,
            password=make_password(password),
        )

        group = Group.objects.get(name='Viewer')
        user.groups.add(group)

        return Response({'message' : 'User created as Viewer'}, status=201)


class MeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({
            "username" : request.user.username,
            "groups" : list(request.user.groups.value_list('name', flat=True))
        })