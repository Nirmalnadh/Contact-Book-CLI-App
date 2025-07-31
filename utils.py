import uuid
from contact import Contact

def create_contact(name, phone, email):
    contact_id = str(uuid.uuid4())[:8]
    return Contact(contact_id, name, phone, email)

def find_contact(contacts, contact_id):
    for contact in contacts:
        if contact.id == contact_id:
            return contact
    return None

def print_contacts(contacts):
    if not contacts:
        print("📭 No contacts found.")
    for contact in contacts:
        print(f"[👤] {contact.name} (ID: {contact.id}) - 📞 {contact.phone} - ✉️ {contact.email}")

def get_contact_by_name(contacts, name):
    for contact in contacts:
        if contact.name.lower() == name.lower():
            return contact
    return None
