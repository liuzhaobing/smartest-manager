# -*- coding:utf-8 -*-
import asyncio
import logging
from concurrent import futures

import grpc
from apps.common.proto import task_pb2, task_pb2_grpc


class TaskService(task_pb2_grpc.TaskService):
    async def Run(self, request, context):
        return task_pb2.Response(
            code=200,
            success=True,
            data=task_pb2.TaskInfo(
                job_instance_id="1",
                task_name="2",
                task_type="3",
                status=4,
                progress_percent=5,
                progress="666",
                accuracy=0.7,
                message="8",
                result_file="9",
                start_time="10",
                end_time="11",
                username="12",
            )
        )

    async def Stop(self, request, context):
        return task_pb2.Response(
            code=200,
            success=True,
            data=task_pb2.TaskInfo(
                job_instance_id="1",
                task_name="2",
                task_type="3",
                status=4,
                progress_percent=5,
                progress="666",
                accuracy=0.7,
                message="8",
                result_file="9",
                start_time="10",
                end_time="11",
                username="12",
            )
        )

    async def List(self, request, context):
        return task_pb2.ListResponse(
            code=200,
            success=True,
            data=[
                task_pb2.TaskInfo(
                    job_instance_id="1",
                    task_name="2",
                    task_type="3",
                    status=4,
                    progress_percent=5,
                    progress="666",
                    accuracy=0.7,
                    message="8",
                    result_file="9",
                    start_time="10",
                    end_time="11",
                    username="12",
                )
            ]
        )


async def serve() -> None:
    server = grpc.aio.server(futures.ThreadPoolExecutor(max_workers=40), options=[
        ('grpc.so_reuseport', 0),
        ('grpc.max_send_message_length', 100 * 1024 * 1024),
        ('grpc.max_receive_message_length', 100 * 1024 * 1024),
        ('grpc.enable_retries', 1),
    ])
    task_pb2_grpc.add_TaskServiceServicer_to_server(TaskService(), server)
    listen_addr = '[::]:50055'
    server.add_insecure_port(listen_addr)
    logging.info("Starting server on %s", listen_addr)
    await server.start()
    await server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(serve())
