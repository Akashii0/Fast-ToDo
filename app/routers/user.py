from typing import Any, Dict

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.models import User

from .. import models, schemas, utils
from ..database import get_db

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # Hash the password - user.password

    # hashed_password = pwd_context.hash(user.password)
    hashed_password = utils.hash(user.password)
    user.password = hashed_password

    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


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
