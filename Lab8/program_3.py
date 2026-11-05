
books = {
    "B1": {
        "title": "Python Basics",
        "author": "Rao",
        "copies": 2,
        "issued_to": []
    },
    "B2": {
        "title": "Data Structures",
        "author": "Iyer",
        "copies": 1,
        "issued_to": []
    },
    "B3": {
        "title": "Algorithms",
        "author": "Rao",
        "copies": 1,
        "issued_to": []
    }
}
def add_book():

    isbn = input("Enter ISBN: ")

    if isbn in books:
        copies = int(input("Enter additional copies: "))

        if copies <= 0:
            print("Copies must be greater than zero!")
            return

        books[isbn]["copies"] += copies

        print("Copies added successfully!")

    else:
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        copies = int(input("Enter number of copies: "))

        if copies <= 0:
            print("Copies must be greater than zero!")
            return

        books[isbn] = {
            "title": title,
            "author": author,
            "copies": copies,
            "issued_to": []
        }

        print("Book added successfully!")

def issue_book():

    isbn = input("Enter ISBN: ")
    member = input("Enter Member ID: ")

    if isbn not in books:
        print("Book not found!")
        return

    book = books[isbn]
    if book["copies"] <= 0:
        print("Rejected: No copies available!")
        return
    if member in book["issued_to"]:
        print("Rejected: Member already holds this book!")
        return

    count = sum(
        member in b["issued_to"]
        for b in books.values()
    )

    if count >= 2:
        print("Rejected: Member has reached 2-book limit!")
        return

    book["copies"] -= 1
    book["issued_to"].append(member)

    print("Book issued successfully!")
    print("Available copies:", book["copies"])


def return_book():

    isbn = input("Enter ISBN: ")
    member = input("Enter Member ID: ")

    if isbn not in books:
        print("Book not found!")
        return

    book = books[isbn]

    if member not in book["issued_to"]:
        print("Rejected: Member does not hold this book!")
        return

    book["issued_to"].remove(member)
    book["copies"] += 1

    print("Book returned successfully!")
    print("Available copies:", book["copies"])


def search_book():

    isbn = input("Enter ISBN: ")

    if isbn in books:

        book = books[isbn]

        print("\nBook Details:")
        print("ISBN:", isbn)
        print("Title:", book["title"])
        print("Author:", book["author"])
        print("Available Copies:", book["copies"])
        print("Issued To:", book["issued_to"])

    else:
        print("Book not found!")


def reports():

    print("\n===== LIBRARY REPORTS =====")

    # A. Books by a given author
    author = input("Enter author name: ")

    author_books = {
        isbn: book["title"]
        for isbn, book in books.items()
        if book["author"].lower() == author.lower()
    }

    print("\n1. Books by Author:")
    print(author_books)


    member_books = {}

    for isbn, book in books.items():

        for member in book["issued_to"]:

            member_books.setdefault(member, []).append(
                book["title"]
            )

    multiple_books = {
        member: titles
        for member, titles in member_books.items()
        if len(titles) > 1
    }

    print("\n2. Members Holding More Than One Book:")
    print(multiple_books)


    unavailable = {
        isbn: book["title"]
        for isbn, book in books.items()
        if book["copies"] == 0
    }

    print("\n3. Currently Unavailable Books:")
    print(unavailable)


    never_issued = {
        isbn: book["title"]
        for isbn, book in books.items()
        if len(book["issued_to"]) == 0
    }

    print("\n4. Books Never Issued:")
    print(never_issued)


while True:

    print("\n===== LIBRARY RECORD SYSTEM =====")
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Search Book")
    print("5. Reports")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()

    elif choice == "2":
        issue_book()

    elif choice == "3":
        return_book()

    elif choice == "4":
        search_book()

    elif choice == "5":
        reports()

    elif choice == "6":
        print("Exiting Library System...")
        break

    else:
        print("Invalid choice! Try again.")