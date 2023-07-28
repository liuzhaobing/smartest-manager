# -*- coding:utf-8 -*-
from rest_framework import routers

from apps.plans.views import *

url = routers.SimpleRouter(trailing_slash=False)
url.register(r"plans", PlansView, basename="plans")

urlpatterns = []
urlpatterns += url.urls
