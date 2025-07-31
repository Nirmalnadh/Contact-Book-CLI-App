import sys
from contact import Contact
from storage import load_contacts, save_contacts
from utils import print_contacts, get_contact_by_name

def main():
    contacts = load_contacts()
    
    if len(sys.argv) < 2:
        print("Usage: python app.py [add|list|search|edit|delete] [args]")
        return

    command = sys.argv[1].lower()

    if command == "add":
        if len(sys.argv) < 5:
            print("Usage: python app.py add <name> <phone> <email>")
            return
        name = sys.argv[2]
        phone = sys.argv[3]
        email = sys.argv[4]
        contact = Contact(name, phone, email)
        contacts.append(contact)
        save_contacts(contacts)
        print("✅ Contact added!")

    elif command == "list":
        print_contacts(contacts)

    elif command == "search":
        if len(sys.argv) < 3:
            print("Usage: python app.py search <name>")
            return
        name = sys.argv[2]
        contact = get_contact_by_name(contacts, name)
        if contact:
            print(contact)
        else:
            print("❌ Contact not found.")

    elif command == "edit":
        if len(sys.argv) < 5:
            print("Usage: python app.py edit <name> <new_phone> <new_email>")
            return
        name = sys.argv[2]
        new_phone = sys.argv[3]
        new_email = sys.argv[4]
        contact = get_contact_by_name(contacts, name)
        if contact:
            contact.phone = new_phone
            contact.email = new_email
            save_contacts(contacts)
            print("✅ Contact updated!")
        else:
            print("❌ Contact not found.")

    elif command == "delete":
        if len(sys.argv) < 3:
            print("Usage: python app.py delete <name>")
            return
        name = sys.argv[2]
        contact = get_contact_by_name(contacts, name)
        if contact:
            contacts.remove(contact)
            save_contacts(contacts)
            print("🗑️ Contact deleted.")
        else:
            print("❌ Contact not found.")

    else:
        print("❌ Unknown command.")

if __name__ == "__main__":
    main()
