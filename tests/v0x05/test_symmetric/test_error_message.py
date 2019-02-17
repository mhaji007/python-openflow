"""Testing v0x05 error message class."""
from pyof.v0x05.symmetric.error_message import ErrorMsg
import pyof.v0x05.symmetric.error_message as Error
from tests.test_struct import TestStruct
from pyof.foundation.basic_types import UBInt8,UBInt16,UBInt32,UBInt64,BinaryData
import unittest

class TestErrorMsg(TestStruct):
    """ErroMsg message tests (also those in :class:`.TestDump`)."""

    @classmethod
    def setUpClass(cls):
        """Configure raw file and its object in parent class (TestDump)."""
        super().setUpClass()
        super().set_raw_dump_file('v0x05', 'ofpt_error_msg')
        super().set_raw_dump_object(ErrorMsg, xid=1, error_type=1, code=1)
        super().set_minimum_size(12)



class TestErrorMessageTestCases(unittest.TestCase):

    def setUp(self):
        self.testGenericFailedCode = Error.GenericFailedCode()
        self.testBadActionCode = Error.BadActionCode()
        self.testBadInstructionCode = Error.BadInstructionCode()
        self.testBadMatchCode = Error.BadMatchCode()
        self.testBadRequestCode = Error.BadRequestCode()
        self.testErrorType = Error.ErrorType()
        self.testFlowModFailedCode = Error.FlowModFailedCode()
        self.testGroupModFailedCode = Error.GroupModFailedCode()
        self.testHelloFailedCode = Error.HelloFailedCode()
        self.testMeterModFailedCode = Error.MeterModFailedCode()
        self.testPortModFailedCode = Error.PortModFailedCode()
        self.testQueueOpFailedCode = Error.QueueOpFailedCode()
        self.testRoleRequestFailedCode = Error.RoleRequestFailedCode()
        self.testSwitchConfigFailedCode = Error.SwitchConfigFailedCode()
        self.testTableFeatureFailedCode = Error.TableFeaturesFailedCode()
        self.testTableModFailedCode = Error.TableModFailedCode()
        self.testBadPropertyCode = Error.BadPropertyCode()
        self.testAsyncConfigFailedCode = Error.AsyncConfigFailedCode()
        self.testFlowMonitorFailedCode = Error.FlowMonitorFailedCode()
        self.testBundleFailedCode = Error.BundleFailedCode()
        self.testErrorMessage = Error.ErrorMsg()
        self.testErrorExperimenterMessage = Error.ErrorExperimenterMsg()



    def tearDown(self):
        pass

    def test_generic_failed_codeValue(self):
        pass

    def test_bad_action_codeValue(self):
        pass


    def test_bad_instruction_codeValue(self):
        pass

    def test_bad_match_codeValue(self):
        pass

    def test_bad_request_codeValue(self):
        pass

    def test_error_type(self):
        pass

    def test_flow_mod_failed_codeValue(self):
        pass

    def test_group_mod_failed_codeValue(self):
        pass

    def test_hello_failed_codeValue(self):
        pass

    def test_meter_mod_failed_codeValue(self):
        pass

    def test_port_mod_failed_codeValue(self):
        pass

    def test_queue_op_failed_codeValue(self):
        pass

    def test_role_request_failed_codeValue(self):
        pass

    def test_switch_config_failed_codeValue(self):
        pass

    def test_table_feature_failed_codeValue(self):
        pass

    def test_table_mod_failed_codeValue(self):
        pass

    def test_bad_property_codeValue(self):
        pass

    def test_async_config_failed_codeValue(self):
        pass

    def test_flow_monitor_failed_codeValue(self):
        pass

    def test_bundle_failed_codeValue(self):
        pass

    def test_error_message(self):
        pass

    def test_error_experimenter_message(self):
        pass

