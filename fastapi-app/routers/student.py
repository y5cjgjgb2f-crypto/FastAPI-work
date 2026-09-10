from typing import Optional

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from models import Student

router = APIRouter(prefix="/student")


# 接收数据的模型
class StudentModel(BaseModel):
    id: Optional[int] = None
    no: str | None = None
    name: str | None = None
    clazz: str | None = None
    major: str | None = None
    college: str | None = None
    phone: str | None = None
    email: str | None = None
    address: str | None = None


@router.get("/selectAll")
async def select_all(name: str = '', no: str = ''):
    stu_list = await Student.filter(name__contains=name).filter(no__contains=no)
    return stu_list


@router.get("/selectPage")
async def select_all(name: str = '', no: str = '', pageNum: int = 1, pageSize: int = 10):
    # 数据库的总共条数 total   # 当前查询页的数据 list
    query = Student.filter(name__contains=name).filter(no__contains=no).order_by("id")
    stu_list = await query.offset((pageNum - 1) * pageSize).limit(pageSize)
    total = await query.count()
    return {"list": stu_list, "total": total}


@router.post("/add")
async def add_student(student_model: StudentModel):
    if student_model.no is None:
        raise HTTPException(status_code=400, detail="参数错误")
    # 根据学号查询
    db_stu = await Student.get_or_none(no=student_model.no)
    if db_stu is None:
        # 参数模型转换成 字典数据
        stu_dict = student_model.model_dump(exclude={"id"}, exclude_unset=True)
        # **{"no": "123"}  =>  no=123
        resp = await Student.create(**stu_dict)
        return resp
    else:
        return None


@router.put("/update")
async def update_student(student_model: StudentModel):
    if student_model.id is None:
        raise HTTPException(status_code=400, detail="ID参数为空")
    # 参数模型转换成 字典数据
    stu_dict = student_model.model_dump(exclude={"id"}, exclude_unset=True)
    resp = await Student.filter(id=student_model.id).update(**stu_dict)   # update student set name = '青哥哥真帅' where id = 1
    return resp


@router.delete("/delete/{stu_id}")
async def delete_student(stu_id: int):
    resp = await Student.filter(id=stu_id).delete()
    return resp


# 导出 router
__all__ = ["router"]
