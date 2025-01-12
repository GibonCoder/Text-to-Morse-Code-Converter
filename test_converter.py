import unittest
from unittest.mock import patch
from converter import Converter


class TestConverter(unittest.TestCase):
    def setUp(self):
        self.converter_1 = Converter()
        self.converter_2 = Converter()

    def tearDown(self):
        pass

    def test_text_to_morse_code(self):
        result_1 = self.converter_1.text_to_morse_code('I am Converter')
        expected_1 = '.. / .- -- / -.-. --- -. ...- . .-. - . .-. '
        result_2 = self.converter_2.text_to_morse_code('I am Converter too')
        expected_2 = '.. / .- -- / -.-. --- -. ...- . .-. - . .-. / - --- --- '

        self.assertEqual(result_1, expected_1)
        self.assertEqual(result_2, expected_2)

    def test_morse_code_to_text(self):
        result_1 = self.converter_1.morse_code_to_text('../.- --/-.-. --- -. ...- . .-. - . .-.')
        expected_1 = 'I AM CONVERTER '
        result_2 = self.converter_2.morse_code_to_text('.. / .- -- / -.-. --- -. ...- . .-. - . .-. / - --- ---')
        expected_2 = 'I AM CONVERTER TOO '

        self.assertEqual(result_1, expected_1)
        self.assertEqual(result_2, expected_2)

    # Test export_messages method
    def test_export_messages_empty(self):
        result = self.converter_1.export_messages()
        expected = False
        self.assertEqual(result, expected)

    def test_export_messages(self):
        self.converter_1.morse_code_to_text('.. / .- -- / -.-. --- -. ...- . .-. - . .-.')
        result = self.converter_1.export_messages()
        expected = True
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
