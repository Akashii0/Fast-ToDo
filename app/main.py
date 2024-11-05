from fastapi import FastAPI, Form, Request, Depends, status
from typing import Union
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from . import models
from .database import engine, get_db
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.mount('/static', StaticFiles(directory='static', html=True), name="static")


templates = Jinja2Templates(directory="templates")

@app.get('/')
async def index(request: Request, db: Session = Depends(get_db)):
    todos = db.query(models.ToDo).all()
    return templates.TemplateResponse("index.html",
                                      {"request": request, "todo_list": todos})

@app.post('/add')
def add(request: Request, title: str = Form(...), db: Session = Depends(get_db)):
    new_todo = models.ToDo(title=title)
    db.add(new_todo)
    db.commit()
    # url = app.url_path_for('/')
    return RedirectResponse(url='/', status_code = status.HTTP_303_SEE_OTHER)

@app.get('/update/{todo_id}')
def update(request: Request, todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(models.ToDo).filter(models.ToDo.id == todo_id).first()
    todo.status = not todo.status
    db.commit()
    
    # url = app.url_path_for('/')
    return RedirectResponse(url='/', status_code = status.HTTP_302_FOUND)
    
@app.get("/delete/{todo_id}")
def delete(request: Request, todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(models.ToDo).filter(models.ToDo.id == todo_id).first()
    db.delete(todo)
    db.commit()
    
    # url = app.url_path_for('/')
    return RedirectResponse(url='/', status_code=status.HTTP_302_FOUND)
