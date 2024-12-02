import csv
from contacts import Contact

def load_contacts(contact_book, filename):

    try:
        with open(filename, mode='r') as file:
            reader= csv.reader(file)
            next(reader)
            contact_book.contacts = [Contact(*row) for row in reader]
        print("Conatacts loaded successfully!")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occured while loading: {e}")
        