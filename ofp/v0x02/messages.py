from ofp.v0x02.structs import GenericStruct, OFPHeader
from ofp.v0x02.enums import OFPType
from ofp.v0x02.consts import OFP_VERSION
from ofp.v0x02.types import *

class OFPHELLO(GenericStruct):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._length = self.get_size()
        _msg_type = OFPType.OFPT_HELLO
        _build_order = ('header', 'x')

        header = OFPHeader(type = _msg_type, length = _length)
        x = UBInt8()

class OFPECHORequest(GenericMessage):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.lenght(self.get_size())
        _msg_type = OFPType.OFPT_ECHO_REQUEST
        _build_order = ('header', 'x')

        header = OFPHeader(type = _msg_type, length = _length)
        x = UBInt8()

class OFPECHOReply(GenericMessage):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.lenght(self.get_size())
        _msg_type = OFPType.OFPT_ECHO_REPLY
        _build_order = ('header', 'x')

        header = OFPHeader(type = _msg_type, length = _length)
        x = UBInt8()
