from typing import Annotated

from fastapi import Cookie, FastAPI

app = FastAPI()


@app.get("/itemscookie/")
async def read_items1(ads_id: Annotated[str | None, Cookie()] = None):
    return {"ads_id": ads_id}

from fastapi import Header
@app.get("/itemsheader/")
async def read_items_2(user_agent: Annotated[str | None, Header()] = None):
    print (type(user_agent))
    print (user_agent)
    return {"User-Agent": user_agent}

from pydantic import BaseModel
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list[str] = []

# Response Model - Return type -> Item
@app.post("/items1/")
async def create_item(item: Item) -> Item:
    return item

@app.get("/items1/")
async def read_items() -> list[Item]:
    return [
        Item(name="Portal Gun", price=42.0),
        Item(name="Plumbus", price=32.0),
    ]

# Response Model - Return type Response Model
# To avoid editor type error
from typing import Any
@app.post("/items2/", response_model=Item)
async def create_item_response_model (item: Item) -> Any:
    return item

@app.get("/items2/", response_model=list[Item])
async def read_items_response_model() -> Any:
    return [
        {"name": "Portal Gun", "price": 42.0},
        {"name": "Plumbus", "price": 32.0},
    ]

# Input and output model
from pydantic import EmailStr

class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: str | None = None


class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None


@app.post("/user/", response_model=UserOut)
async def create_user(user: UserIn) -> Any:
    return user # filters the pwd field by modelling by response_model UserOut

# Other way to do the same with response type with better tooling type checking support.

class BaseUser(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None


class UserIn2(BaseUser):
    password: str


@app.post("/user2/")
async def create_user2(user: UserIn2) -> BaseUser:
    return user
