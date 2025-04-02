from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models.users import User
from database import get_db

router = APIRouter()


@router.get("/users", tags=["users"])
async def read_users():
    return {"users": [{"username": "Rick"}, {"username": "Morty"}]}


@router.get("/users/me", tags=["users"])
async def read_user_me():
    return {"username": "fakecurrentuser"}


@router.get("/users/{username}", tags=["users"])
async def read_user(username: str):
    return {"username": username}


# 获取用户数据 - 查询数据库
@router.get("/user-data", tags=["users"])
async def get_users(db: Session = Depends(get_db)):
    users = db.query(User).order_by(User.id.desc()).all()
    return [user.to_dict() for user in users]

