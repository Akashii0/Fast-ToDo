from fastapi import (
    APIRouter,
    Depends,
    Form,
    HTTPException,
    Request,
    status,
)
from fastapi.responses import RedirectResponse
# from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session

from app import database, models, oauth2, schemas, utils
from app.routers.crud import templates

router = APIRouter(tags=["Authentication"])
router.mount("/static", StaticFiles(directory="static", html=True), name="static")


@router.get("/login")
def showlogin(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@router.post("/login", response_model=schemas.Token)
def login(
    username: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(database.get_db),
):
    user = db.query(models.User).filter(models.User.username == username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials"
        )

    if not utils.verify(password, user.password):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials"
        )

    # Create a Token
    # Return token

    access_token = oauth2.create_access_token(data={"user_id": user.id})

    resp = RedirectResponse(url='/todo', status_code=303)

    resp.set_cookie(key="token", value=access_token)

    return resp

