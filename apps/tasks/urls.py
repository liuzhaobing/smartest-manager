# -*- coding:utf-8 -*-
from rest_framework import routers

from apps.tasks.views import TasksView

url = routers.SimpleRouter(trailing_slash=False)
url.register(r"tasks", TasksView, basename="tasks")

urlpatterns = []
urlpatterns += url.urls
