# -*- coding:utf-8 -*-
from apps.plans.models import PlansModel
from apps.plans.serializers import PlansSerializer
from utils.viewset import CustomModelViewSet


class PlansView(CustomModelViewSet):
    queryset = PlansModel.objects.all().order_by("id")
    serializer_class = PlansSerializer
    lookup_field = "id"

    filterset_fields = (
        "task_name",
        "task_type",
        "task_group",
        "task_data_source_label",
        "is_crontab",
        "crontab_string",
        "task_config",
        "task_data_source"
    )
