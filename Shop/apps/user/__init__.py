import hashlib


def set_password(password):
    # 密码加密
    h = hashlib.md5(password.encode('utf-8'))
    return h.hexdigest()
