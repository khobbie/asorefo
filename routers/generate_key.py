# fastApi
import secrets
import uuid
from models.generate_key import ApiRegisterRequestModel, ApiLoginRequestModel
from fastapi import APIRouter
# from mysql
from connection.mysql_db import conn
# ApiRegisterRequestModel
# Hash
import hashlib

# UUID
# SECRET HASHING
# create api consumer
# from functions import api_consumer_func

# instantiate APIRouter
router = APIRouter()

cur = conn.cursor()


def password_hashing(password_1):
    password_1: password_1.upper()

    mystring = password_1 + "Asorefo Team"
    hash_obj = hashlib.sha1(mystring.encode())
    password = hash_obj.hexdigest()
    return password
    print(hash_obj.hexdigest())


def create_api_consumer(user):
    x_api_key = uuid.uuid5(uuid.NAMESPACE_DNS, "kite.com")
    x_api_key = '{}'.format(x_api_key)
    x_api_secret = secrets.token_hex(6)
    password = password_hashing(user.password_1.upper())
    cur.callproc("create_api_consumer", (user.first_name.upper(), user.last_name.upper(),
                                         user.first_name.upper(), user.email.upper(), None, password.upper(), x_api_key.upper(), x_api_secret.upper()))
    conn.commit()
    return {'code': '000', 'message': 'User registered successfully', 'data': {'password': password, 'x-api-key': x_api_key, 'x-api-secret': x_api_secret}}


def login_api_consumer(user):
    email = user.email.upper()
    password = user.password.upper()
    password = password_hashing(password)

    # with conn.cursor() as cur:
    #     # Read a single record
    #     sql = "SELECT * FROM `api_consumers` WHERE email = %s AND password = %s LIMIT 1"
    #     cur.execute(sql, (email.upper(),  password.upper(),))
    #     result = cur.fetchone()
    #     print(result)
    #     return result

    # return {email, password}
    query = "SELECT * FROM `api_consumers` WHERE email = %s AND password = %s LIMIT 1"
    data = cur.execute(
        query, (email.upper(),  password.upper(),))
    data = cur.fetchone()
    if data == None:
        return {"code": '404', 'message': 'No data found', 'data': None}
    return {"code": '000', 'message': 'User login successful', 'data': data}


@ router.post("/register", tags=["api-services"])
async def register_for_api_service(user: ApiRegisterRequestModel):
    if(user.password_1 != user.password_2):
        return {"code": '101', 'message': 'Both password do not match', 'data': None}

    return create_api_consumer(user)


@ router.post("/login", tags=["api-services"])
async def login_for_api_service(user: ApiLoginRequestModel):
    return login_api_consumer(user)
