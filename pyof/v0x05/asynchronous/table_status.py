"""Defines an Table Status Message."""

# System imports
from enum import IntEnum

# Local source tree imports

from pyof.foundation.base import GenericMessage, GenericStruct
from pyof.foundation.basic_types import BinaryData, FixedTypeList, UBInt16, UBInt8, UBInt32, UBInt64, Pad
from pyof.v0x05.common.header import Header, Type
from pyof.v0x05.controller2Switch.table_description import TableDescription

# Third-party imports

__all__ = ('TableStatus', 'TableReason')

class TableReason(IntEnum):
    """What changed about the table."""

    #: Vacancy down threshold event
    OFPTR_VACANCY_DOWN = 3
    #: Vacancy up threshold event
    OFPTR_VACANCY_UP = 4



class TableStatus(GenericMessage):
    """OpenFlow TableStatus Message OFPT_TABLE_STATUS.
    """

    header = Header(message_type=Type.OFPT_TABLE_STATUS)
    reason = UBInt8()

   # pad = FixedTypeList(UBInt8())
    pad = Pad(7)
    generation_id = UBInt64()

    table = TableDescription()

    def __init__(self, xid=None, reason=None, generation_id=None, table=None):
        """Create a message with the optional parameters below.

        Args:
            xid (int): xid to be used on the message header.
            elements: List of elements - 0 or more
        """
        super().__init__(xid)
        self.reason=reason
        self.generation_id=generation_id
        self.table=table

