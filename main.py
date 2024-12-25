from interface import Interface

interface = Interface()

while True:
    action = int(input("""
            What you want to do?
            1 - Convert text to morse code
            2 - Convert morse code to text
            3 - Import your messages
            0 - Exit program
            
            Action: 
    """))
    interface.choose_action(action)
