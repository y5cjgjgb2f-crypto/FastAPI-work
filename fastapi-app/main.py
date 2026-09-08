from fastapi import FastAPI
import uvicorn
from tortoise.contrib.fastapi import register_tortoise

from models import Student
from settings import TORTOISE_ORM

app = FastAPI()

# 注册 orm
register_tortoise(app, config=TORTOISE_ORM, add_exception_handlers=True)


@app.get("/student/selectAll")
async def select_all(name: str = '', no: str = ''):
    stu_list = await Student.filter(name__contains=name).filter(no__contains=no)
    return stu_list


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, port=9090)

