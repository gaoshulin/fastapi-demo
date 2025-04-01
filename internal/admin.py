from fastapi import APIRouter, Depends, HTTPException
from dependencies import get_token_header

router = APIRouter(
    prefix="/admin",
    tags=["admin"],
    dependencies=[Depends(get_token_header)],
    responses={418: {"description": "I'm a teapot"}},
)


@router.get("/")
async def read_main():
    return {"message": "Hello World"}


@router.post("/")
async def update_admin():
    return {"message": "Admin getting schwifty"}

