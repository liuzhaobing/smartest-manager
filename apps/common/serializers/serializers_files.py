# -*- coding:utf-8 -*-
from rest_framework import serializers

from apps.common.models.models_files import FilesModel


class FilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilesModel
        fields = "__all__"
