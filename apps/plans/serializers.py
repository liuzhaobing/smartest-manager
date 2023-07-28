# -*- coding:utf-8 -*-
from rest_framework import serializers

from apps.plans.models import PlansModel


class PlansSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlansModel
        fields = "__all__"
