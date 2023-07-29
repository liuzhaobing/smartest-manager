import logging

from apps.report.models.models_tasks import TasksModel
from apps.report.serializers.serializers_tasks import TasksSerializer
from utils.viewset import CustomModelViewSet

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
