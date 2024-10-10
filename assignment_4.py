def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name.capitalize()] = phone
    return "Contact added."

def change_contact(args, contacts: dict):
    name, phone = args
    if name.capitalize() not in contacts:
        return "Name not found in contacts"
    else:
        contacts.update({name.capitalize(): phone})
    return "Contact update"

def show_phone(args, contacts: dict):
    name = args[0]
    name = name.capitalize()
    return f"{name} not found in contacts " if name not in contacts else contacts[name]

def show_all(contacts: dict):
    result = []
    for key, value in contacts.items():
        result.append(f"Name: {key.capitalize()} phone: {value}")
    return "\n".join(result)

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        try:
            if command in ["close", "exit"]:
                print("Good bye!")
                break
            elif command == "hello":
                print("How can I help you?")
            elif command == "add":
                print(add_contact(args, contacts))
            elif command == "change":
                print(change_contact(args, contacts))
            elif command == "phone":
                print(show_phone(args ,contacts))
            elif command == "all":
                print(show_all(contacts))
            else:
                print("Invalid command.")
        except ValueError:
            print("Error")

if __name__ == "__main__":
    main()
