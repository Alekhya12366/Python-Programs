1. Start a transaction and update marks of student with id = 2 to 80, then commit the changes.
START TRANSACTION;

UPDATE students
SET marks = 80
WHERE id = 2;

COMMIT;


2. Start a transaction, delete the student whose id = 3, and rollback the transaction.
START TRANSACTION;

DELETE FROM students
WHERE id = 3;

ROLLBACK;

________________________________________
3. Insert a new student (4, 'Kiran', 88) and commit the transaction.
START TRANSACTION;

INSERT INTO students (id, name, marks)
VALUES (4, 'Kiran', 88);

COMMIT;

________________________________________
4. Start a transaction, update marks of id = 1 to 95, create a savepoint, then update marks of id = 2 to 60. Rollback only the second update.
START TRANSACTION;

UPDATE students
SET marks = 95
WHERE id = 1;

SAVEPOINT sp1;

UPDATE students
SET marks = 60
WHERE id = 2;

ROLLBACK TO SAVEPOINT sp1;

COMMIT;
________________________________________
5. Write a query to demonstrate the use of SAVEPOINT and ROLLBACK TO SAVEPOINT.
START TRANSACTION;

UPDATE students
SET marks = 90
WHERE id = 1;

SAVEPOINT sp1;

UPDATE students
SET marks = 70
WHERE id = 2;

ROLLBACK TO SAVEPOINT sp1;

COMMIT;
________________________________________
6. Start a transaction, insert two records, then rollback the entire transaction.
START TRANSACTION;

INSERT INTO students (id, name, marks)
VALUES (5, 'Rahul', 85);

INSERT INTO students (id, name, marks)
VALUES (6, 'Anu', 90);

ROLLBACK;
________________________________________
7. Start a transaction, update multiple rows, and commit only if all updates are successful.
START TRANSACTION;

UPDATE students
SET marks = 85
WHERE id = 1;

UPDATE students
SET marks = 90
WHERE id = 2;

UPDATE students
SET marks = 95
WHERE id = 3;

COMMIT;
________________________________________
8. What will happen if you execute a ROLLBACK after COMMIT? Write a query to demonstrate this.
START TRANSACTION;

UPDATE students
SET marks = 100
WHERE id = 1;

COMMIT;

ROLLBACK;
________________________________________
9. Write a TCL query to undo only part of a transaction using SAVEPOINT.
START TRANSACTION;

UPDATE students
SET marks = 75
WHERE id = 1;

SAVEPOINT sp1;

UPDATE students
SET marks = 65
WHERE id = 2;

ROLLBACK TO SAVEPOINT sp1;

COMMIT;
________________________________________
10. Write SQL queries showing the difference between COMMIT and ROLLBACK.
COMMIT
START TRANSACTION;

UPDATE students
SET marks = 90
WHERE id = 1;

COMMIT;
COMMIT: Permanently saves the changes.
ROLLBACK
START TRANSACTION;

UPDATE students
SET marks = 50
WHERE id = 1;

ROLLBACK;

