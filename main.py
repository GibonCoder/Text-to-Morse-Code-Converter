from converter import Converter

morse_code_converter = Converter()

message = input("Input message that will be converted into morse code: ")

converted_message = morse_code_converter.text_to_morse_code(message)

print(converted_message)
