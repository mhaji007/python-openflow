"""Hello message tests."""
#from pyof.v0x05.symmetric.hello import Hello, HelloElemVersionbitmap
from tests.test_struct import TestStruct
import unittest
# import pyof.v0x01.symmetric.hello as Hello
# import pyof.v0x04.symmetric.hello as Hello
import pyof.v0x05.symmetric.hello as Hello


class TestHello(unittest.TestCase):

    def setUpClass(cls):
        pass

    def tearDownClass(cls):
        pass

    def setUp(self):
        self.test_VersionBitMap = Hello.HelloElemVersionbitmap(Hello.HelloElemType.OFPHET_VERSIONBITMAP)

    def tearDown(self):
        pass

    def test_HelloElemType(self):
        self.assertEqual(Hello.HelloElemType.OFPHET_VERSIONBITMAP, 1)

    def test_HelloElemHeader(self):
        self.testObject = Hello.HelloElemHeader(b'0110110011110010', b'0001000010101010')
        self.assertEqual(self.testObject.type, b'0110110011110010')
        self.assertEqual(self.testObject.length, b'0001000010101010')













#
# class TestHello(TestStruct):
#     """Hello message tests (also those in :class:`.TestDump`)."""
#
#     @classmethod
#     def setUpClass(cls):
#         """Configure raw file and its object in parent class (TestDump)."""
#         super().setUpClass()
#         super().set_raw_dump_file('v0x05', 'ofpt_hello')
#         super().set_raw_dump_object(Hello, xid=1)
#         super().set_minimum_size(8)



if __name__ == '__main__':
    unittest.main()