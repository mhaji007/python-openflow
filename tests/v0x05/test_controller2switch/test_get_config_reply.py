"""Config Reply message tests."""
#import pyof.v0x05.controller2switch.get_config_reply as GetConfigReply
#from pyof.v0x05.common.header import Type
# from pyof.foundation.basic_types import UBInt32, UBInt16, UBInt8
from tests.v0x05.test_controller2switch.test_utils import TestFakeSwitch
# from tests.test_struct import TestStruct
import unittest
import random



class TestGetConfigReply(unittest.TestCase):

    def test_getting_reply(self):

        print()
        print('Testing the GetConfigReply class.')

        #self.testObject = GetConfigReply.GetConfigReply()
        #values = TestFakeSwitch(Type.OFPT_GET_CONFIG_REPLY)

        # for i in range(0, values.length()):
        #
        #     val = values.get(i)

            # self.testObject.unpack(val, 8)
            # testValue = self.testObject.pack()
            # print('Testing the unpack message {} versus {}'.format(val, testValue))
            # self.assertEqual(val, testValue)



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
    unittest.main()