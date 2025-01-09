import os
from colorama import Fore, Style


def navigate_to_directory(start_path='.'):
    """
    Allows user to navigate to desired directory

    Parameters:
        start_path ('.'): Current directory

    Returns:
        current_path: Directory that file will be saved in
    """
    print(Fore.CYAN + 'Select directory where you would like to save the file.' + Style.RESET_ALL)
    current_path = os.path.abspath(start_path)

    while True:
        print(Fore.CYAN + f'\nCurrent Directory: {current_path}' + Style.RESET_ALL)
        print(Fore.BLUE + 'Select an option:' + Style.RESET_ALL)

        # List directories and files
        items = os.listdir(current_path)
        directories = [d for d in items if os.path.isdir(os.path.join(current_path, d))]

        for i, directory in enumerate(directories, start=1):
            print(Fore.LIGHTMAGENTA_EX + f'{i}. {directory}' + Style.RESET_ALL)
        print(Fore.CYAN + '0: Select this directory' + Style.RESET_ALL)
        print(Fore.CYAN + '-1: Go up one level' + Style.RESET_ALL)
        print(Fore.CYAN + 'Position of a specific directory inside current directory: to the subdirectory' + Style.RESET_ALL)

        try:
            choice = int(input(Fore.BLUE + '\nEnter your choice: ' + Style.RESET_ALL))
            if choice == 0:
                return current_path
            elif choice == -1:
                parent_path = os.path.dirname(current_path)
                if parent_path == current_path:
                    print(Fore.CYAN + 'You are already in the root directory.' + Style.RESET_ALL)
                else:
                    current_path = parent_path
            elif 1 <= choice <= len(directories):
                current_path = os.path.join(current_path, directories[choice - 1])
            else:
                print(Fore.YELLOW + 'Invalid choice. Please try again.' + Style.RESET_ALL)
        except ValueError:
            print(Fore.RED + 'Invalid input. Please enter a number.' + Style.RESET_ALL)
