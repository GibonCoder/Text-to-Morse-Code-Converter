import os


def navigate_to_directory(start_path='.'):
    print('Please select directory where you would like to save the file.')
    current_path = os.path.abspath(start_path)

    while True:
        print(f'\nCurrent Directory: {current_path}')
        print('Select an option:')

        # List directories and files
        items = os.listdir(current_path)
        directories = [d for d in items if os.path.isdir(os.path.join(current_path, d))]

        for i, directory in enumerate(directories, start=1):
            print('0: Select this directory')
            print('-1: Go up one level')
            print('Position of a specific directory inside current directory: to the subdirectory')

            try:
                choice = int(input('\nEnter your choice: '))
                if choice == 0:
                    return current_path
                elif choice == -1:
                    parent_path = os.path.dirname(current_path)
                    if parent_path == current_path:
                        print('You are already in the root directory.')
                    else:
                        current_path = parent_path
                elif 1 <= choice <= len(directories):
                    current_path = os.path.join(current_path, directories[choice - 1])
                else:
                    print('Invalid choice. Please try again.')
            except ValueError:
                print('Invalid input. Please enter a number.')
