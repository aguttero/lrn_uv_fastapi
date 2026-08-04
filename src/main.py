from fastapi import FastAPI, HTTPException
import sys
# import os

app = FastAPI()

@app.get ("/")
async def root():
    return {"message": "Hello World! This is Panorámix"}

@app.get("/getpythonversion")
async def get_python_version():
    return {"version": sys.version}

# @app.get("/getenv")
# def get_all_env_vars():
#     # Converts the environment mapping into a standard Python dictionary
#     return dict(os.environ)

# @app.get("/getenv/{var_name}")
# def get_specific_env_var(var_name: str):
#     value = os.getenv(var_name)

    # if value is None:
        # raise HTTPException(status_code=404, detail="Environment variable not found")

    # return {var_name: value}

@app.get("/intitems/{item_id}")
async def read_int_item(item_id:int):
    return {"item_id": item_id}

@app.get("/stringitem/{item_id}")
async def read_str_item(item_id:str):
    return {"item_id": item_id}

# Predefined Path Values
from enum import Enum

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}

# FILE PATHS in PATH Parameter
# Documentation will tell is a regular path parameeter
@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}

# QUERY Parameters
fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get("/slice_items/")
async def slice_list_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]

# QUERY OPTIONAL parameter
@app.get("/opt_par_items/{item_id}")
async def read_item_and_opt_param(item_id: str, q: str | None = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}

@app.get("/items2/{item_id}")
async def read_item_bool(item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})

    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

# MULTIPLE Path and Query Parameters
@app.get("/users/{user_id}/items/{item_id}")
async def read__multiple_items(user_id: int, item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

# Request BODY
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.model_dump()
    if item.tax is not None:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    print (f"Item type= {type(item)}")
    print (f"Item= {item!r}")
    print (f"Item name = {item.name!r}")
    return item

# UPDATE
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item, q: str | None = None):
    result = {"item_id": item_id, **item.model_dump()}
    if q:
        result.update({"q": q})
    return result

# VALIDATION: Query parameters and string and regular expressions
# import ANNOTATED, QUERY
from typing import Annotated
from fastapi import Query

@app.get("/items3/")
async def read_validate_items(q: Annotated[str | None, Query(min_length=3, max_length=15,  pattern="^fixedquery$")] = None): # =Nonoe is the default value
    results = {"things": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        print(results['things'])
        print("---")
        print(results.values())
        results['things'].append({"q": q})
        results.update ({"q":q})
        # results.items.append({"q": q})
    return results




# VALIDATION for
# Query parameter Query()
# Path paramenter Path()
# Body contente Body()
# Header content Header()
# Cookie content Cookie()
