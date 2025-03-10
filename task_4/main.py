from app.entrypoint import execute_sql
from task_4.file_to_db import FileToDB


file_to_db = FileToDB(file_path="example.csv", sql_executor=execute_sql, keys=("name", "position", "salary"))
print(file_to_db.write_file_content_to_db())
print(file_to_db.retrieve_employees_by_position(position="test_position_3"))
print(file_to_db.update_salary(name="test_name_2", salary=200000))