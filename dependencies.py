from fastapi import Header, HTTPException

"""
    依赖项
    x_token 和 token 测试写死的，实际开发中应该从数据库中获取
"""

async def get_token_header(x_token: str = Header(...)):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


async def get_query_token(token: str):
    if token != "fake-token":
        raise HTTPException(status_code=400, detail="No fake token provided")

        