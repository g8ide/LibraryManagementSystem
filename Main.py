from StudentModule import *
from BookModule import *
from IssueModule import *

while True:
    print("\n===== Library Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Add Book")
    print("4. View Books")
    print("5. Issue Book")
    print("6. View Issued Books")
    print("7. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        add_book()

    elif choice == "4":
        view_books()

    elif choice == "5":
        issue_book()

    elif choice == "6":
        view_issued()

    elif choice == "7":
        break

    else:
        print("Invalid Choice")
