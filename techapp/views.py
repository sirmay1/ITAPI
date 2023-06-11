from django.shortcuts import render
from rest_framework import viewsets
from .models import Tech
from .serializers import TechSerializer


class TechView(viewsets.ModelViewSet):
    queryset = Tech.objects.all()
    serializer_class = TechSerializer
