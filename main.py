from fastapi import FastAPI, Depends
from dependencies import get_query_token
from routers import items, users
from internal import admin

app = FastAPI(dependencies=[Depends(get_query_token)])
app.include_router(users.router)
app.include_router(items.router)
app.include_router(admin.router)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}

    