"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class TestMessage(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    FOO_FIELD_NUMBER: builtins.int
    foo: builtins.str
    def __init__(self,
        *,
        foo: builtins.str = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["foo",b"foo"]) -> None: ...
global___TestMessage = TestMessage
