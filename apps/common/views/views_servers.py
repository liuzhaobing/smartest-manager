# -*- coding:utf-8 -*-
from apps.common.models.models_servers import ServersModel
from apps.common.serializers.serializers_servers import ServersSerializer
from utils.viewset import CustomModelViewSet


class ServersView(CustomModelViewSet):
    queryset = ServersModel.objects.all().order_by("-create_time")
    serializer_class = ServersSerializer
    lookup_field = "id"

    filterset_fields = (
        "id",
        "name",
        "address",
        "types",
    )
