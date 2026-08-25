
Assignment:

Assuming the  table is named tfi and it has these columns:
•	emp_name 
•	dept 
•	salary

Create a CTE to find the average salary of each department.

WITH dept_avg AS (
    SELECT dept, AVG(salary) AS avg_salary
    FROM tfi
    GROUP BY dept
)
SELECT *
FROM dept_avg;

Create a CTE to find the maximum salary of each department.

WITH dept_max AS (
    SELECT dept, MAX(salary) AS max_salary
    FROM tfi
    GROUP BY dept
)
SELECT *
FROM dept_max;

-- Create a CTE that calculates the average salary for each department. Then display only departments
--  whose average salary is greater than 70000

WITH dept_avg AS (
    SELECT dept, AVG(salary) AS avg_salary
    FROM tfi
    GROUP BY dept
)
SELECT *
FROM dept_avg
WHERE avg_salary > 70000;


-- Using a CTE, find departments having more than 5 employees.

WITH dept_emp_count AS (
    SELECT dept, COUNT(*) AS employee_count
    FROM tfi
    GROUP BY dept
)
SELECT *
FROM dept_emp_count
WHERE employee_count > 5;


-- Create a CTE containing the total salary paid by each department. Display the department with 
-- a total salary greater than 500000

WITH dept_total_salary AS (
    SELECT dept, SUM(salary) AS total_salary
    FROM tfi
    GROUP BY dept
)
SELECT *
FROM dept_total_salary
WHERE total_salary > 500000;


-- Using a CTE, find the highest salary in each department.

WITH dept_highest_salary AS (
    SELECT dept, MAX(salary) AS highest_salary
    FROM tfi
    GROUP BY dept
)
SELECT *
FROM dept_highest_salary;


-- Create a CTE containing the average salary of each department. Then join it with tfi and display:
-- emp_name, dept, salary, avg_salary

WITH dept_avg AS (
    SELECT dept, AVG(salary) AS avg_salary
    FROM tfi
    GROUP BY dept
)
SELECT 
    t.emp_name,
    t.dept,
    t.salary,
    d.avg_salary
FROM tfi t
JOIN dept_avg d
ON t.dept = d.dept;


-- Find only the employees whose salary is greater than their department's average salary.


WITH dept_avg AS (
    SELECT dept, AVG(salary) AS avg_salary
    FROM tfi
    GROUP BY dept
)
SELECT 
    t.emp_name,
    t.dept,
    t.salary
FROM tfi t
JOIN dept_avg d
ON t.dept = d.dept
WHERE t.salary > d.avg_salary;


-- Using a CTE, find employees whose salary is LESS than their department's average salary
WITH dept_avg AS (
    SELECT dept, AVG(salary) AS avg_salary
    FROM tfi
    GROUP BY dept
)
SELECT 
    t.emp_name,
    t.dept,
    t.salary
FROM tfi t
JOIN dept_avg d
ON t.dept = d.dept
WHERE t.salary < d.avg_salary;


