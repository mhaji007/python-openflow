import random
from pyof.foundation.basic_types import UBInt16,UBInt32, UBInt8
from pyof.v0x05.common.header import Type


class TestFakeSwitch():
    MIN_NUM_OF_MESSAGE = 10
    random.seed()
    type_of_mesg = Type
    listOfConfigMessage = list()
    max_num_of_mesg = random.randint(MIN_NUM_OF_MESSAGE, MIN_NUM_OF_MESSAGE * 2)
    xid = UBInt32()

    for index in range(0,max_num_of_mesg):

        version = b'\x05'
        type = UBInt8(type_of_mesg.value(type_of_mesg)).pack()
        length = b'\x08'
        if xid is None:
            xid = UBInt32(random.randint(2,500)).pack()

        header = version + type + length + xid

        if type_of_mesg == Type.OFPT_GET_CONFIG_REPLY:

            flags = UBInt16(random.randint(0, 3)).pack()

            miss_send = UBInt16(random.randint(0, 0xffe5)).pack()

            value = header + flags + miss_send

            listOfConfigMessage.append(value)

        else:
            pass

    def __init__(self, type_of_mesg=Type.value, xid=None):

        if type_of_mesg is None:
            raise Exception()

        self.type_of_mesg = type_of_mesg
        self.xid = xid

    def get(self, index=None):
        if index is not None:
            return self.listOfConfigMessage[index]

    def length(self):
        return self.listOfConfigMessage.__len__()
