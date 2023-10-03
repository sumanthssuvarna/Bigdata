-- How to extract only month or only date or only year from a date column

SELECT extract(month from hire_date) from employees;

SELECT extract(year from hire_date) from employees;