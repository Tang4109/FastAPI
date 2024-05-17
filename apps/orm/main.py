from fastapi import FastAPI  # 引入FastAPI
import uvicorn  # 引入uvicorn
from tortoise.contrib.fastapi import register_tortoise  # 引入tortoise的监控
from employee import employee_api
from settings import TORTOISE_ORM

app = FastAPI()  # FastAPI()实例化一个app对象
app.include_router(employee_api, prefix="/employee", tags=["员工系统的员工接口"])  # 注册路由

# 注册tortoise：fastapi一旦运行，register_tortoise已经执行，实现监控
# 该方法会在fastapi启动时触发，内部通过传递进去的app对象，监听服务启动和终止事件
# 当检测到启动事件时，会初始化Tortoise对象，如果generate_schemas为True则还会进行数据库迁移
# 当检测到终止事件时，会关闭连接
register_tortoise(
    app=app,
    config=TORTOISE_ORM,
    # generate_schemas=True,  # 如果数据库为空，则自动生成对应表单，生产环境不要开
    # add_exception_handlers=True,  # 生产环境不要开，会泄露调试信息
)

if __name__ == '__main__':
    uvicorn.run("main:app", port=8090, reload=True)  # 启动服务
