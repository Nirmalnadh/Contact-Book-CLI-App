import csv
from contact import Contact

FILENAME = 'contacts.csv'

def save_contacts(contacts):
    with open(FILENAME, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['id', 'name', 'phone', 'email'])  # Header
        for contact in contacts:
            writer.writerow([contact.id, contact.name, contact.phone, contact.email])

def load_contacts():
    contacts = []
    try:
        with open(FILENAME, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                contact = Contact(
                    id=row['id'],
                    name=row['name'],
                    phone=row['phone'],
                    email=row['email']
                )
                contacts.append(contact)
    except FileNotFoundError:
        pass
    return contacts
