
import random
from pyof.foundation.basic_types import UBInt16,UBInt32, UBInt8
from pyof.v0x05.common.header import Type


class MessageGenerator():
    MAX_XID_VALUE = 1000
    MIN_NUM_OF_MESSAGE = 10
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
                xid = UBInt32(random.randint(0,self.MAX_XID_VALUE))

            if self.type_of_mesg == Type.OFPT_GET_CONFIG_REPLY:

                length = b'\x00\x0c'

                header = version + msg_type + length + xid.pack()

                flags = UBInt16(random.randint(0, 3)).pack()

                miss_send = UBInt16(random.randint(0, 0xffe5)).pack()

                value = header + flags + miss_send
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


class PrintTables():


    def print_table(self, obj=None):
        pass
