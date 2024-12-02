def remove_contact(contact_book):

    name = input("Enter the name of the contact to remove: ")
    for contact in contact_book.contacts:
        if contact.name == name:
            contact_book.contacts.remove(contact)
            print("Contact removed successfully!")
            return
    print("Contact not found.")
            