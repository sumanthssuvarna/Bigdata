
create table departments (
    department varchar(100),
    division varchar(100),
    primary key (department)
  );


insert into departments values ('Clothing','Home');
insert into departments values ('Grocery','Home');
insert into departments values ('Decor','Home');
insert into departments values ('Furniture','Home');
insert into departments values ('Computers','Electronics');
insert into departments values ('Device Repair','Electronics');
insert into departments values ('Phones & Tablets','Electronics');
insert into departments values ('Garden','Outdoors');
insert into departments values ('Camping & Fishing','Outdoors');
insert into departments values ('Sports','Outdoors');
insert into departments values ('Children Clothing','Kids');
insert into departments values ('Toys','Kids');
insert into departments values ('Vitamins','Health');
insert into departments values ('Pharmacy','Health');
insert into departments values ('First Aid','Health');
insert into departments values ('Automotive','Hardware');
insert into departments values ('Tools','Hardware');
insert into departments values ('Jewelry','Fashion');
insert into departments values ('Beauty','Fashion');
insert into departments values ('Cosmetics','Fashion');
insert into departments values ('Books','Entertainment');
insert into departments values ('Games','Entertainment');
insert into departments values ('Music','Entertainment');
insert into departments values ('Movies','Entertainment');


create table regions (
   region_id int,
   region varchar(20),
   country varchar(20),
   primary key (region_id)
  );

insert into regions values (1, 'Southwest', 'United States');
insert into regions values (2, 'Northeast', 'United States');
insert into regions values (3, 'Northwest', 'United States');
insert into regions values (4, 'Central', 'Asia');
insert into regions values (5, 'East Asia', 'Asia');
insert into regions values (6, 'Quebec', 'Canada');
insert into regions values (7, 'Nova Scotia', 'Canada');


create table employees (
	employee_id INT,
	first_name VARCHAR(50),
	last_name VARCHAR(50),
	email VARCHAR(50),
	hire_date DATE,
	department VARCHAR(17),
	gender VARCHAR(1),
	salary INT,
	region_id INT,
	primary key (employee_id)
);

insert into employees values (1, 'Berrie', 'Manueau', 'bmanueau0@dion.ne.jp', TO_DATE('2009-01-26', 'YYYY-MM-DD'), 'Sports', 'F', 154864, 4);


