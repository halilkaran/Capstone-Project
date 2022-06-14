from django.shortcuts import render
from rest_framework.generics import CreateAPIView, UpdateAPIView
from django.contrib.auth.models import User

from users.permissions import IsOwnerOrReadOnly
from .serializers import ProfileSerializer, RegisterSerializer
from rest_framework.response import Response
from .models import Profile

class RegisterAPIs(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {
                "messega" : "User created successfully."
            }
        )

class ProfileAPIs(UpdateAPIView):
    permission_classes=[IsOwnerOrReadOnly]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    lookup_field="id"