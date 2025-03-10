create_emploees_task_4_table = """
            CREATE TABLE IF NOT EXISTS employees_task_4 (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                position VARCHAR(100) NOT NULL,
                salary FLOAT NOT NULL
            );
            """

drop_employees_task_4_table = """
            DROP TABLE employees_task_4;
            """

insert_employees_into_employees_task_4_table = """
            INSERT INTO employees_task_4 (name, position, salary)
            VALUES (%s, %s, %s);
            """

retrieve_employees_by_position = """
            SELECT *
            FROM employees_task_4
            WHERE position = %s;
            """
