"""Defines Get Config Reply message."""

# System imports

# Third-party imports
from pyof.foundation.basic_types import GenericStruct, UBInt16
from pyof.foundation.base import IntEnum
from pyof.v0x05.common.header import Type, Header
#from pyof.v0x05.controller2switch.common import SwitchConfig

__all__ = ('GetConfigReply','ConfigFlags')

#: Enums
class ConfigFlags(IntEnum):
    """Handling of IP fragments."""

    #: No special handling for fragments.
    OFPC_FRAG_NORMAL = 0
    #: Drop fragments.
    OFPC_FRAG_DROP = 1 << 0
    #: Reassemble (only if OFPC_IP_REASM set).
    OFPC_FRAG_REASM = 1 << 1
    #: Bit,ask of flags dealing with frag
    OFPC_FRAG_MASK = 3


#: Classes

class GetConfigReply(GenericStruct):
    """Get Config Reply message."""

    header = Header(message_type=Type.OFPT_GET_CONFIG_REPLY)

    #: Bitmap of OFPC_* flags.
    flags = UBInt16()

    #: Max bytes of packet that datapath should send to the controller.
    #: See ofp_controller_max_len for valid values.
    miss_send_len = UBInt16()

    def __init__(self, xid=None, flags=None, miss_send_len=None):
        """Create a GetConfigReply with the optional parameters below.

        Args:
            xid (int): xid to be used on the message header.
            flags (ConfigFlags):
                OFPC_* flags.
            miss_send_len (int): UBInt16 max bytes of new flow that the
                datapath should send to the controller.
        """
        self.header.xid = xid
        self.flags = flags
        self.miss_send_len = miss_send_len


