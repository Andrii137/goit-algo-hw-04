def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

def add_contact(args, contacts):
    if len(args) == 2:
        name, phone = args
        contacts[name] = phone
        return 'Contact added.'
    else: 
        return 'Enter name and phone number. Try again.'
    
def change_contact(args, contacts):
    if len(args) == 2:
        name, new_phone = args
        if name in contacts:
            contacts[name] = new_phone
            return 'Contact added.'
        else:
            return 'Contact not found'
        
def show_phone(args, contacts):
    if len(args) == 1:
        name = args[0]
        if name in contacts:
            return contacts[name]
        else:
            return 'Conntact not found'
        
def show_all(contacts):
    if contacts:
        return '\n'.join([f'{name} : {phone}' for name, phone in contacts.items()])
    else: 
        return 'No saved contacts'
        

    
