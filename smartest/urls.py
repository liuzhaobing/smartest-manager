from django.views.static import serve
from django.contrib import admin
from django.urls import path, include, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from smartest import settings

schema_view = get_schema_view(
    openapi.Info(
        title="SmartVoice自动化测试",
        default_version="v1",
        description="SmartVoice自动化测试",
        terms_of_service="",
        contact=openapi.Contact(email="zhaobing.liu@outlook.com"),
        license=openapi.License(name="SmartVoice Group")
    ),
    public=True
)

urlpatterns = [
    path("admin/", admin.site.urls),

    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('api/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    path('api/v1/', include('apps.urls')),

]
