from collections.abc import Callable

from task_3.auxiliary_sql_statements import (
    create_customer_table,
    create_orders_table,
    insert_customer,
    insert_order,
    drop_customer_table,
    drop_orders_table
)
from task_3.sql_statements import (
    amount_per_customer,
    customer_max_total_order,
    orders_in_2023,
    average_order
)
from task_3.app.entrypoint import execute_sql
from task_3.app.infrastructure.validation import ValidationMethods


def prepare_db(exec_func: Callable):
    customers = [
        {"name": "test_name_1", "email": "test_email_1"},
        {"name": "test_name_2", "email": "test_email_2"},
        {"name": "test_name_3", "email": "test_email_3"}
    ]

    orders = [
        {"customer_id": 1, "order_date": "2022-05-01", "amount": 100.0},
        {"customer_id": 2, "order_date": "2023-05-02", "amount": 200.0},
        {"customer_id": 3, "order_date": "2023-05-03", "amount": 300.0},
        {"customer_id": 1, "order_date": "2021-05-04", "amount": 400.0},
        {"customer_id": 2, "order_date": "2024-05-05", "amount": 500.0},
        {"customer_id": 3, "order_date": "2025-01-06", "amount": 600.0}
    ]
    exec_func(sql_statement=drop_customer_table)
    exec_func(sql_statement=drop_orders_table)
    exec_func(sql_statement=create_customer_table)
    exec_func(sql_statement=create_orders_table)
    for item in customers:
        exec_func(
            sql_statement=insert_customer,
            values=item,
            validation_method=ValidationMethods.CREATE_CUSTOMER
        )
    for item in orders:
        exec_func(
            sql_statement=insert_order,
            values=item,
            validation_method=ValidationMethods.CREATE_ORDER
        )


if __name__ == "__main__":
    prepare_db(exec_func=execute_sql)
    res_amount_per_customer = execute_sql(sql_statement=amount_per_customer, fetchall=True)
    res_customer_max_total_order = execute_sql(
        sql_statement=customer_max_total_order, fetchall=True
    )
    res_orders_in_2023 = execute_sql(sql_statement=orders_in_2023, fetchall=True)
    res_average_order = execute_sql(
        sql_statement=average_order, fetchall=True
    )

    assert {item for item in res_amount_per_customer["data_fetched"]} == {
        (1, "test_name_1", 500), (2, "test_name_2", 700), (3, "test_name_3", 900)
    }
    assert res_customer_max_total_order["data_fetched"] == [(3, "test_name_3", 900)]
    assert res_orders_in_2023["data_fetched"] == [(2,)]
    assert {item for item in res_average_order["data_fetched"]} == {
        (1, "test_name_1", 250.00), (2, "test_name_2", 350.00), (3, "test_name_3", 450.00)
    }
