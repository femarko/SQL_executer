import psycopg2
import dataclasses
import enum
from typing import Optional
from collections import OrderedDict

from task_1.app.infrastructure import validation
from task_1.app.infrastructure.validation import ValidationMethods


class ResultStatus(str, enum.Enum):
    SUCCESS = "success"
    ERROR = "error"


@dataclasses.dataclass
class SQLExecutorResult:
    status: ResultStatus
    message: Optional[str] = None
    data_fetched: Optional[str] = None



class SQLExecutor:
    """
    SQLExecutor is responsible for executing SQL statements with optional validation and fetching results.

    Attributes:
        connection: The database connection object.
        validator: An instance of the Validator class used for validating SQL operations.
        fetchall: A boolean indicating whether to fetch all results of a query or not.

    Methods:
        __init__: Initializes the SQLExecutor with a database connection, a validator, and a fetchall option.
        execute_sql: Executes a given SQL statement with optional validation and parameterized values.
    """
    def __init__(self, connection, validator: validation.Validator, fetchall: bool = False) -> None:
        """
        Initialize the SQLExecutor with a database connection, a validator, and a fetchall option.

        :param connection: The database connection object to be used for executing SQL statements.
        :param err_mapper: A dictionary mapping exceptions to error messages.
        :param validator: An instance of the Validator class used for validating SQL operations.
        :param fetchall: A boolean indicating whether to fetch all results of a query or not.
        """
        self.connection = connection
        self.err_mapper = {
            IndexError: 'Values for SQL statement are missing.', psycopg2.ProgrammingError: 'SQL syntax error.'
        }
        self.validator = validator
        self.fetchall = fetchall

    def execute_sql(self, sql_statement: str,
                    validation_method: ValidationMethods,
                    values: Optional[dict] = None,) -> dict[str, Optional[str]]:
        """
        Execute the provided SQL statement with optional validation and parameterized values.

        :param sql_statement: The SQL statement to be executed.
        :param validation_method: The validation method to be used for validating input data.
                                  It should be one of the `ValidationMethods` or None if no validation is needed.
        :param values: Optional dictionary of values to be used in the SQL statement.
                       If provided, the keys should match the SQL statement's placeholders.
        :return: A dictionary with keys "status", "message", and optional "data_fetched".
                 "status" indicates the success or error of the execution.
                 "message" provides error details in case of failure.
                 "data_fetched" contains fetched data if `fetchall` is True and the execution is successful.
        :raises ValueError: If the validation method is not specified when values are provided.
        :raises NotImplementedError: If the specified validation method is not implemented.
        """
        if values is not None:
            frozen_values: OrderedDict[str, str | float] = OrderedDict(values)
            if not validation_method:
                raise ValueError("Validation method is not specified.")
            try:
                validation_method = getattr(self.validator, validation_method.value)
            except AttributeError:
                raise NotImplementedError(f"Validation method '{validation_method}' is not implemented.")
            validated_data = validation_method(**frozen_values)
            frozen_validated_values = OrderedDict.fromkeys(frozen_values.keys())
            for key in frozen_validated_values.keys():
                frozen_validated_values[key] = validated_data[key]
            values = tuple(value for key, value in frozen_validated_values.items())
        else:
            values = tuple()
        with self.connection as c:
            cursor = c.cursor()
        try:
            cursor.execute(sql_statement, values)
            c.commit()
        except Exception as e:
            message = self.err_mapper.get(type(e), str(e))  # type: ignore
            return {"status": "error", "message": message}
        if self.fetchall:
            try:
                result = {"status": "success", "data_fetched": cursor.fetchall()}
            except Exception as e:
                message = self.err_mapper.get(type(e), str(e))  # type: ignore
                result = {"status": "error", "message": message}
            return result
        return {"status": "success"}
