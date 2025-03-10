from random import randint

import app.infrastructure.db_connection as db
import app.domain.sql_executor as domain
from app.entrypoint import execute_sql
from app.infrastructure import validation

from input_sql_statements import (
    create_products_table,
    insert_products,
    retrieve_products_lt_10,
    update_product_price,
    drop_products_table
)

values = [
    {"name": f"test_name_{i}", "price": randint(5000, 200001), "quantity": randint(3, 101)}
    for i in range(1, 11)
]


if __name__ == "__main__":
    print(execute_sql(sql_statement=drop_products_table))
    print(execute_sql(sql_statement=create_products_table))
    for value_set in values:
        print(
            execute_sql(
                sql_statement=insert_products,
                values=value_set,
                validation_method=validation.ValidationMethods.CREATE_PRODUCT
            )
        )

    print(execute_sql(sql_statement=retrieve_products_lt_10, fetchall=True))
    print(
        execute_sql(
            sql_statement=update_product_price,
            values={"price": 10000.35, "name": "test_name_9"},
            validation_method=validation.ValidationMethods.UPDATE_DELETE_PRODUCT
        )
    )



