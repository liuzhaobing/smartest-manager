# -*- coding:utf-8 -*-
from django.views.static import serve
from rest_framework import routers
from django.urls import path, include, re_path

from smartest import settings

urlpatterns = [
    path('common/', include('apps.common.urls')),
    path('report/', include('apps.report.urls')),
    re_path(r'upload/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'download/(?P<path>.*)$', serve, {'document_root': settings.RUNTIME_ROOT}),
]
url = routers.SimpleRouter(trailing_slash=False)
urlpatterns += url.urls
