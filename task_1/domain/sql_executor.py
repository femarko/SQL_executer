import dataclasses
import enum
from typing import Optional
from collections import OrderedDict

import psycopg2

from app.infrastructure import validation
from app.domain import custom_errors
from app.infrastructure.validation import ValidationMethods


class ResultStatus(str, enum.Enum):
    SUCCESS = "success"
    ERROR = "error"


@dataclasses.dataclass
class SQLExecutorResult:
    status: ResultStatus
    message: Optional[str] = None
    data_fetched: Optional[str] = None


class SQLExecutor:
    def __init__(self, connection, validator: validation.Validator, fetchall: bool = False):
        self.connection = connection
        self.err_mapper = {IndexError: 'Values for SQL statement are missing.', psycopg2.ProgrammingError: 'SQL syntax error.'}
        self.validator = validator
        self.fetchall = fetchall

    def execute_sql(
            self, sql_statement: str,
            validation_method: ValidationMethods,
            values: Optional[dict] = None,
    ) -> tuple[str, Optional[str]]:
        if values is not None:
            frozen_values: OrderedDict[str, str | float] = OrderedDict(values)
            if not validation_method:
                raise ValueError("Validation method is not specified.")
            try:
                validation_method = getattr(self.validator, validation_method.value)
            except AttributeError:
                raise NotImplementedError(f"Validation method '{validation_method}' is not implemented.")
            validated_data =  validation_method(**frozen_values)
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
            message = self.err_mapper.get(type(e), str(e))
            result = SQLExecutorResult(status=ResultStatus.ERROR.value, message=message)
            return {"status": result.status, "message": result.message}
        if self.fetchall:
            try:
                result = SQLExecutorResult(status=ResultStatus.SUCCESS.value, data_fetched=cursor.fetchall())
            except Exception as e:
                message = self.err_mapper.get(type(e), str(e))
                result = SQLExecutorResult(status=ResultStatus.ERROR.value, message=message)
            return {"status": result.status, "message": result.message, "data_fetched": result.data_fetched}
        result = SQLExecutorResult(status=ResultStatus.SUCCESS.value)
        return {"status": result.status, "message": result.message}
