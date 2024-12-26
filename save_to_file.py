def save_to_file(file_name, msg_arr):
    with open(file_name, 'a+') as f:
        for dictionary in msg_arr:
            for key, value in dictionary.items():
                f.write(f"{key}: {value}\n")
            f.write('\n\n')
