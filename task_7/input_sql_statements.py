from input_sql_task_1 import update_salary

drop_products_table = """
    DROP TABLE products;
    """

create_products_table = """
            CREATE TABLE IF NOT EXISTS products (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                price FLOAT NOT NULL,
                quantity INT NOT NULL
            );
            """

insert_products = """
            INSERT INTO products (name, price, quantity)
            VALUES (%s, %s, %s);
            """

retrieve_products_lt_10 = """
            SELECT *
            FROM products
            WHERE quantity < 10;
            """

update_product_price = """
            UPDATE products
            SET price = %s
            WHERE name = %s;
            """