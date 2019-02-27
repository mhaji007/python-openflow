"""Hello message tests."""
import unittest
from tests.test_struct import TestStruct
import pyof.v0x05.symmetric.hello as Hello
import random
from pyof.foundation.basic_types import UBInt32, UBInt16, TypeList, BinaryData


class TestHello(unittest.TestCase):

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
        print('Testing fix value {} versus given value {}'.format(testValue, val))

        self.assertEqual(testValue, val)

    def test_hello(self):

        _NUM_OF_TEST = 25
        print()
        print('Testing the Hello Message pack.')

        for i in range(0, _NUM_OF_TEST):
            random.seed()

            testVal = i + random.randint(0,100)
            testValue = b'\x05\x00\x00\x08'+ UBInt32(testVal).pack()
            self.testObjectHello = Hello.Hello(testVal)

            val = self.testObjectHello.pack()

            print('Testing the fix value message {} versus the given value {}'.format(testValue, val))
            self.assertEqual(testValue, val)




    def test_helloElemVersionBitmap(self):
        print()
        print('Testing the class HelloElemVersionBitmap.')
        """ Test support 2 versions (ver 1 = 0x01 and ver 1.3 = 0x04) """

        ver1 = 0x01
        ver3 = 0x04
        ver = ver1 << ver3
        ver = ver | 2

        testVal = b'\x00\x01\x00\x08\x00\x00\x00\x12'
        self.testObjectHelloElemVersion = Hello.HelloElemVersionBitmap(UBInt16(8), UBInt32(ver).pack())
        val = self.testObjectHelloElemVersion.pack()
        print('Testing 2 version support ver 1 and ver 1.3 based on the specification\'s example.')
        print('Testing fix value {} versus given value {}.'.format(testVal, val))

        self.assertEqual(testVal,val)






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