Persistense strategy:
    1 - create a simple list
    2 - open and save csv file
    3 - append data to simple 
    4 - generate data into csv file

Entities:
    Book,
    Member,
    User

State transitions:
    availble => borrowed = ok
    borrowed => availble = ok
    borrowed => borowed = fuck