from connection.mysql_db import conn
# ApiKeyRequestModel
# from models.generate_key import ApiKeyRequestModel
# UUID
import uuid
# SECRET HASHING
import hashlib
import secrets

# Instantiate
cur = conn.cursor()

# PASSWORD HASHING


def password_hashing(password_1):
    password_1: password_1.upper()

    mystring = password_1 + "Asorefo Team"
    hash_obj = hashlib.sha1(mystring.encode())
    password = hash_obj.hexdigest()
    print(hash_obj.hexdigest())
    return password


def create_user_profile(user):
    password = password_hashing(user.password_1.upper())
    # return password
    cur.callproc("create_user_profile", (user.first_name.upper(
    ), user.last_name.upper(), user.email.upper(),  password.upper()))
    data = cur.fetchone()
    conn.commit()
    return {'code': '000', 'message': 'User registered successfully', 'data': data}


def login_user_profile(user):
    email = user.email.upper()
    password = user.password.upper()
    # hashing my paasword
    password = password_hashing(password)
    # doin my query
    query = "SELECT * FROM `api_consumers` WHERE email = %s AND password = %s LIMIT 1"
    data = cur.execute(
        query, (email.upper(),  password.upper(),))
    data = cur.fetchone()
    if data == None:
        return {"code": '404', 'message': 'No data found', 'data': None}
    return {"code": '000', 'message': 'User login successful', 'data': data}
