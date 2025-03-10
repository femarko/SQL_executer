from typing import Optional

from task_1 import app as domain, app as db, app as validation


def execute_sql(
        sql_statement: str,
        validation_method: Optional[validation.ValidationMethods] = None,
        values: Optional[dict] = None,
        fetchall: bool = False
) -> dict[str, str | None]:
    """
    Execute an SQL statement with optional validation and fetching options.

    :param sql_statement: The SQL statement to be executed.
    :param validation_method: Optional; the method to be used for validating input data.
                              Should be one of the `ValidationMethods` or None if no validation is needed.
    :param values: Optional; a dictionary of values to be used in the SQL statement.
                   Keys should match the SQL statement's placeholders if provided.
    :param fetchall: Optional; a boolean indicating whether to fetch all results of a query or not.
    :return: A dictionary with keys "status", "message", and "data_fetched" if applicable.
             "status" indicates success or error of the execution.
             "message" provides error details in case of failure.
             "data_fetched" contains fetched data if `fetchall` is True and execution is successful.
    """
    if fetchall:
        executor = domain.SQLExecutor(
            connection=db.pspg2_conn,
            validator=validation.Validator(validation_models=validation.ValidationModels()),
            fetchall=True
        )
    else:
        executor = domain.SQLExecutor(
            connection=db.pspg2_conn,
            validator=validation.Validator(validation_models=validation.ValidationModels()),
            fetchall=False
        )
    return executor.execute_sql(sql_statement=sql_statement, values=values, validation_method=validation_method)

