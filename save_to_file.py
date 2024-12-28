import os
from navigate_to_directory import navigate_to_directory


def save_to_file(msg_arr):
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
        print(f'Error saving file: {e}')


def define_file_name():
    return input('Enter a filename (e.g., output.txt): ')
