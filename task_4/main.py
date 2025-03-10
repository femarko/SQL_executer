from typing import Callable

from app.entrypoint import execute_sql
from task_4 import input_sql_statements
from task_4.file_to_db import FileToDB


def script_for_task_4(file_to_db: FileToDB, sql_executor: Callable, *args) -> dict[str, list[dict[str, str | None]]]:
    file_to_db_result = file_to_db.write_file_content_to_db()
    retrieve_result: dict[str, str | None] = file_to_db.retrieve_employees_by_position(position="test_position_3")
    update_salary_result = file_to_db.update_salary(name="test_name_2", salary=200000)
    retrieve_after_update = file_to_db.retrieve_employees_by_position(position="test_position_2")
    return {
        "file_to_db_result": file_to_db_result,
        "retrieve_result": retrieve_result,
        "update_salary_result": update_salary_result,
        "retrieve_after_update": retrieve_after_update
    }


if __name__ == "__main__":
    execute_sql(sql_statement=input_sql_statements.drop_employees_task_4_table)
    execute_sql(sql_statement=input_sql_statements.create_emploees_task_4_table)
    file_to_db = FileToDB(file_path="example.csv", sql_executor=execute_sql, keys=("name", "position", "salary"))
    result: dict = script_for_task_4(file_to_db=file_to_db, sql_executor=execute_sql)

    for item in result["file_to_db_result"]:
        assert item["status"] == "success"
    assert result["retrieve_result"]["status"] == "success"
    assert result["retrieve_result"]["data_fetched"] == [(3, "test_name_3", "test_position_3", 150000)]
    assert result["retrieve_after_update"]["data_fetched"] == [(2, "test_name_2", "test_position_2", 200000)]
    assert result["update_salary_result"]["status"] == "success"