from fastapi import FastAPI
from enum import Enum
from pydantic import BaseModel

class fruits(str, Enum):
    apple = "apple"
    pear = "pear"
    banana = "banana"

class Item(BaseModel):
    name: str
    price: float

app = FastAPI()

@app.get("/")
def testGet():
    return "HIIIII"


