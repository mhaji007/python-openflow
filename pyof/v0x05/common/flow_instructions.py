"""Flow instructions to be executed.

The flow instructions associated with a flow table entry are executed when a
flow matches the entry.
"""
# System imports
from enum import IntEnum

# Local source tree imports
from pyof.foundation.base import GenericStruct
from pyof.foundation.basic_types import (
    FixedTypeList, Pad, UBInt8, UBInt16, UBInt32, UBInt64)
from pyof.foundation.exceptions import PackException

from pyof.v0x05.common.action import ListOfActions
from pyof.v0x05.controller2switch.meter_mod import Meter

# Third-party imports


__all__ = ('InstructionApplyAction', 'InstructionClearAction',
           'InstructionGotoTable', 'InstructionMeter', 'InstructionType',
           'InstructionWriteAction', 'InstructionWriteMetadata',
           'ListOfInstruction')

# Enums


class InstructionType(IntEnum):
    """List of instructions that are currently defined."""

    #: Setup the next table in the lookup pipeline
    OFPIT_GOTO_TABLE = 1
    #: Setup the metadata field for use later in pipeline
    OFPIT_WRITE_METADATA = 2
    #: Write the action(s) onto the datapath action set
    OFPIT_WRITE_ACTIONS = 3
    #: Applies the action(s) immediately
    OFPIT_APPLY_ACTIONS = 4
    #: Clears all actions from the datapath action set
    OFPIT_CLEAR_ACTIONS = 5
    #: Apply meter (rate limiter)
    OFPIT_METER = 6
    #: Experimenter instruction
    OFPIT_EXPERIMENTER = 0xFFFF

    def find_class(self):
        """Return a class related with this type."""
        classes = {1: InstructionGotoTable, 2: InstructionWriteMetadata,
                   3: InstructionWriteAction, 4: InstructionApplyAction,
                   5: InstructionClearAction, 6: InstructionMeter}
        return classes.get(self.value, None)


# Classes

class InstructionHeader(GenericStruct):
    """ Instruction header that is common to all instructions. The
        length includes the header and any padding used to make the
        instruction 64-bit aligned.
        NB: The length of an instruction *MUST* always be a multiple of eight.
    """
    #: One of OFPIT_*.
    type = UBInt16(enum_ref=InstructionType)
    #: Length of this struct in bytes.
    length = UBInt16()

    def __init__(self, instruction_type=None):
        """Create a Instruction with the optional parameters below.

        Args:
            instruction_type(InstructionType): Type of instruction.
        """
        super().__init__()
        self.instruction_type = instruction_type

    def pack(self, value=None):
        """Update the length and pack the massege into binary data.

        Returns:
            bytes: A binary data that represents the Message.

        Raises:
            Exception: If there are validation errors.

        """
        if value is None:
            self.update_length()
            return super().pack()
        elif isinstance(value, type(self)):
            return value.pack()
        else:
            msg = "{} is not an instance of {}".format(value,
                                                       type(self).__name__)
            raise PackException(msg)

    def update_length(self):
        """Update length attribute."""
        self.length = self.get_size()

    def unpack(self, buff=None, offset=0):
        """Unpack *buff* into this object.

        This method will convert a binary data into a readable value according
        to the attribute format.

        Args:
            buff (bytes): Binary buffer.
            offset (int): Where to begin unpacking.

        Raises:
            :exc:`~.exceptions.UnpackException`: If unpack fails.

        """
        instruction_type = UBInt16(enum_ref=InstructionType)
        instruction_type.unpack(buff, offset)
        self.__class__ = InstructionType(instruction_type.value).find_class()

        length = UBInt16()
        length.unpack(buff, offset=offset+2)

        super().unpack(buff[:offset+length.value], offset)


class InstructionApplyAction(InstructionHeader):
    """Instruction structure for OFPIT_APPLY_ACTIONS.

    The :attr:`~actions` field is treated as a list, and the actions are
    applied to the packet in-order.
    """

    #: Align to 64-bits
    pad = Pad(4)
    #: Actions associated with OFPIT_APPLY_ACTIONS
    actions = ListOfActions()

    def __init__(self, actions=None):
        """Create a InstructionApplyAction with the optional parameters below.

        Args:
            actions (:class:`~.actions.ListOfActions`):
                Actions associated with OFPIT_APPLY_ACTIONS.
        """
        super().__init__(InstructionType.OFPIT_APPLY_ACTIONS)
        self.actions = actions if actions else []


