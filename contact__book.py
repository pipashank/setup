from contacts import Contact

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, email, phone_number, address) :
        new_contact = Contact(name, email, phone_number, address)
        self.contacts.append(new_contact)
        print("Contact added successfully")

        