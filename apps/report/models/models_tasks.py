# -*- coding:utf-8 -*-
from djongo import models


class TasksModel(models.Model):
    class Meta:
        db_table = "tasks"
        verbose_name = "测试执行历史"
        verbose_name_plural = "测试执行历史"
        app_label = "apps.report.apps.ReportConfig"

    _id = models.ObjectIdField(editable=False, primary_key=True)
    job_instance_id = models.CharField(verbose_name="任务ID", max_length=1024)
    task_name = models.CharField(verbose_name="任务名称", max_length=1024)
    task_type = models.CharField(verbose_name="任务类型", max_length=1024)
    status = models.IntegerField(verbose_name="任务状态")
    progress_percent = models.IntegerField(verbose_name="进度百分比")
    progress = models.CharField(verbose_name="任务进度", max_length=1024)
    accuracy = models.FloatField(verbose_name="准确率", default=0)
    message = models.CharField(verbose_name="测试报告", max_length=1024)
    result_file = models.CharField(verbose_name="测试日志", max_length=1024)
    start_time = models.CharField(verbose_name="开始时间", max_length=1024)
    end_time = models.CharField(verbose_name="结束时间", max_length=1024)
