from fastapi import FastAPI, Request
from typing import Union
from fastapi.templating import Jinja2Templates

app = FastAPI()

# @app.get('/')
# def read_root():
#     return {"Message":"Hello World."}

# @app.get('items/{item_id}')
# def getItems(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}

templates = Jinja2Templates(directory="templates")

@app.get('/')
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