class InstructionClearAction(InstructionHeader):
    """Instruction structure for OFPIT_CLEAR_ACTIONS.

    This structure does not contain any actions.
    """

    #: Align to 64-bits
    pad = Pad(4)
    #: OFPIT_CLEAR_ACTIONS does not have any action on the list of actions.
    actions = ListOfActions()

    def __init__(self, actions=None):
        """Create a InstructionClearAction with the optional parameters below.

        Args:
            actions (:class:`~.actions.ListOfActions`):
                Actions associated with OFPIT_CLEAR_ACTIONS.
        """
        super().__init__(InstructionType.OFPIT_CLEAR_ACTIONS)
        self.actions = actions if actions else []

class InstructionWriteAction(InstructionHeader):
    """Instruction structure for OFPIT_WRITE_ACTIONS.

    The actions field must be treated as a SET, so the actions are not
    repeated.
    """

    #: Align to 64-bits
    pad = Pad(4)
    #: Actions associated with OFPIT_WRITE_ACTIONS
    actions = ListOfActions()

    def __init__(self, actions=None):
        """Create a InstructionWriteAction with the optional parameters below.

        Args:
            actions (:class:`~.actions.ListOfActions`):
                Actions associated with OFPIT_WRITE_ACTIONS.
        """
        super().__init__(InstructionType.OFPIT_WRITE_ACTIONS)
        self.actions = actions if actions else []

# Check
class InstructionActions(GenericStruct):
    """ Instruction structure for OFPIT_WRITE/APPLY/CLEAR_ACTIONS """

    #: One of OFPIT_*_ACTIONS
    type = UBInt16()
    #: Length is padded to 64 bits
    len = UBInt16()
    #: Align to 64-bits
    pad = Pad(4)
    #: 0 or more actions associated with OFPIT_WRITE/APPLY_ACTIONS
    actions = ListOfActions()

    def __init__(self, actions=None):
        """Create a InstructionApplyAction with the optional parameters below.

        Args:
            actions (:class:`~.actions.ListOfActions`):
                Actions associated with OFPIT_APPLY_ACTIONS.
        """
        super().__init__(InstructionType.OFPIT_APPLY_ACTIONS)
        self.actions = actions if actions else []



class InstructionGotoTable(InstructionHeader):
    """Instruction structure for OFPIT_GOTO_TABLE."""

    #: OFPIT_GOTO_TABLE
    type = UBInt16()
    #: Length is 8.
    len = UBInt16()
    #: Set next table in the lookup pipeline
    table_id = UBInt8()
    #: Pad to 64 bits.
    pad = Pad(3)

    def __init__(self, table_id=Meter.OFPM_ALL, len=None):
        """Create a InstructionGotoTable with the optional parameters below.

        Args:
            len (int): Length of this struct in bytes.
            table_id (int): set next table in the lookup pipeline.
        """
        super().__init__(InstructionType.OFPIT_GOTO_TABLE)
        self.length = len
        self.table_id = table_id


class InstructionMeter(GenericStruct):
    """Instruction structure for OFPIT_METER.

    meter_id indicates which meter to apply on the packet.
    """

    #: OFPIT_METER
    type = UBInt16()
    #: Length is 8.
    len = UBInt16()
    #: Meter instance.
    meter_id = UBInt32()

    def __init__(self, meter_id=Meter.OFPM_ALL):
        """Create a InstructionMeter with the optional parameters below.

        Args:
            meter_id (int): Meter instance.
        """
        super().__init__(InstructionType.OFPIT_METER)
        self.meter_id = meter_id




class InstructionExperimenterHeader(InstructionHeader):
    """ Instruction structure for experimental instructions """

    #: Experimenter ID
    experimenter = UBInt32()
    #: Experimenter-defined arbitrary additional data.


class InstructionWriteMetadata(InstructionHeader):
    """Instruction structure for OFPIT_WRITE_METADATA."""

    #: OFPIT_WRITE_METADATA
    type = UBInt16()
    #: Length is 24.
    len = UBInt16()
    #: Align to 64-bits
    pad = Pad(4)
    #: Metadata value to write
    metadata = UBInt64()
    #: Metadata write bitmask
    metadata_mask = UBInt64()

    def __init__(self, metadata=0, metadata_mask=0):
        """Create InstructionWriteMetadata with the optional parameters below.

        Args:
            metadata (int): Metadata value to write.
            metadata_mask (int): Metadata write bitmask.
        """
        super().__init__(InstructionType.OFPIT_WRITE_METADATA)
        self.metadata = metadata
        self.metadata_mask = metadata_mask


class ListOfInstruction(FixedTypeList):
    """List of Instructions.

    Represented by instances of Instruction.
    """

    def __init__(self, items=None):
        """Create ListOfInstruction with the optional parameters below.

        Args:
            items (:class:`~pyof.v0x05.common.flow_instructions.InstructionHeader`):
                Instance or a list of instances.
        """
        super().__init__(pyof_class=InstructionHeader, items=items)
