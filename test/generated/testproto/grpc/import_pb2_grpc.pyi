"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import google.protobuf.empty_pb2
import grpc
import testproto.test_pb2

class SimpleServiceStub:
    """SimpleService"""
    def __init__(self, channel: grpc.Channel) -> None: ...
    UnaryUnary: grpc.UnaryUnaryMultiCallable[
        google.protobuf.empty_pb2.Empty,
        testproto.test_pb2.Simple1]
    """UnaryUnary"""

    UnaryStream: grpc.UnaryUnaryMultiCallable[
        testproto.test_pb2.Simple1,
        google.protobuf.empty_pb2.Empty]
    """UnaryStream"""

    NoComment: grpc.UnaryUnaryMultiCallable[
        testproto.test_pb2.Simple1,
        google.protobuf.empty_pb2.Empty]


class SimpleServiceServicer(metaclass=abc.ABCMeta):
    """SimpleService"""
    @abc.abstractmethod
    def UnaryUnary(self,
        request: google.protobuf.empty_pb2.Empty,
        context: grpc.ServicerContext,
    ) -> testproto.test_pb2.Simple1:
        """UnaryUnary"""
        ...

    @abc.abstractmethod
    def UnaryStream(self,
        request: testproto.test_pb2.Simple1,
        context: grpc.ServicerContext,
    ) -> google.protobuf.empty_pb2.Empty:
        """UnaryStream"""
        ...

    @abc.abstractmethod
    def NoComment(self,
        request: testproto.test_pb2.Simple1,
        context: grpc.ServicerContext,
    ) -> google.protobuf.empty_pb2.Empty: ...


def add_SimpleServiceServicer_to_server(servicer: SimpleServiceServicer, server: grpc.Server) -> None: ...
