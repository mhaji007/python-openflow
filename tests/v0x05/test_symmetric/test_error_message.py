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
        print('Testing the Generic Failed Codes Value')
        for elem in self.testGenericFailedCode:
            print('Testing values {} versus {}'.format(value, elem))
            self.assertEqual(value, elem)
            value += 1

    def test_bad_action_codeValue(self):
        print()
        print('Testing the Bad Action Codes Value')
        value = 0

        for elem in self.testBadActionCode:
            print('Testing values {} versus {}'.format(value, elem))
            self.assertEqual(value, elem)
            value += 1


    def test_bad_instruction_codeValue(self):
        print()
        print('Testing the Bad Instruction Codes Value')
        value = 0

        for elem in self.testBadInstructionCode:
            print('Testing values {} versus {}'.format(value, elem))
            self.assertEqual(value, elem)
            value += 1

    def test_bad_match_codeValue(self):
        print()
        print('Testing the Bad Match Codes Value')
        value = 0

        for elem in self.testBadMatchCode:
            print('Testing values {} versus {}'.format(value, elem))
            self.assertEqual(value, elem)
            value += 1

    def test_bad_request_codeValue(self):
        print()
        print('Testing the Bad Request Codes Value')
        value = 0

        for elem in self.testBadRequestCode:
            print('Testing values {} versus {}'.format(value, elem))
            self.assertEqual(value, elem)
            value += 1

    def test_error_type(self):
        print()
        print('Testing the Error Types Codes Value')
        value = 0
        temp = 0
        for elem in self.testErrorType:

            if elem == 0xffff:
                temp = value
                value = 0xffff
            print('Testing values {} versus {}'.format(value, elem))
            self.assertEqual(value, elem)
            value += 1
            if elem == 0xffff:
                value = temp + 1

    def test_flow_mod_failed_codeValue(self):
        print()
        print('Testing the Flow Mod Failed Codes Value')
        value = 0

        for elem in self.testFlowModFailedCode:
            print('Testing values {} versus {}'.format(value, elem))
            self.assertEqual(value, elem)
            value += 1

    def test_group_mod_failed_codeValue(self):
        print()
        print('Testing the Group Mod Failed Codes Value')
        value = 0

        for elem in self.testGroupModFailedCode:
            print('Testing values {} versus {}'.format(value, elem))
            self.assertEqual(value, elem)
            value += 1

    def test_hello_failed_codeValue(self):
        print()
        print('Testing the Hello Failed Codes Value')
        value = 0

        for elem in self.testHelloFailedCode:
            print('Testing values {} versus {}'.format(value, elem))
            self.assertEqual(value, elem)
            value += 1

    def test_meter_mod_failed_codeValue(self):
        print()
        print('Testing the Meter Mod Failed Codes Value')
        value = 0

        for elem in self.testMeterModFailedCode:
            print('Testing values {} versus {}'.format(value, elem))
            self.assertEqual(value, elem)
            value += 1

    def test_port_mod_failed_codeValue(self):
        print()
        print('Testing the Port Mod Failed Codes Value')
        value = 0

        for elem in self.testPortModFailedCode:
            print('Testing values {} versus {}'.format(value, elem))
            self.assertEqual(value, elem)
            value += 1

    def test_queue_op_failed_codeValue(self):
        print()
        print('Testing the Queue Op Failed Codes Value')
        value = 0

        for elem in self.testQueueOpFailedCode:
            print('Testing values {} versus {}'.format(value, elem))
            self.assertEqual(value, elem)
            value += 1

    def test_role_request_failed_codeValue(self):
        print()
        print('Testing the Role Request Failed Codes Value')
        value = 0

        for elem in self.testRoleRequestFailedCode:
            print('Testing values {} versus {}'.format(value, elem))
            self.assertEqual(value, elem)
            value += 1

    def test_switch_config_failed_codeValue(self):
        print()
        print('Testing the Switch Config Failed Codes Value')
        value = 0

        for elem in self.testSwitchConfigFailedCode:
            print('Testing values {} versus {}'.format(value, elem))
            self.assertEqual(value, elem)
            value += 1

    def test_table_feature_failed_codeValue(self):
        print()
        print('Testing the Table Feature Failed Codes Value')
        value = 0

        for elem in self.testTableFeatureFailedCode:
            if elem > value:
                value = 5
            print('Testing values {} versus {}'.format(value, elem))
            self.assertEqual(value, elem)
            value += 1




    def test_table_mod_failed_codeValue(self):
        print()
        print('Testing the Table Mod Failed Codes Value')
        value = 0

        for elem in self.testTableModFailedCode:
            print('Testing values {} versus {}'.format(value, elem))
            self.assertEqual(value, elem)
            value += 1

    def test_bad_property_codeValue(self):
        print()
        print('Testing the Bad Property Codes Value')
        value = 0

        for elem in self.testBadPropertyCode:
            print('Testing values {} versus {}'.format(value, elem))
            self.assertEqual(value, elem)
            value += 1

    def test_async_config_failed_codeValue(self):
        print()
        print('Testing the Async Config Failed Codes Value')
        value = 0

        for elem in self.testAsyncConfigFailedCode:
            print('Testing values {} versus {}'.format(value, elem))
            self.assertEqual(value, elem)
            value += 1

    def test_flow_monitor_failed_codeValue(self):
        print()
        print('Testing the Flow Monitor Failed Codes Value')
        value = 0

        for elem in self.testFlowMonitorFailedCode:
            print('Testing values {} versus {}'.format(value, elem))
            self.assertEqual(value, elem)
            value += 1

    def test_bundle_failed_codeValue(self):
        print()
        print('Testing the Bundle Failed Codes Value')
        value = 0

        for elem in self.testBundleFailedCode:
            print('Testing values {} versus {}'.format(value, elem))
            self.assertEqual(value, elem)
            value += 1

    def test_error_message(self):
        print()
        print('Testing the Bundle Failed Codes Value')
        errorTypeValue = 0
        for errorType in self.testErrorType:
            codeValue = 0
            for elem in Error.ErrorType.get_class(errorType):

                if errorTypeValue == 13 and codeValue in range(2,4):
                    codeValue = 5
                elif errorType == 0xffff:
                    errorTypeValue = 0xffff

                testValue = Error.ErrorMsg(12, errorTypeValue, codeValue, b'00001110010')

                self.testErrorMessage.__init__(12, errorType, elem, b'00001110010')

                print('Testing error type values {} and code value {} versus error type value {} and code value {}'.format(errorTypeValue, codeValue,
                                                                                                                            self.testErrorMessage.type,
                                                                                                                            self.testErrorMessage.code))

                self.assertEqual(testValue, self.testErrorMessage)

                codeValue += 1

            errorTypeValue += 1


    def test_error_experimenter_message(self):
        pass




if __name__ == '__main__':
    unittest.main()