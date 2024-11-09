from fastapi import FastAPI, Form, Request, Depends, status
from typing import Union
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from . import models
from .database import engine, get_db
from sqlalchemy.orm import Session
from .routers import crud, auth, user

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.mount("/static", StaticFiles(directory="static", html=True), name="static")


templates = Jinja2Templates(directory="templates")


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(crud.router)
app.include_router(auth.router)
app.include_router(user.router)
