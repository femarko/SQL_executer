
# 1. Найти общую сумму заказов для каждого клиента.
amount_per_customer = """
            SELECT 
                c.id, c.name, 
                SUM(o.amount) AS total_amount
            FROM 
                customer_task_3 c
            JOIN 
                orders_task_3 o ON c.id = o.customer_id
            GROUP BY 
                c.id, c.name
            ORDER BY 
                total_amount DESC;
            """

# 2. Найти клиента с максимальной суммой заказов.
customer_max_total_order = """
            SELECT 
                c.id, c.name, 
                SUM(o.amount) AS total_amount
            FROM 
                customer_task_3 c
            JOIN 
                orders_task_3 o ON c.id = o.customer_id
            GROUP BY 
                c.id
            ORDER BY 
                total_amount DESC
            LIMIT 1;
            """

# 3. Найти количество заказов, сделанных в 2023 году.
orders_in_2023 = """
            SELECT 
                COUNT(*) AS number_of_orders
            FROM 
                orders_task_3
            WHERE 
                order_date >= '2023-01-01' AND order_date <= '2023-12-31';
            """

# 4. Найти среднюю сумму заказа для каждого клиента.
average_order = """
            SELECT 
                c.id, c.name, 
                ROUND(AVG(o.amount), 2) AS average_amount
            FROM 
                customer_task_3 c
            JOIN 
                orders_task_3 o ON c.id = o.customer_id
            GROUP BY 
                c.id, c.name
            ORDER BY 
                average_amount DESC;
            """
