from flask import abort
from flask_login import current_user
from functools import wraps
from simpledu.models import User


# 这是嵌套装饰器函数，其返回值就是用来创建装饰器的函数
def role_required(role):
    # 这个是内层装饰器函数
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwrargs):
            if not current_user.is_authenticated or current_user.role < role:
                abort(404)
            return func(*args, **kwrargs)
        return wrapper
    return decorator


staff_required = role_required(User.ROLE_STAFF)
admin_required = role_required(User.ROLE_ADMIN)


