"""Echo request message tests."""
from pyof.v0x05.symmetric.echo_request import EchoRequest
from pyof.foundation.basic_types import UBInt32, UBInt16, UBInt8, BinaryData
from tests.test_struct import TestStruct
import unittest



class TestEchoRequest(TestStruct):
    """Echo request message tests (also those in :class:`.TestDump`)."""

    @classmethod
    def setUpClass(cls):
        """Configure raw file and its object in parent class (TestDump)."""
        super().setUpClass()
        super().set_raw_dump_file('v0x05', 'ofpt_echo_request')
        super().set_raw_dump_object(EchoRequest, xid=0)
        super().set_minimum_size(8)




class TestEchoReuestByCases(unittest.TestCase):

    def setUp(self):
        self.type = UBInt8(3)
        self.length = UBInt16(6)
        self.xid = UBInt32(23)
        self.data = BinaryData(b'001100111101')
        self.testObject = EchoRequest()
        self.testObject.header.__init__(self.type,self.length,self.xid)
        self.testObject1 = EchoRequest(self.xid,self.data)


    def test_echoRequest(self):
        self.assertEqual(self.type, self.testObject.header.message_type)
        self.assertEqual(self.length, self.testObject.header.length)
        self.assertEqual(self.xid, self.testObject.header.xid)
        self.assertEqual(self.data, self.testObject1.data)
        self.assertNotEqual(self.type, self.testObject1.header.message_type)



if __name__ == '__main__':
    unittest.main()