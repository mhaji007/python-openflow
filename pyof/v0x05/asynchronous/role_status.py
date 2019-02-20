
from pyof.foundation.base import GenericMessage, GenericStruct
from pyof.foundation.basic_types import BinaryData, FixedTypeList, UBInt16, UBInt8, UBInt32, UBInt64
from pyof.v0x05.common.header import Header, Type


# class OfpHeader(GenericStruct):
#     """Ofp Header"""
#
#
#     element_type = UBInt16()
#     content = BinaryData()
#
#     def __init__(self, message_type=None, content = b''):
#         """Create a Header with the optional parameters below.
#
#         Args:
#             element_type: One of OFPHET_*.
#         """
#         super().__init__()
#         self.message_type = message_type
#         self.content = content


class OfpRolePropHeader(GenericStruct):
    type = UBInt16()
    length = UBInt16()

    def __init__(self, type = None, length = None):
        super().__init__()
        self.type = type
        self.length = length


class OfpRoleStatus(GenericMessage):
    """OpenFlow Hello Message OFPT_HELLO.

    This message includes zero or more hello elements having variable size.
    Unknown element types must be ignored/skipped, to allow for future
    extensions.
    """

    header = OfpHeader(message_type=Type.OFPT_ROLE_STATUS)
    role = UBInt32()
    reason = UBInt8()
    pad = FixedTypeList(UBInt8())
    generation_id = UBInt64()

    properties = FixedTypeList(OfpRolePropHeader())

    def __init__(self, xid=None, data=None):
        """Create a message with the optional parameters below.

        Args:
            xid (int): xid to be used on the message header.
            elements: List of elements - 0 or more
        """
        super().__init__(xid)
        self.data = data

