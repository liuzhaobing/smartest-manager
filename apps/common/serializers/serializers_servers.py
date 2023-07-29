# -*- coding:utf-8 -*-
from rest_framework import serializers

from apps.common.models.models_servers import ServersModel


class ServersSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServersModel
        fields = "__all__"
