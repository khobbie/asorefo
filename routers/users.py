from fastapi import APIRouter


# import db
from connection.db import conn

# from postgress
# from .database.mysql_db import conn
router = APIRouter()


@router.get("/users/", tags=["users"])
async def read_users():
    cur = conn.cursor()
    cur.execute("SELECT * FROM STUDENTS")
    # cur.callproc("getAllPayment")
    # cur.callproc("getAllAvailablePaidPackageByEmployerId", ('3'))

    rows = cur.fetchone()
    return rows
    # query = "SELECT * FROM code_desc"
    # data = conn.execute(query).fetchall()
    # return data


@router.get("/users/me", tags=["users"])
async def read_user_me():
    return {"username": "fakecurrentuser"}


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
