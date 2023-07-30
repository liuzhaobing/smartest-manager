# -*- coding:utf-8 -*-
import grpc

from apps.common.proto import task_pb2_grpc

channel = grpc.insecure_channel(target="127.0.0.1:50055")
stub = task_pb2_grpc.TaskServiceStub(channel)
