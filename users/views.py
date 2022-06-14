from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from django.contrib.auth.models import User
from .serializers import RegisterSerializer
from rest_framework.response import Response

class RegisterAPIs(CreateAPIView):
    queryset= User.objects.all()
    serializer_class = RegisterSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        print(serializer)        
        return Response(
            {"message" : "User created successfully"}
        )