from fastapi import FastAPI, APIRouter, Header, Request

# TYPE CHECKER
from typing import List, Optional


# import db
from connection.db import conn
# User Model
from models.user_model import ApiRegisterUserRequest, ApiLoginUserRequest
# import function
from functions.users_func import password_hashing, create_user_profile, login_user_profile

# from postgress
# from .database.mysql_db import conn
router = APIRouter()
app = FastAPI()


@router.post("/register", tags=["users"])
async def user_registeration(user: ApiRegisterUserRequest):
    if(user.password_1 != user.password_2):
        return {"code": '101', 'message': 'Both password do not match', 'data': None}
    return create_user_profile(user)


@router.post("/login", tags=["users"])
async def user_login(
        user: ApiLoginUserRequest
):
    return 'hello'
    # return login_user_profile(user)
    # return {"x-api-key": x_api_key, "x-api-secret": x_api_secret}


@router.get("/users/{username}", tags=["users"])
async def read_user(username: str):

    return {"username": username}


@router.put(
    "/{item_id}",
    tags=["custom"],
    responses={403: {"description": "Operation forbidden"}},
)
async def update_item(item_id: str):
    if item_id != "foo":
        raise HTTPException(
            status_code=403, detail="You can only update the item: foo")
    return {"item_id": item_id, "name": "The Fighters"}
