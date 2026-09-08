TORTOISE_ORM = {
    "connections": {
        "default": {
            "engine": "tortoise.backends.mysql",
            "credentials": {
                "host": "localhost",
                "port": 3306,
                "database": "fastapi_vue3",  # 数据库名称
                "user": "root",
                "password": "123456",  # 数据库密码
                "minsize": 1,
                "maxsize": 10,
                "charset": "utf8mb4",
                "echo": True
            }
        },
    },
    "apps": {
        "models": {
            "models": ["models"],
            "default_connection": "default",
        }
    },
    "use_tz": True,  # 是否使用时区
    "timezone": "Asia/Shanghai"
}

