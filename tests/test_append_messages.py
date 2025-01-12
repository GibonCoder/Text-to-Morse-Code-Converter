import unittest
from src.append_messages import append_messages


class TestAppendMessages(unittest.TestCase):
    def test_mode_1(self):
        print('Test mode 1')
        arr = []
        append_messages('Hello', '.... . .-.. .-.. ---', arr, mode=1)
        expected = [{'Text message: ': 'Hello', 'Code message: ': '.... . .-.. .-.. ---'}]
        self.assertEqual(arr, expected)

    def test_mode_2(self):
        print('Test mode 2')
        arr = []
        append_messages('Hello', '.... . .-.. .-.. ---', arr, mode=2)
        expected = [{'Code message: ': '.... . .-.. .-.. ---', 'Text message: ': 'Hello'}]
        self.assertEqual(arr, expected)

    def test_invalid_mode(self):
        print('Test invalid mode')
        arr = []
        append_messages('Hello', '.... . .-.. .-.. ---', arr, mode=3)
        expected = []
        self.assertEqual(arr, expected)


if __name__ == '__main__':
    unittest.main()
