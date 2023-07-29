from django.db import models

from utils.base_model import BaseModel


class ServersModel(BaseModel):
    class Meta:
        db_table = "servers"
        verbose_name = "环境管理"
        verbose_name_plural = "环境管理"
        app_label = "apps.common.apps.CommonConfig"

    id = models.AutoField(primary_key=True, verbose_name="ID")
    name = models.CharField(verbose_name="环境名称", max_length=1024)
    address = models.CharField(verbose_name="环境地址", max_length=1024)
    types = models.CharField(verbose_name="类型", max_length=1024)
