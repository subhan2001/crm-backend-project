from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


@api_view(['POST'])
def register_user(request):

    username = request.data.get('username')
    password = request.data.get('password')

    if User.objects.filter(username=username).exists():

        return Response(
            {"error": "Username already exists"},
            status=status.HTTP_400_BAD_REQUEST
        )

    user = User.objects.create(
        username=username,
        password=make_password(password)
    )

    return Response(
        {"message": "User registered successfully"},
        status=status.HTTP_201_CREATED
    )