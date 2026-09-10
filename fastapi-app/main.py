import uvicorn
from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from settings import TORTOISE_ORM
from routers import student

app = FastAPI()

app.include_router(student.router)

# 注册 orm
register_tortoise(app, config=TORTOISE_ORM, add_exception_handlers=True)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, port=9090)
