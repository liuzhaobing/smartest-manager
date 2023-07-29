# -*- coding:utf-8 -*-
from rest_framework import routers

from apps.common.views.views_files import FilesView
from apps.common.views.views_plans import PlansView
from apps.common.views.views_servers import ServersView

url = routers.SimpleRouter(trailing_slash=False)
url.register(r"files", FilesView, basename="files")
url.register(r"plans", PlansView, basename="plans")
url.register(r"servers", ServersView, basename="servers")

urlpatterns = []
urlpatterns += url.urls
