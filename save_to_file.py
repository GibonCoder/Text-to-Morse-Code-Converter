def save_to_file(file_name, msg_arr):
    with open(file_name, 'a+') as f:
        for internal_arr in msg_arr:
            for message in internal_arr:
                f.write(message)
            f.write('\n')
