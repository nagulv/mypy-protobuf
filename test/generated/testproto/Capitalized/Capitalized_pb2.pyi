"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class lower(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    A_FIELD_NUMBER: builtins.int
    a: builtins.int
    def __init__(self,
        *,
        a: builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["a",b"a"]) -> None: ...
global___lower = lower

class Upper(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    LOWER_FIELD_NUMBER: builtins.int
    @property
    def Lower(self) -> global___lower: ...
    def __init__(self,
        *,
        Lower: typing.Optional[global___lower] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["Lower",b"Lower"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["Lower",b"Lower"]) -> None: ...
global___Upper = Upper

class lower2(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    UPPER_FIELD_NUMBER: builtins.int
    @property
    def upper(self) -> global___Upper: ...
    def __init__(self,
        *,
        upper: typing.Optional[global___Upper] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["upper",b"upper"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["upper",b"upper"]) -> None: ...
global___lower2 = lower2
