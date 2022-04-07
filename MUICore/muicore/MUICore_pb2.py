# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: muicore/MUICore.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x15muicore/MUICore.proto\x12\x07muicore" \n\rMUILogMessage\x12\x0f\n\x07\x63ontent\x18\x01 \x01(\t":\n\x0eMUIMessageList\x12(\n\x08messages\x18\x02 \x03(\x0b\x32\x16.muicore.MUILogMessage"\x1c\n\x08MUIState\x12\x10\n\x08state_id\x18\x03 \x01(\x05"\xe4\x01\n\x0cMUIStateList\x12(\n\ractive_states\x18\x04 \x03(\x0b\x32\x11.muicore.MUIState\x12)\n\x0ewaiting_states\x18\x05 \x03(\x0b\x32\x11.muicore.MUIState\x12(\n\rforked_states\x18\x06 \x03(\x0b\x32\x11.muicore.MUIState\x12)\n\x0e\x65rrored_states\x18\x07 \x03(\x0b\x32\x11.muicore.MUIState\x12*\n\x0f\x63omplete_states\x18\x08 \x03(\x0b\x32\x11.muicore.MUIState"!\n\x11ManticoreInstance\x12\x0c\n\x04uuid\x18\t \x01(\t"$\n\x11TerminateResponse\x12\x0f\n\x07success\x18\n \x01(\x08"\xad\x01\n\x0fNativeArguments\x12\x14\n\x0cprogram_path\x18\x0b \x01(\t\x12\x13\n\x0b\x62inary_args\x18\x10 \x03(\t\x12\x0c\n\x04\x65nvp\x18\x11 \x03(\t\x12\x16\n\x0esymbolic_files\x18\x12 \x03(\t\x12\x16\n\x0e\x63oncrete_start\x18\x13 \x01(\t\x12\x12\n\nstdin_size\x18\x14 \x01(\t\x12\x1d\n\x15\x61\x64\x64itional_mcore_args\x18\x15 \x01(\t"\xac\x01\n\x0c\x45VMArguments\x12\x15\n\rcontract_path\x18\x0c \x01(\t\x12\x15\n\rcontract_name\x18\r \x01(\t\x12\x10\n\x08solc_bin\x18\x0e \x01(\t\x12\x10\n\x08tx_limit\x18\x16 \x01(\t\x12\x12\n\ntx_account\x18\x17 \x01(\t\x12\x1c\n\x14\x64\x65tectors_to_exclude\x18\x18 \x03(\t\x12\x18\n\x10\x61\x64\x64itional_flags\x18\x19 \x01(\t"\x81\x01\n\x0e\x41\x64\x64ressRequest\x12\x0f\n\x07\x61\x64\x64ress\x18\x1a \x01(\x04\x12\x30\n\x04type\x18\x1b \x01(\x0e\x32".muicore.AddressRequest.TargetType",\n\nTargetType\x12\x08\n\x04\x46IND\x10\x00\x12\t\n\x05\x41VOID\x10\x01\x12\t\n\x05\x43LEAR\x10\x02"!\n\x0eTargetResponse\x12\x0f\n\x07success\x18\x1c \x01(\x08",\n\x16ManticoreRunningStatus\x12\x12\n\nis_running\x18\x0f \x01(\x08\x32\x8d\x04\n\x0bManticoreUI\x12\x45\n\x0bStartNative\x12\x18.muicore.NativeArguments\x1a\x1a.muicore.ManticoreInstance"\x00\x12?\n\x08StartEVM\x12\x15.muicore.EVMArguments\x1a\x1a.muicore.ManticoreInstance"\x00\x12\x45\n\tTerminate\x12\x1a.muicore.ManticoreInstance\x1a\x1a.muicore.TerminateResponse"\x00\x12\x43\n\x0cGetStateList\x12\x1a.muicore.ManticoreInstance\x1a\x15.muicore.MUIStateList"\x00\x12G\n\x0eGetMessageList\x12\x1a.muicore.ManticoreInstance\x1a\x17.muicore.MUIMessageList"\x00\x12V\n\x15\x43heckManticoreRunning\x12\x1a.muicore.ManticoreInstance\x1a\x1f.muicore.ManticoreRunningStatus"\x00\x12I\n\x13TargetAddressNative\x12\x17.muicore.AddressRequest\x1a\x17.muicore.TargetResponse"\x00\x62\x06proto3'
)


_MUILOGMESSAGE = DESCRIPTOR.message_types_by_name["MUILogMessage"]
_MUIMESSAGELIST = DESCRIPTOR.message_types_by_name["MUIMessageList"]
_MUISTATE = DESCRIPTOR.message_types_by_name["MUIState"]
_MUISTATELIST = DESCRIPTOR.message_types_by_name["MUIStateList"]
_MANTICOREINSTANCE = DESCRIPTOR.message_types_by_name["ManticoreInstance"]
_TERMINATERESPONSE = DESCRIPTOR.message_types_by_name["TerminateResponse"]
_NATIVEARGUMENTS = DESCRIPTOR.message_types_by_name["NativeArguments"]
_EVMARGUMENTS = DESCRIPTOR.message_types_by_name["EVMArguments"]
_ADDRESSREQUEST = DESCRIPTOR.message_types_by_name["AddressRequest"]
_TARGETRESPONSE = DESCRIPTOR.message_types_by_name["TargetResponse"]
_MANTICORERUNNINGSTATUS = DESCRIPTOR.message_types_by_name["ManticoreRunningStatus"]
_ADDRESSREQUEST_TARGETTYPE = _ADDRESSREQUEST.enum_types_by_name["TargetType"]
MUILogMessage = _reflection.GeneratedProtocolMessageType(
    "MUILogMessage",
    (_message.Message,),
    {
        "DESCRIPTOR": _MUILOGMESSAGE,
        "__module__": "muicore.MUICore_pb2"
        # @@protoc_insertion_point(class_scope:muicore.MUILogMessage)
    },
)
_sym_db.RegisterMessage(MUILogMessage)

