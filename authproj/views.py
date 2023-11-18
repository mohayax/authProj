from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.shortcuts import get_object_or_404

@api_view(['POST'])
def signUP(request):
    serializer = serializers.UserSerlizer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(username = request.data['username'])
        user.set_password(request.data['password'])  #for hashing password
        user.save()
        token = Token.objects.create(user = user)
        return Response({"token": token.key, "user": serializer.data})
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def getUsers(request, id = None):
    if id:
        user = User.objects.get(id = id)
        serializer = serializers.UserSerlizer(user)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    
    # users = User.objects.all()
    # serializer = serializers.UserSerlizer(users, many=True)
    # return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)


@api_view(['POST'])
def logIn(request):
    user = get_object_or_404(User, username = request.data['username'])
    if not user.check_password(request.data['password']):
        return Response({"deatail": "Not Found"}, status = status.HTTP_404_NOT_FOUND)
    
    token, created = Token.objects.get_or_create(user = user)
    serializer = serializers.UserSerlizer(instance=user)
    return Response({"token": token.key, "user": serializer.data})

@api_view(['GET'])
def testToken(request):
    pass