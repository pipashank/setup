from fileinput import filename

from contact__book import ContactBook
from view_all_contacts import view_all_contacts
from remove_contacts import remove_contact
from save_contacts import save_contacts
from load_contacts import load_contacts
from search_contacts import search_contact
from duplicate_contacts import check_duplicates

def main():
    contact_book = ContactBook()

    while True:
        print("Contact Book Management System")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Save Contacts to CSV File")
        print("4. Load Contacts from CSV File")
        print("5. Remove Contact")
        print("6. Search Contact")
        print("7. Check Duplicates")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1" :
            name = input("Enter name: ")
            email = input("Enter email: ")
            phone_number = input("Enter phone number: ")
            address = input("Enter address: ")
            contact_book.add_contact(name, email, phone_number, address)
        elif choice == "2" :
            view_all_contacts(contact_book)
        elif choice == "3" :
            filename = input("Enter CSV filename to save contacts:  ")
            save_contacts(contact_book, filename)
        elif choice == "4" :
            filename = input("Enter CSV filename to load contacts: ")
            load_contacts(contact_book, filename)
        elif choice == "5" :
            remove_contact(contact_book)
        elif choice == "6" :
            query = input("Enter name or phone number to search: ")
            search_contact(contact_book, query)
        elif choice == "7" :
            check_duplicates(contact_book)
        elif choice == "8" :
            print("Thank You For Using Contact Book Management")
            break
        else:
            print("Invalid choice. Pleease re-do the work")
if __name__ =="__main__":
    main()
        




