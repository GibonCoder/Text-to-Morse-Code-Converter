def append_messages(txt_msg, code_msg, arr: [], mode: int):
    """
    Appends dictionary consisting of original and converted message to the array

    Parameters:
        txt_msg (str): Message in readable format.
        code_msg (str): Message in morse code format.
        arr (array of dicts): Array consisting of dictionaries.
        mode (int): Decides how message should be saved
    """
    match mode:
        case 1:
            msgs_dict = {'Text message: ': txt_msg, 'Code message: ': code_msg}
            arr.append(msgs_dict)
        case 2:
            msgs_dict = {'Code message: ': code_msg, 'Text message: ': txt_msg}
            arr.append(msgs_dict)