MUIMessageList = _reflection.GeneratedProtocolMessageType(
    "MUIMessageList",
    (_message.Message,),
    {
        "DESCRIPTOR": _MUIMESSAGELIST,
        "__module__": "muicore.MUICore_pb2"
        # @@protoc_insertion_point(class_scope:muicore.MUIMessageList)
    },
)
_sym_db.RegisterMessage(MUIMessageList)

MUIState = _reflection.GeneratedProtocolMessageType(
    "MUIState",
    (_message.Message,),
    {
        "DESCRIPTOR": _MUISTATE,
        "__module__": "muicore.MUICore_pb2"
        # @@protoc_insertion_point(class_scope:muicore.MUIState)
    },
)
_sym_db.RegisterMessage(MUIState)

MUIStateList = _reflection.GeneratedProtocolMessageType(
    "MUIStateList",
    (_message.Message,),
    {
        "DESCRIPTOR": _MUISTATELIST,
        "__module__": "muicore.MUICore_pb2"
        # @@protoc_insertion_point(class_scope:muicore.MUIStateList)
    },
)
_sym_db.RegisterMessage(MUIStateList)

ManticoreInstance = _reflection.GeneratedProtocolMessageType(
    "ManticoreInstance",
    (_message.Message,),
    {
        "DESCRIPTOR": _MANTICOREINSTANCE,
        "__module__": "muicore.MUICore_pb2"
        # @@protoc_insertion_point(class_scope:muicore.ManticoreInstance)
    },
)
_sym_db.RegisterMessage(ManticoreInstance)

TerminateResponse = _reflection.GeneratedProtocolMessageType(
    "TerminateResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _TERMINATERESPONSE,
        "__module__": "muicore.MUICore_pb2"
        # @@protoc_insertion_point(class_scope:muicore.TerminateResponse)
    },
)
_sym_db.RegisterMessage(TerminateResponse)

NativeArguments = _reflection.GeneratedProtocolMessageType(
    "NativeArguments",
    (_message.Message,),
    {
        "DESCRIPTOR": _NATIVEARGUMENTS,
        "__module__": "muicore.MUICore_pb2"
        # @@protoc_insertion_point(class_scope:muicore.NativeArguments)
    },
)
_sym_db.RegisterMessage(NativeArguments)

EVMArguments = _reflection.GeneratedProtocolMessageType(
    "EVMArguments",
    (_message.Message,),
    {
        "DESCRIPTOR": _EVMARGUMENTS,
        "__module__": "muicore.MUICore_pb2"
        # @@protoc_insertion_point(class_scope:muicore.EVMArguments)
    },
)
_sym_db.RegisterMessage(EVMArguments)

AddressRequest = _reflection.GeneratedProtocolMessageType(
    "AddressRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _ADDRESSREQUEST,
        "__module__": "muicore.MUICore_pb2"
        # @@protoc_insertion_point(class_scope:muicore.AddressRequest)
    },
)
_sym_db.RegisterMessage(AddressRequest)

TargetResponse = _reflection.GeneratedProtocolMessageType(
    "TargetResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _TARGETRESPONSE,
        "__module__": "muicore.MUICore_pb2"
        # @@protoc_insertion_point(class_scope:muicore.TargetResponse)
    },
)
_sym_db.RegisterMessage(TargetResponse)

ManticoreRunningStatus = _reflection.GeneratedProtocolMessageType(
    "ManticoreRunningStatus",
    (_message.Message,),
    {
        "DESCRIPTOR": _MANTICORERUNNINGSTATUS,
        "__module__": "muicore.MUICore_pb2"
        # @@protoc_insertion_point(class_scope:muicore.ManticoreRunningStatus)
    },
)
_sym_db.RegisterMessage(ManticoreRunningStatus)

_MANTICOREUI = DESCRIPTOR.services_by_name["ManticoreUI"]
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _MUILOGMESSAGE._serialized_start = 34
    _MUILOGMESSAGE._serialized_end = 66
    _MUIMESSAGELIST._serialized_start = 68
    _MUIMESSAGELIST._serialized_end = 126
    _MUISTATE._serialized_start = 128
    _MUISTATE._serialized_end = 156
    _MUISTATELIST._serialized_start = 159
    _MUISTATELIST._serialized_end = 387
    _MANTICOREINSTANCE._serialized_start = 389
    _MANTICOREINSTANCE._serialized_end = 422
    _TERMINATERESPONSE._serialized_start = 424
    _TERMINATERESPONSE._serialized_end = 460
    _NATIVEARGUMENTS._serialized_start = 463
    _NATIVEARGUMENTS._serialized_end = 636
    _EVMARGUMENTS._serialized_start = 639
    _EVMARGUMENTS._serialized_end = 811
    _ADDRESSREQUEST._serialized_start = 814
    _ADDRESSREQUEST._serialized_end = 943
    _ADDRESSREQUEST_TARGETTYPE._serialized_start = 899
    _ADDRESSREQUEST_TARGETTYPE._serialized_end = 943
    _TARGETRESPONSE._serialized_start = 945
    _TARGETRESPONSE._serialized_end = 978
    _MANTICORERUNNINGSTATUS._serialized_start = 980
    _MANTICORERUNNINGSTATUS._serialized_end = 1024
    _MANTICOREUI._serialized_start = 1027
    _MANTICOREUI._serialized_end = 1552
# @@protoc_insertion_point(module_scope)
