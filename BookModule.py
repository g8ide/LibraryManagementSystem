books = []

def add_book():
    bid = input("Book ID: ")
    title = input("Book Title: ")

    books.append({
        "id": bid,
        "title": title
    })

    print("Book Added")

def view_books():
    for b in books:
        print(b)
