from fastapi import FastAPI
from enum import Enum
from pydantic import BaseModel
import os
import subprocess

app = FastAPI()


class UName(str,Enum):
    a = "Farid"
    b = "Faruk"


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

class Code_body(BaseModel):
    code: str | None = None
    lang: Languages
    u_name: UName | None = None


@app.post("/codesend/")
async def send(codes:Code_body):
    code_dict = dict(codes)
    if codes.code:

        fName = 't.py'
        with open(fName,'w') as f:
            f.write(codes.code)

        if os.path.isfile(fName):
            code_dict.update({"FileInfo": fName+" file created"})
            result = subprocess.run(['python3',fName] ,capture_output=True, encoding='UTF-8')
            show = result.stdout if len(result.stderr) == 0 else "error found\n" + result.stderr
            code_dict.update({"output":show})
        code_dict.update({"test":codes.code.upper()})

    return code_dict


