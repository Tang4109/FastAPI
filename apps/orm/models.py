# 员工信息
from tortoise.models import Model
from tortoise import fields

# 员工表
class Employee(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=32, description="姓名")
    pwd = fields.CharField(max_length=32, description="密码")
    eno = fields.IntField(description="编号")

    # 一对多的关系
    clas = fields.ForeignKeyField("models.Clas", related_name="employees")

    # 多对多的关系
    projects = fields.ManyToManyField("models.Project", related_name="employees")

#工程项目表
class Project(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=32, description="工程名称")
    leader = fields.ForeignKeyField("models.Leader", )
    addr = fields.CharField(max_length=32, description="办公室", default="")
    # 对于已经有的字段必须加一个默认值或者可为空

# 班组表
class Clas(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=32, description="班组名称")

# 领导表
class Leader(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=32, description="姓名")
    pwd = fields.CharField(max_length=32, description="密码")
    lno = fields.IntField(description="领导编号")
