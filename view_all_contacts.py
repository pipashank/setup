def view_all_contacts(contact_book):
    if not contact_book.contacts:
        print("No contacts found.")
    else:
        print(f"{"Name" :<5} {"Email" :<7} {"Phone_Number" :<26} {"Address" :<30}")
        print("-" * 68)
        for contact in contact_book.contacts:
            print(f"{contact.name:<5} {contact.email:<7} {contact.phone_number:<26} {contact.address:<30}" )