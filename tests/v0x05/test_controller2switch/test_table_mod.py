"""Table flow modification tests."""
import unittest

from pyof.v0x05.common.header import Type
from pyof.v0x05.controller2switch.modify_flow_table_message import TableMod


class TestTableMod(unittest.TestCase):
    """TableMod test."""

    def test_min_size(self):
        """Test minimum message size."""
        self.assertEqual(16, TableMod().get_size())

    def test_header_type(self):
        """Test header type."""
        self.assertEqual(Type.OFPT_TABLE_MOD, TableMod().header.message_type)
