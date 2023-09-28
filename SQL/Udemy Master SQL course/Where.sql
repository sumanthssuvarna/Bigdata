SELECT department from departments where division like '%ome%'
--or
SELECT department from departments where division like '%o%e%'
--or 
SELECT * FROM employees WHERE salary > 100000;
--or
SELECT * FROM employees WHERE 1=1;


-- WHERE with AND/OR

SELECT * FROM employees WHERE salary < 100000 AND first_name like 'S%';

-- Combining AND and OR -- use brackets :)
SELECT * FROM employees WHERE (salary < 100000 AND (last_name like 'Sa%' OR employee_id>200));