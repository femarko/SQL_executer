from typing import Literal, Optional

import app.domain.sql_executor as domain
import app.infrastructure.db_connection as db
import app.infrastructure.validation as validation



# todo: implemet to tasks 1, 3, 4
def execute_sql(
        sql_statement: str,
        validation_method: Optional[validation.ValidationMethods] = None,
        values: Optional[dict] = None,
        fetchall: bool = False
) -> tuple[str, Optional[str]]:
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


def executor_for_task_4(sql_statement: str):
    execute_sql()
