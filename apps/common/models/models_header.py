from django.db import models

from utils.base_model import BaseModel


class HeaderModel(BaseModel):
    class Meta:
        db_table = "header"
        verbose_name = "表头管理"
        verbose_name_plural = "表头管理"
        app_label = "apps.common.apps.CommonConfig"

    id = models.AutoField(primary_key=True, verbose_name="ID")
    data = models.TextField(verbose_name="详细数据")
    headers = models.TextField(verbose_name="表头结构")
    types = models.CharField(verbose_name="类型", max_length=1024)
