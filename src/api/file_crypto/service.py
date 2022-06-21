from schema import FileCrypto


def getOneFile(filename):
    return FileCrypto.objects(name=filename).first()


def getAllFiles():
    return FileCrypto.objects()


def uploadFile(name, sessionKey, nonce, tag, cipher):
    file = FileCrypto(
        name=name,
        sessionKey=sessionKey,
        nonce=nonce,
        tag=tag,
        cipher=cipher,
    )
    file.save()
    return file


def deleteFile(filename):
    file = getOneFile(filename)
    file.delete()
    return file


def updateFile(filename, sessionKey, nonce, tag, cipher):
    file = getOneFile(filename)
    file.sessionKey = sessionKey
    file.nonce = nonce
    file.tag = tag
    file.cipher.replace(cipher)
    file.save()
    return file
