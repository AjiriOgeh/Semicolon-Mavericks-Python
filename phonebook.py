phonebook = []


def display_menu():
    phonebook_menu = """Phonebook Menu
1.Add contact
2.Delete contact
3.Edit contact
4.Search contact
5.View existing contacts   
6.Exit"""
    return phonebook_menu


def add_contact_to_phonebook(name, address, phone_number, email):
    contact = {"name": name, "address": address, "number": phone_number, "email": email}
    phonebook.append(contact)
    print()
    return phonebook


def delete_contact_in_phonebook(name):
    for index in range(len(phonebook)):
        if name.casefold() in phonebook[index].values():
            del phonebook[index]
            print(f"{name} has been deleted from your contacts")
            break
    else:
        print(f"{name} is not listed in your contacts")
    print()
    return phonebook


def search_for_contact_in_phonebook(name):
    for index in range(len(phonebook)):
        if name.casefold() in phonebook[index].values():
            for key, value in phonebook[index].items():
                print(key, ": ", value)
            break
    else:
        print(f"{name} is not listed in your contact")
    print()
    return phonebook


def edit_contact_in_phonebook(name):
    for index in range(len(phonebook)):
        if name.casefold() in phonebook[index].values():
            phonebook[index]["name"] = input("Enter a new name: ")
            phonebook[index]["address"] = input("Enter a new address: ")
            phonebook[index]["number"] = input("Enter a new number: ")
            phonebook[index]["email"] = input("Enter a new email: ")
            break
    else:
        print(f"{name} is not listed in your contact")
    print()
    return phonebook


def view_contact_in_phonebook():
    for contact in phonebook:
        for key, value in contact.items():
            print(key, ": ", value)
        print()
    print()
    return phonebook


def return_or_exit_menu():
    print("""1.Go to the main menu
2.Exit""")
    option = input("Select an option: ")
    print()
    if option == "1":
        phonebook_app()
    return phonebook


def phonebook_app():
    print(display_menu())
    option = input("Select an option: ")
    print()
    match option:
        case "1":
            print("Add a contact to your phonebook")
            name = input("Enter a name: ")
            address = input("Enter address: ")
            phone_number = input("Enter phone-number: ")
            email = input("Enter email: ")
            add_contact_to_phonebook(name.casefold(), address, phone_number, email)
            return_or_exit_menu()

        case "2":
            if len(phonebook) > 0:
                print("Delete a contact from your phonebook")
                name = input("Enter a name: ")
                delete_contact_in_phonebook(name)
            else:
                print("No saved contacts")
                print()
            return_or_exit_menu()

        case "3":
            if len(phonebook) > 0:
                print("Edit a contact in your phonebook")
                name = input("Enter a name: ")
                edit_contact_in_phonebook(name)
            else:
                print("No saved contacts")
                print()
            return_or_exit_menu()

        case "4":
            if len(phonebook) > 0:
                print("Search for contact in your phonebook")
                name = input("Enter a name: ")
                search_for_contact_in_phonebook(name)
            else:
                print("No saved contacts")
                print()
            return_or_exit_menu()

        case "5":
            if len(phonebook) > 0:
                print("All the Contacts in your Phonebook: ")
                view_contact_in_phonebook()
            else:
                print("No saved contacts")
                print()
            return_or_exit_menu()


#phonebook_app()



