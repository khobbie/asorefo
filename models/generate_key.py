from pydantic import BaseModel


class ApiRegisterRequestModel(BaseModel):
    first_name: str
    last_name: str
    email: str
    password_1: str
    password_2: str


class ApiLoginRequestModel(BaseModel):
    email: str
    password: str
