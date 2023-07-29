from django.db import models

from utils.base_model import BaseModel


class FilesModel(BaseModel):
    class Meta:
        db_table = "files"
        verbose_name = "上传文件列表"
        verbose_name_plural = "上传文件列表"
        app_label = "apps.common.apps.CommonConfig"

    id = models.AutoField(primary_key=True, verbose_name="文件ID")
    username = models.CharField(verbose_name="用户名", max_length=1024)
    filepath = models.CharField(verbose_name="文件地址", max_length=1024)
    filename = models.CharField(verbose_name="文件名", max_length=1024)
