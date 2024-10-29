from fastapi import FastAPI, Form, Request, Depends, status
from typing import Union
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from . import models
from .database import engine, get_db
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)

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

@app.post('/add')
def add(request: Request, title: str = Form(...) ,db: Session = Depends(get_db)):
    new_todo = models.ToDo(title=title)
    db.add(new_todo)
    db.commit()
    url = app.url_path_for("home")
    return RedirectResponse(redirect_url=url, status_code = status.HTTP_303_SEE_OTHER)

