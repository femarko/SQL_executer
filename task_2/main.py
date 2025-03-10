import pprint
from typing import Literal
from collections import OrderedDict


def employees_processor(employees: list[dict[Literal["name", "position", "salary"], str | float | int]]):
    return OrderedDict(
        {"salary_gt_50000": [employee["name"] for employee in employees if employee["salary"] > 50000],
        "average_salary": round((sum([employee["salary"] for employee in employees]) / len(employees)), 2),
        "employees_sorted": sorted(employees, key=lambda employee: employee["salary"], reverse=True)
         }
    )


if __name__ == "__main__":
    res = employees_processor(
        employees=[
            {"name": "Иван", "position": "разработчик", "salary": 55000},
            {"name": "Анна", "position": "аналитик", "salary": 48000},
            {"name": "Петр", "position": "тестировщик", "salary": 52000}
        ]
    )
    pprint.pprint(res)