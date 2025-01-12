import unittest
from src.interface import Interface


class TestInterface(unittest.TestCase):
    def setUp(self):
        self.interface = Interface()

    def test_choose_action(self):
        self.assertTrue(self.interface.choose_action(1))
        self.assertTrue(self.interface.choose_action(2))
        self.assertTrue(self.interface.choose_action(3))
        self.assertFalse(self.interface.choose_action(0))
        self.assertTrue(self.interface.choose_action(4))

    def test_type_in_message(self):
        self.assertEqual(self.interface._type_in_message('morse code'), 'test')
        self.assertEqual(self.interface._type_in_message('text'), '- . ... -')


if __name__ == '__main__':
    unittest.main()
