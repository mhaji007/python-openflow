"""Defines a Controller Role Status Message."""

# System imports
from enum import IntEnum

# Local source tree imports
from pyof.foundation.base import GenericMessage, GenericStruct
from pyof.foundation.basic_types import BinaryData, FixedTypeList, UBInt16, UBInt8, UBInt32, UBInt64, Pad
from pyof.v0x05.common.header import Header, Type

# Third-party imports

__all__ = ('RoleReason', 'RolePropertyType', 'RolePropHeader', 'RoleStatus')


# Enums

class RoleReason(IntEnum):
    """What changed about the controller role."""

    #: Another controller asked to be master
    OFPCRR_MASTER_REQUEST = 0
    #: Configuration changed on the switch
    OFPCRR_CONFIG = 1
    #: Experimenter data changed
    OFPCRR_EXPERIMENTER = 2


class RolePropertyType(IntEnum):
        """Role property types"""

        #: Experimenter property
        OFPRT_EXPERIMENTER = 0xFFFF



class RolePropHeader(GenericStruct):
    """Common header for all Role properties"""

    #: One of OFPRPT_
    type = UBInt16()
    #: Length in bytes of this property
    length = UBInt16()

    def __init__(self, type = None, length = None):
        super().__init__()
        self.type = type
        self.length = length


class RoleStatus(GenericMessage):
    """OpenFlow Controller Role Status Message OFPT_ROLE_REQUEST. """

    #: Type OFPT_ROLE_STATUS
    header = Header(message_type=Type.OFPT_ROLE_STATUS)
    #: One of OFPCR_ROLE_*
    role = UBInt32()
    #: One of OFPCRR_*.
    reason = UBInt8(enum_ref=RoleReason)
    #: Align to 64 bits
    pad = Pad(3)
    #: Master Election Generation Id
    generation_id = UBInt64()
    #: Role Property list
    properties = FixedTypeList(RolePropHeader)

    def __init__(self, xid=None, role=None, reason=None, generation_id=None, properties=None):
        """Create a message with the optional parameters below.

        Args:
            xid (int): xid to be used on the message header.
            elements: List of elements - 0 or more
        """
        super().__init__(xid)
        self.role = role
        self.reason = reason
        self.generation_id = generation_id
        self.properties = properties


class ExperimenterRoleProperty():
    """ Experimenter role property"""

    type = UBInt16()
    length = UBInt16()
    experimenter = UBInt32()
    exp_type = UBInt32()
    experimenter_data = UBInt32()

    def __int__(self, type=Type.OFPRPT_EXPERIMENTER, length=None, experimenter=None, exp_type=None, experimenter_data=None):
        self.type = type
        self.length = length
        self.experimenter = experimenter
        self.exp_type = exp_type
        self.experimenter_data = experimenter_data
