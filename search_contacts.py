def search_contact(contact_book, query):

    results = [contact for contact in contact_book.contacts if query.lower() in contact.name.lower() or query in contact.phone_number]
    if results:
        for contact in results:
            print(f"Name: {contact.name}, Email: {contact.email}, Phone Number: {contact.phone_number}, Address: {contact.address}")
    else:
        print("No matching contacts found.")
        