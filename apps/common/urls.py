# -*- coding:utf-8 -*-
from rest_framework import routers

from apps.common.views.views_files import FilesView
from apps.common.views.views_plans import PlansView

url = routers.SimpleRouter(trailing_slash=False)
url.register(r"files", FilesView, basename="files")
url.register(r"plans", PlansView, basename="plans")

urlpatterns = []
urlpatterns += url.urls
