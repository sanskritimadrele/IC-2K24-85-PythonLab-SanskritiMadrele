students = {
    101: {
        "name": "Asha",
        "marks": {"Math": 88, "Physics": 76, "Chem": 92}
    },
    102: {
        "name": "Ravi",
        "marks": {"Math": 35, "Physics": 58, "Chem": 64}
    },
    103: {
        "name": "Meena",
        "marks": {"Math": 72, "Physics": 81, "Chem": 69}
    }
}


def add_student():
    roll = int(input("Enter roll number: "))

    if roll in students:
        print("Error: Duplicate roll number!")
        return

    name = input("Enter student name: ")
    marks = {}

    n = int(input("Enter number of subjects: "))

    for i in range(n):
        subject = input("Enter subject name: ")
        score = int(input("Enter marks (0-100): "))

        if score < 0 or score > 100:
            print("Invalid marks! Must be between 0 and 100.")
            return

        marks[subject] = score

    students[roll] = {
        "name": name,
        "marks": marks
    }

    print("Student added successfully!")


def update_marks():
    roll = int(input("Enter roll number: "))

    if roll not in students:
        print("Student not found!")
        return

    subject = input("Enter subject name: ")
    score = int(input("Enter new marks: "))

    if score < 0 or score > 100:
        print("Invalid marks! Must be between 0 and 100.")
        return

    students[roll]["marks"][subject] = score

    print("Marks updated successfully!")


def delete_student():
    roll = int(input("Enter roll number: "))

    if roll in students:
        del students[roll]
        print("Student deleted successfully!")
    else:
        print("Student not found!")


def show_student():
    roll = int(input("Enter roll number: "))

    if roll in students:
        print("\nStudent Record")
        print("Name:", students[roll]["name"])
        print("Roll Number:", roll)
        print("Marks:", students[roll]["marks"])
    else:
        print("Student not found!")


def reports():

    if not students:
        print("No student records available!")
        return

    print("\nSTUDENT REPORTS")

    averages = {
        roll: round(
            sum(data["marks"].values()) /
            len(data["marks"]), 2
        )
        for roll, data in students.items()
        if data["marks"]
    }

    print("\n1. Average Marks:")
    for roll, avg in averages.items():
        print(roll, "->", avg)

    if averages:
        topper_roll = max(averages, key=averages.get)
        print("\n2. Topper:",
              students[topper_roll]["name"])

    print("\n3. Highest Scorer in Each Subject:")

    subjects = set(
        subject
        for data in students.values()
        for subject in data["marks"]
    )

    for subject in sorted(subjects):
        scorers = [
            (data["name"], data["marks"][subject])
            for data in students.values()
            if subject in data["marks"]
        ]

        highest = max(scorers, key=lambda x: x[1])
        print(subject, "->", highest[0],
              "(", highest[1], ")")

    print("\n4. Students Below 40:")

    found = False

    for data in students.values():
        low_marks = {
            subject: score
            for subject, score in data["marks"].items()
            if score < 40
        }

        if low_marks:
            found = True
            print(data["name"], "->", low_marks)

    if not found:
        print("No students scored below 40.")

    print("\n5. Grade-wise Grouping:")

    grades = {
        "A": [], "B": [], "C": [],
        "D": [], "F": []
    }

    for roll, avg in averages.items():
        name = students[roll]["name"]

        if avg >= 90:
            grades["A"].append(name)
        elif avg >= 75:
            grades["B"].append(name)
        elif avg >= 60:
            grades["C"].append(name)
        elif avg >= 40:
            grades["D"].append(name)
        else:
            grades["F"].append(name)

    print(grades)


while True:

    print("\n STUDENT DATABASE ")
    print("1. Add Student")
    print("2. Update Subject Marks")
    print("3. Delete Student")
    print("4. Show Student Record")
    print("5. Reports")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        update_marks()

    elif choice == "3":
        delete_student()

    elif choice == "4":
        show_student()

    elif choice == "5":
        reports()

    elif choice == "6":
        print("Exiting Student Database...")
        break

    else:
        print("Invalid choice! Try again.")
