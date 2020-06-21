# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class WorkFlow(models.Model):
    name = models.CharField(max_length=500)
    description = models.TextField()

    def __unicode__(self):
        return self.first_name


class Step(models.Model):
    wkStep = models.ForeignKey(WorkFlow, on_delete=models.CASCADE, related_name='steps', null=True, blank=True)
    name = models.CharField(max_length=500)
    description = models.TextField()

class Comment(models.Model):
    wkID = models.ForeignKey(WorkFlow, on_delete = models.CASCADE, related_name='commentaries', null = True, blank = True)
    name = models.CharField(max_length=100)
    text = models.TextField()

    def __str__(self):
        return self.name