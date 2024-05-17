from fastapi import APIRouter
from fastapi import Request
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, field_validator
from fastapi.exceptions import HTTPException

from typing import List, Union
from models import *
import os

employee_api = APIRouter()


@employee_api.get("/")
async def getAllEmployee():
# (1) 查询所有 all方法
    Employees = await Employee.all()  # Queryset: [Employee(),Employee(),Employee()]
    print("Employees", Employees)

    for employee in Employees:
        print(employee.name, employee.eno)
    print(Employees[0].name)
    return Employees


# (2) 过滤查询 filter
# Employees = await Employee.filter(name="员工1")  # Queryset: [Employee(),Employee(),Employee()]
# print("Employees", Employees)
# Employees = await Employee.filter(clas_id=2)  # Queryset: [Employee(),Employee(),Employee()]
# print("Employees", Employees)

# (3) 过滤查询 get方法：返回模型类型对象
# employee = await Employee.filter(id=1)  # [Employee(),]
# print(employee)
# print(employee[0].name)
#
# employee = await Employee.get(id=1)  # Employee()
# print(employee.name)
# Employees=employee

# (4) 模糊查询
# employees = await Employee.filter(eno__gt=2001)
# employees = await Employee.filter(eno__range=[1, 10000])
# employees = await Employee.filter(eno__in=[2001, 2002])
# print(employees)  # [<Employee: 7>, <Employee: 8>]
# Employees = employees

# (5) values查询
# employees = await Employee.filter(eno__range=[1, 10000])  # [Employee(),Employee(),Employee(),...]
# employees = await Employee.all().values("name", "eno")  # [{},{},{},...]
# print(employees)
# Employees = employees

# (6) 一对多查询 多对多查询
# employee_1 = await Employee.get(name="员工1")
# print(employee_1.name)
# print(employee_1.eno)
# print(await employee_1.clas.values("name"))  # {'name': '第一班组'}
# Employees = await Employee.all().values("name", "clas__name")
# print(Employees)
# print(await employee_1.projects.all().values("name", "leader__name"))
# Employees = await Employee.all().values("name", "clas__name", "projects__name")
# print(Employees)
#
# return Employees

# 对数据库表进行查询操作
# @employee_api.get("/index.html")
# async def getAllEmployee(request: Request):
#     templates = Jinja2Templates(directory="templates")
#     # templates = Jinja2Templates(directory=os.path.abspath(os.path.expanduser('templates')))
#     Employees = await Employee.all()  # [Employee(),Employee(),...]
#
#     return templates.TemplateResponse(
#         "index.html", {
#             "request": request,
#             "Employees": Employees
#         }
#     )


class EmployeeIn(BaseModel):
    name: str
    pwd: str
    eno: int
    clas_id: int
    projects: List[int] = []

    @field_validator("name")
    def name_must_alpha(cls, value):
        assert value.isalpha(), 'name must be alpha'
        return value

    @field_validator("eno")
    def sno_validate(cls, value):
        assert 1000 < value < 10000, '员工编号要在2000-10000的范围内'
        return value

# #对数据库表进行插入操作
# @employee_api.post("/")
# async def addEmployee(employee_in: EmployeeIn):
#     # 插入到数据库
#     # 方式1
#     # Employee = Employee(name=employee_in.name, pwd=employee_in.pwd, sno=employee_in.eno, clas_id=employee_in.clas_id)
#     # await Employee.save() # 插入到数据库Employee表
#     # 方式2
#     employee = await Employee.create(name=employee_in.name, pwd=employee_in.pwd, eno=employee_in.eno,
#                                      clas_id=employee_in.clas_id)
#
#     # 多对多的关系绑定
#     choose_projects = await Project.filter(id__in=employee_in.projects)
#     await employee.projects.add(*choose_projects)
#
#     return employee

# @employee_api.get("/{Employee_id}")
# async def getOneEmployee(Employee_id: int):
#     employee = await Employee.get(id=Employee_id)
#
#     return employee

# 对数据库表进行更新操作
# @employee_api.put("/{Employee_id}")
# async def updateEmployee(Employee_id: int, employee_in: EmployeeIn):
#     data = employee_in.dict()
#     print("data", data)
#     projects = data.pop("projects")
#
#     await Employee.filter(id=Employee_id).update(**data)
#
#     #  设置多对多关系
#     edit_emp = await Employee.get(id=Employee_id)
#     choose_projects = await Project.filter(id__in=projects)
#     await edit_emp.projects.clear()
#     await edit_emp.projects.add(*choose_projects)
#
#     return edit_emp

# 对数据库表进行删除操作
# @employee_api.delete("/{Employee_id}")
# async def deleteEmployee(Employee_id: int):
#     deleteCount = await Employee.filter(id=Employee_id).delete()
#     if not deleteCount:
#         raise HTTPException(status_code=404, detail=f"主键为{Employee_id}的员工不存在")
#
#     return {}
