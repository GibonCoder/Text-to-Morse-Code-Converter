from colorama import Fore, Style

from interface import Interface

interface = Interface()

while True:
    action = int(input(Fore.MAGENTA + """What you want to do?
            1 - Convert text to morse code
            2 - Convert morse code to text (please remember to separate each character with space and each word with /)
            3 - Import your messages
            0 - Exit program
            
            Action: """ + Style.RESET_ALL))
    if not interface.choose_action(action):
        break
