"""Hello message tests."""
#from pyof.v0x05.symmetric.hello import Hello, HelloElemVersionbitmap
from tests.test_struct import TestStruct
import unittest
# import pyof.v0x01.symmetric.hello as Hello
# import pyof.v0x04.symmetric.hello as Hello
#from pyof.v0x05.symmetric.hello import HelloElemType, HelloElemHeader
import pyof.v0x05.symmetric.hello as Hello
from pyof.foundation.basic_types import UBInt32,UBInt64, UBInt16, UBInt8

class TestHello(unittest.TestCase):

    # @classmethod
    # def setUpClass(cls):


    # def tearDownClass(cls):
    #     pass

    def setUp(self):
        self.type = UBInt16(2)
        self.length = UBInt16(6)
        self.type1 = UBInt16(1)
        self.length1 = UBInt16(8)

    def tearDown(self):
        pass

    def test_helloElemType(self):
        self.testValue = Hello.HelloElemType.OFPHET_VERSIONBITMAP
        self.assertEqual(1, self.testValue)


    def test_helloElemHeader(self):

        # Create objects with type and length values
        # Assert if the values were store correctly in the object
        self.testObject = Hello.HelloElemHeader(self.type, self.length)
        self.assertEqual(self.type, self.testObject.type)
        self.assertEqual(self.length, self.testObject.length)

        # This needs understanding because the length changes
        # Test if unpack works with binary input and length 7
        data = self.testObject.unpack(b'0000000000100010' , 2)
        bData = self.testObject.length

        # Update the update_length method
        self.testObject.update_length()

        # NOTE: This test is going to fail until Understand what is going on in the packing method
        # # This needs understanding because the values changes.
        # Test if pack works with the supposed output of the unpack value and assert if they are equal
        bData1 = self.testObject.pack(data)
#        self.assertEqual(b'0000000000100010', bData1)


    def test_helloListOfHelloElements(self):
        # Assert if the creation of the object and its initialization method and its values are equal
        # Create two objects of class ListOfHelloElements
        self.test = Hello.ListOfHelloElements()
        self.test1 = Hello.ListOfHelloElements()
        # Initialize the two created objects with same type and length values
        Hello.ListOfHelloElements.__init__(self.test, Hello.HelloElemHeader(self.type, self.length))
        Hello.ListOfHelloElements.__init__(self.test1, Hello.HelloElemHeader(self.type, self.length))
        self.assertEqual(self.test, self.test1)

        # Assert if the type value change they are not equal
        self.test.__init__(Hello.HelloElemHeader(self.type1, self.length1))
        self.test1.__init__(Hello.HelloElemHeader(self.type, self.length1))
        self.assertNotEqual(self.test, self.test1)

        # Different method to initialize and update the values of the objects
        # Assert if one of the length value change they are equal because the types are equal
        self.test.__init__(Hello.HelloElemHeader(self.type, self.length))
        self.test1.__init__(Hello.HelloElemHeader(self.type, self.length1))
        self.assertEqual(self.test, self.test1)

        # Assert if I could add an item to the list
        self.test.append(self.test1)
        self.assertEqual(2, self.test.__len__())


    def test_hello(self):
        pass

    def test_helloElemVersionBitmap(self):
        # Testing the creation of the object
        pass


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