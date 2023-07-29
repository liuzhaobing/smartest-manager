# -*- coding:utf-8 -*-
from apps.common.models.models_header import HeaderModel
from apps.common.serializers.serializers_header import HeaderSerializer
from utils.viewset import CustomModelViewSet


class HeaderView(CustomModelViewSet):
    queryset = HeaderModel.objects.all().order_by("-create_time")
    serializer_class = HeaderSerializer
    lookup_field = "id"

    filterset_fields = (
        "id",
        "data",
        "headers",
        "types",
    )
