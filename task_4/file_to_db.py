from typing import Callable
from typing import Iterable, Optional, Literal

from app.infrastructure.validation import ValidationMethods


class FileToDB:
    """
    FileToDB is a class responsible for interfacing between a file containing employee data and a database.

    Attributes:
        sql_executor: A callable for executing SQL statements.
        file_path: The path to the file containing employee data.
        keys: An iterable of strings representing the keys for the employee data.

    Methods:
        _get_content: Reads the file and returns its contents as a list of dictionaries.
        write_file_content_to_db: Writes the file content into the database.
        retrieve_employees_by_position: Retrieves employees from the database based on their position.
        update_salary: Updates the salary of an employee in the database.
    """
    def __init__(self, sql_executor: Callable[..., dict[str, str | None]], file_path: str, keys: Iterable[str]) -> None:
        """
        Constructor for FileToDB

        Args:
            sql_executor: A callable for executing SQL statements.
            file_path: The path to the file containing employee data.
            keys: An iterable of strings representing the keys for the employee data.
        """
        self.sql_executor = sql_executor
        self.file_path = file_path
        self.keys = keys

    def _get_content(self) -> list[dict[str, Optional[str]]]:
        """
        Reads the file and returns its contents as a list of dictionaries.

        Returns:
            list[dict[str, Optional[str]]]: A list of dictionaries where each dictionary represents an employee
        """
        result_list = []
        with open(self.file_path, 'r') as f:
            for line in f:
                result_list.append(dict((zip(self.keys, line.rstrip("\n").split(",")))))
        return result_list

    def write_file_content_to_db(self) -> list[dict[str, str | None]]:
        """
        Write the content of the file into the database.

        This method gets content making call to `_get_content` method, creates SQL insert statements for each line,
        and executes these statements using the `sql_executor`. The execution results for each statement are collected
        and returned.

        Returns:
            list[dict[str, str | None]]: A list of dictionaries containing the status and message (if any) of each
            SQL execution.
        """
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

    def retrieve_employees_by_position(self, position: str) -> dict[str, str | None]:
        """
        Retrieve employees by position from the database.

        Args:
            position (str): The position to retrieve employees for.

        Returns:
            dict[str, str | None]: A dictionary containing the status and message (if any) of the SQL execution.
        """
        sql_statement = """
                    SELECT *
                    FROM employees_task_4
                    WHERE position = %s;
                    """
        return self.sql_executor(
            sql_statement, ValidationMethods.UPDATE_DELETE_EMPLOYEE, {"position": position}, fetchall=True
        )

    def update_salary(self, name: str, salary: float) -> dict[str, str | None]:
        """
        Update an employee's salary in the database.

        Args:
            name (str): The name of the employee to update.
            salary (float): The new salary of the employee.

        Returns:
            dict[str, str | None]: A dictionary containing the status and message (if any) of the SQL execution.
        """
        sql_statement = """
                    UPDATE employees_task_4
                    SET salary = %s
                    WHERE name = %s;
                    """
        return self.sql_executor(
            sql_statement, ValidationMethods.UPDATE_DELETE_EMPLOYEE, {"salary": salary, "name": name}
        )

