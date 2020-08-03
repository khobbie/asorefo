from pydantic import BaseModel


class ApiRegisterUserRequest(BaseModel):
    first_name: str
    last_name: str
    email: str
    password_1: str
    password_2: str


class ApiLoginUserRequest(BaseModel):
    email: str
    password: str
