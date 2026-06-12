issued_books = []

def issue_book():
    sid = input("Student ID: ")
    bid = input("Book ID: ")

    issued_books.append({
        "student": sid,
        "book": bid
    })

    print("Book Issued")

def view_issued():
    for item in issued_books:
        print(item)
