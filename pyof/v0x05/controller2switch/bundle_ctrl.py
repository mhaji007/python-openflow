""" Defines Bundle Control message."""

# System imports

from enum import IntEnum

from pyof.foundation.base import GenericBitMask, GenericMessage, GenericStruct
from pyof.foundation.basic_types import Pad, UBInt8, UBInt32, UBInt16, FixedTypeList
from pyof.v0x05.common.header import Header, Type

# Third-party imports

__all__=('BundleControlType','BundleControl')


# Enums


class BundleControlType(IntEnum):
    OFPBCT_OPEN_REQUEST = 0
    OFPBCT_OPEN_REPLY = 1
    OFPBCT_CLOSE_REQUEST = 2
    OFPBCT_CLOSE_REPLY = 3
    OFPBCT_COMMIT_REQUEST = 4
    OFPBCT_COMMIT_REPLY = 5
    OFPBCT_DISCARD_REQUEST = 6
    OFPBCT_DISCARD_REPLY = 7


class BundleFlags(GenericBitMask):
    """ Bundle configuration flags"""
    #: Execute atomically
    OFPBF_ATOMIC = 1 << 0
    #: Execute in specified order
    OFPBF_ORDERED = 1 << 1



class BundlePropType(IntEnum):
    """Bundle property types"""

    #: Experimenter property
    OFPBPT_EXPERIMENTER = 0xFFFF


# Classes


class BundleControl(GenericMessage):
    header = Header(message_type=Type.OFPT_BUNDLE_CONTROL)
    #: Identify the bundle
    bundle_id = UBInt32()
    #: OFPBCT_ *
    type=UBInt16()
    #: Bitmap of OFPBF_* flags
    flags=UBInt16(enum_ref=BundleFlags)
    #: Bundle Property list
    properties = FixedTypeList(BundlePropHeader)


    def __init__(self, xid=None, bundle_id=None, type=None, flags=None,properties=None):
        super().__init__(xid)
        self.bundle_id=bundle_id
        self.type=type
        self.flags=flags
        self.properties=properties