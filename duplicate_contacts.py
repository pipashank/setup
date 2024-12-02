def check_duplicates(contact_book):

    seen_names = set()
    seen_numbers = set()
    duplicates = []

    for contacts in contact_book.contacts:
        if contact.name in seen_names or contact.phone_number in seen_numbers:
            duplicates.append(contact)
        seen_names.add(contact.name)
        seen_numbers.add(contact.phone_number)

    if  duplicates: 
        print("Duplicate contact found: ")
        for contact in duplicates:
            print(f"Name: {contact.name}, Phone Number: {contact.phone_number}")
    else:
        print("No duplicate contact found. ")

    
    
    