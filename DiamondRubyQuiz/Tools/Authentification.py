from passlib.hash import pbkdf2_sha256 as encryptor


def encrypt(value):
    try:
        enc = encryptor.hash(value)
        if enc:
            return enc
        else:
            return False
    except Exception as e:
        return e


def validate_encrypt(value, hashed):
    try:
        verfication = encryptor.verify(value, hashed)
        if verfication:
            return True
        else:
            return False
    except Exception as e:
        raise e
