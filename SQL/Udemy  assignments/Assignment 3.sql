Assignment 3: Practice with Functions, Conditional Expressions and Concatenation
Complete following problems related to the professors table you created in assignment 1.

LAST_NAME	DEPARTMENT	SALARY	HIRE_DATE
Chong	Science	88000	04/18/2006
Brown	Math	97000	08/22/2002
Jones	History	67000	11/17/2009
Wilson	Astronomy	82000	05/08/2008
Williams	Law	105000	06/05/2001

Instructor Solutions for this assignment
Write a query against the professors table that can output the following in the result: "Chong works in the Science department"

SELECT last_name || ' ' || 'works in the '|| department ||

' department'

FROM professors



Write a SQL query against the professors table that would return the following result:

"It is false that professor Chong is highly paid"
"It is true that professor Brown is highly paid"
"It is false that professor Jones is highly paid"
"It is true that professor Wilson is highly paid"
"It is false that professor Miller is highly paid"
"It is true that professor Williams is highly paid"

NOTE: A professor is highly paid if they make greater than 95000.

SELECT 'It is ' || (salary > 95000) ||

' that professor ' || last_name || ' is highly paid'

FROM professors



Write a query that returns all of the records and columns from the professors table but shortens the department names to only the first three characters in upper case.

SELECT last_name,

       UPPER(SUBSTRING(department, 1, 3)) as department,

       salary, hire_date

FROM professors



Write a query that returns the highest and lowest salary from the professors table excluding the professor named 'Wilson'.

SELECT MAX(salary) as higest_salary,

MIN(salary) as lowest_salary

FROM professors

WHERE last_name != 'Wilson'



Write a query that will display the hire date of the professor that has been teaching the longest.

SELECT MIN(hire_date)

FROM professors