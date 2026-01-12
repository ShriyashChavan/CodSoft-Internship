# Simple Contact Management System

contacts = []   # List to store all contacts


def add_contact():
    print("\n--- Add New Contact ---")
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }

    contacts.append(contact)
    print("Contact added successfully!\n")


def show_contacts():
    print("\n--- Contact List ---")

    if len(contacts) == 0:
        print("No contacts available.\n")
        return

    for i in range(len(contacts)):
        print(i + 1, ".", contacts[i]["name"], "-", contacts[i]["phone"])

    print()


def search_contact():
    print("\n--- Search Contact ---")
    search = input("Enter name or phone number: ")

    found = False
    for contact in contacts:
        if search.lower() in contact["name"].lower() or search == contact["phone"]:
            print("\nContact Found")
            print("Name:", contact["name"])
            print("Phone:", contact["phone"])
            print("Email:", contact["email"])
            print("Address:", contact["address"])
            found = True

    if not found:
        print("Contact not found.\n")


def update_contact():
    print("\n--- Update Contact ---")
    phone = input("Enter phone number to update: ")

    for contact in contacts:
        if contact["phone"] == phone:
            new_name = input("Enter new name (press enter to skip): ")
            new_email = input("Enter new email (press enter to skip): ")
            new_address = input("Enter new address (press enter to skip): ")

            if new_name != "":
                contact["name"] = new_name
            if new_email != "":
                contact["email"] = new_email
            if new_address != "":
                contact["address"] = new_address

            print("Contact updated successfully!\n")
            return

    print("Contact not found.\n")


def delete_contact():
    print("\n--- Delete Contact ---")
    phone = input("Enter phone number to delete: ")

    for contact in contacts:
        if contact["phone"] == phone:
            contacts.remove(contact)
            print("Contact deleted successfully!\n")
            return

    print("Contact not found.\n")


def main_menu():
    while True:
        print("===== Contact Management System =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            show_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Thank you! Program closed.")
            break
        else:
            print("Invalid choice. Try again.\n")


main_menu()

contact_management_system