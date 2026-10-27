import csv
from uuid import uuid4

books = []
members = []


# load data
def open_file():

    try:
        with open("book_info.csv", "r") as book_file:
            lines = csv.DictReader(book_file)
            for line in lines:
                books.append(line)
    except FileNotFoundError as e:
        raise FileNotFoundError("file not found!")


open_file()


def open_member_file():

    try:
        with open("member_info.csv", "r") as member_file:
            lines = csv.DictReader(member_file)
            for line in lines:
                members.append(line)
    except FileNotFoundError as e:
        raise FileNotFoundError("file not found!")


open_member_file()


# save data
def save_file():

    try:
        with open("book_info.csv", "w", newline="") as book_file:
            fields_name = ["id", "title", "author", "year", "category", "status", "borrowed_by"]

            new_content = csv.DictWriter(book_file, fields_name)

            new_content.writeheader()
            new_content.writerows(books)
    except FileNotFoundError as e:
        raise FileNotFoundError("file not found!")


save_file()


def save_member_file():

    try:
        with open("member_info.csv", "w", newline="") as member_file:
            fields_name = ["id", "name", "email", "borrowed_books"]

            new_content = csv.DictWriter(
                member_file, fields_name, extrasaction="ignore"
            )

            new_content.writeheader()
            new_content.writerows(members)
    except FileNotFoundError as e:
        raise FileNotFoundError("file not found!")


save_member_file()


# add new book
def add_book():

    id = uuid4()
    title = input("enter your title of book: ")
    author = input("enter the author of book: ")
    year_input = input("enter the year of book: ")
    category = input("enter the category of book: ")

    # validations
    try:
        if title == "":
            print("title can't be a empty")
            return
        elif type(title) != str:
            print("title must be a string")
            return
        elif author == "":
            print("author can't be a empty")
            return
        elif author.isdigit():
            print("author must be a string")
            return
        elif year_input == "":
            print("year can't be a empty")
            return
        elif not year_input.isdigit():
            print("year must be numeric")
            return
        elif category == "":
            print("category can't be a empty!")
            return
        elif category.isdigit():
            print("category must be string!")
            return

        year = int(year_input)

        new_book = {
            "id": id,
            "title": title,
            "author": author,
            "year": year,
            "category": category,
            "status": "available",
        }
        books.append(new_book)
        save_file()
        print(f"title: {new_book['title']} has created.")
        print("*" * 30)
        print(f"id: {new_book['id']}.")
        print(f"{new_book['title']}")
        print(f"{new_book['author']}")
        print(f"{new_book['category']}")
        print(f"{new_book['year']}")
        print(f"{new_book['status']}")

    except Exception as e:
        print(f"Error: {e}")
        print("invalid value")


def view_all_books():

    for book in books:
        try:
            print("*" * 30)
            print(f"id: {book['id']}")
            print(f"title: {book['title']}")
            print(f"author: {book['author']}")
            print(f"category: {book['category']}")
            print(f"status: {book['status']}")
            print("*" * 30)
        except Exception as e:
            print("there is no book in your library!")


def search_book():

    search_keyboards = input(
        "which book do you want to see? (you can search by title, author, category) \n"
    )
    found = False

    try:
        for book in books:
            count = 0
            for value in book.values():
                if search_keyboards.lower() in str(value):
                    found = True
                    count += 1
                    break

        # if found == True:
        #     print("yes we have.")
        print(count)
            # else:
            # print("there is no book with this title, author, category")
    except Exception as e:
        print(f"Invalid operation: {e}")


def add_member():

    id = uuid4()
    name = input("enter the name of member: ")
    email = input("enter the email of member: ")

    is_registred = False

    try:
        if name == "":
            print("title can't be a empty")
            return
        elif name.isdigit():
            print("title must be a string")
            return
        elif email == "":
            print("email can't be a empty")
            return
        elif "@" not in email:
            print("email must be a valid: (you might be forgot use @?)")
            return
        elif "gmail" not in email:
            print(
                "email must contain 'email' word: (you might be forgot to write email ?)"
            )
            return
        for member in members:
            if email == member["email"]:
                is_registred = True
                break

        if is_registred == False:
            new_member = {"id": id, "name": name, "email": email}
            members.append(new_member)
            save_member_file()
            print("member added successfully!")
        else:
            print("this email is already registred!")

    except ValueError as e:
        print(f"invalid operation: {e}")


def view_all_members():

    for member in members:
        try:
            print("*" * 30)
            print(f"id: {member['id']}")
            print(f"name: {member['name']}")
            print(f"email: {member['email']}")
            print("*" * 30)
        except Exception as e:
            print("there is no any member in your library!")


