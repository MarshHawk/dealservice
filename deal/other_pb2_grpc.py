# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import other_pb2 as other__pb2


class TaskerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateTask = channel.unary_unary(
                '/todo_app.Tasker/CreateTask',
                request_serializer=other__pb2.Task.SerializeToString,
                response_deserializer=other__pb2.CreateTaskResponse.FromString,
                )
        self.GetAllTasks = channel.unary_unary(
                '/todo_app.Tasker/GetAllTasks',
                request_serializer=other__pb2.GetAllTasksRequest.SerializeToString,
                response_deserializer=other__pb2.TasksList.FromString,
                )
        self.GetTask = channel.unary_unary(
                '/todo_app.Tasker/GetTask',
                request_serializer=other__pb2.Task.SerializeToString,
                response_deserializer=other__pb2.Task.FromString,
                )
        self.UpdateTask = channel.unary_unary(
                '/todo_app.Tasker/UpdateTask',
                request_serializer=other__pb2.Task.SerializeToString,
                response_deserializer=other__pb2.CreateTaskResponse.FromString,
                )
        self.DeleteTask = channel.unary_unary(
                '/todo_app.Tasker/DeleteTask',
                request_serializer=other__pb2.Task.SerializeToString,
                response_deserializer=other__pb2.DeleteTaskResponse.FromString,
                )


class TaskerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateTask(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAllTasks(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTask(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateTask(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteTask(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TaskerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateTask': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateTask,
                    request_deserializer=other__pb2.Task.FromString,
                    response_serializer=other__pb2.CreateTaskResponse.SerializeToString,
            ),
            'GetAllTasks': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAllTasks,
                    request_deserializer=other__pb2.GetAllTasksRequest.FromString,
                    response_serializer=other__pb2.TasksList.SerializeToString,
            ),
            'GetTask': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTask,
                    request_deserializer=other__pb2.Task.FromString,
                    response_serializer=other__pb2.Task.SerializeToString,
            ),
            'UpdateTask': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateTask,
                    request_deserializer=other__pb2.Task.FromString,
                    response_serializer=other__pb2.CreateTaskResponse.SerializeToString,
            ),
            'DeleteTask': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteTask,
                    request_deserializer=other__pb2.Task.FromString,
                    response_serializer=other__pb2.DeleteTaskResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'todo_app.Tasker', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Tasker(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateTask(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/todo_app.Tasker/CreateTask',
            other__pb2.Task.SerializeToString,
            other__pb2.CreateTaskResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAllTasks(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/todo_app.Tasker/GetAllTasks',
            other__pb2.GetAllTasksRequest.SerializeToString,
            other__pb2.TasksList.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTask(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/todo_app.Tasker/GetTask',
            other__pb2.Task.SerializeToString,
            other__pb2.Task.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateTask(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/todo_app.Tasker/UpdateTask',
            other__pb2.Task.SerializeToString,
            other__pb2.CreateTaskResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteTask(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/todo_app.Tasker/DeleteTask',
            other__pb2.Task.SerializeToString,
            other__pb2.DeleteTaskResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)