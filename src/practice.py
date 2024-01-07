import subprocess
from fastapi import FastAPI
from enum import Enum
from pydantic import BaseModel
import os
import subprocess

app = FastAPI()


### SUBPROCESS ###
code = """
for i in range(3)
    print("Hello world")
"""

result = subprocess.run(['python3'],input=code, capture_output=True, encoding='UTF-8')

show = result.stdout if len(result.stderr) == 0 else "error found\n"+result.stderr
print(show)


@app.get("/")
async def root():
    return {"message": "Hello, Faisal!"}

uList = ["3241","1121","1122","1123","1124","1125","1126"]

class UName(str,Enum):
    a = "Farid"
    b = "Faruk"

@app.get("/username/{u_name}")
async def get_username(u_name: UName):
    if u_name == UName.a:
        return {"message": "Hi Farid!"}
    if u_name == UName.b:
        return {"message": "Hi  Faruk!"}

@app.get("/users/{u_id}")

async def users(u_id):
    if u_id in uList:
        return {"message": "This is a valid u_id"}
    else:
        return {"message": "User id not found"}


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict