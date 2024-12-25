import pandas as pd


class Converter:
    def __init__(self):
        self._morse_code = pd.read_csv('morse-code.csv', names=['CHARACTER', 'CODE'], header=None)

    def text_to_morse_code(self, text: str) -> str:
        morse_code_message = ''
        for char in text.upper():
            if char == ' ':
                morse_code_message += ' / '
            for index, row in self._morse_code.iterrows():
                if char == row.CHARACTER:
                    morse_code_message += row.CODE + ' '
        return morse_code_message

    def morse_code_to_text(self, code: str) -> str:
        text_message = ''
        if '/' not in code:
            return 'You have to use / in order to separate characters!'
        else:
            code_arr = code.split('/')
            for word in code_arr:
                for char in word:
                    for index, row in self._morse_code.iterrows():
                        if char == row.CODE:
                            text_message += row.CHARACTER + ' '
        return text_message
