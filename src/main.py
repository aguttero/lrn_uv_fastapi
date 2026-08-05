from typing import Annotated

from fastapi import Cookie, FastAPI

app = FastAPI()


@app.get("/items1/")
async def read_items1(ads_id: Annotated[str | None, Cookie()] = None):
    return {"ads_id": ads_id}

from fastapi import Header
@app.get("/items2/")
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


@app.post("/items/")
async def create_item(item: Item) -> Item:
    return item


@app.get("/items/")
async def read_items() -> list[Item]:
    return [
        Item(name="Portal Gun", price=42.0),
        Item(name="Plumbus", price=32.0),
    ]
