# List to store contacts
contacts = []

# Function to add a contact
def add_contact():
    name = input("Enter name: ").strip() 
    phone = input("Enter phone number: ").strip() 
    email = input("Enter email address: ").strip() 

    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contacts.append(contact)
    print("\nContact added successfully!\n") 

# Function to search for a contact
def search_contact(name):
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            return contact
    return None

# Function to delete a contact
def delete_contact(name):
    contact = search_contact(name) 

    if contact:
        contact.remove(contact)
        print("\nContact deleted successfully!\n")
    else:
        print("\nContact not found.\n")

    # Function to view all contacts
    def view_all():
        if not contacts:
            print("\nNo contacts available.\n")
            return
        print("\n========== CONTACT LIST ==========") 

        for index, contact in enumerate(contacts, start=1):
            print(f"\nContact {index}")
            print(f"Name : {contact['name']}") 
            print(f"Phone: {contact['phone']}") 
            print(f"Email: {contact['email']}") 

        print("===================================\n") 

# Main menu loop
while True:
    print("===== CONTACT BOOK =====")
    print("1. Add Contact") 
    print("2. Search Contact") 
    print("3. Delete Contact") 
    print("4. View All Contacts")
    print("5. Exit") 

    choice = input("Choose an option (1-5): ") 

    if choice == "1":
        add_contact() 

    elif choice == "2":
        name = input("Enter the contact name to search: ") 
        result = search_contact(name) 

        if result: 
            print("\nContact Found:")
            print(f"Name : {result['name']}") 
            print(f"Phone: {result['phone']}") 
            print(f"Email: {result['email']}\n")
        else:
            print("\nContact not Found.\n")

    elif choice == "3":
        name = input("Enter the contact name to delete: ")
        delete_contact(name) 

    elif choice == "4": 
        view_all: any
        view_all()

    elif choice =="5":
        print("\nThank you for using Contact Book. Goodbye!")
        break

    else:
        print("\nInvalid choice. Please select a number between 1 and 5.\n")



