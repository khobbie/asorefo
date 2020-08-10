import time
from fastapi import Depends, FastAPI, Header, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
# TYPE CHECKER
from typing import List, Optional

from routers import users, generate_key
# Import  API HEADER CHECK
from functions.check_api_headers import check_headers

# Request
import requests

app = FastAPI()

app = FastAPI(title="Asorefo Backend RestfulAPI")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


async def get_token_header(x_token: str = Header(...)):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


app.include_router(
    generate_key.router,
    prefix="/api-services",
    tags=["api-services"],
)


app.include_router(
    users.router,
    prefix="/users",
    tags=["users"],
    dependencies=[Depends(check_headers)]
)


@app.get("/external-api-call", tags=["external api call"])
def read_root():
    resp = requests.get('http://jsonplaceholder.typicode.com/posts')
    if resp.status_code != 200:
        # This means something went wrong.
        raise HTTPException(
            status_code=401, detail='GET /tasks/ {}'.format(resp.status_code))
        # raise ApiError('GET /tasks/ {}'.format(resp.status_code))
    return {'data': resp.json()}
    # for todo_item in resp.json():
    #     print('{} {}'.format(todo_item['id'], todo_item['summary']))
    # return {"Hello": "World"}

# app.include_router(
#     items.router,
#     prefix="/items",
#     tags=["items"],
#     dependencies=[Depends(get_token_header)],
#     responses={404: {"description": "Not found"}},
# )
