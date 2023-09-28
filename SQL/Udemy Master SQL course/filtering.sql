SELECT * FROM employees WHERE NOT gender='M' -- This NOT negates the condition

--or

SELECT * FROM employees WHERE gender!='M' -- We can also use != to negate the condition


--NULL can nevers be compared with anything but we can use like below
SELECT * FROM employees WHERE email IS NULL; --but never use operator like = > < etc
SELECT * FROM employees WHERE email IS NOT NULL;


--Using IN clause
SELECT * FROM employees where department in ('Toys','Movies')


-- Using BETWEEN clause
SELECT * FROM employees where salary BETWEEN 80000 AND 100000;
