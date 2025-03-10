from pprint import pprint

import input_sql_task_1
from task_1.app.entrypoint import execute_sql
from task_1.app.infrastructure import validation

execute_sql(sql_statement=input_sql_task_1.drop_employees_table)
print(
    execute_sql(
        sql_statement=input_sql_task_1.create_emploees_table,
        validation_method=validation.ValidationMethods.CREATE_EMPLOYEE
    )
)
values_list = [
    {"name": "test_name_1", "position": "test_position_1", "salary": 83000},
    {"name": "Иван", "position": "Manager", "salary": 25000},
    {"name": "test_name_2", "position": "test_position_2", "salary": 54000},
    {"name": "Анна", "position": "Manager", "salary": 51000},
    {"name": "test_name_3", "position": "test_position_3", "salary": 15000}
]
for values_item in values_list:
    execute_sql(
        sql_statement=input_sql_task_1.insert_employees,
        values=values_item,
        validation_method=validation.ValidationMethods.CREATE_EMPLOYEE
    )

result = execute_sql(sql_statement=input_sql_task_1.retrive_salary_gt_50000, fetchall=True)
pprint(result)

print(
    execute_sql(
        sql_statement=input_sql_task_1.update_salary,
        values={"salary": 60000, "name": "Иван"},
        validation_method=validation.ValidationMethods.UPDATE_EMPLOYEE
    )
)
print(
    execute_sql(
        sql_statement=input_sql_task_1.delete_employee,
        values={"name": 4},
        validation_method=validation.ValidationMethods.DELETE_EMPLOYEE
    )
)