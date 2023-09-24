-- Here are the questions I provided for your practice:

-- 1. Basic SELECT Statement: Retrieve all columns from the "employees" table.
SELECT * FROM employe;

-- 2. Filtering Data: Retrieve the names of all employees who have a salary greater than $50,000 from the "employees" table.
SELECT * FROM employe where salary>55000;

-- 3. Sorting Data: Retrieve the names and hire dates of employees in ascending order of hire date from the "employees" table.
select EMPLOYEE_NAME as Name, HIRE_DATE as Hired_on from employe order by HIRE_DATE asc;

-- 4. Aggregate Functions: Calculate the average salary of all employees in the "employees" table.
select avg(salary) from employe;

-- 5. Joins: Retrieve the names of employees and the names of their respective departments from the "employees" and "departments" tables. Use a JOIN statement.
select e.EMPLOYEE_NAME, d.DEPARTMENT_NAME 
from employe e
join departments d on e.DEPARTMENT_ID=d.DEPARTMENT_ID;

-- 6. Subqueries: Retrieve the names of employees who have a salary greater than the average salary of all employees in the "employees" table.
SELECT employee_name
FROM employe
WHERE salary > (SELECT AVG(salary) FROM employe);

-- 7. Updating Data: Update the salary of employee with ID 101 to $60,000 in the "employees" table.
UPDATE employe set SALARY=66000 where EMPLOYEE_ID=101;

-- 8. Inserting Data: Insert a new employee with the name "John Doe" and a salary of $45,000 into the "employees" table.
INSERT INTO EMPLOYE (EMPLOYEE_ID, EMPLOYEE_NAME, HIRE_DATE, SALARY, DEPARTMENT_ID)
VALUES (104, 'Jane Smith', TO_DATE('2023-09-17', 'YYYY-MM-DD'), 52000, 2);

-- 9. Deleting Data: Delete all employees from the "employees" table who have a salary less than $40,000.
delete employe where salary=52000;

-- 10. Grouping and Aggregating: Retrieve the department names and the total number of employees in each department from the "employees" table, grouping by department.
select DEPARTMENT_NAME,count(*)
from departments d
join employe e on e.DEPARTMENT_ID=d.DEPARTMENT_ID
group by DEPARTMENT_NAME;

