drop_customer_table = """
            DROP TABLE customer;
            """

drop_orders_table = """
            DROP TABLE orders;
            """


create_customer_table = """
            CREATE TABLE IF NOT EXISTS customer (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                email VARCHAR(100) NOT NULL
            );
            """

create_orders_table = """
                CREATE TABLE orders (
                    id SERIAL PRIMARY KEY,
                    customer_id INT NOT NULL,
                    order_date DATE NOT NULL,
                    amount FLOAT NOT NULL,
                    CONSTRAINT fk_customer_id FOREIGN KEY (customer_id) REFERENCES customer(id)
                );
                """

insert_customer = """
            INSERT INTO customer (name, email)
            VALUES (%s, %s);
            """

insert_order = """
            INSERT INTO orders (customer_id, order_date, amount)
            VALUES (%s, %s, %s);
)
"""

total_order_amount_per_customer = """
            SELECT 
                c.id, c.name, 
                SUM(o.amount) AS total_amount
            FROM 
                customer c
            JOIN 
                orders o ON c.id = o.customer_id
            GROUP BY 
                c.id, c.name
            ORDER BY 
                total_amount DESC;
            """


max_order_amount_per_customer = """
            SELECT 
                c.name, 
                MAX(o.amount) AS max_amount
            FROM 
                customer c
            JOIN 
                orders o ON c.id = o.customer_id
            GROUP BY 
                c.name
            ORDER BY 
                max_amount DESC;
            """


customer_with_max_total_order_amount = """
            SELECT 
                c.id, c.name, 
                SUM(o.amount) AS total_amount
            FROM 
                customer c
            JOIN 
                orders o ON c.id = o.customer_id
            GROUP BY 
                c.id
            ORDER BY 
                total_amount DESC
            LIMIT 1;
            """


number_of_orders_in_2023 = """
            SELECT 
                COUNT(*) AS number_of_orders
            FROM 
                orders
            WHERE 
                order_date >= '2023-01-01' AND order_date <= '2023-12-31';
            """


average_order_amount_per_customer = """
            SELECT 
                c.id, c.name, 
                AVG(o.amount) AS average_amount
            FROM 
                customer c
            JOIN 
                orders o ON c.id = o.customer_id
            GROUP BY 
                c.id, c.name
            ORDER BY 
                average_amount DESC;
            """
