from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA256
from Crypto.Random import get_random_bytes


def hash_password(plain_text_password: str) -> bytes:

    salt = get_random_bytes(32)

    hashed_pw = PBKDF2(
        plain_text_password, salt, 32, count=1000000, hmac_hash_module=SHA256
    )

    mixed_hashed_pw = salt + hashed_pw

    return mixed_hashed_pw


def verify_password(plain_text_password: str, mixed_hashed_password: bytes) -> bool:

    salt = mixed_hashed_password[:32]

    stored_hashed_pw = mixed_hashed_password[32:]

    hashed_pw = PBKDF2(
        plain_text_password, salt, 32, count=1000000, hmac_hash_module=SHA256
    )

    if hashed_pw == stored_hashed_pw:
        return True
    else:
        return False


def generateUserKeys(passphrase: str):
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


def updatePassphrase(
    privateKey: bytes, oldPassphrase: str, newPassphrase: str
) -> tuple[bytes]:
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


def signFile(privateKey: bytes, filePath: str, passphrase: str) -> bytes:

    from Crypto.Signature import pss
    from Crypto.Hash import SHA256
    from Crypto.PublicKey import RSA

    from src.helpers.file import readFile

    # NOTE: Ref: https://pycryptodome.readthedocs.io/en/latest/src/signature/pkcs1_pss.html

    # Read file
    fileContent = readFile(filePath, mode="rb")

    # Hash file content
    fileContentHash = SHA256.new(fileContent)

    # Sign file content
    key = RSA.import_key(privateKey, passphrase=passphrase)
    signature = pss.new(key).sign(fileContentHash)

    return signature


def verifySignature(publicKey: bytes, filePath: str, signaturePath: str) -> bool:

    from Crypto.Signature import pss
    from Crypto.Hash import SHA256
    from Crypto.PublicKey import RSA

    from src.helpers.file import readFile

    # NOTE: Ref: https://pycryptodome.readthedocs.io/en/latest/src/signature/pkcs1_pss.html

    # Read file
    fileContent = readFile(filePath, mode="rb")

    # Hash file content
    fileContentHash = SHA256.new(fileContent)

    # Read signature
    signature = readFile(signaturePath, mode="rb")

    # Verify signature
    key = RSA.import_key(publicKey)

    # This will raise an exception if the signature is invalid
    try:
        pss.new(key).verify(fileContentHash, signature)

        return True
    except (ValueError, TypeError):
        return False


def encryptFile(
    publicKey: bytes, filePath: str, folderPath: str = ".", outPutExt: str = ".bin"
) -> bool:

    from Crypto.PublicKey import RSA
    from Crypto.Random import get_random_bytes
    from Crypto.Cipher import AES, PKCS1_OAEP

    from pathlib import Path

    from src.helpers.file import readFile

    # Read file
    fileContent = readFile(filePath, mode="rb")

    # NOTE: Ref:
    # https://pycryptodome.readthedocs.io/en/latest/src/examples.html?#encrypt-data-with-rsa

    # Generate session key
    sessionKey = get_random_bytes(16)

    try:
        # Encrypt session key with RSA public key
        key = RSA.import_key(publicKey)
        cipherRSA = PKCS1_OAEP.new(key)
        encryptedSessionKey = cipherRSA.encrypt(sessionKey)

        # Encrypt file content
        cipherAES = AES.new(sessionKey, AES.MODE_EAX)
        cipherText, tag = cipherAES.encrypt_and_digest(fileContent)

        # Write encrypted file
        fileNameOut = Path(filePath + outPutExt).name

        fileOut = open(Path(folderPath).joinpath(fileNameOut), "wb")
        # Combine encrypted session key and encrypted file content
        [
            fileOut.write(x)
            for x in (encryptedSessionKey, cipherAES.nonce, tag, cipherText)
        ]

        return True

    except (ValueError, TypeError):
        return False


def decryptFile(
    privateKey: bytes,
    filePath: str,
    passphrase: str,
    folderPath: str = ".",
    outPutExt: str = ".txt",
) -> bool:

    from Crypto.PublicKey import RSA
    from Crypto.Cipher import AES, PKCS1_OAEP

    from src.helpers.file import writeFileToFolder

    # Read file
    fileIn = open(filePath, "rb")

    # NOTE: Ref:
    # https://pycryptodome.readthedocs.io/en/latest/src/examples.html?#encrypt-data-with-rsa

    try:
        # Decrypt session key with RSA private key
        key = RSA.import_key(privateKey, passphrase=passphrase)
        cipherRSA = PKCS1_OAEP.new(key)

        # Separate encrypted session key, nonce, tag and encrypted file content
        encryptedSessionKey, nonce, tag, cipherText = [
            fileIn.read(x) for x in (key.size_in_bytes(), 16, 16, -1)
        ]
        sessionKey = cipherRSA.decrypt(encryptedSessionKey)

        # Decrypt file content
        cipherAES = AES.new(sessionKey, AES.MODE_EAX, nonce)
        decryptedFileContent = cipherAES.decrypt_and_verify(cipherText, tag)

        # Write decrypted file
        writeFileToFolder(
            filePath + outPutExt, folderPath, decryptedFileContent.decode("utf-8")
        )

        return True

    except (ValueError, TypeError):
        return False


def encryptData(
    publicKey: bytes, content: bytes
) -> tuple[bytes, bytes, bytes, bytes] | None:

    from Crypto.PublicKey import RSA
    from Crypto.Random import get_random_bytes
    from Crypto.Cipher import AES, PKCS1_OAEP

    # NOTE: Ref:
    # https://pycryptodome.readthedocs.io/en/latest/src/examples.html?#encrypt-data-with-rsa

    # Generate session key
    sessionKey = get_random_bytes(16)

    try:
        # Encrypt session key with RSA public key
        key = RSA.import_key(publicKey)
        cipherRSA = PKCS1_OAEP.new(key)
        encryptedSessionKey = cipherRSA.encrypt(sessionKey)

        # Encrypt file content
        cipherAES = AES.new(sessionKey, AES.MODE_EAX)
        cipherText, tag = cipherAES.encrypt_and_digest(content)

        return (encryptedSessionKey, cipherAES.nonce, tag, cipherText)

    except (ValueError, TypeError):
        return None


def decryptData(
    privateKey: bytes,
    passphrase: str,
    encryptedSessionKey: bytes,
    nonce: bytes,
    tag: bytes,
    cipherText: bytes,
) -> bytes | None:

    from Crypto.PublicKey import RSA
    from Crypto.Cipher import AES, PKCS1_OAEP

    # NOTE: Ref:
    # https://pycryptodome.readthedocs.io/en/latest/src/examples.html?#encrypt-data-with-rsa

    try:
        # Decrypt session key with RSA private key
        key = RSA.import_key(privateKey, passphrase=passphrase)
        cipherRSA = PKCS1_OAEP.new(key)

        sessionKey = cipherRSA.decrypt(encryptedSessionKey)

        # Decrypt file content
        cipherAES = AES.new(sessionKey, AES.MODE_EAX, nonce)
        decryptedFileContent = cipherAES.decrypt_and_verify(cipherText, tag)

        return decryptedFileContent.decode("utf-8")

    except (ValueError, TypeError):
        return None
