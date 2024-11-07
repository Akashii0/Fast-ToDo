from fastapi import FastAPI, Form, HTTPException, Request, Depends, status, APIRouter
from typing import Union
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from .. import models, schemas, oauth2
from ..database import engine, get_db
from sqlalchemy.orm import Session

router = APIRouter(
    tags=['ToDos']
)
router.mount('/static', StaticFiles(directory='static', html=True), name="static")

templates = Jinja2Templates(directory="templates")


@router.get('/')
async def index(request: Request, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    todos = db.query(models.ToDo).filter(models.ToDo.owner_id == current_user.id).all()
    
    # if todos.owner_id != current_user.id:
    #     raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
    #                         detail="Not authorized to perform requested action")
    
    return templates.TemplateResponse("index.html",
                                      {"request": request, "todo_list": todos})

@router.post('/add')
def add(request: Request, title: str = Form(...), db: Session = Depends(get_db)):
    new_todo = models.ToDo(content=title)
    db.add(new_todo)
    db.commit()

    return RedirectResponse(url='/', status_code = status.HTTP_303_SEE_OTHER)

@router.get('/update/{todo_id}')
def update(request: Request, todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(models.ToDo).filter(models.ToDo.id == todo_id).first()
    todo.status = not todo.status
    db.commit()
    
    return RedirectResponse(url='/todo', status_code = status.HTTP_302_FOUND)
    
@router.get("/delete/{todo_id}")
def delete(request: Request, todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(models.ToDo).filter(models.ToDo.id == todo_id).first()
    db.delete(todo)
    db.commit()
    
    return RedirectResponse(url='/todo', status_code=status.HTTP_302_FOUND)


