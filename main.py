import time
from fastapi import Depends, FastAPI, Header, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
# TYPE CHECKER
from typing import List, Optional

from routers import users, generate_key

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


@app.middleware("http")
async def add_process_time_header(
    request: Request,
    call_next,
    x_api_key: Optional[str] = Header(None, convert_underscores=True),
    x_api_secret: Optional[str] = Header(None, convert_underscores=True)
):
    if (x_api_key is None) or (x_api_secret is None):
        raise HTTPException(status_code=401, detail={
                            "code": '401', 'message': 'User unauthorized api consumer', 'data': None})

    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response

app.include_router(
    users.router,
    prefix="/users",
    tags=["users"],
)

# app.include_router(
#     items.router,
#     prefix="/items",
#     tags=["items"],
#     dependencies=[Depends(get_token_header)],
#     responses={404: {"description": "Not found"}},
# )
