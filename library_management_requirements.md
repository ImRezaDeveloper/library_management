# Project — Library Management System

## Project Overview

Build a **command-line library management application**.

The application should simulate the core operations of a small library.
A user should be able to manage books and library members, borrow books, return books, search for books, and view useful summaries.

The main goal of this project is to practice:

- Problem decomposition
- Data modeling
- CRUD operations
- State management
- Business rules
- Validation
- Exception handling
- File persistence
- Searching and filtering
- Program flow

Do not use a database or external packages for this project.

---

# 1. Main Menu

The program must repeatedly show a menu similar to:

```text
===== Library Management System =====

1. Add book
2. View all books
3. Search books
4. Add member
5. View all members
6. Borrow book
7. Return book
8. Delete book
9. Delete member
10. Show library summary
11. Exit

Choose an option:
```

The program must continue running until the user chooses `Exit`.

Invalid menu input must not crash the program.

---

# 2. Book Data

Each book must contain at least:

```text
id
title
author
year
category
status
```

Example conceptually:

```text
id: 7b2f...
title: Clean Code
author: Robert C. Martin
year: 2008
category: programming
status: available
```

### Requirements

- Every book must have a unique identifier.
- The identifier must not depend on the title.
- A book must have a title.
- A book must have an author.
- The year must be valid.
- The category must not be empty.
- A newly created book must start as `available`.

You may choose your own strategy for generating book IDs.

---

# 3. Member Data

Each library member must contain at least:

```text
id
name
email
```

Example:

```text
id: 91af...
name: Ali Ahmadi
email: ali@example.com
```

### Requirements

- Every member must have a unique identifier.
- Member name cannot be empty.
- Email cannot be empty.
- You should perform reasonable validation on the data entered by the user.

You may choose your own ID generation strategy.

---

# 4. Add Book

The user should be able to add a new book by entering:

```text
Title:
Author:
Year:
Category:
```

### Validation

At minimum:

- Title cannot be empty.
- Author cannot be empty.
- Year must be numeric.
- Year cannot be negative.
- Category cannot be empty.

After a successful operation, show a confirmation message.

---

# 5. View All Books

Display all books with their important information.

Example format:

```text
ID: ...
Title: Clean Code
Author: Robert C. Martin
Year: 2008
Category: programming
Status: available
------------------------------
```

If there are no books, handle that situation appropriately.

---

# 6. Search Books

The user must be able to search for books.

At minimum, support searching by:

- Title
- Author
- Category

The search should not require an exact match for title or author.

For example, searching for:

```text
python
```

may match:

```text
Python Crash Course
Fluent Python
Learning Python
```

### Requirements

- Search should be case-insensitive.
- Display all matching books.
- If nothing matches, show an appropriate message.

You may decide how the user selects the search field.

---

# 7. Add Member

The user should be able to create a new library member.

Input:

```text
Name:
Email:
```

### Validation

- Name cannot be empty.
- Email cannot be empty.
- You should reject obviously invalid email input.

After creation, show a confirmation message.

---

# 8. View All Members

Display all registered members.

Example:

```text
ID: ...
Name: Ali Ahmadi
Email: ali@example.com
------------------------------
```

If there are no members, handle the situation appropriately.

---

# 9. Borrow Book

This is the first major business-rule section of the project.

The user should provide:

```text
Book ID:
Member ID:
```

The program should attempt to create a borrowing operation.

### Business Rules

1. The book must exist.
2. The member must exist.
3. The book must currently be `available`.
4. An unavailable book cannot be borrowed again.
5. After a successful borrow, the book status must change to `borrowed`.

Show an appropriate message for every failure case.

Example successful flow:

```text
Book found
Member found
Book is available
Borrow operation succeeds
Book status -> borrowed
```

---

# 10. Return Book

The user should provide the book ID.

### Business Rules

1. The book must exist.
2. The book must currently be `borrowed`.
3. A book that is already available cannot be returned.
4. After a successful return, the status becomes `available`.

Example:

```text
Book status before: borrowed
Return succeeds
Book status after: available
```

---

# 11. Delete Book

The user can delete a book using its ID.

### Rules

- The book must exist.
- A book that does not exist must be handled gracefully.
- You must decide what should happen if the book is currently borrowed.

Important:

The requirement intentionally does **not** tell you whether a borrowed book should be deletable.

You must make the business decision yourself and document your assumption before coding.

---

# 12. Delete Member

The user can delete a member using the member ID.

### Rules

- The member must exist.
- A missing member must be handled gracefully.
- You must decide what should happen if the member currently has a borrowed book.

Again, document your assumption before implementation.

---

# 13. Library Summary

The program must provide a summary of the current library state.

At minimum, display:

- Total number of books
- Number of available books
- Number of borrowed books
- Total number of members

Example:

```text
===== Library Summary =====

Total books: 20
Available books: 15
Borrowed books: 5
Total members: 12
```

You may add other useful statistics if you think they are valuable.

---

