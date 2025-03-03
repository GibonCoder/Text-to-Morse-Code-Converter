from colorama import Fore, Style

from interface import Interface

interface = Interface()

while True:
    try:
        action = int(input(Fore.CYAN + """What you want to do?
                1 - Convert text to Morse code
                2 - Convert Morse code to text (please remember to separate each character with space and each word with /)
                3 - Export your messages
                0 - Exit program
                
                Action: """ + Style.RESET_ALL))
    except ValueError:
        print(Fore.RED + 'Invalid input. Please enter a number.' + Style.RESET_ALL)
    else:
        if not interface.choose_action(action):
            break
