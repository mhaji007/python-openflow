import random
from pyof.foundation.basic_types import UBInt16,UBInt32, UBInt8


class TestFakeSwitch():
    MIN_NUM_OF_MESSAGE = 10
    random.seed()

    listOfConfigMessage = list()
    max_num_of_mesg = random.randint(MIN_NUM_OF_MESSAGE, MIN_NUM_OF_MESSAGE * 2)

    for index in range(0,max_num_of_mesg):

        header = b'\x05\x08\x00\x08'
        xid = UBInt32(random.randint(2,500)).pack()
        flags = UBInt16(random.randint(0, 3)).pack()
        miss_send = UBInt16(random.randint(0, 0xffe5)).pack()
        value = header + xid + flags + miss_send

        listOfConfigMessage.append(value)

    def get(self, index=None):
        if index is not None:
            return self.listOfConfigMessage[index]

    def length(self):
        return self.listOfConfigMessage.__len__()
