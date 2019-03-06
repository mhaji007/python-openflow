"""Flow Table Modification message."""
from enum import IntEnum

from pyof.foundation.base import GenericBitMask, GenericMessage, GenericStruct
from pyof.foundation.basic_types import Pad, UBInt8, UBInt32, UBInt16, FixedTypeList
from pyof.v0x05.common.header import Header, Type


__all__ = ('Table', 'TableMod')



class Table(IntEnum):
    """Table numbering. Tables can use any number up to OFPT_MAX."""

    #: Last usable table number.
    OFPTT_MAX = 0xfe
    # Fake tables.
    #: Wildcard table used for table config, flow stats and flow deletes.
    OFPTT_ALL = 0xff



class TableModPropType(IntEnum):
    #: Eviction property
    OFPTMPT_EVICTION = 0x2
    #: Vacancy property
    OFPTMPT_VACANCY = 0x3
    #:Experimenter
    OFPTMPT_EXPERIMENTER = 0xFFFF


class TableModPropEvictionFlag(GenericBitMask):
    #: Using other factors
    OFPTMPEF_OTHER = 1 << 0
    #: Using flow entry importance
    OFPTMPEF_IMPORTANCE = 1 << 1
    #: Using flow entry lifetime
    OFPTMPEF_LIFETIME = 1 << 2




class TableModPropHeader(GenericStruct):
    #: One of OFPTMPT_
    type = UBInt16()
    #: Length in bytes of this property
    length = UBInt16()

    def __init__(self, type = None, length = None):
        super().__init__()
        self.type = type
        self.length = length


class TableModPropEviction(GenericStruct):
    #: OFPTMPT_EVICTION
    type = UBInt16()
    #: Length in bytes of this property
    length = UBInt16()
    #: Bitmap of OFPTMPEF_* flags
    flags = UBInt32










class TableMod(GenericMessage):
    """Configure/Modify behavior of a flow table."""

    header = Header(message_type=Type.OFPT_TABLE_MOD)
    table_id = UBInt8()
    #: Pad to 32 bits
    pad = Pad(3)
    config = UBInt32()

    properties = FixedTypeList(TableModPropHeader)

    def __init__(self, xid=None, table_id=Table.OFPTT_ALL, config=3):
        """Assing parameters to object attributes.

        Args:
            xid (int): :class:`~pyof.v0x05.common.header.Header`'s xid.
                Defaults to random.
            table_id (int): ID of the table, OFPTT_ALL indicates all tables.
            config (int): Bitmap of OFPTC_* flags
        """
        super().__init__(xid)
        self.table_id = table_id
        # This is reserved for future used. The default value is the only valid
        # one from the Enum.
        self.config = config
