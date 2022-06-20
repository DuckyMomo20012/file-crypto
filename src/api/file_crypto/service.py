from schema import FileCrypto


def getOneFile(filename):
    return FileCrypto.objects(name=filename).first()


def getAllFiles():
    return FileCrypto.objects()


def uploadFile(name, size, sessionKey, nonce, tag, cipher):
    file = FileCrypto(
        name=name,
        size=size,
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
