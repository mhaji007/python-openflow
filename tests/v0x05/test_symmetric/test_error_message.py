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



    def tearDown(self):
        pass

    def test_generic_failed_codeValue(self):
        value = 0
        print()
        print('Testing the Generic Failed Codes Values')
        for elem in self.testGenericFailedCode:
            print('Testing code value {} versus code value{}'.format(value, elem))
            self.assertEqual(value, elem)
            value += 1

    def test_bad_action_codeValue(self):
        print()
        print('Testing the Bad Action Codes Values')
        value = 0

        for elem in self.testBadActionCode:
            print('Testing code value {} versus code value {}'.format(value, elem))
            self.assertEqual(value, elem)
            value += 1


    def test_bad_instruction_codeValue(self):
        print()
        print('Testing the Bad Instruction Codes Values')
        value = 0

        for elem in self.testBadInstructionCode:
            print('Testing code value {} versus code value {}'.format(value, elem))
            self.assertEqual(value, elem)
            value += 1

    def test_bad_match_codeValue(self):
        print()
        print('Testing the Bad Match Codes Values')
        value = 0

        for elem in self.testBadMatchCode:
            print('Testing code value {} versus code value {}'.format(value, elem))
            self.assertEqual(value, elem)
            value += 1

    def test_bad_request_codeValue(self):
        print()
        print('Testing the Bad Request Codes Values')
        value = 0

        for elem in self.testBadRequestCode:
            print('Testing code value {} versus code value {}'.format(value, elem))
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
            print('Testing code value {} versus code value {}'.format(value, elem))
            self.assertEqual(value, elem)
            value += 1


    def test_flow_mod_failed_codeValue(self):
        print()
        print('Testing the Flow Mod Failed Codes Values')
        value = 0

        for elem in self.testFlowModFailedCode:
            print('Testing code value {} versus code value {}'.format(value, elem))
            self.assertEqual(value, elem)
            value += 1

    def test_group_mod_failed_codeValue(self):
        print()
        print('Testing the Group Mod Failed Codes Values')
        value = 0

        for elem in self.testGroupModFailedCode:
            print('Testing code value {} versus code value {}'.format(value, elem))
            self.assertEqual(value, elem)
            value += 1

    def test_hello_failed_codeValue(self):
        print()
        print('Testing the Hello Failed Codes Values')
        value = 0

        for elem in self.testHelloFailedCode:
            print('Testing code value {} versus code value {}'.format(value, elem))
            self.assertEqual(value, elem)
            value += 1

    def test_meter_mod_failed_codeValue(self):
        print()
        print('Testing the Meter Mod Failed Codes Values')
        value = 0

        for elem in self.testMeterModFailedCode:
            print('Testing code value {} versus code value {}'.format(value, elem))
            self.assertEqual(value, elem)
            value += 1

    def test_port_mod_failed_codeValue(self):
        print()
        print('Testing the Port Mod Failed Codes Values')
        value = 0

        for elem in self.testPortModFailedCode:
            print('Testing code value {} versus code value{}'.format(value, elem))
            self.assertEqual(value, elem)
            value += 1

    def test_queue_op_failed_codeValue(self):
        print()
        print('Testing the Queue Op Failed Codes Values')
        value = 0

        for elem in self.testQueueOpFailedCode:
            print('Testing code value {} versus code value {}'.format(value, elem))
            self.assertEqual(value, elem)
            value += 1

    def test_role_request_failed_codeValue(self):
        print()
        print('Testing the Role Request Failed Codes Values')
        value = 0

        for elem in self.testRoleRequestFailedCode:
            print('Testing code value {} versus code value {}'.format(value, elem))
            self.assertEqual(value, elem)
            value += 1

    def test_switch_config_failed_codeValue(self):
        print()
        print('Testing the Switch Config Failed Codes Values')
        value = 0

        for elem in self.testSwitchConfigFailedCode:
            print('Testing code value {} versus code value {}'.format(value, elem))
            self.assertEqual(value, elem)
            value += 1

    def test_table_feature_failed_codeValue(self):
        print()
        print('Testing the Table Feature Failed Codes Values')
        value = 0

        for elem in self.testTableFeatureFailedCode:
            if elem > value:
                value = 5
            print('Testing code value {} versus code value {}'.format(value, elem))
            self.assertEqual(value, elem)
            value += 1




    def test_table_mod_failed_codeValue(self):
        print()
        print('Testing the Table Mod Failed Codes Values')
        value = 0

        for elem in self.testTableModFailedCode:
            print('Testing code value {} versus code value {}'.format(value, elem))
            self.assertEqual(value, elem)
            value += 1

    def test_bad_property_codeValue(self):
        print()
        print('Testing the Bad Property Codes Values')
        value = 0

        for elem in self.testBadPropertyCode:
            print('Testing code value {} versus code value {}'.format(value, elem))
            self.assertEqual(value, elem)
            value += 1

    def test_async_config_failed_codeValue(self):
        print()
        print('Testing the Async Config Failed Codes Values')
        value = 0

        for elem in self.testAsyncConfigFailedCode:
            print('Testing code value {} versus code value {}'.format(value, elem))
            self.assertEqual(value, elem)
            value += 1

    def test_flow_monitor_failed_codeValue(self):
        print()
        print('Testing the Flow Monitor Failed Codes Values')
        value = 0

        for elem in self.testFlowMonitorFailedCode:
            print('Testing code value {} versus code value {}'.format(value, elem))
            self.assertEqual(value, elem)
            value += 1

    def test_bundle_failed_codeValue(self):
        print()
        print('Testing the Bundle Failed Codes Values')
        value = 0

        for elem in self.testBundleFailedCode:
            print('Testing code value {} versus code value {}'.format(value, elem))
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

                print('Testing error type values {} and code value {} versus '
                      'error type value {} and code value {}'.format(errorTypeValue, codeValue,
                                                                     self.testErrorMessage.type,
                                                                     self.testErrorMessage.code))

                # Test results
                self.assertEqual(testValue, self.testErrorMessage)

                codeValue += 1

            errorTypeValue += 1

    def test_error_message_header(self):
        pass

    def test_error_experimenter_message(self):
        pass




if __name__ == '__main__':
    unittest.main()