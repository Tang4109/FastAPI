# Description: 配置文件
TORTOISE_ORM = {
    'connections': {
        'default': {
            # 'engine': 'tortoise.backends.asyncpg',  PostgreSQL
            'engine': 'tortoise.backends.mysql',  # 数据库类型
            'credentials': {
                'host': '127.0.0.1',  # 数据库地址
                'port': '3306',  # 数据库端口
                'user': 'root',  # 数据库用户名
                'password': 'mysql',  # 数据库密码
                'database': 'fastapi',  # 数据库名称
                'minsize': 1,  # 最小连接数
                'maxsize': 5,  # 最大连接数
                'charset': 'utf8mb4',  # 字符集
                "echo": True  # 是否打印sql语句
            }
        },
    },
    'apps': {
        'models': {
            'models': ['models', "aerich.models"],  # 模型所在的文件夹
            'default_connection': 'default',  # 默认连接
        }
    },
    'use_tz': False,  # 是否使用时区
    'timezone': 'Asia/Shanghai'  # 时区
}
