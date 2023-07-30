# -*- coding:utf-8 -*-
from google.protobuf import json_format
from rest_framework.decorators import action
from rest_framework.response import Response

from utils.viewset import CustomModelViewSet
from apps.common.models.models_plans import PlansModel
from apps.common.proto import task_pb2
from apps.common.serializers.serializers_plans import PlansSerializer
from apps import stub


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

    @action(methods=["POST"], detail=True, description="执行测试计划")
    def run(self, request, id=None, *args, **kwargs):
        serializer = self.get_serializer(self.get_object())

        plan = dict(serializer.data)

        message = task_pb2.RunRequest(
            plan=task_pb2.PlanInfo(
                task_name=plan["task_name"],
                task_type=plan["task_type"],
                task_config=plan["task_config"],
                task_data_source=plan["task_data_source"],
                task_data_source_label=plan["task_data_source_label"],
            ),
            task=task_pb2.TaskInfo(
                job_instance_id=request.data.get("job_instance_id", "")
            )
        )

        result = stub.Run(message)

        return Response(data=json_format.MessageToDict(result))
