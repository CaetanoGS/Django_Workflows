from rest_framework import serializers
from .models import WorkFlow

class WorkFlowSerializers(serializers.ModelSerializer):
    class Meta:
        model = WorkFlow
        fields = ('id', 'name', 'description', 'steps')