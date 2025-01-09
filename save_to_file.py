import os
from navigate_to_directory import navigate_to_directory
from colorama import Fore, Style


def save_to_file(msg_arr: []):
    """
    Saves file in selected by user directory

    Parameters:
        msg_arr (array of dicts): Array of messages dictionaries
    """
    selected_dir = navigate_to_directory()
    filename = define_file_name()
    filepath = os.path.join(selected_dir, filename)
    try:
        with open(filepath, 'a+') as f:
            for dictionary in msg_arr:
                for key, value in dictionary.items():
                    f.write(f"{key}: {value}\n")
                f.write('\n\n')
    except Exception as e:
        print(Fore.RED + f'Error saving file: {e}' + Style.RESET_ALL)


def define_file_name():
    """
    Gives user ability o give name for the file

    Returns:
        input function
    """
    return input(Fore.BLUE + 'Enter a filename (e.g., output.txt). It can be an existing one, or you can name a fresh new file: ' + Style.RESET_ALL)
