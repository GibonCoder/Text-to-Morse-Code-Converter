from colorama import Fore, Style

from text_to_morse_code.code.converter import Converter


class Interface:
    def __init__(self):
        self._converter = Converter()

    def choose_action(self, action: int):
        match action:
            case 1:
                msg = self._type_in_message('morse code')
                print(Fore.LIGHTMAGENTA_EX + self._converter.text_to_morse_code(msg) + Style.RESET_ALL)
                return True
            case 2:
                msg = self._type_in_message('text')
                print(Fore.LIGHTMAGENTA_EX + self._converter.morse_code_to_text(msg) + Style.RESET_ALL)
                return True
            case 3:
                self._converter.export_messages()
                print(Fore.GREEN + "Saved your messages to an external file." + Style.RESET_ALL)
                return True
            case 0:
                print(Fore.CYAN + "Program Finished!" + Style.RESET_ALL)
                return False
            case _:
                print(Fore.YELLOW + "Unrecognized command, please try again." + Style.RESET_ALL)
                return True

    @staticmethod
    def _type_in_message(m_type: str):
        return input(Fore.BLUE + f"Type in message that will be converted into {m_type}: " + Style.RESET_ALL)
