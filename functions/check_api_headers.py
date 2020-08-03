# TYPE CHECKER
from typing import List, Optional
# FASTAPI
from fastapi import Depends, FastAPI, Header, HTTPException, Request
# IMPORT TIME
import time
# Database connection
from connection.mysql_db import conn
# INSTANTIATE FASTAPI
app = FastAPI()

# Instantiate
cur = conn.cursor()


@app.middleware("http")
async def check_headers(
    request: Request,
    x_api_key: str = Header(..., convert_underscores=True),
    x_api_secret: str = Header(..., convert_underscores=True)
):
    # CHECK IF REQUIRED HEADERS ARE EMPTY
    if (x_api_key is None) or (x_api_secret is None):
        raise HTTPException(status_code=401, detail={
                            "code": '401', 'message': 'User unauthorized api consumer', 'data': None})
    query = "SELECT * FROM `api_consumers` WHERE x_api_key = %s AND x_api_secret = %s LIMIT 1"
    data = cur.execute(
        query, (x_api_key.upper(),  x_api_secret.upper(),))
    data = cur.fetchone()
    # IF QUERY IS EMPTY
    if data == None:
        raise HTTPException(status_code=401, detail={
                            "code": '401', 'message': 'User unauthorized api consumer', 'data': None})
