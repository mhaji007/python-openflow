# System imports
from enum import IntEnum

# Local source tree imports
from pyof.foundation.basic_types import BinaryData, FixedTypeList, UBInt16, UBInt8, UBInt32, UBInt64, Pad
from pyof.foundation.base import GenericMessage
from pyof.foundation.basic_types import UBInt16, UBInt8, UBInt32
from pyof.v0x05.controller2switch.table_mod import TableModPropHeader
# Third-party imports

__all__ = ('TableDescription',)



# Classes

class TableDescription(GenericMessage):
    """
    Body of reply to OFPMP_TABLE_DESC request.
    """

    #: Length is padded to 64 bits
    length = UBInt16()

    #: Identifier of table. Lower numbered tables are consulted first
    table_id = UBInt8()

    #:  Align to 32-bits
    pad = Pad(1)

    #: Bitmap of OFPTC_* values
    config = UBInt32()

    #: Table Mod Property list - 0 or more.
    properties = FixedTypeList(TableModPropHeader)

    def __init__(self, xid=None, length=None, table_id=None, config=None, properties=None):
        super().__init__(xid)
        self.length = length
        self.table_id = table_id
        self.config = config
        self.properties = properties
