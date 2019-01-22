import hashlib

from Shop.settings import SECRET_KEY


def set_password(password):
    # 密码加密
    for _ in range(1000):
        pass_str = "{}{}".format(password, SECRET_KEY)
        h = hashlib.md5(pass_str.encode('utf-8'))
        password = h.hexdigest()

        # 返回密码
    return password
