""" Defines Bundle Control message."""

# System imports

from enum import IntEnum

from pyof.foundation.base import GenericBitMask, GenericMessage, GenericStruct
from pyof.foundation.basic_types import UBInt32, UBInt16, FixedTypeList
from pyof.v0x05.common.header import Header, Type

# Third-party imports

__all__ = ('BundleControlType', 'BundleControlMsg', 'BundleFlags', 'BundlePropHeader'
           , 'BundlePropExperimenter', 'BundlePropType')


# Enums


class BundleControlType(IntEnum):
    """ Bundle control message types"""

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

class BundlePropHeader(GenericStruct):
    """Common header for all Bundle Properties"""

    #: One of OFPBPT_*.
    type = UBInt16()
    #: Length in bytes of this property
    length = UBInt16()

    def __int__(self, enum_ref=BundlePropType, length=None):
        self.type = type
        self.length = length


class BundlePropExperimenter(BundlePropHeader):
    """Experimenter bundle property"""

    #: OFPBPT_EXPERIMENTER
    type = BundlePropType.OFPTMPT_EXPERIMENTE
    #: Length in bytes of this property
    length = UBInt16()
    #: Experimenter ID which takes the same form as in struct experimenter_header
    experimenter = UBInt32()
    #: Experimenter defined
    exp_type = UBInt32()

    """Followed by:
        - Exactly (length - 12) bytes containing the experimenter data, then
        - Exactly (length + 7)/ 8 * 8 - (length) (between 0 and 7) bytes of all-zero bytes.
    """

    experimenter_data = UBInt32()

    def __init__(self, experimenter=None, exp_type=None):
        super().__init__()

        super().type = BundlePropType.OFPBPT_EXPERIMENTER

        self.experimenter = experimenter

        self.exp_type = exp_type


class BundleControlMsg(GenericMessage):
    """Message structure for OFPT_BUNDLE_CONTROL"""


    header = Header(message_type=Type.OFPT_BUNDLE_CONTROL)
    #: Identify the bundle
    bundle_id = UBInt32()
    #: OFPBCT_ *
    type = UBInt16()
    #: Bitmap of OFPBF_* flags
    flags = UBInt16(enum_ref=BundleFlags)
    #: Bundle Property list
    properties = FixedTypeList(BundlePropHeader)

    def __init__(self, xid=None, bundle_id=None, type=BundleControlType, flags=BundleFlags, properties=None):
        """Assign parameters to object attributes.

        Args:
            xid (int): :class:`~pyof.v0x05.common.header.Header`'s xid.
                Defaults to random.
            bundle_id (int): ID of the bundle
            flags (int): Bitmap of OFPBF_* flags
        """
        super().__init__(xid)
        self.bundle_id = bundle_id
        self.type = type
        self.flags = flags
        self.properties = properties
