"""Hello message tests."""
import unittest
from tests.test_struct import TestStruct
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




    def test_helloVersionBitmap(self):

        # Test if the bitmap version is 1
        self.assertEqual(1, Hello.HelloElemType.OFPHET_VERSIONBITMAP)


    def test_helloElemHeader(self):

        print()
        print('Testing the HelloElemHeader one element')
        testValue = b'\x00\x01\x00\x04'

        self.testObjectElemHeader = Hello.HelloElemHeader(Hello.HelloElemType.OFPHET_VERSIONBITMAP, 4)
        value = self.testObjectElemHeader.pack()

        print('Testing the values fix value {} and given value from the header {}'.format(testValue, value))

        self.assertEqual(testValue,value)


    def test_helloListOfHelloElements(self):
        print()
        print('Testing the HelloElemHeader more than one element')
        testValue = b'\x00\x01\x00\x04\x00\x01\x00\x04\x00\x01\x00\x04'

        self.testObjectListOfHelloElem = Hello.ListOfHelloElements()

        self.testListOfElem = [Hello.HelloElemHeader(Hello.HelloElemType.OFPHET_VERSIONBITMAP,4),
                               Hello.HelloElemHeader(Hello.HelloElemType.OFPHET_VERSIONBITMAP,4),
                               Hello.HelloElemHeader(Hello.HelloElemType.OFPHET_VERSIONBITMAP,4)]

        self.testObjectListOfHelloElem.__init__(self.testListOfElem)

        val = self.testObjectListOfHelloElem.pack()

        print('Testing the pack value return by the ListOfHelloElements more than one element.')
        print('Testing fix value {} versus given value {}'.format(testValue, val))

        self.assertEqual(testValue, val)


    def test_helloListOfHelloElement(self):
        print()
        print('Testing the HelloElemHeader one element')
        testValue = b'\x00\x01\x00\x04'
        self.testObjectListOfHelloElem = Hello.ListOfHelloElements()

        self.testObjectListOfHelloElem.__init__(Hello.HelloElemHeader(Hello.HelloElemType.OFPHET_VERSIONBITMAP,4))


        val = self.testObjectListOfHelloElem.pack()

        print('Testing the pack value return by the ListOfHelloElements one element.')
        print('Texting fix value {} versus given value {}'.format(testValue, val))

        self.assertEqual(testValue, val)

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
        # the reference is the OpenFlow 1.4 specification/page 147 of this struct(class) the sizeof is 8 bytes
        # so we are testing it with 8 bytes * 8 bits/bytes = 64 bits
        #self.assertEqual((8 * 8), Hello.Hello.__sizeof__(Hello.Hello()))
        #self.assertEqual((8 * 8), self.testObjectHello.__sizeof__())



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
        # the reference is the OpenFlow 1.4 specification/page 147 of this struct(class) the sizeof is 4 bytes
        # so we are testing it with 4 bytes * 8 bits/bytes = 32 bits
        self.assertEqual((4 * 8), Hello.HelloElemVersionBitmap.__sizeof__(Hello.HelloElemVersionBitmap()))
        self.assertEqual((4 * 8), self.testObjectVersion.__sizeof__())

# UNCOMMENT to used the previous tests
# class TestHelloStruct(TestStruct):
#     """Hello message tests (also those in :class:`.TestDump`)."""
#
#     @classmethod
#     def setUpClass(cls):
#         """Configure raw file and its object in parent class (TestDump)."""
#         super().setUpClass()
#         super().set_raw_dump_file('v0x05', 'ofpt_hello')
#         super().set_raw_dump_object(Hello.Hello, xid=1)
#         super().set_minimum_size(8)




if __name__ == '__main__':
    unittest.main()