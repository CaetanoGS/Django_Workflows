from django.shortcuts import render
from rest_framework import viewsets
from .models import WorkFlow
from .serializers import WorkFlowSerializers

class WorkFlowView(viewsets.ModelViewSet):
    queryset = WorkFlow.objects.all()
    serializer_class = WorkFlowSerializers


