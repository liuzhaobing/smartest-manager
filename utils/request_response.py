# -*- coding:utf-8 -*-
import datetime
import logging
import threading
import time
from typing import Any

from django.utils.deprecation import MiddlewareMixin
from rest_framework.response import Response
# from motor.motor_asyncio import AsyncIOMotorClient as MongoClient
from pymongo import MongoClient
from smartest.settings import DATABASES

logger = logging.getLogger("django")


def resp(
        response_data: Any = None,
        success: bool = True,
        msg: str = "",
        code: int = 200,
        status=None,
        template_name=None,
        headers=None,
        exception=False,
        content_type=None,
        **kwargs
) -> Response:
    _resp = dict(
        code=code,
        success=success,
        msg=msg,
        data=response_data,
    )
    if kwargs:
        _resp.update(kwargs)

    return Response(
        data=_resp,
        status=status,
        template_name=template_name,
        headers=headers,
        exception=exception,
        content_type=content_type
    )


class RequestResponseLogMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
        super().__init__(get_response)
        mongo = DATABASES.get("mongo_smartest")["CLIENT"]
        uri = f"mongodb://{mongo['username']}:{mongo['password']}@{mongo['host']}:{mongo['port']}/{mongo['authSource']}"
        self.client = MongoClient(uri)
        self.db = self.client["smartest"]
        self.collection = self.db["logs"]

    def process_request(self, request):
        request.start_time = time.perf_counter()
        return self.get_response(request)

    def process_response(self, request, response):
        if request.path.startswith("/static/"):
            return response
        try:
            request_log = dict(
                request_ip=request.META.get("REMOTE_ADDR", ""),
                request_method=request.method,
                request_path=request.path,
                request_body=request.body.decode("utf-8"),
                response_status=response.status_code,
                response_body=response.content.decode("utf-8"),
                response_time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                cost=1000 * (time.perf_counter() - request.start_time),
            )
            threading.Thread(target=self.insert_one, args=(request_log,)).start()

        except Exception as e:
            logger.error(f"save request log failed: {e}")
        return response

    def insert_one(self, data):
        logger.info(data)
        self.collection.insert_one(data)
