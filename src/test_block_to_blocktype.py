import unittest
from blocktype import BlockType
from blocktoblocktype import block_to_block_type

class TestBlockToBlockType(unittest.TestCase):
    def test_UNORDERED_LIST_block(self):
        expected_blocktype = BlockType.UNORDERED_LIST
        block = "- This is a list\n- with items"
        block_type = block_to_block_type(block)
        self.assertEqual(expected_blocktype, block_type)
    
    def test_HEADING_block(self):
        expected_blocktype = BlockType.HEADING
        block = "### Hello everyone"
        block_type = block_to_block_type(block)
        self.assertEqual(expected_blocktype, block_type)
    
    def test_one_heading_block_with_hashtags(self):
        expected_blocktype = BlockType.HEADING
        block = "# ## Hello everyone"
        block_type = block_to_block_type(block)
        self.assertEqual(expected_blocktype, block_type)
    
    def test_broken_heading(self):
        expected_blocktype = BlockType.PARAGRAPH
        block = " # # # Hello everyone"
        block_type = block_to_block_type(block)
        self.assertEqual(expected_blocktype, block_type)
    
    def test_not_allowed_seven_headings(self):
        expected_blocktype = BlockType.PARAGRAPH
        block = "####### Hello everyone"
        block_type = block_to_block_type(block)
        self.assertEqual(expected_blocktype, block_type)
    
    def test_ordered_list(self):
        expected_blocktype = BlockType.ORDERED_LIST
        block = "1. Hello\n2. What are you doing"
        block_type = block_to_block_type(block)
        self.assertEqual(expected_blocktype, block_type)
    
    def test_quotes(self):
        expected_blocktype = BlockType.QUOTE
        block = "> Hello\n>What are you doing\n>Someone"
        block_type = block_to_block_type(block)
        self.assertEqual(expected_blocktype, block_type)
    
    def test_code_block(self):
        expected_blocktype = BlockType.CODE
        block = "```\n1. Hello\n2. What are you doing```"
        block_type = block_to_block_type(block)
        self.assertEqual(expected_blocktype, block_type)
    
    def test_broken_code_block(self):
        expected_blocktype = BlockType.PARAGRAPH
        block = "```\n1. Hello\n2. What are you doing``"
        block_type = block_to_block_type(block)
        self.assertEqual(expected_blocktype, block_type)
    
    def test_multiple_blocks(self):
        expected_blocktype = BlockType.HEADING
        block = "### ```\n1. Hello\n2. What are you doing```"
        block_type = block_to_block_type(block)
        self.assertEqual(expected_blocktype, block_type)
