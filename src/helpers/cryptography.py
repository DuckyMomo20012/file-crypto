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


def generateUserKeys(passphrase):
    from Crypto.PublicKey import RSA

    # Generate RSA private and public key pair 2048 bits long
    key = RSA.generate(2048)

    # Use user password as passphrase to encrypt private key

    # NOTE: Ref:
    # https://pycryptodome.readthedocs.io/en/latest/src/io/pkcs8.html#module-Crypto.IO.PKCS8

    # 1. A "16" byte AES key is derived from the passphrase using
    #    Crypto.Protocol.KDF.scrypt() with 8 bytes salt.
    # READ more: https://github.com/Legrandin/pycryptodome/blob/master/lib/Crypto/IO/_PBES.py#L239
    # 2. The private key is encrypted using CBC.
    # 3. The encrypted key is encoded according to PKCS#8.
    privateKey = key.export_key(
        passphrase=passphrase, pkcs=8, protection="scryptAndAES128-CBC"
    )

    publicKey = key.publickey().export_key()

    return privateKey, publicKey


def updatePassphrase(privateKey, oldPassphrase: str, newPassphrase: str):
    from Crypto.PublicKey import RSA

    # First, we import the private key with the old passphrase
    key = RSA.import_key(privateKey, passphrase=oldPassphrase)

    # Then we encrypt private key with the new passphrase
    newPrivateKey = key.export_key(
        passphrase=newPassphrase, pkcs=8, protection="scryptAndAES128-CBC"
    )

    # And export new public key
    newPublicKey = key.publickey().export_key()

    return newPrivateKey, newPublicKey
