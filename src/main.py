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

@app.get("/gimmefroot/{frootname}")
def gimmeDat(frootname: fruits):
    if frootname is fruits.apple:
        return "You tryna keep the doctor away huh!!"
    elif frootname is fruits.pear:
        return "You nasty ahh for eating dis stuff..."
    elif frootname is fruits.banana:
        return "Based fruit choice"
    else:
        return "You're not an average fruit enjoyer are you?"
    
@app.post("/newfroot/")
async def create_froot(item: Item):
    item.name = item.name.capitalize()
    return item
