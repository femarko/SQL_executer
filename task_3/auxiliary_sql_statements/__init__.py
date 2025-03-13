create_customer_table = """
            CREATE TABLE IF NOT EXISTS customer_task_3 (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                email VARCHAR(100) NOT NULL
            );
            """
create_orders_table = """
                CREATE TABLE IF NOT EXISTS orders_task_3 (
                    id SERIAL PRIMARY KEY,
                    customer_id INT NOT NULL,
                    order_date DATE NOT NULL,
                    amount INTEGER NOT NULL,
                    CONSTRAINT fk_customer_id FOREIGN KEY (customer_id) REFERENCES customer_task_3(id)
                );
                """
insert_customer = """
            INSERT INTO customer_task_3 (name, email)
            VALUES (%s, %s);
            """
insert_order = """
            INSERT INTO orders_task_3 (customer_id, order_date, amount)
            VALUES (%s, %s, %s);
            """

drop_customer_table = """
            DROP TABLE IF EXISTS customer_task_3;
            """

drop_orders_table = """
            DROP TABLE IF EXISTS orders_task_3;
            """
