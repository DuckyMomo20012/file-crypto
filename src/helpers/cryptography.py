from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA256
from Crypto.Random import get_random_bytes


def hash_password(plain_text_password):
    salt = get_random_bytes(32).hex()
    hashed_pw = PBKDF2(
        plain_text_password, salt, 32, count=1000000, hmac_hash_module=SHA256
    ).hex()
    mixed_hashed_pw = salt + hashed_pw
    return mixed_hashed_pw


def verify_password(plain_text_password, mixed_hashed_password):
    salt = mixed_hashed_password[:64]
    stored_hashed_pw = mixed_hashed_password[64:]
    hashed_pw = PBKDF2(
        plain_text_password, salt, 32, count=1000000, hmac_hash_module=SHA256
    ).hex()
    if hashed_pw == stored_hashed_pw:
        return True
    else:
        return False
