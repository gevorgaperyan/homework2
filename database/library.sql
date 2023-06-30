create database Library;

create table Author
(
    id smallserial primary key,
    first_name char(50) not null,
    last_name char(50) not null
);

create table Book
(
    id smallserial primary key,
    title varchar(100) not null,
    year_first_published int
);

create table BookAuthor
(
    author_id int REFERENCES Author(id) not null,
    book_id int REFERENCES Book(id) not null
);

create table BookCopies
(
    id smallserial primary key,
    book_id int REFERENCES Book(id) not null,
    ISBN int,
    year_published int not null
);

create table Student
(
    id smallserial primary key,
    first_name char(50) not null,
    last_name char(50) not null
);

create table Borrows
(
    id smallserial primary key,
    book_copy_id int REFERENCES BookCopies(id) not null,
    student_id int REFERENCES Student(id) not null,
    borrow_date int not null,
    return_date int
);