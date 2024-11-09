from typing import Any, Dict

from fastapi import APIRouter, Depends, Form, status
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from app.models import User

from .. import models, schemas, utils
from ..database import get_db

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_user(
    db: Session = Depends(get_db),
    username: str = Form(),
    password: str = Form(),
):
    # Hash the password - user.password

    # hashed_password = pwd_context.hash(user.password)
    hashed_password = utils.hash(password)

    # new_user = User(**user.model_dump(username=username, password=password))
    new_user = User(username=username, password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    print(new_user)
    return RedirectResponse(url="/login", status_code=status.HTTP_307_TEMPORARY_REDIRECT)


def get_user(self):
    return self.sess.query(models.User).all()


def get_user_by_username(self, username: str):
    return self.sess.query(User).filter(User.username == username).first()


def update_user(self, id: int, details: Dict[str, Any]) -> bool:
    try:
        self.sess.query(User).filter(User.id == id).update(details)
        self.sess.commit()
    except:
        return False
    return True


def delete_user(self, id: int) -> bool:
    try:
        self.sess.query(User).filter(User.id == id).delete()
        self.sess.commit()
    except:
        return False
    return True
