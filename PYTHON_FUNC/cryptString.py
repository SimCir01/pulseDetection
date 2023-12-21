import hashlib

def cryptString(value):

    result = hashlib.sha256(value.encode())
    result = result.hexdigest()

    return result