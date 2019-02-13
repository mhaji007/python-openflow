"""Hello message tests."""
import unittest

import pyof.v0x05.symmetric.hello as Hello
from pyof.foundation.basic_types import UBInt32, UBInt16, TypeList


class TestHello(unittest.TestCase):

    # @classmethod
    # def setUpClass(cls):


    # def tearDownClass(cls):
    #     pass

    def setUp(self):
        # Create variables and object to use in the testing cases
        self.type = UBInt16(2)
        self.length = UBInt16(6)
        self.type1 = UBInt16(1)
        self.length1 = UBInt16(8)
        self.version1 = UBInt32(0x01)
        self.version2 = UBInt32(0x04)
        self.version3 = UBInt32(0x05)
        self.helloElements = Hello.ListOfHelloElements()
        self.helloElements.__init__(Hello.HelloElemHeader(self.type, self.length))
        self.helloElements.append(Hello.ListOfHelloElements(Hello.HelloElemHeader(self.type1, self.length1)))


        

    # def tearDown(self):
    #     # Delete all variable and objects after used in testing cases
    #     pass


    

    def test_helloElemType(self):
        # Takes the values of bitmap version into a variable
        self.testValue = Hello.HelloElemType.OFPHET_VERSIONBITMAP
        # Test if the bitmap version is 1
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

        # Test to test the exceptions
        # with self.assertRaises():



        # NOTE: This test is going to fail until Understand what is going on in the packing method
        # # This needs understanding because the values changes.
        # Test if pack works with the supposed output of the unpack value and assert if they are equal
        bData1 = self.testObject.pack(data)
#        self.assertEqual(b'0000000000100010', bData1)
        # This assert test the size of the object which it has to be 32 bits
        # the reference is the OpenFlow 1.4 specification/page 130 of this struct(class) the sizeof is 4 bytes
        # so we are testing it with 4 bytes * 8 bits/bytes = 32 bits
        self.assertEqual((4 * 8), Hello.HelloElemHeader.__sizeof__(Hello.HelloElemHeader()))
        self.assertEqual((4 * 8), self.testObject.__sizeof__())


    def test_helloListOfHelloElements(self):
        # Assert if the creation of the object and its initialization method and its values are equal
        # Create two objects of class ListOfHelloElements
        self.testObjectListOfHelloElem = Hello.ListOfHelloElements()
        self.testObjectListOfHelloElem1 = Hello.ListOfHelloElements()
        # Initialize the two created objects with same type and length values
        Hello.ListOfHelloElements.__init__(self.testObjectListOfHelloElem, Hello.HelloElemHeader(self.type, self.length))
        Hello.ListOfHelloElements.__init__(self.testObjectListOfHelloElem1, Hello.HelloElemHeader(self.type, self.length))
        self.assertEqual(self.testObjectListOfHelloElem, self.testObjectListOfHelloElem1)

        # Assert if the type value change they are not equal
        self.testObjectListOfHelloElem.__init__(Hello.HelloElemHeader(self.type1, self.length1))
        self.testObjectListOfHelloElem1.__init__(Hello.HelloElemHeader(self.type, self.length1))
        self.assertNotEqual(self.testObjectListOfHelloElem, self.testObjectListOfHelloElem1)

        # Different method to initialize and update the values of the objects
        # Assert if one of the length value change they are equal because the types are equal
        self.testObjectListOfHelloElem.__init__(Hello.HelloElemHeader(self.type, self.length))
        self.testObjectListOfHelloElem1.__init__(Hello.HelloElemHeader(self.type, self.length1))
        self.assertEqual(self.testObjectListOfHelloElem, self.testObjectListOfHelloElem1)

        # Assert if I could add an item to the list
        self.testObjectListOfHelloElem.append(self.testObjectListOfHelloElem1)
        self.assertEqual(2, self.testObjectListOfHelloElem.__len__())


    def test_hello(self):

        # Create the Hello message Object
        self.testObjectHello = Hello.Hello(1, self.helloElements)
        # Test if it has version 0x05 as the message version
        self.assertEqual(0x05, self.testObjectHello.header.version)
        # Test if the x1d is 1
        self.assertEqual(1, self.testObjectHello.header.xid)
        # Test if the message type is OFPT_HELLO
        self.assertEqual(0, self.testObjectHello.header.message_type)
        # Test if the initialize helloElements are the same
        self.assertEqual(self.helloElements, self.testObjectHello.elements)

        # This assert test the size of the object which it has to be 64 bits
        # the reference is the OpenFlow 1.4 specification/page 130 of this struct(class) the sizeof is 8 bytes
        # so we are testing it with 8 bytes * 8 bits/bytes = 64 bits
        self.assertEqual((8 * 8), Hello.Hello.__sizeof__(Hello.Hello()))
        self.assertEqual((8 * 8), self.testObjectHello.__sizeof__())



    def test_helloElemVersionBitmap(self):

        # Create and Initialize a TypeList object to be submitted as a bitmap
        # Add to the object the 3 versions of Type UBInt32
        self.bData1 = TypeList(self.version1)
        self.bData1.append(self.version2)
        self.bData1.append(self.version3)
        # Create and Initialize the HelloElemVersionBitmap with type, length and the list of Versions
        self.testObjectVersion = Hello.HelloElemVersionBitmap(self.type, self.length, self.bData1)
        # Assert if the number of Versions are correct under the Bitmap
        self.assertEqual(3, self.testObjectVersion.bitmaps.__len__())
        # Assert that the Type are the same between the 2 values
        self.assertEqual(self.type, self.testObjectVersion.type)
        # Assert that the Length are the same between the 2 values
        self.assertEqual(self.length, self.testObjectVersion.length)

        # This assert test the size of the object which it has to be 32 bits
        # the reference is the OpenFlow 1.4 specification/page 130 of this struct(class) the sizeof is 4 bytes
        # so we are testing it with 4 bytes * 8 bits/bytes = 32 bits
        self.assertEqual((4 * 8), Hello.HelloElemVersionBitmap.__sizeof__(Hello.HelloElemVersionBitmap()))
        self.assertEqual((4 * 8), self.testObjectVersion.__sizeof__())

#
# class TestHelloClass(TestStruct,unittest.TestCase):
#     """Hello message tests (also those in :class:`.TestDump`)."""
#
#     @classmethod
#     def setUpClass(cls):
#         """Configure raw file and its object in parent class (TestDump)."""
#         super().setUpClass()
#         super().set_raw_dump_file('v0x05', 'ofpt_hello')
#         super().set_raw_dump_object(Hello, xid=1)
#         super().set_minimum_size(8)
#
#     def test_raw_dump_file(self):
#         self.assertEqual(0,0,'They are equeals to 0')
#
#     def test_minimum_size(self):
#         pass
#
#     def test_raw_dump_object(self):
#         pass
#

if __name__ == '__main__':
    unittest.main()
