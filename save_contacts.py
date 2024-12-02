import csv

def save_contacts(contact_book, filename):

    try:
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Name', 'Email', 'Phone Number', 'Address'])
            for contact in contact_book.contacts:
                writer.writerow([contact.name, contact.email, contact.phone_number, contact.address])
        
        print("Contacts saved successfully!")

    except Exception as e:
        print(f"An error occured while saving cantacts: {e}")