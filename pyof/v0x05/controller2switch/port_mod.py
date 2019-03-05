"""Modifications to the port from the controller."""

# System imports

# Third-party imports

# Local source tree imports
from pyof.foundation.base import GenericMessage, IntEnum, GenericStruct
from pyof.foundation.basic_types import HWAddress, Pad, UBInt32, FixedTypeList, UBInt16
from pyof.v0x05.common.header import Header, Type
from pyof.v0x05.common.port import PortConfig, PortFeatures

__all__ = ('PortMod','PortModPropType', 'PortModPropHeader', )

#: Enums
class PortModPropType(IntEnum):
    """Port mod property types"""

    #: Ethernet property.
    OFPPMPT_ETHERNET = 0
    #: Optical property.
    OFPPMPT_OPTICAL = 1
    #: Experimenter property.
    OFPPMPT_EXPERIMENTER = 0xffff

# Classes

class PortModPropHeader(GenericStruct):
    """Common header for all port mod properties."""

    #: One of OFPPMPT_*
    type = UBInt16()
    #: Length in bytes of this property.
    length = UBInt16()


class PortMod(GenericMessage):
    """Implement messages to modify the physical port behavior."""

    header = Header(message_type=Type.OFPT_PORT_MOD)

    port_no = UBInt32()
    pad = Pad(4)
    #: The hardware address is not configurable. This is used to
    #: sanity-check the request, so it must be the same as returned in an port struct.
    hw_addr = HWAddress()
    #: Pad to 64 bits.
    pad2 = Pad(2)
    #: Bitmap of OFPPC_* flags.
    config = UBInt32(enum_ref=PortConfig)
    #: Bitmap of OFPPC_* flags to be changed.
    mask = UBInt32(enum_ref=PortConfig)
    #: Port mod property list - 0 or more properties
    properties = FixedTypeList(pyof_class=PortModPropHeader)



    def __init__(self, xid=None, port_no=None, hw_addr=None, config=None,
                 mask=None, properties=FixedTypeList(pyof_class=PortModPropHeader)):
        """Create a PortMod with the optional parameters below.

        Args:
            xid (int): OpenFlow xid to the header.
            port_no (int): Physical port number.
            hw_addr (HWAddress): The hardware address is not configurable.
                This is used to sanity-check the request,
                so it must be the same as returned in an ofp_phy_port struct.
            config (~pyof.v0x05.common.port.PortConfig):
                Bitmap of OFPPC_* flags
            mask (~pyof.v0x05.common.port.PortConfig):
                Bitmap of OFPPC_* flags to be changed
            properties (FixedTypeList(pyof_class=PortModPropHeader)):
                Port mod property list - 0 or more properties
        """
        super().__init__(xid)
        self.port_no = port_no
        self.hw_addr = hw_addr
        self.config = config
        self.mask = mask
        self.properties = properties

class PortModPropEthernet(PortModPropHeader):
    """Ethernet port mod property"""

    #: Bitmap of OFPPF_*. Zero all bits to prevent any action taking place.
    advertise = UBInt32()


    def __init__(self, advertise=None):
        super().type = PortModPropType.OFPPMPT_ETHERNET
        self.advertise = advertise
        super().length = self.__sizeof__()

