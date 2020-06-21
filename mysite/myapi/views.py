# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import Step, WorkFlow, Comment
from .serializers import StepSerializer,WorkFlowSerializer, CommentSerializer
from rest_framework import generics, viewsets



class WorkFlowListView(generics.ListCreateAPIView):
    queryset = WorkFlow.objects.all()
    serializer_class = WorkFlowSerializer


class WorkFlowView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WorkFlowSerializer
    queryset = WorkFlow.objects.all()


class StepListView(generics.ListCreateAPIView):
    queryset = Step.objects.all()
    serializer_class = StepSerializer


class StepView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StepSerializer
    queryset = Step.objects.all()

class CommentListView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    

class CommentView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    