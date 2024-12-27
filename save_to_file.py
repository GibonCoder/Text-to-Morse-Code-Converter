def save_to_file( msg_arr):
    directory = select_directory()
    with open(directory, 'a+') as f:
        for dictionary in msg_arr:
            for key, value in dictionary.items():
                f.write(f"{key}: {value}\n")
            f.write('\n\n')


def select_directory():
    print("Please select your directory where you would like to save the file. Also at thendt of provided directory specify file name. Otherwise. file localisation and its name "
          "will be default")
    direct = input("Provide directory to save file: ")
    return direct

#TODO: work on select_directory function to d desired directory instead of typing it in
