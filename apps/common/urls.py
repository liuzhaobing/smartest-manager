# -*- coding:utf-8 -*-
from rest_framework import routers

from apps.common.views.views_files import FilesView
from apps.common.views.views_plans import PlansView
from apps.common.views.views_servers import ServersView
from apps.common.views.views_header import HeaderView

url = routers.SimpleRouter(trailing_slash=False)
url.register(r"files", FilesView, basename="files")
url.register(r"plans", PlansView, basename="plans")
url.register(r"servers", ServersView, basename="servers")
url.register(r"header", HeaderView, basename="header")

urlpatterns = []
urlpatterns += url.urls