def borrow_book():
    book_id = input("please enter your book_id: \n")
    member_id = input("please enter your member_id: \n")
    print("*" * 30)

    # Flags
    book_found = False
    member_found = False
    is_available = True

    for book in books:
        if book_id == book["id"]:
            book_found = True
            exist_book = book

            if exist_book["status"] == "non-available":
                is_available = False
                print("this book has borrowed to someone~")
                print(exist_book["title"])
            break

    if book_found == True:
        print("*" * 30)
        print("yes, we have this book")
        print(exist_book["title"])
        print("*" * 30)

        if is_available == True:
            print("as well as this book is available")
        else:
            print("this book is not available")
    else:
        print("book not found!")
    
    for member in members:
        if member_id == member["id"]:
            exist_member = member
            member_found = True
            print("yes we have this member")
            break

    if member_found:
        print("*" * 30)
        print(member["name"])
        print("*" * 30)
    else:
        print("member not found!")

    borrow_book = input(f"would you like to borrow {exist_book['title']} book?")
    if exist_book['status'] == 'non-available':
        is_available = False
        print("this book is not available")

    if borrow_book == "yes":
        if is_available == True:
            exist_book['status'] = 'borrowed'
            exist_member['borrowed_books'] = exist_book['title']
            exist_book['borrowed_by'] = exist_member['id']
            print(f"member : {exist_member['name']} - {exist_book['title']} borrowed")
            save_file()
            save_member_file()
    else:
        print("take it easy")

def return_book():

    book_id = input("please enter your book_id for return: \n")
    is_borrowed = False
    for book in books:
        if book_id == book['id']:
            exist_book = book
            print(f"yes we have this book: {exist_book['title']}")
            if exist_book['status'] == 'borrowed':
                is_borrowed = True
        else:
            print("we could not find this book")

    if is_borrowed == False:
        print("sorry but this book might be has available state")
        
    if is_borrowed == True:
        print("you can return this book to library.")

        returnd_book = input("would you like to return this book to library?")

        if returnd_book == "yes":
            exist_book['status'] = 'available'
            print(f"book with title: {exist_book['title']} returnd to library!")
            save_file()
        else:
            print("sorry but this book might be has available state")

def delete_book():

    book_id = input("please enter your book_id for return: \n")
    found = False
    is_borrowed = False
    for book in books:
        if book_id == book['id']:
            found = True
            exist_book = book
            print(f"yes we have this book: {exist_book['title']}")

    if found == False:
        print("there is no book with this id")

    if exist_book['status'] == 'borrowed' or exist_book['status'] == 'non-available':
        is_borrowed = True
        print(f"this book: {exist_book['title']} has borrowed to someone! it must be has available state")

    if is_borrowed == False:
        remove_book = input("would you like to remove this book from library?")

        if remove_book == 'yes':
            books.remove(exist_book)
            print("book is deleted!")
            save_file()
        else:
            print("something went wrong!")

def delete_member():
    
    member_id = input("please enter the member id: \n")
    is_found = False
    for member in members:
        if member_id == member['id']:
            exist_member = member
            is_found = True
            break

    if is_found == True:
        print(f"member: {exist_member['name']}")

        remove_member = input("are you sure to delete this member? (yes, no) \n ")

        has_borrowed = False
        if remove_member == "yes":
            for book in books:
                if exist_member['id'] == book['borrowed_by']:
                    has_borrowed = True
                    print(f"member: {exist_member['name']} has a borrowed books , you can't delete until books come back")
                    break

        if has_borrowed == False:
            members.remove(exist_member)
            print(f"member: {exist_member['name']} deleted")
            save_member_file()
    else:
        print("we could not found this member.")

def library_summary():

    # total_numbers_of_books
    print(f"len of books are: {len(books)}")

    available_books = 0
    borrowed_books = 0
    for book in books:
        if book['status'] == "available":
            available_books += 1    

        if book['status'] == "borrowed":
            borrowed_books += 1

    print(f'availables books are: {available_books}')
    print(f'borrowed books are: {borrowed_books}')

    member_count = 0
    for member in members:
        if member['id'] == member["id"]:
            member_count += 1

    print(f"members are: {member_count}")

while True:

    print("1. Add new book")
    print("2. View all books")
    print("3. Search book")
    print("4. Add member to library")
    print("5. Delete member")
    print("6. View all members")
    print("7. Borrow book")
    print("8. Return book")
    print("9. Delete book")
    print("10. Library Summary")


    choose_operation = int(input("what operation would you like: 1/2/3/4/5/6/7/8/9/10 \n"))

    if choose_operation == 1:
        add_book()
    elif choose_operation == 2:
        view_all_books()
    elif choose_operation == 3:
        search_book()
    elif choose_operation == 4:
        add_member()
    elif choose_operation == 5:
        delete_member()             
    elif choose_operation == 6:
        view_all_members()
    elif choose_operation == 7:
        borrow_book()
    elif choose_operation == 8:
        return_book()
    elif choose_operation == 9:
        delete_book()
    elif choose_operation == 10:
        library_summary()         