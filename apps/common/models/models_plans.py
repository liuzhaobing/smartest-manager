from django.db import models

from utils.base_model import BaseModel


class PlansModel(BaseModel):
    class Meta:
        db_table = "plans"
        verbose_name = "测试计划列表"
        verbose_name_plural = "测试计划列表"
        app_label = "apps.common.apps.CommonConfig"

    """
    null 是针对数据库而言，如果 null=True, 表示数据库的该字段可以为空，即在Null字段显示为YES
    blank 是针对表单的，如果 blank=True，表示你的表单填写该字段的时候可以不填，但是对数据库来说，没有任何影响
    """
    id = models.AutoField(primary_key=True, verbose_name="计划ID")
    task_name = models.CharField(verbose_name="计划名称", max_length=1024)
    task_type = models.CharField(verbose_name="计划类型", max_length=1024)
    task_group = models.CharField(verbose_name="计划分组", max_length=1024)
    task_config = models.TextField(verbose_name="计划配置")
    task_data_source_label = models.TextField(verbose_name="数据源标签", max_length=1024)
    task_data_source = models.TextField(verbose_name="数据源配置")
    is_crontab = models.CharField(verbose_name="定时任务", max_length=1024)
    crontab_string = models.CharField(verbose_name="定时器", null=True, blank=True, max_length=1024)
