"""Testing v0x05 error message class."""
from pyof.v0x05.symmetric.error_message import ErrorMsg
import pyof.v0x05.symmetric.error_message as Error
from tests.test_struct import TestStruct
from pyof.foundation.basic_types import UBInt8,UBInt16,UBInt32,UBInt64,BinaryData
import unittest
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
        # Creating the list of Error Types to be used in the testing
        self.listErrorType = dict()
        index = 0
        for e in self.testErrorType:
            self.listErrorType.__setitem__(index, e)
            index += 1

    def tearDown(self):
        pass

    def test_generic_failed_codeValue(self):
        value = 0
        print()
        print('Testing the Generic Failed Codes Values')
        for elem in self.testGenericFailedCode:
            print('Testing expected code value {} versus actual code value{}'.format(value, elem))
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
            print('Testing expected code value {} versus actual code value{}'.format(value, elem))
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

    def test_error_message(self):
        print()
        print('Testing the Error Message\'s Values')

        errorTypeValue = 0               # Variable for the error type value simulated

        for errorType in self.testErrorType:

            codeValue = 0                # Variable for the code value inside the errorTypeValue simulated

            for elem in Error.ErrorType.get_class(errorType):

                if errorTypeValue == 13 and codeValue == 2:
                    codeValue = 5            # It will skip from 2-4 in the error message OFPET_TABLE_FEATURES_FAILED
                elif errorTypeValue == 18:
                    errorTypeValue = 0xffff  # Experimenter error type value

                # Create object with fix values to test the Error Message
                testValue = Error.ErrorMsg(12, errorTypeValue, codeValue, b'00001110010')
                # Error object message to be tested
                self.testErrorMessage.__init__(12, errorType, elem, b'00001110010')

                print('Testing expected error type values {} and code value {} versus '
                      'actual error type value {} and code value {}'.format(errorTypeValue, codeValue,
                                                                     self.testErrorMessage.type,
                                                                     self.testErrorMessage.code))

                # Test results
                self.assertEqual(testValue, self.testErrorMessage)

                codeValue += 1

            errorTypeValue += 1

    def test_error_message_header_hello_failed_codes(self):
        pass

    def test_error_message_header_bad_request_codes(self):
        pass

    def test_error_message_header_bad_action_codes(self):
        pass

    def test_error_message_header_bad_instruction_codes(self):
        pass

    def test_error_message_header_bad_match_codes(self):
        pass

    def test_error_message_header_flow_mod_failed_codes(self):
        pass


    def test_error_message_header_group_mod_failed_codes(self):
        pass

    def test_error_message_header_port_mod_failed_codes(self):
        pass

    def test_error_message_header_table_mod_failed_codes(self):
        pass

    def test_error_message_header_queue_op_failed_codes(self):
        pass

    def test_error_message_header_switch_config_failed_codes(self):
        pass

    def test_error_message_header_role_request_failed_codes(self):
        pass

    def test_error_message_header_meter_mod_failed_codes(self):
        pass

    def test_error_message_header_table_features_failed_codes(self):
        pass

    def test_error_message_header_bad_property_codes(self):
        pass

    def test_error_message_header_async_config_failed_codes(self):
        pass

    def test_error_message_header_flow_monitor_failed_codes(self):
        pass

    def test_error_message_header_bundle_failed_codes(self):
        pass

    def test_error_message_header_experimenter_codes(self):
        pass



    def test_error_message_header(self):

        dictErrorValues = {0:1, 1:15, 2:15, 3:9, 4:11, 5:10, 6:14, 7:4, 8: 2, 9:2,10:2,
                           11:2, 12:11, 13:5, 14:8, 15:2, 16:7, 17:15 }

        print()
        print('Testing the Error Message\'s Header\n')

        errorTypeValue = 0  # Variable for the error type value simulated

        # for errorType in self.testErrorType:

        codeValue = 0  # Variable for the code value inside the errorTypeValue simulated
        index = 0
        #errorCodes = Error.ErrorType.get_class(self.listErrorType[index])
        count = 0
        errorTypeValue1 = self.listErrorType.get(index)
        testErrorType = Error.ErrorType

        q = Error.ErrorType.get_class(errorTypeValue1)._member_map_
        iterElem = q.values().__iter__()

        while index < 19:

            if index == 13 and count == 2:
                count = 5  # It will skip from 2-4 in the error message OFPET_TABLE_FEATURES_FAILED
                codeValue = count
            elif index == 18:
                errorTypeValue = 0xffff  # Experimenter error type value
            else:
                errorType = index
                codeValue = count


            elem = iterElem.__next__()

            # Create object with fix values to test the Error Message
            testValue = Error.ErrorMsg(12, errorTypeValue, codeValue, b'00001110010')
            # Error object message to be tested
            # self.testErrorMessage.__init__(12, errorType, elem, b'00001110010')

            testValuePack = testValue.pack()
            # testErrorMessagePack = self.testErrorMessage.pack()

            # print('Testing error message value {} \nversus\nexpected error message value {}\n\n'.format(testValuePack,
            #                                                                                      testErrorMessagePack))

            # Test results
            # self.assertEqual(testValuePack, testErrorMessagePack)

            if count == dictErrorValues.get(index):
                index += 1
                #errorCodes = Error.ErrorType.get_class(self.listErrorType[index])
                errorTypeValue1 = self.listErrorType.get(index)
                q = Error.ErrorType.get_class(errorTypeValue1)._member_map_
                iterElem = q.values().__iter__()
                count = 0
            else:
                count += 1

            # index += 1

        errorTypeValue += 1

    def test_error_experimenter_message(self):
        pass




if __name__ == '__main__':
    unittest.main()