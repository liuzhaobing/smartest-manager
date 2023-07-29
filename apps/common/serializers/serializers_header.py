# -*- coding:utf-8 -*-
from rest_framework import serializers

from apps.common.models.models_header import HeaderModel


class HeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeaderModel
        fields = "__all__"