# 14. Borrowing Rules and State

The book has at least two states:

```text
available
borrowed
```

A valid state transition is:

```text
available -> borrowed
borrowed -> available
```

Invalid transitions must be rejected.

For example:

```text
borrowed -> borrowed
```

must not be accepted as a successful borrow.

And:

```text
available -> available
```

must not be treated as a successful return.

---

# 15. Persistence

The application must preserve its data between program runs.

Use files for persistence.

You may use:

- CSV
- JSON

You must choose one format and use it consistently.

At minimum, the application must persist:

- Books
- Members

If your design stores borrowing information separately, that data must also survive a restart.

### Startup Flow

Conceptually:

```text
Start program
     ↓
Load saved data
     ↓
Initialize application state
     ↓
Show menu
```

### Exit / Update Flow

Your program must save changes so that the data is available during the next run.

---

# 16. Invalid Input Handling

The program should not crash because of ordinary user mistakes.

Handle cases such as:

- Invalid menu option
- Non-numeric year
- Invalid book ID
- Invalid member ID
- Missing book
- Missing member
- Empty title
- Empty author
- Empty category
- Empty member name
- Invalid email
- Borrowing an already borrowed book
- Returning an available book
- Missing file
- Invalid or corrupted saved data

You should use exception handling where it is actually appropriate.

Do not simply wrap the entire program in one broad `except Exception` block.

---

# 17. Data Consistency

The program must keep its internal data consistent.

Examples:

- A book cannot be both `available` and `borrowed` at the same time.
- A borrow operation cannot succeed if the book does not exist.
- A borrow operation cannot succeed if the member does not exist.
- A return operation cannot succeed if the book does not exist.
- Failed operations must not partially change the data.

Think about what happens when an operation fails halfway through.

---

# 18. File Error Handling

The application should behave reasonably when:

- The data file does not exist yet.
- The file exists but contains invalid data.
- A required field is missing from saved data.

The program should not immediately crash just because the storage file is missing on the first run.

You must decide how your application initializes an empty library in that situation.

---

# 19. Project Constraints

Use only Python standard-library features.

Allowed examples:

- `dict`
- `list`
- `set`
- functions
- loops
- conditionals
- exceptions
- `csv`
- `json`
- `datetime`
- `uuid`
- file handling

Do not use:

- SQLite
- SQLAlchemy
- Django
- FastAPI
- pandas
- external packages

Keep this project as a Python problem-solving exercise.

---

# 20. Suggested Functional Flow

The overall system should conceptually behave like this:

```text
Start
  ↓
Load saved data
  ↓
Show menu
  ↓
User chooses operation
  ↓
Validate input
  ↓
Check business rules
  ↓
Modify application state
  ↓
Persist successful changes
  ↓
Show menu again
  ↓
...
  ↓
Exit
```

---

# 21. Important Design Decisions You Must Make

Before writing code, write down your assumptions for these questions:

### Question 1
Can a member borrow more than one book at the same time?

### Question 2
Can a member borrow a book if they already have another borrowed book?

### Question 3
Can a borrowed book be deleted?

### Question 4
Can a member with a borrowed book be deleted?

### Question 5
Should search match partial titles/authors?

### Question 6
Should category matching be case-insensitive?

### Question 7
Should book years be allowed to be in the future?

### Question 8
What happens when the persistence file is missing?

### Question 9
What happens when the persistence file is corrupted?

### Question 10
Should IDs be generated automatically or entered by the user?

Do not wait for someone else to answer these questions.

Your job is to choose reasonable assumptions and implement your system consistently with them.

---

# 22. What You Should Be Able to Demonstrate

By completing this project, you should be able to demonstrate practical understanding of:

- Requirement analysis
- Breaking a problem into smaller parts
- Data modeling
- CRUD operations
- State management
- Business rules
- Validation
- Search and filtering
- File persistence
- Exception handling
- Program flow
- Handling edge cases
- Making and documenting implementation assumptions

---

# 23. Challenge Mode

Once the main project works, add at least **two** of the following features without changing the core requirements:

### Challenge A — Borrow History

Keep a record of previous borrow and return operations.

Example conceptually:

```text
Book X
Borrowed by Member Y
Returned
Borrowed again by Member Z
```

### Challenge B — Due Dates

Every borrow operation gets a due date.

The system should be able to identify overdue books.

### Challenge C — Advanced Search

Support combinations such as:

```text
author = Robert
category = programming
status = available
```

### Challenge D — Statistics

Add statistics such as:

- Most borrowed book
- Most active member
- Number of books per category

### Challenge E — Update Operations

Allow editing book and member information.

---

# Final Rule

Do not start by writing functions immediately.

First produce a small design note containing:

1. Entities
2. Data structures
3. Main operations
4. State transitions
5. Business rules
6. Error cases
7. Persistence strategy
8. Your answers to the design questions above

Then begin implementation.

The goal is not simply to make the program run.

The goal is to practice turning a real requirement into a working program **without being given the solution structure**.
