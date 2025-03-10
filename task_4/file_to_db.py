from typing import Callable
from typing import Iterable, Optional, Literal

from app.infrastructure.validation import ValidationMethods


class FileToDB:
    def __init__(self, sql_executor: Callable[..., dict[str, str]], file_path: str, keys: Iterable[str]) -> None:
        self.sql_executor = sql_executor
        self.file_path = file_path
        self.keys = keys

    def _get_content(self) -> list[dict[str, Optional[str]]]:
        result_list = []
        with open(self.file_path, 'r') as f:
            for line in f:
                result_list.append(dict((zip(self.keys, line.rstrip("\n").split(",")))))
        return result_list

    def write_file_content_to_db(self) -> list[dict[Literal["status", "message", "data_fetched"], str]]:
        sql_statement = """
                    INSERT INTO employees_task_4 (name, position, salary)
                    VALUES (%s, %s, %s);
                    """
        sql_statements_with_values = [
            {"sql_statement": sql_statement, "values": value} for value in self._get_content()
        ]
        results = []
        for sttmnt_with_val in sql_statements_with_values:
            result = self.sql_executor(
                sttmnt_with_val["sql_statement"], ValidationMethods.CREATE_EMPLOYEE, sttmnt_with_val["values"]
            )
            results.append(result)
        return results

    def retrieve_employees_by_position(self, position: str) -> dict[Literal["status", "message", "data_fetched"], str]:
        sql_statement = """
                    SELECT *
                    FROM employees_task_4
                    WHERE position = %s;
                    """
        return self.sql_executor(
            sql_statement, ValidationMethods.UPDATE_EMPLOYEE, {"position": position}, fetchall=True
        )

    def update_salary(self, name: str, salary: float) -> dict[Literal["status", "message", "data_fetched"], str]:
        sql_statement = """
                    UPDATE employees_task_4
                    SET salary = %s
                    WHERE name = %s;
                    """
        return self.sql_executor(sql_statement, ValidationMethods.UPDATE_EMPLOYEE, {"salary": salary, "name": name})

