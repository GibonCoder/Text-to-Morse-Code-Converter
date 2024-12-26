from converter import Converter


class Interface:
    def __init__(self):
        self._converter = Converter()

    def choose_action(self, action: int):
        match action:
            case 1:
                msg = self._type_in_message('morse code')
                print(self._converter.text_to_morse_code(msg))
                return True
            case 2:
                msg = self._type_in_message('text')
                print(self._converter.morse_code_to_text(msg))
                return True
            case 3:
                print("Save your messages to an external file.")
                return True
            case 0:
                print("Program Finished!")
                return False
            case _:
                print("Unrecognized command, please try again.")

    @staticmethod
    def _type_in_message(m_type: str):
        return input(f"Type in message that will be converted into {m_type}: ")
