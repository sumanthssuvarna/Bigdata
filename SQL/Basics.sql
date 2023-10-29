
-- 2. Filtering Data: Retrieve the names of all employees who have a salary greater than $50,000 from the "employees" table.
SELECT * FROM employe where salary>55000;

-- 3. Sorting Data: Retrieve the names and hire dates of employees in ascending order of hire date from the "employees" table.
select EMPLOYEE_NAME as Name, HIRE_DATE as Hired_on from employe order by HIRE_DATE asc;

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

-- 11.Getting unique column names
select distinct(department) from employees order by department ;

-- To get top results
-- In oracle
select distinct(department) from employees order by department FETCH FIRST 10 ROWS ONLY;
-- In others
select distinct(department) from employees order by department LIMIT 10;

--Name aliasing
select distinct(department) as "Department name" from employees order by department ;

-- Between clause
SELECT first_name, hire_date from employees where hire_date BETWEEN '02/07/2005' AND '03/20/2007';

--between,and or
select first_name,Gender, department 
from employees 
where ((department='Automotive' and gender='M') OR (department='Toys' AND gender='F'))
AND salary between 40000 and 100000;

--18. UPPER(), LOWER(), LENGTH(), TRIM() + Boolean Expressions & Concatenation
SELECT UPPER(FIRST_NAME) FROM EMPLOYEES;
SELECT LOWER(FIRST_NAME) FROM EMPLOYEES;
SELECT LENGTH(FIRST_NAME) FROM EMPLOYEES;
SELECT TRIM(BOTH ' ' FROM '          FIRST_NAME') FROM EMPLOYEES;
SELECT FIRST_NAME || ' ' || LAST_NAME FROM EMPLOYEES; -- Concatenation in sql
SELECT FIRST_NAME || ' ' || LAST_NAME as Full_name FROM EMPLOYEES;

SELECT FIRST_NAME, CASE WHEN salary > 40000 THEN 'High' ELSE 'Low' END AS salary_status 
FROM EMPLOYEES order by salary desc; -- too print boolean or case statments


-- 20. String Functions: SUBSTRING(), REPLACE(), POSITION() and COALESCE()
SELECT SUBSTR(column_name, start_position, length) FROM your_table;
SELECT SUBSTR(first_name, 1, 3) FROM employees;

SELECT REPLACE('Hello, World', 'Hello', 'Hi') FROM dual;

SELECT INSTR('Hello, World', 'World') FROM dual; -- This returns 7 -- That is the position checking

SELECT COALESCE(first_name, last_name, 'N/A') FROM employees; -- used to deal with null values
-- If column1 contains a non-null value, that value will be returned.
-- If column1 is null, it will check column2. If column2 contains a non-null value, that value will be returned.
-- If both column1 and column2 are null, it will return the default value 'N/A'.

-- Grouping Functions: MIN(), MAX(), AVG(), SUM(), COUNT()
SELECT Min(salary) FROM employees;
SELECT Max(salary) FROM employees;
SELECT Avg(salary) FROM employees;
SELECT round(avg(salary)) FROM employees;
SELECT Sum(salary) FROM employees;
SELECT Count(*) FROM employees;





