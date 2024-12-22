import pandas as pd


class Converter:
    def __init__(self):
        self._morse_code = pd.read_csv('morse-code.csv', names=['CHARACTER', 'CODE'], header=None)

    def convert_text_to_morse_code(self, text: str) -> str:
        morse_code_message = ''
        for char in text.upper():
            if char == ' ':
                morse_code_message += ' / '
            if char not in self._morse_code.CHARACTER:
                morse_code_message += '#'
            for index, row in self._morse_code.iterrows():
                if char == row.CHARACTER:
                    morse_code_message += row.CODE + ' '
        return morse_code_message
