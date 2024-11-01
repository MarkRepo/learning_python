import unittest
from name_function import get_formatted_name

# 测试函数
class NameTestCase(unittest.TestCase):
    """测试 name_function.py"""
    def test_first_last_name(self):
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')
    
    def test_first_last_middle_name(self):
        formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

unittest.main()

# 测试类