"""Config Reply message tests."""
from pyof.v0x05.controller2switch.get_config_reply import GetConfigReply
from tests.test_struct import TestStruct
import unittest




class TestFakeSwitch():

    listOfConfigMessage = list()


    def __int__(self, item=None):
        if item is not None:
            self.listOfConfigMessage.append(item)



    def append(self, item=None):
        if item is not None:
            self.listOfConfigMessage.append(item)

    def get(self, index=None):
        if index is None:
            return None
        else:
            self.listOfConfigMessage.__getitem__(index)


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
