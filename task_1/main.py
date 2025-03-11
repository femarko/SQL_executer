from task_1 import input_sql_statements
from task_1.app.entrypoint import execute_sql
from task_1.app.infrastructure import validation


values_list = [
    {"name": "test_name_1", "position": "test_position_1", "salary": 30000},
    {"name": "Иван", "position": "Manager", "salary": 45000},
    {"name": "test_name_2", "position": "test_position_2", "salary": 52000},
    {"name": "Анна", "position": "Manager", "salary": 80000},
    {"name": "test_name_3", "position": "test_position_3", "salary": 49000}
]

def script_for_task_1() -> dict:
    drop_employees_table_result = execute_sql(sql_statement=input_sql_statements.drop_employees_table)
    create_emploees_table_result = execute_sql(
        sql_statement=input_sql_statements.create_emploees_table,
        validation_method=validation.ValidationMethods.CREATE_EMPLOYEE
    )
    insert_employees_results = []
    for values_item in values_list:
        res = execute_sql(
            sql_statement=input_sql_statements.insert_employees,
            values=values_item,
            validation_method=validation.ValidationMethods.CREATE_EMPLOYEE
        )
        insert_employees_results.append(res)
    retrieve_result = execute_sql(sql_statement=input_sql_statements.retrive_salary_gt_50000, fetchall=True)
    update_salary_result = execute_sql(
            sql_statement=input_sql_statements.update_salary,
            values={"salary": 60000, "name": "Иван"},
            validation_method=validation.ValidationMethods.UPDATE_DELETE_EMPLOYEE
    )
    employee_deletion_result = execute_sql(
        sql_statement=input_sql_statements.delete_employee,
        values={"name": "Анна"},
        validation_method=validation.ValidationMethods.UPDATE_DELETE_EMPLOYEE
    )
    retrieve_ivan = execute_sql(
        sql_statement=input_sql_statements.retrive_employee_by_name,
        values={"name": "Иван"},
        validation_method=validation.ValidationMethods.UPDATE_DELETE_EMPLOYEE,
        fetchall=True
    )
    retrieve_anna = execute_sql(
        sql_statement=input_sql_statements.retrive_employee_by_name,
        values={"name": "Анна"},
        validation_method=validation.ValidationMethods.UPDATE_DELETE_EMPLOYEE,
        fetchall=True
    )

    return {
        "drop": drop_employees_table_result,
        "create": create_emploees_table_result,
        "insert": insert_employees_results,
        "retrieve": retrieve_result,
        "update": update_salary_result,
        "delete": employee_deletion_result,
        "retrieve_ivan": retrieve_ivan,
        "retrieve_anna": retrieve_anna
    }


if __name__ == "__main__":

    result = script_for_task_1()

    assert result["drop"]["status"] == "success"
    assert result["create"]["status"] == "success"
    for item in result["insert"]:
        assert item["status"] == "success"
    assert result["retrieve"]["status"] == "success"
    assert result["retrieve"]["data_fetched"] == [
        ("test_name_2", "test_position_2", 52000), ("Анна", "Manager", 80000)
    ]
    assert result["update"]["status"] == "success"
    assert result["delete"]["status"] == "success"
    assert result["retrieve_ivan"]["data_fetched"] == [("Иван", 60000)]
    assert result["retrieve_anna"]["data_fetched"] == []
