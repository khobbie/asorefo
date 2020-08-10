from connection.mysql_db import conn

# IMPORT FASTAPI
from fastapi import HTTPException
# UUID
import uuid
# SECRET HASHING
import hashlib
import secrets

# Instantiate
cur = conn.cursor()

# PASSWORD HASHING


def if_email_already_exist(email):
    # doin my query
    query = "SELECT * FROM `user_profile` WHERE email = %s LIMIT 1"
    data = cur.execute(
        query, (email.upper(),))
    data = cur.fetchone()
    if data != None:
        raise HTTPException(status_code=200, detail={
                            "code": '333', 'message': "User with " + email + " already exist", 'data': None})


def password_hashing(password_1):
    password_1: password_1.upper()

    mystring = password_1 + "Asorefo Team"
    hash_obj = hashlib.sha1(mystring.encode())
    password = hash_obj.hexdigest()
    print(hash_obj.hexdigest())
    return password


def create_user_profile(user):
    # Hash
    password = password_hashing(user.password_1.upper())
    # CHECK USER WITH EMAIL ALREADY EXIST IN DATABASE
    if_email_already_exist(user.email)
    # CALL THE CREATE CONSUMER PROCEDURE
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
