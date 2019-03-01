"""Config Reply message tests."""
from pyof.v0x05.controller2switch.get_config_reply import ConfigFlags, GetConfigReply
from pyof.foundation.basic_types import UBInt32, UBInt16, UBInt8
from tests.test_struct import TestStruct
import unittest
import random



class TestFakeSwitch():
    MIN_NUM_OF_MESSAGE = 10
    random.seed()

    listOfConfigMessage = list()
    max_num_of_mesg = random.randint(MIN_NUM_OF_MESSAGE, MIN_NUM_OF_MESSAGE * 2)

    for index in range(0,max_num_of_mesg):

        header = b'\x05\x00\x00\x00'
        xid = UBInt32(random.randint(2,500)).pack()
        flags = UBInt16(random.randint(0, 3)).pack()
        miss_send = UBInt16(random.randint(100, 500)).pack()
        value = header + xid + flags + miss_send

        listOfConfigMessage.append(value)

    def get(self, index=None):
        if index is not None:
            return self.listOfConfigMessage[index]

    def length(self):
        return self.listOfConfigMessage.__len__()






# class TestGetConfigReply(TestStruct):
#     """Config Reply message tests."""
#
#     @classmethod
#     def setUpClass(cls):
#         """Configure raw file and its object in parent class (TestDump)."""
#         super().setUpClass()
#         super().set_raw_dump_file('v0x05', 'ofpt_get_config_reply')
#         super().set_raw_dump_object(GetConfigReply, xid=1)
#         super().set_minimum_size(12)


if __name__ == '__main__':
    TestFakeSwitch()