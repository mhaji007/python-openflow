
import random
from pyof.foundation.basic_types import UBInt16,UBInt32, UBInt8, UBInt64
from pyof.foundation.base import GenericMessage, GenericType
from pyof.v0x05.common.header import Type, Header
from pyof.foundation.constants import UBINT32_MAX_VALUE, UBINT16_MAX_VALUE, UBINT8_MAX_VALUE, UBINT64_MAX_VALUE
from pyof.v0x05.common.flow_match import Match, MatchType, OxmTLV

class MessageGenerator():

    MAX_32BITS_VALUE = 1000
    MAX_8BITS_VALUE = 128
    MAX_16BITS_VALUE = 1000
    MAX_64BITS_VALUE = 1000
    MIN_NUM_OF_MESSAGE = 10
    MAX_NUM_OF_OXMTLV = 5

    random.seed()
    type_of_msg = Type
    listOfConfigMessage = list()
    max_num_of_mesg = random.randint(MIN_NUM_OF_MESSAGE, MIN_NUM_OF_MESSAGE * 2)
    xid = UBInt32()

    def generate_messages(self):

        for index in range(0, self.max_num_of_mesg):

            version = b'\x05'
            msg_type = UBInt8(self.type_of_mesg.__int__()).pack()

            if self.xid is None:
                xid = UBInt32(random.randint(0,self.MAX_32BITS_VALUE))

            if self.type_of_mesg == Type.OFPT_GET_CONFIG_REPLY:

                test_length = b'\x00\x00'

                test_header = version + msg_type + test_length + xid.pack()

                flags = UBInt16(random.randint(0, 3)).pack()

                miss_send = UBInt16(random.randint(0, 0xffe5)).pack()

                test_value = test_header + flags + miss_send

                length = UBInt16(len(test_value)).pack()

                header = version + msg_type + length + xid.pack()

                value = header + flags + miss_send

                item = (xid, value)

            elif self.type_of_mesg == Type.OFPT_PACKET_IN:

                test_length = b'\x00\x08'

                header = version + msg_type + test_length + xid.pack()

                buffer_id = UBInt32(random.randint(0, self.MAX_32BITS_VALUE)).pack()

                total_len = UBInt16(random.randint(0, self.MAX_16BITS_VALUE)).pack()

                reason = UBInt8(random.randint(0, 5)).pack()

                table_id = UBInt8(random.randint(0, self.MAX_8BITS_VALUE)).pack()

                cookie = UBInt64(random.randint(0, self.MAX_64BITS_VALUE)).pack()

                oxmtlv = b''

                for i in range(0, random.randint(1,self.MAX_NUM_OF_OXMTLV)):

                    oxm_class = UBInt16(0x8000).pack()
                    oxm_field_and_mask = UBInt8(0).pack()
                    oxm_length = UBInt8(0)
                    oxm_value = UBInt32(random.randint(1, self.MAX_32BITS_VALUE)).pack()

                    test_value = oxm_class + oxm_field_and_mask + oxm_length.pack()
                    oxm_length = UBInt8(len(test_value)).pack()
                    val = oxm_class + oxm_field_and_mask + oxm_length + oxm_value

                    oxmtlv += val

                match_type = UBInt16(1).pack()
                match_length = UBInt16(0)
                match_pad = UBInt32(0).pack()
                test_length = match_type + match_length.pack() + oxmtlv + match_pad

                match_length = UBInt16(len(test_length)).pack()

                matchVal = match_type + match_length + oxmtlv + match_pad

                test_value = header + buffer_id + total_len + reason + table_id + cookie + matchVal

                length = UBInt16(len(test_value)).pack()

                header = version + msg_type + length + xid.pack()

                value = header + buffer_id + total_len + reason + table_id + cookie + matchVal

                item = (xid, value)

            else:
                pass

            self.listOfConfigMessage.append(item)

    def __init__(self, type_of_mesg=Type, xid=None):

        if type_of_mesg is None:
            raise Exception()

        self.type_of_mesg = type_of_mesg
        self.xid = xid


    def get(self, index=None):
        if index is not None:
            return self.listOfConfigMessage[index]

    def length(self):
        return self.listOfConfigMessage.__len__()

#Needs Work
class PrintTables():
    div = '-'
    strTable = ''

    def print_table(self, obj=GenericMessage):

        version = obj.header.version
        msg_type = obj.header.message_type.__str__()
        length = obj.header.length.__str__()
        xid = obj.header.xid.__str__()

        attr = obj.__getattribute__('flags').__str__()
        self.strTable = hex(version.value) + self.div + msg_type + self.div + length + self.div + xid + self.div + attr

