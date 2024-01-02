from fastapi import FastAPI
from enum import Enum

app = FastAPI()

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


class Languages(str, Enum):
    java = "Java"
    python = "Python"
    cpp = "cpp"
    js = "javascript"
@app.get("/code/run/{lang}")

async def runCode(code:str|None = None, lang:Languages = Languages.python):

    returns = {"code": code, "lang": lang}
    # return returns
    if code:
        returns.update({"got code ": code})
    if lang:
        returns.update({"got lang ": lang})

    return returns

