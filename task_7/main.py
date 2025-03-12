from random import randint

from task_7.app.entrypoint import execute_sql
from task_7.app.infrastructure import validation

from task_7.input_sql_statements import (
    create_products_table,
    insert_products,
    retrieve_products_lt_10,
    update_product_price,
    drop_products_table,
    retrieve_products_by_id
)

values_list = [
    {"name": f"test_name_{i}", "price": randint(5000, 200001), "quantity": i + 6}
    for i in range(1, 11)
]

def script_for_task_7() -> dict:
    drop_poducts_table_result = execute_sql(sql_statement=drop_products_table)
    create_products_table_result = execute_sql(
        sql_statement=create_products_table,
        validation_method=validation.ValidationMethods.CREATE_PRODUCT
    )
    insert_products_result = []
    for values_item in values_list:
        res = execute_sql(
            sql_statement=insert_products,
            values=values_item,
            validation_method=validation.ValidationMethods.CREATE_PRODUCT
        )
        insert_products_result.append(res)
    retrieve_result = execute_sql(sql_statement=retrieve_products_lt_10, fetchall=True)
    update_product_price_result = execute_sql(
            sql_statement=update_product_price,
            values={"price": 42, "name": "test_name_2"},
            validation_method=validation.ValidationMethods.UPDATE_DELETE_PRODUCT
    )
    retrieve_after_update_result = execute_sql(
        sql_statement=retrieve_products_by_id,
        values={"id": "2"},
        validation_method=validation.ValidationMethods.UPDATE_DELETE_PRODUCT,
        fetchall=True
    )

    return {
        "drop": drop_poducts_table_result,
        "create": create_products_table_result,
        "insert": insert_products_result,
        "retrieve": retrieve_result,
        "update": update_product_price_result,
        "retrieve_after_update_result": retrieve_after_update_result
    }


if __name__ == "__main__":

    result = script_for_task_7()
    pass

    assert result["drop"]["status"] == "success"
    assert result["create"]["status"] == "success"
    for item in result["insert"]:
        assert item["status"] == "success"
    assert result["retrieve"]["status"] == "success"
    assert result["retrieve"]["data_fetched"] == [(1, "test_name_1"), (2, "test_name_2"), (3, "test_name_3")]
    assert result["update"]["status"] == "success"
    assert result["retrieve_after_update_result"]["data_fetched"] == [(2, "test_name_2", 42)]

