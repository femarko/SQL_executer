import dataclasses
import enum
import pydantic

from typing import TypeVar, Optional

from task_1.app.domain import custom_errors

PydanticModel = TypeVar("PydanticModel", bound=pydantic.BaseModel)


class CreateEmployee(pydantic.BaseModel):
    name: str
    position: str
    salary: float

class UpdateDeleteEmployee(pydantic.BaseModel):
    name: Optional[str] = None
    position: Optional[str] = None
    salary: Optional[float] = None

class CreateProduct(pydantic.BaseModel):
    name: str
    price: float
    quantity: int


class UpdateDeleteProduct(pydantic.BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    quantity: Optional[int] = None


@dataclasses.dataclass
class ValidationModels:
    create_employee = CreateEmployee
    update_delete_employee = UpdateDeleteEmployee
    create_products = CreateProduct
    update_delete_product = UpdateDeleteProduct

class ValidationMethods(str, enum.Enum):
    CREATE_EMPLOYEE = "validate_employee_creation_data"
    UPDATE_DELETE_EMPLOYEE = "validate_update_delete_employee_data"
    CREATE_PRODUCT = "validate_product_creation_data"
    UPDATE_DELETE_PRODUCT = "validate_update_delete_product_data"

class Validator:
    """
    The Validator class is used to validate data against pydantic models.

    The Validator receives a ValidationModels object in its constructor and
    provides methods to validate data against the models defined in the
    ValidationModels object.

    The `validate_data` method is a generic method that takes a model and
    validates the given data against it. All the other methods are just
    wrappers around this method.

    :param validation_models: An instance of the ValidationModels dataclass.
    """
    def __init__(self, validation_models: ValidationModels):
        self.validation_models = validation_models

    @staticmethod
    def _validate_data(data: dict, validation_model):
        try:
            return validation_model.model_validate(data).model_dump(exclude_unset=True)
        except pydantic.ValidationError as e:
            raise custom_errors.ValidationError(e.errors())

    def validate_employee_creation_data(self, **employee_data: dict):
        return self._validate_data(validation_model=self.validation_models.create_employee, data=employee_data)

    def validate_product_creation_data(self, **product_data: dict):
        return self._validate_data(validation_model=self.validation_models.create_products, data=product_data)

    def validate_update_delete_employee_data(self, **employee_data: dict):
        return self._validate_data(validation_model=self.validation_models.update_delete_employee, data=employee_data)

    def validate_update_delete_product_data(self, **product_data: dict):
        return self._validate_data(validation_model=self.validation_models.update_delete_product, data=product_data)
