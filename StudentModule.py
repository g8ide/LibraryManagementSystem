students = []

def add_student():
    sid = input("Enter Student ID: ")
    name = input("Enter Student Name: ")

    students.append({
        "id": sid,
        "name": name
    })

    print("Student Added Successfully")

def view_students():
    for s in students:
        print(s)
