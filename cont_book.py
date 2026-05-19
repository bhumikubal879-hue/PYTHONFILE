contacts = {}

while True:
    print("\n1. Add\n2. View\n3. Search\n4. Delete\n5. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Name: ")
        phone = input("Phone: ")
        contacts[name] = phone

    elif choice == "2":
        for name, phone in contacts.items():
            print(name, ":", phone)

    elif choice == "3":
        name = input("Enter name: ")
        print(contacts.get(name, "Not found"))

    elif choice == "4":
        name = input("Enter name to delete: ")
        contacts.pop(name, None)

    elif choice == "5":
        break