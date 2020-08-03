import time
from fastapi import Depends, FastAPI, Header, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
# TYPE CHECKER
from typing import List, Optional

from routers import users, generate_key
# Import  API HEADER CHECK
from functions.check_api_headers import check_headers

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

# app.include_router(
#     items.router,
#     prefix="/items",
#     tags=["items"],
#     dependencies=[Depends(get_token_header)],
#     responses={404: {"description": "Not found"}},
# )
