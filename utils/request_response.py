# -*- coding:utf-8 -*-
from typing import Any
from rest_framework.response import Response as _Response


def response(
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
) -> _Response:
    resp = dict(
        code=code,
        success=success,
        msg=msg,
        data=response_data,
    )
    if kwargs:
        resp.update(kwargs)

    return _Response(
        data=resp,
        status=status,
        template_name=template_name,
        headers=headers,
        exception=exception,
        content_type=content_type
    )
