# -*- coding:utf-8 -*-
from rest_framework import serializers

from apps.tasks.models import TasksModel


class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = TasksModel
        fields = "__all__"
