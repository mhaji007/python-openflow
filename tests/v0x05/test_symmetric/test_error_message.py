"""Testing v0x05 error message class."""
from pyof.v0x05.symmetric.error_message import ErrorMsg
import pyof.v0x05.symmetric.error_message as Error
from tests.test_struct import TestStruct
from pyof.foundation.basic_types import UBInt8,UBInt16,UBInt32,UBInt64,BinaryData
import unittest
import random

#
# class TestErrorMsg(TestStruct):
#     """ErroMsg message tests (also those in :class:`.TestDump`)."""
#
#     @classmethod
#     def setUpClass(cls):
#         """Configure raw file and its object in parent class (TestDump)."""
#         super().setUpClass()
#         super().set_raw_dump_file('v0x05', 'ofpt_error_msg')
#         super().set_raw_dump_object(ErrorMsg, xid=1, error_type=1, code=1)
#         super().set_minimum_size(12)


class TestErrorMessageTestCases(unittest.TestCase):

    def setUp(self):
        self.testGenericFailedCode = Error.GenericFailedCode
        self.testBadActionCode = Error.BadActionCode
        self.testBadInstructionCode = Error.BadInstructionCode
        self.testBadMatchCode = Error.BadMatchCode
        self.testBadRequestCode = Error.BadRequestCode
        self.testErrorType = Error.ErrorType
        self.testFlowModFailedCode = Error.FlowModFailedCode
        self.testGroupModFailedCode = Error.GroupModFailedCode
        self.testHelloFailedCode = Error.HelloFailedCode
        self.testMeterModFailedCode = Error.MeterModFailedCode
        self.testPortModFailedCode = Error.PortModFailedCode
        self.testQueueOpFailedCode = Error.QueueOpFailedCode
        self.testRoleRequestFailedCode = Error.RoleRequestFailedCode
        self.testSwitchConfigFailedCode = Error.SwitchConfigFailedCode
        self.testTableFeatureFailedCode = Error.TableFeaturesFailedCode
        self.testTableModFailedCode = Error.TableModFailedCode
        self.testBadPropertyCode = Error.BadPropertyCode
        self.testAsyncConfigFailedCode = Error.AsyncConfigFailedCode
        self.testFlowMonitorFailedCode = Error.FlowMonitorFailedCode
        self.testBundleFailedCode = Error.BundleFailedCode
        self.testErrorMessage = Error.ErrorMsg()
        self.testErrorExperimenterMessage = Error.ErrorExperimenterMsg()

        random.seed()

    def tearDown(self):
        pass

    def test_generic_failed_codeValue(self):
        value = 0
        print()
        print('Testing the Generic Failed Codes Values')
        for elem in self.testGenericFailedCode:
            print('Testing expected code value {} versus actual code value {}'.format(value, elem))
            self.assertEqual(value, elem)


    def test_bad_action_codeValue(self):
        print()
        print('Testing the Bad Action Codes Values')
        value = 0

        for elem in self.testBadActionCode:
            print('Testing expected code value {} versus actual code value {}'.format(value, elem))
            self.assertEqual(value, elem)
            if value == 16:
                break
            else:
                value += 1


    def test_bad_instruction_codeValue(self):
        print()
        print('Testing the Bad Instruction Codes Values')
        value = 0

        for elem in self.testBadInstructionCode:
            print('Testing expected code value {} versus actual code value {}'.format(value, elem))
            self.assertEqual(value, elem)
            value += 1

    def test_bad_match_codeValue(self):
        print()
        print('Testing the Bad Match Codes Values')
        value = 0

        for elem in self.testBadMatchCode:
            print('Testing expected code value {} versus actual code value {}'.format(value, elem))
            self.assertEqual(value, elem)
            value += 1

    def test_bad_request_codeValue(self):
        print()
        print('Testing the Bad Request Codes Values')
        value = 0

        for elem in self.testBadRequestCode:
            print('Testing expected code value {} versus actual code value {}'.format(value, elem))
            self.assertEqual(value, elem)
            value += 1

    def test_error_type(self):
        print()
        print('Testing the Error Types Codes Values')
        value = 0
        temp = 0
        for elem in self.testErrorType:

            if value == 18:
                value = 0xffff
            print('Testing expected code value {} versus actual code value {}'.format(value, elem))
            self.assertEqual(value, elem)
            value += 1


    def test_flow_mod_failed_codeValue(self):
        print()
        print('Testing the Flow Mod Failed Codes Values')
        value = 0

        for elem in self.testFlowModFailedCode:
            print('Testing expected code value {} versus actual code value {}'.format(value, elem))
            self.assertEqual(value, elem)
            value += 1

    def test_group_mod_failed_codeValue(self):
        print()
        print('Testing the Group Mod Failed Codes Values')
        value = 0

        for elem in self.testGroupModFailedCode:
            print('Testing expected code value {} versus actual code value {}'.format(value, elem))
            self.assertEqual(value, elem)
            value += 1

    def test_hello_failed_codeValue(self):
        print()
        print('Testing the Hello Failed Codes Values')
        value = 0

        for elem in self.testHelloFailedCode:
            print('Testing expected code value {} versus actual code value {}'.format(value, elem))
            self.assertEqual(value, elem)
            value += 1

    def test_meter_mod_failed_codeValue(self):
        print()
        print('Testing the Meter Mod Failed Codes Values')
        value = 0

        for elem in self.testMeterModFailedCode:
            print('Testing expected code value {} versus actual code value {}'.format(value, elem))
            self.assertEqual(value, elem)
            value += 1

    def test_port_mod_failed_codeValue(self):
        print()
        print('Testing the Port Mod Failed Codes Values')
        value = 0

        for elem in self.testPortModFailedCode:
            print('Testing expected code value {} versus actual code value {}'.format(value, elem))
            self.assertEqual(value, elem)
            value += 1

    def test_queue_op_failed_codeValue(self):
        print()
        print('Testing the Queue Op Failed Codes Values')
        value = 0

        for elem in self.testQueueOpFailedCode:
            print('Testing expected code value {} versus actual code value {}'.format(value, elem))
            self.assertEqual(value, elem)
            value += 1

    def test_role_request_failed_codeValue(self):
        print()
        print('Testing the Role Request Failed Codes Values')
        value = 0

        for elem in self.testRoleRequestFailedCode:
            print('Testing expected code value {} versus actual code value {}'.format(value, elem))
            self.assertEqual(value, elem)
            value += 1

    def test_switch_config_failed_codeValue(self):
        print()
        print('Testing the Switch Config Failed Codes Values')
        value = 0

        for elem in self.testSwitchConfigFailedCode:
            print('Testing expected code value {} versus actual code value {}'.format(value, elem))
            self.assertEqual(value, elem)
            value += 1

    def test_table_feature_failed_codeValue(self):
        print()
        print('Testing the Table Feature Failed Codes Values')
        value = 0

        for elem in self.testTableFeatureFailedCode:
            if value == 2:
                value = 5
            print('Testing expected code value {} versus actual code value {}'.format(value, elem))
            self.assertEqual(value, elem)
            value += 1

    def test_table_mod_failed_codeValue(self):
        print()
        print('Testing the Table Mod Failed Codes Values')
        value = 0

        for elem in self.testTableModFailedCode:
            print('Testing expected code value {} versus actual code value {}'.format(value, elem))
            self.assertEqual(value, elem)
            value += 1

    def test_bad_property_codeValue(self):
        print()
        print('Testing the Bad Property Codes Values')
        value = 0

        for elem in self.testBadPropertyCode:
            print('Testing expected code value {} versus actual code value {}'.format(value, elem))
            self.assertEqual(value, elem)
            value += 1

    def test_async_config_failed_codeValue(self):
        print()
        print('Testing the Async Config Failed Codes Values')
        value = 0

        for elem in self.testAsyncConfigFailedCode:
            print('Testing expected code value {} versus actual code value {}'.format(value, elem))
            self.assertEqual(value, elem)
            value += 1

    def test_flow_monitor_failed_codeValue(self):
        print()
        print('Testing the Flow Monitor Failed Codes Values')
        value = 0

        for elem in self.testFlowMonitorFailedCode:
            print('Testing expected code value {} versus actual code value {}'.format(value, elem))
            self.assertEqual(value, elem)
            value += 1

    def test_bundle_failed_codeValue(self):
        print()
        print('Testing the Bundle Failed Codes Values')
        value = 0

        for elem in self.testBundleFailedCode:
            print('Testing expected code value {} versus actual code value {}'.format(value, elem))
            self.assertEqual(value, elem)
            value += 1


    def test_error_message_header_hello_failed_codes(self):
        errorType = 0
        errorTypeValue = Error.ErrorType.OFPET_HELLO_FAILED

        print('Testing the header HelloFailedCodes.')

        errorCode = 0

        for elem in Error.ErrorType.get_class(errorTypeValue):

            data = UBInt32(random.randint(2, 250)).pack()
            xid = random.randint(2, 250)

            testValue = b'\x05\x01\x00\x10' + UBInt32(xid).pack() + UBInt16(errorType).pack() + \
                        UBInt16(errorCode).pack() + data

            errorCode += 1

            testObjectErrorMessages = Error.ErrorMsg(xid, errorTypeValue, elem, data).pack()

            print('Testing expected value {} versus actual value {}'.format(testValue, testObjectErrorMessages))

            self.assertEqual(testValue, testObjectErrorMessages)


    def test_error_message_header_bad_request_codes(self):
        errorType = 1
        errorTypeValue = Error.ErrorType.OFPET_BAD_REQUEST

        print('Testing the header BadRequestCodes.')

        errorCode = 0

        for elem in Error.ErrorType.get_class(errorTypeValue):
            data = UBInt32(random.randint(2, 250)).pack()
            xid = random.randint(2, 250)

            testValue = b'\x05\x01\x00\x10' + UBInt32(xid).pack() + UBInt16(errorType).pack() + \
                        UBInt16(errorCode).pack() + data

            errorCode += 1

            testObjectErrorMessages = Error.ErrorMsg(xid, errorTypeValue, elem, data).pack()

            print('Testing expected value {} versus actual value {}'.format(testValue, testObjectErrorMessages))

            self.assertEqual(testValue, testObjectErrorMessages)

    def test_error_message_header_bad_action_codes(self):
        errorType = 2
        errorTypeValue = Error.ErrorType.OFPET_BAD_ACTION

        print('Testing the header BadActionCodes.')

        errorCode = 0

        for elem in Error.ErrorType.get_class(errorTypeValue):
            data = UBInt32(random.randint(2, 250)).pack()
            xid = random.randint(2, 250)

            testValue = b'\x05\x01\x00\x10' + UBInt32(xid).pack() + UBInt16(errorType).pack() + \
                        UBInt16(errorCode).pack() + data

            errorCode += 1

            testObjectErrorMessages = Error.ErrorMsg(xid, errorTypeValue, elem, data).pack()

            print('Testing expected value {} versus actual value {}'.format(testValue, testObjectErrorMessages))

            self.assertEqual(testValue, testObjectErrorMessages)

    def test_error_message_header_bad_instruction_codes(self):
        errorType = 3
        errorTypeValue = Error.ErrorType.OFPET_BAD_INSTRUCTION

        print('Testing the header BadInstructionCodes.')

        errorCode = 0

        for elem in Error.ErrorType.get_class(errorTypeValue):
            data = UBInt32(random.randint(2, 250)).pack()
            xid = random.randint(2, 250)

            testValue = b'\x05\x01\x00\x10' + UBInt32(xid).pack() + UBInt16(errorType).pack() + \
                        UBInt16(errorCode).pack() + data

            errorCode += 1

            testObjectErrorMessages = Error.ErrorMsg(xid, errorTypeValue, elem, data).pack()

            print('Testing expected value {} versus actual value {}'.format(testValue, testObjectErrorMessages))

            self.assertEqual(testValue, testObjectErrorMessages)

    def test_error_message_header_bad_match_codes(self):
        errorType = 4
        errorTypeValue = Error.ErrorType.OFPET_BAD_MATCH

        print('Testing the header BadMatchCodes.')

        errorCode = 0

        for elem in Error.ErrorType.get_class(errorTypeValue):
            data = UBInt32(random.randint(2, 250)).pack()
            xid = random.randint(2, 250)

            testValue = b'\x05\x01\x00\x10' + UBInt32(xid).pack() + UBInt16(errorType).pack() + \
                        UBInt16(errorCode).pack() + data

            errorCode += 1

            testObjectErrorMessages = Error.ErrorMsg(xid, errorTypeValue, elem, data).pack()

            print('Testing expected value {} versus actual value {}'.format(testValue, testObjectErrorMessages))

            self.assertEqual(testValue, testObjectErrorMessages)

    def test_error_message_header_flow_mod_failed_codes(self):
        errorType = 5
        errorTypeValue = Error.ErrorType.OFPET_FLOW_MOD_FAILED

        print('Testing the header FlowModFailedCodes.')

        errorCode = 0

        for elem in Error.ErrorType.get_class(errorTypeValue):
            data = UBInt32(random.randint(2, 250)).pack()
            xid = random.randint(2, 250)

            testValue = b'\x05\x01\x00\x10' + UBInt32(xid).pack() + UBInt16(errorType).pack() + \
                        UBInt16(errorCode).pack() + data

            errorCode += 1

            testObjectErrorMessages = Error.ErrorMsg(xid, errorTypeValue, elem, data).pack()

            print('Testing expected value {} versus actual value {}'.format(testValue, testObjectErrorMessages))

            self.assertEqual(testValue, testObjectErrorMessages)


    def test_error_message_header_group_mod_failed_codes(self):
        errorType = 6
        errorTypeValue = Error.ErrorType.OFPET_GROUP_MOD_FAILED

        print('Testing the header GroupModFailedCodes.')

        errorCode = 0

        for elem in Error.ErrorType.get_class(errorTypeValue):
            data = UBInt32(random.randint(2, 250)).pack()
            xid = random.randint(2, 250)

            testValue = b'\x05\x01\x00\x10' + UBInt32(xid).pack() + UBInt16(errorType).pack() + \
                        UBInt16(errorCode).pack() + data

            errorCode += 1

            testObjectErrorMessages = Error.ErrorMsg(xid, errorTypeValue, elem, data).pack()

            print('Testing expected value {} versus actual value {}'.format(testValue, testObjectErrorMessages))

            self.assertEqual(testValue, testObjectErrorMessages)

    def test_error_message_header_port_mod_failed_codes(self):
        errorType = 7
        errorTypeValue = Error.ErrorType.OFPET_PORT_MOD_FAILED

        print('Testing the header PortModFailedCodes.')

        errorCode = 0

        for elem in Error.ErrorType.get_class(errorTypeValue):
            data = UBInt32(random.randint(2, 250)).pack()
            xid = random.randint(2, 250)

            testValue = b'\x05\x01\x00\x10' + UBInt32(xid).pack() + UBInt16(errorType).pack() + \
                        UBInt16(errorCode).pack() + data

            errorCode += 1

            testObjectErrorMessages = Error.ErrorMsg(xid, errorTypeValue, elem, data).pack()

            print('Testing expected value {} versus actual value {}'.format(testValue, testObjectErrorMessages))

            self.assertEqual(testValue, testObjectErrorMessages)

    def test_error_message_header_table_mod_failed_codes(self):
        errorType = 8
        errorTypeValue = Error.ErrorType.OFPET_TABLE_MOD_FAILED

        print('Testing the header TableModFailedCodes.')

        errorCode = 0

        for elem in Error.ErrorType.get_class(errorTypeValue):
            data = UBInt32(random.randint(2, 250)).pack()
            xid = random.randint(2, 250)

            testValue = b'\x05\x01\x00\x10' + UBInt32(xid).pack() + UBInt16(errorType).pack() + \
                        UBInt16(errorCode).pack() + data

            errorCode += 1

            testObjectErrorMessages = Error.ErrorMsg(xid, errorTypeValue, elem, data).pack()

            print('Testing expected value {} versus actual value {}'.format(testValue, testObjectErrorMessages))

            self.assertEqual(testValue, testObjectErrorMessages)

    def test_error_message_header_queue_op_failed_codes(self):
        errorType = 9
        errorTypeValue = Error.ErrorType.OFPET_QUEUE_OP_FAILED

        print('Testing the header QueueOpFailedCodes.')

        errorCode = 0

        for elem in Error.ErrorType.get_class(errorTypeValue):
            data = UBInt32(random.randint(2, 250)).pack()
            xid = random.randint(2, 250)

            testValue = b'\x05\x01\x00\x10' + UBInt32(xid).pack() + UBInt16(errorType).pack() + \
                        UBInt16(errorCode).pack() + data

            errorCode += 1

            testObjectErrorMessages = Error.ErrorMsg(xid, errorTypeValue, elem, data).pack()

            print('Testing expected value {} versus actual value {}'.format(testValue, testObjectErrorMessages))

            self.assertEqual(testValue, testObjectErrorMessages)

    def test_error_message_header_switch_config_failed_codes(self):
        errorType = 10
        errorTypeValue = Error.ErrorType.OFPET_SWITCH_CONFIG_FAILED

        print('Testing the header SwitchConfigFailedCodes.')

        errorCode = 0

        for elem in Error.ErrorType.get_class(errorTypeValue):
            data = UBInt32(random.randint(2, 250)).pack()
            xid = random.randint(2, 250)

            testValue = b'\x05\x01\x00\x10' + UBInt32(xid).pack() + UBInt16(errorType).pack() + \
                        UBInt16(errorCode).pack() + data

            errorCode += 1

            testObjectErrorMessages = Error.ErrorMsg(xid, errorTypeValue, elem, data).pack()

            print('Testing expected value {} versus actual value {}'.format(testValue, testObjectErrorMessages))

            self.assertEqual(testValue, testObjectErrorMessages)

    def test_error_message_header_role_request_failed_codes(self):
        errorType = 11
        errorTypeValue = Error.ErrorType.OFPET_ROLE_REQUEST_FAILED

        print('Testing the header RoleRequestFailedCodes.')

        errorCode = 0

        for elem in Error.ErrorType.get_class(errorTypeValue):
            data = UBInt32(random.randint(2, 250)).pack()
            xid = random.randint(2, 250)

            testValue = b'\x05\x01\x00\x10' + UBInt32(xid).pack() + UBInt16(errorType).pack() + \
                        UBInt16(errorCode).pack() + data

            errorCode += 1

            testObjectErrorMessages = Error.ErrorMsg(xid, errorTypeValue, elem, data).pack()

            print('Testing expected value {} versus actual value {}'.format(testValue, testObjectErrorMessages))

            self.assertEqual(testValue, testObjectErrorMessages)

    def test_error_message_header_meter_mod_failed_codes(self):
        errorType = 12
        errorTypeValue = Error.ErrorType.OFPET_METER_MOD_FAILED

        print('Testing the header MeterModFailedCodes.')

        errorCode = 0

        for elem in Error.ErrorType.get_class(errorTypeValue):
            data = UBInt32(random.randint(2, 250)).pack()
            xid = random.randint(2, 250)

            testValue = b'\x05\x01\x00\x10' + UBInt32(xid).pack() + UBInt16(errorType).pack() + \
                        UBInt16(errorCode).pack() + data

            errorCode += 1

            testObjectErrorMessages = Error.ErrorMsg(xid, errorTypeValue, elem, data).pack()

            print('Testing expected value {} versus actual value {}'.format(testValue, testObjectErrorMessages))

            self.assertEqual(testValue, testObjectErrorMessages)

    def test_error_message_header_table_features_failed_codes(self):
        errorType = 13
        errorTypeValue = Error.ErrorType.OFPET_TABLE_FEATURES_FAILED

        print('Testing the header TableFeaturesFailedCodes.')

        errorCode = 0

        for elem in Error.ErrorType.get_class(errorTypeValue):

            data = UBInt32(random.randint(2, 250)).pack()
            xid = random.randint(2, 250)

            if errorCode == 2:
                errorCode = 5

            testValue = b'\x05\x01\x00\x10' + UBInt32(xid).pack() + UBInt16(errorType).pack() + \
                        UBInt16(errorCode).pack() + data

            errorCode += 1

            testObjectErrorMessages = Error.ErrorMsg(xid, errorTypeValue, elem, data).pack()

            print('Testing expected value {} versus actual value {}'.format(testValue, testObjectErrorMessages))

            self.assertEqual(testValue, testObjectErrorMessages)

    def test_error_message_header_bad_property_codes(self):
        errorType = 14
        errorTypeValue = Error.ErrorType.OFPET_BAD_PROPERTY

        print('Testing the header BadPropertyCodes.')

        errorCode = 0

        for elem in Error.ErrorType.get_class(errorTypeValue):
            data = UBInt32(random.randint(2, 250)).pack()
            xid = random.randint(2, 250)

            testValue = b'\x05\x01\x00\x10' + UBInt32(xid).pack() + UBInt16(errorType).pack() + \
                        UBInt16(errorCode).pack() + data

            errorCode += 1

            testObjectErrorMessages = Error.ErrorMsg(xid, errorTypeValue, elem, data).pack()

            print('Testing expected value {} versus actual value {}'.format(testValue, testObjectErrorMessages))

            self.assertEqual(testValue, testObjectErrorMessages)

    def test_error_message_header_async_config_failed_codes(self):
        errorType = 15
        errorTypeValue = Error.ErrorType.OFPET_ASYNC_CONFIG_FAILED

        print('Testing the header AsyncConfigFailedCodes.')

        errorCode = 0

        for elem in Error.ErrorType.get_class(errorTypeValue):
            data = UBInt32(random.randint(2, 250)).pack()
            xid = random.randint(2, 250)

            testValue = b'\x05\x01\x00\x10' + UBInt32(xid).pack() + UBInt16(errorType).pack() +\
                        UBInt16(errorCode).pack() + data

            errorCode += 1

            testObjectErrorMessages = Error.ErrorMsg(xid, errorTypeValue, elem, data).pack()

            print('Testing expected value {} versus actual value {}'.format(testValue, testObjectErrorMessages))

            self.assertEqual(testValue, testObjectErrorMessages)

    def test_error_message_header_flow_monitor_failed_codes(self):
        errorType = 16
        errorTypeValue = Error.ErrorType.OFPET_FLOW_MONITOR_FAILED

        print('Testing the header FlowMonitorFailedCodes.')

        errorCode = 0

        for elem in Error.ErrorType.get_class(errorTypeValue):
            data = UBInt32(random.randint(2, 250)).pack()
            xid = random.randint(2, 250)

            testValue = b'\x05\x01\x00\x10' + UBInt32(xid).pack() + UBInt16(errorType).pack() + \
                        UBInt16(errorCode).pack() + data

            errorCode += 1

            testObjectErrorMessages = Error.ErrorMsg(xid, errorTypeValue, elem, data).pack()

            print('Testing expected value {} versus actual value {}'.format(testValue, testObjectErrorMessages))

            self.assertEqual(testValue, testObjectErrorMessages)

    def test_error_message_header_bundle_failed_codes(self):
        errorType = 17
        errorTypeValue = Error.ErrorType.OFPET_BUNDLE_FAILED

        print('Testing the header BundleFailed.')

        errorCode = 0

        for elem in Error.ErrorType.get_class(errorTypeValue):
            data = UBInt32(random.randint(2, 250)).pack()
            xid = random.randint(2, 250)

            testValue = b'\x05\x01\x00\x10' + UBInt32(xid).pack() + UBInt16(errorType).pack() + \
                        UBInt16(errorCode).pack() + data

            errorCode += 1

            testObjectErrorMessages = Error.ErrorMsg(xid, errorTypeValue, elem, data).pack()

            print('Testing expected value {} versus actual value {}'.format(testValue, testObjectErrorMessages))

            self.assertEqual(testValue, testObjectErrorMessages)

    def test_error_message_header_experimenter_codes(self):

        errorTypeValue = Error.ErrorType.OFPET_EXPERIMENTER
        errorType = 0xffff

        print('Testing the header ExperimenterCodes.')

        errorCode = 0

        for elem in Error.ErrorType.get_class(errorTypeValue):
            data = UBInt32(random.randint(2, 250)).pack()
            xid = random.randint(2, 250)

            testValue = b'\x05\x01\x00\x10' + UBInt32(xid).pack() + UBInt16(errorType).pack() + \
                        UBInt16(errorCode).pack() + data

            errorCode += 1

            testObjectErrorMessages = Error.ErrorMsg(xid, errorTypeValue, elem, data).pack()

            print('Testing expected value {} versus actual value {}'.format(testValue, testObjectErrorMessages))

            self.assertEqual(testValue, testObjectErrorMessages)


    def test_error_experimenter_message(self):
        # Max number of IDs to be created in the test
        MAX_NUM_ID = 20

        print()
        print('Testing the Experimenter Message.')

        type = 0xffff

        for id in range(0, MAX_NUM_ID):

            # Generate a random int number between 2 and 250
            exp_code = random.randint(2, 250)

            # Generate a random int number between 2 and 120 and then convert it in binary
            data = UBInt8(random.randint(2, 120)).pack()

            # Generate a random int number between 2 and 250
            xid = random.randint(2, 250)

            testValue = b'\x05\x01\x00\x11' + UBInt32(xid).pack() + UBInt16(type).pack() + \
                        UBInt16(exp_code).pack() + UBInt32(id).pack() + data

            self.testErrorExperimenterMessage.__init__(xid,exp_code, id, data)
            testObjectValue = self.testErrorExperimenterMessage.pack()

            print('Testing expected value {} versus actual value {}'.format(testValue, testObjectValue))

            self.assertEqual(testValue, testObjectValue)




if __name__ == '__main__':
    unittest.main()