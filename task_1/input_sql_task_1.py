# task 1
from functools import total_ordering

create_emploees_table = """
            CREATE TABLE IF NOT EXISTS employees (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                position VARCHAR(100) NOT NULL,
                salary FLOAT NOT NULL
            );
            """

drop_employees_table = """
            DROP TABLE employees;
            """

insert_employees = """
            INSERT INTO employees (name, position, salary)
            VALUES (%s, %s, %s);
            """

retrive_salary_gt_50000 = """
            SELECT name, position, salary
            FROM employees
            WHERE salary > 50000;
            """

update_salary = """
            UPDATE employees
            SET salary = %s
            WHERE name = %s;
            """

delete_employee = """
            DELETE FROM employees
            WHERE name = %s;
            """


# task 3 # FOREIGN KEY REFERENCES customer(id)


