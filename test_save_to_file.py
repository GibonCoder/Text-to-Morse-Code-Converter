import unittest
from unittest.mock import patch, mock_open

from save_to_file import save_to_file, define_file_name


class TestSaveToFile(unittest.TestCase):
    @patch('save_to_file.navigate_to_directory', return_value='/mocked/directory')
    @patch('save_to_file.define_file_name', return_value='output.txt')
    @patch('builtins.open', new_callable=mock_open)
    def test_save_to_file_success(self,
                                  mock_open_func,
                                  mock_define_file_name,
                                  mock_navigate_to_directory):
        # Mock input data
        test_msg_arr = [{'Text message: ': 'Hello', 'Code message: ': '.... . .-.. .-.. ---'}]

        save_to_file(test_msg_arr)

        # Verify file operations
        mock_open_func.asser_called_once_with('/mocked/directory/output.txt', 'a+')
        handle = mock_open_func()
        handle.write.assert_any_call('Text message: Hello\n')
        handle.write.assert_any_call('Code message: .... . .-.. .-.. ---\n')
        handle.write.assert_any_call('\n\n')

        @patch('text_to_morse_code.save_to_file.navigate_to_directory', return_value='/mocked/directory')
        @patch('text_to_morse_code.save_to_file.define_file_name', return_value='output.txt')
        @patch('builtins.open', side_effect=Exception("Mocked exception"))
        def test_save_to_file_exception(self,
                                        mock_open_func,
                                        mock_define_file_name,
                                        mock_navigate_to_directory):
            # Mock input data
            test_msg_arr = [{'Text message: ': 'Hello', 'Code message: ': '.... . .-.. .-.. ---'}]

            # Call the function and ensure no exceptions propagate
            with self.assertLogs() as log:
                save_to_file(test_msg_arr)
                self.assertIn('Error saving file', log.output[0])

    @patch('builtins.input', return_value='test.txt')
    def test_define_file_name(self, mock_input):
        result = define_file_name()
        self.assertEqual(result, 'test.txt')
        mock_input.assert_called_once_with('\033[34mEnter a filename (e.g., output.txt). It can be an existing one, or you can name a fresh new file: \033[0m')


