def append_messages(txt_msg, code_msg, arr: [], mode: int):
    match mode:
        case 1:
            msgs_dict = {'Text message: ': txt_msg, 'Code message: ': code_msg}
            arr.append(msgs_dict)
        case 2:
            msgs_dict = {'Code message: ': code_msg, 'Text message: ': txt_msg}
            arr.append(msgs_dict)
