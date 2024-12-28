from colorama import Fore, Style

from interface import Interface

interface = Interface()

while True:
    try:
        action = int(input(Fore.MAGENTA + """What you want to do?
                1 - Convert text to morse code
                2 - Convert morse code to text (please remember to separate each character with space and each word with /)
                3 - Import your messages
                0 - Exit program
                
                Action: """ + Style.RESET_ALL))
    except ValueError:
        print('Invalid input. Please enter a number.')
    else:
        if not interface.choose_action(action):
            break
