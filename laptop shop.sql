
CREATE TABLE laptops (
    laptop_id INT AUTO_INCREMENT PRIMARY KEY,
    registration_number VARCHAR(20) NOT NULL,
    brand VARCHAR(50) NOT NULL,
    model VARCHAR(50) NOT NULL,
    price INT NOT NULL,
    quantity INT NOT NULL
);



CREATE TABLE employees (
    employee_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    phone_number VARCHAR(20),
    address VARCHAR(200),
    password VARCHAR(100) NOT NULL
);


create table salary(
	employee_id INT AUTO_INCREMENT PRIMARY KEY,
    salary INT NOT NULL,
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
    );
    
