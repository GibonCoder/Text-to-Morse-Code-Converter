import pandas as pd
from save_to_file import save_to_file
from append_messages import append_messages


class Converter:
    def __init__(self):
        self._morse_code = pd.read_csv('morse-code.csv', names=['CHARACTER', 'CODE'], header=None)
        self._msgs_arr = []

    def text_to_morse_code(self, text: str) -> str:
        morse_code_message = ''
        for char in text.upper():
            if char == ' ':
                morse_code_message += ' / '
            for index, row in self._morse_code.iterrows():
                if char == row.CHARACTER:
                    morse_code_message += row.CODE + ' '
        append_messages(text, morse_code_message, self._msgs_arr, 1)
        return morse_code_message

    def morse_code_to_text(self, code: str) -> str:
        text_message = ''
        words_arr = code.split('/')
        letters_arr = [word.split() for word in words_arr]
        for word in letters_arr:
            for char in word:
                for index, row in self._morse_code.iterrows():
                    if char == row.CODE:
                        text_message += row.CHARACTER
            text_message += ' '
        append_messages(text_message, code, self._msgs_arr, 2)
        return text_message

    def export_messages(self):
        save_to_file("messages.txt", self._msgs_arr)
