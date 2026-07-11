library = []
def menu():
    print("========== LIBRARY MANAGEMENT ==========")
    print("1. Add Book")
    print("2. Show Books ")
    print("3. Search Book ")
    print("4. Borrow Book ")
    print("5. Return Book ")
    print("6. Delete Book ")
    print("7. Exit ")

def add_book():
    Book_name = input("Enter book name: ")
    Author_name = input("Enter Author name: ")
    Book_id = int(input("Emter Book Id No.: "))
    Status = "Available"
    library.append([Book_name, Author_name, Book_id, Status])
    print("Book Added Successfully")

def show_book():
    if len(library) == 0:
        print("No Book avilable.")
        return
    print("\n Book name  \t\t Author Name \t Book Id \t Status")
    print("="*49)
    for i in library:
        print(f"{i[0]} \t\t {i[1]} \t {i[2]} \t {i[3]}")

def search_book():
    sbook = input("Enter book name: ")
    found = False

    for l in library:
        if sbook == l[0]:
            print("\n ====== Book Details ======")
            print(f"Book Name :   {l[0]}")
            print(f"Author Name  :   {l[1]}")
            print(f"Book ID  :   {l[2]}")
            print(f"Status  :   {l[3]}")
            found = True
            break
    if not found :
        print("Book not found")

def delete_book():
    dname = input("Enter Book name: ")
    found = False
    for s in library:
        if dname == s[0]:
            library.remove(s)
            print("Book is removed from Library")
            found = True
            break
    if not found:
        print("Book not found in Library")

def borrow_book():
    bbook = input("Enter book name: ")
    found = False
    for j in library:
        if bbook == j[0]:
            if j[3] == "Available":
                j[3] = "Borrowed"
                print("Book borrowed Susseccfull.")
            else:
                print("Book is already borrowed")
            found = True
            break
    if not found:
        print("Book is found.")

def return_book():
    rbook = input("Enter book name")
    found = False
    for j in library:
        if rbook == j[0] :
            if j[3] == "Borrowed":
                j[3] = "Available"
                print("Your Book returned.")
            else: 
                print("Book is already available")
            found = True
            break     
    if not found:
        print("Book is not found.")

while True:
    menu()
    choice = int(input("Enter your choice: "))
    if choice == 1:
        add_book()
    elif choice == 2:
        show_book()
    elif choice == 3:
        search_book()
    elif choice == 4:
        borrow_book()
    elif choice == 5:
        return_book()
    elif choice == 6:
        delete_book()
    elif choice == 7:
        print("Thanks for visiting to aur Library management system")
        break
    else:
        print("Invalid choice.")
