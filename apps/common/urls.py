# -*- coding:utf-8 -*-
from rest_framework import routers

from apps.common.views import *

url = routers.SimpleRouter(trailing_slash=False)
url.register(r"files", FilesView, basename="files")

urlpatterns = []
urlpatterns += url.urls
