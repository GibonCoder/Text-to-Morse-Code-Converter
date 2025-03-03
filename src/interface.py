from colorama import Fore, Style

from converter import Converter


class Interface:
    def __init__(self):
        self._converter = Converter()

    def choose_action(self, action: int):
        """
        Chooses what to do next

        Parameters:
            action (int): Number that user gives to decide what to do next

        Returns:
            boolean
        """
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
                if self._converter.export_messages():
                    print(Fore.GREEN + "Saved your messages to an external file." + Style.RESET_ALL)
                else:
                    print(Fore.YELLOW + "You haven't converted any message yet. Please convert message first before proceeding to exporting them." + Style.RESET_ALL)
                return True
            case 0:
                print(Fore.CYAN + "Program Finished!" + Style.RESET_ALL)
                return False
            case _:
                print(Fore.YELLOW + "Unrecognized command, please try again." + Style.RESET_ALL)
                return True

    @staticmethod
    def _type_in_message(m_type: str):
        """
        Gives user ability to type in message to convert

        Parameters:
            m_type (str): Type (tet or morse code) to which message will be converted

        Returns:
             input function
        """
        return input(Fore.BLUE + f"Type in message that will be converted into {m_type}: " + Style.RESET_ALL)
