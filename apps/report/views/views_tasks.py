import logging

from google.protobuf import json_format
from rest_framework.decorators import action
from rest_framework.response import Response

from utils.viewset import CustomModelViewSet
from apps.report.models.models_tasks import TasksModel
from apps.report.serializers.serializers_tasks import TasksSerializer
from apps.common.proto import task_pb2
from apps import stub

logger = logging.getLogger("django")


class TasksView(CustomModelViewSet):
    queryset = TasksModel.objects.all().order_by("-start_time")
    serializer_class = TasksSerializer
    lookup_field = "job_instance_id"
    filterset_fields = (
        "job_instance_id",
        "task_name",
        "task_type",
        "status",
        "start_time",
        "end_time"
    )

    @action(methods=["PUT"], detail=True, description="终止运行中的任务")
    def stop(self, request, job_instance_id=None, *args, **kwargs):
        message = task_pb2.StopRequest(
            job_instance_id=job_instance_id
        )
        result = stub.Stop(message)
        return Response(data=json_format.MessageToDict(result))

    @action(methods=["GET"], detail=False, description="查询运行中的任务")
    def running(self, request, *args, **kwargs):
        task = request.GET.dict()
        message = task_pb2.TaskInfo(
            job_instance_id=task.get("job_instance_id", ""),
            task_name=task.get("task_name", ""),
            task_type=task.get("task_type", ""),
            status=task.get("status", 0),
            progress_percent=task.get("progress_percent", 0),
            progress=task.get("progress", ""),
            accuracy=task.get("accuracy", 0.0),
            message=task.get("message", ""),
            result_file=task.get("result_file", ""),
            start_time=task.get("start_time", ""),
            end_time=task.get("end_time", ""),
            username=task.get("username", ""),
        )
        result = stub.List(message)
        return Response(data=json_format.MessageToDict(result))
