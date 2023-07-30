import dataclasses
import logging
from typing import Dict, List

from google.protobuf import json_format
from rest_framework.decorators import action
from rest_framework.response import Response

from utils.request_response import resp
from utils import mongo_smartest_client
from utils.viewset import CustomModelViewSet
from apps.report.models.models_tasks import TasksModel
from apps.report.serializers.serializers_tasks import TasksSerializer
from apps.common.proto import task_pb2
from apps import stub

logger = logging.getLogger("django")


@dataclasses.dataclass
class LogsRequest:
    index: int
    count: int
    database: str
    collection: str
    filter: Dict
    object_id: str = ""
    update: Dict = None
    column: Dict = None
    sort: Dict = None
    aggregate: List = None


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

    @action(methods=["POST"], detail=False, description="查询运行详细日志")
    def get_logs(self, request, *args, **kwargs):
        request_data = dict(request.data)

        try:
            req = LogsRequest(**request_data)
            database = mongo_smartest_client[req.database]
            collection = database[req.collection]
            result = collection.find(filter=req.filter).skip((req.index - 1) * req.count).limit(req.count)
            # 遍历mongo cursor结果把ObjectId转为string
            data = []
            for r in result:
                r["_id"] = str(r["_id"])
                data.append(r)

            return resp(response_data=data)
        except Exception as e:
            return resp(response_data=[], success=False, code=500, status=500, msg=str(e))
