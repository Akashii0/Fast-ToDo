from fastapi import FastAPI
from typing import Union

app = FastAPI()

@app.get('/')
def read_root():
    return {"Message":"Hello World."}

@app.get('items/{item_id}')
def getItems(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

