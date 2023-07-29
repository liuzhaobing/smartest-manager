# -*- coding:utf-8 -*-
import copy
import datetime
import os
from pathlib import Path

from rest_framework import status

from apps.common.models import FilesModel
from apps.common.serializers import FilesSerializer
from smartest.settings import MEDIA_ROOT
from utils.request_response import response
from utils.viewset import CustomModelViewSet


class FilesView(CustomModelViewSet):
    queryset = FilesModel.objects.all().order_by("-create_time")
    serializer_class = FilesSerializer
    lookup_field = "id"

    filterset_fields = (
        "id",
        "username",
        "filepath",
        "filename",
    )

    def create(self, request, *args, **kwargs):
        file_obj = request.FILES.get("file")
        if not file_obj:
            return response(success=False, msg="filed file does not exist!",
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        request_data = copy.deepcopy(request.data)
        old_filename = request_data.get("filename", "")
        old_filepath = request_data.get("filepath", "")

        if not old_filename:
            return response(success=False, msg="filed filename does not exist!",
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        request_data["filename"] = datetime.datetime.now().strftime("%Y%m%d%H%M%S") + "_" + old_filename
        request_data["filepath"] = old_filepath.removeprefix("/").removesuffix("/")
        if not request_data.get("username", ""):
            request_data["username"] = request.user.username

        full_path = os.path.join(MEDIA_ROOT, request_data["filepath"], request_data["filename"])
        Path(full_path).parent.mkdir(parents=True, exist_ok=True)
        with open(full_path, "wb+") as f:
            for chunk in file_obj.chunks():
                f.write(chunk)

        serializer = self.get_serializer(data=request_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return response(serializer.data, status=status.HTTP_200_OK, headers=headers)
