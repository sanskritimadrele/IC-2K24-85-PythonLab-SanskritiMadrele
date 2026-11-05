
contacts = {
    "Anita": {
        "phones": ["9876543210"],
        "email": "anita@mail.com",
        "city": "Pune"
    },
    "Manoj": {
        "phones": ["9123456780", "9988776655"],
        "email": "manoj@mail.com",
        "city": "Delhi"
    },
    "Zara": {
        "phones": ["9000011111"],
        "email": "zara@mail.com",
        "city": "Pune"
    }
}

def valid_phone(number):
    return len(number) == 10 and number.isdigit()

def number_exists(number, current_name=None):

    for name, data in contacts.items():

        if name != current_name and number in data["phones"]:
            return name

    return None

def add_contact():

    name = input("Enter contact name: ")

    if name in contacts:
        print("Contact already exists!")
        return

    number = input("Enter phone number: ")

    if not valid_phone(number):
        print("Invalid number! Must contain exactly 10 digits.")
        return

    owner = number_exists(number)

    if owner:
        print("Number already belongs to", owner)
        return

    email = input("Enter email: ")
    city = input("Enter city: ")

    contacts[name] = {
        "phones": [number],
        "email": email,
        "city": city
    }

    print("Contact added successfully!")


def add_number():
    name = input("Enter contact name: ")

    if name not in contacts:
        print("Contact not found!")
        return

    number = input("Enter another phone number: ")

    if not valid_phone(number):
        print("Invalid number! Must contain exactly 10 digits.")
        return

    owner = number_exists(number, name)

    if owner:
        print("Number already belongs to", owner)
        return

    if number in contacts[name]["phones"]:
        print("Number already exists for this contact!")
        return

    contacts[name]["phones"].append(number)

    print("Number added successfully!")

def update_contact():
    name = input("Enter contact name: ")

    if name not in contacts:
        print("Contact not found!")
        return

    print("1. Update Email")
    print("2. Update City")

    choice = input("Enter choice: ")

    if choice == "1":
        contacts[name]["email"] = input("Enter new email: ")
        print("Email updated successfully!")

    elif choice == "2":
        contacts[name]["city"] = input("Enter new city: ")
        print("City updated successfully!")

    else:
        print("Invalid choice!")

def delete_contact():
    name = input("Enter contact name: ")

    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!")

    else:
        print("Contact not found!")

def search_contact():
    print("1. Search by Partial Name")
    print("2. Reverse Lookup by Number")

    choice = input("Enter choice: ")

    if choice == "1":

        search_name = input("Enter name to search: ").lower()

        found = False

        for name, data in contacts.items():

            if search_name in name.lower():

                print("\nName:", name)
                print("Phones:", data["phones"])
                print("Email:", data["email"])
                print("City:", data["city"])

                found = True

        if not found:
            print("Contact not found!")

    elif choice == "2":

        number = input("Enter phone number: ")

        reverse_lookup = {
            phone: name
            for name, data in contacts.items()
            for phone in data["phones"]
        }

        if number in reverse_lookup:
            print("Number belongs to:", reverse_lookup[number])

        else:
            print("Number not found!")

    else:
        print("Invalid choice!")

def reports():
    print("\n PHONE DIRECTORY REPORTS ")

    city_groups = {}
    for name, data in contacts.items():

        city = data["city"]

        city_groups.setdefault(city, []).append(name)

    for city in city_groups:
        city_groups[city].sort()

    print("\n1. Contacts Grouped by City:")
    print(city_groups)

    multiple_numbers = {
        name: data["phones"]
        for name, data in contacts.items()
        if len(data["phones"]) > 1
    }
    print("\n2. Contacts with More Than One Number:")
    print(multiple_numbers)

    print("\n3. Complete Directory (Alphabetical):")

    for name in sorted(contacts):
        data = contacts[name]
        print("\nName:", name)
        print("Phones:", data["phones"])
        print("Email:", data["email"])
        print("City:", data["city"])

while True:
    print("\n===== PHONE DIRECTORY =====")
    print("1. Add Contact")
    print("2. Add Another Number")
    print("3. Update Email or City")
    print("4. Delete Contact")
    print("5. Search")
    print("6. Reports")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        add_number()

    elif choice == "3":
        update_contact()

    elif choice == "4":
        delete_contact()

    elif choice == "5":
        search_contact()

    elif choice == "6":
        reports()

    elif choice == "7":
        print("Exiting Phone Directory...")
        break

    else:
        print("Invalid choice! Try again.")
