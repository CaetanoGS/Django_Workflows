from .models import Step, WorkFlow, Comment
from rest_framework import serializers, fields


class StepSerializer(serializers.ModelSerializer):

    class Meta:
        model = Step
        fields = ('wkStep', 'name', 'description')

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('wkID', 'name', 'text')


class WorkFlowSerializer(serializers.ModelSerializer):
    steps = StepSerializer(many=True)

    class Meta:
        model = WorkFlow
        fields = ('id', 'name', 'description', 'steps')

    # Functions to able the creating and updating of data
    # Based on https://www.django-rest-framework.org 

    def create(self, validated_data):
        steps_data = validated_data.pop('steps')
        workflows = WorkFlow.objects.create(**validated_data)
        for step_data in steps_data:
            Step.objects.create(wkStep=workflows, **step_data)
        return workflows

    def update(self, instance, validated_data):
        steps_data = validated_data.pop('steps')
        steps = (instance.steps).all()
        steps = list(steps)
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.save()

        for step_data in steps_data:
            step = steps.pop(0)
            step.name = step_data.get('name', step.name)
            step.description = step_data.get('description', step.description)
            step.save()
        return instance
