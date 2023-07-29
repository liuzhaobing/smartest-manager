# -*- coding:utf-8 -*-
from rest_framework import serializers

from apps.common.models.models_plans import PlansModel


class PlansSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlansModel
        fields = "__all__"
