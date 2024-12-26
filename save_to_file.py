def save_to_file(msg_arr):
    file_name = "messages.txt"
    with open(file_name, 'a+') as f:
        for internal_arr in msg_arr:
            for message in internal_arr:
                f.write(message)
            f.write('\n')
