from mongoengine.queryset.visitor import Q  # type: ignore

from schema import FileCrypto


def getOneFile(emailUser, filename):
    return FileCrypto.objects(Q(emailUser=emailUser) & Q(name=filename)).first()


def getAllFiles(emailUser):
    return FileCrypto.objects(emailUser=emailUser)


def uploadFile(name, sessionKey, nonce, tag, cipher, emailUser):
    file = FileCrypto(
        name=name,
        sessionKey=sessionKey,
        nonce=nonce,
        tag=tag,
        cipher=cipher,
        emailUser=emailUser,
    )
    file.save()
    return file


def uploadFileNoDuplicate(name, sessionKey, nonce, tag, cipher, emailUser):

    from src.helpers.file import generateRandomFileName

    checkDup = getOneFile(emailUser, name)

    if checkDup is None:
        return uploadFile(name, sessionKey, nonce, tag, cipher, emailUser)

    else:

        newFileName = generateRandomFileName(name)

        return uploadFile(newFileName, sessionKey, nonce, tag, cipher, emailUser)


def deleteFile(emailUser, filename):
    file = getOneFile(emailUser, filename)
    file.delete()
    return file


def updateFile(emailUser, filename, sessionKey, nonce, tag, cipher):
    file = getOneFile(emailUser, filename)
    file.sessionKey = sessionKey
    file.nonce = nonce
    file.tag = tag
    file.cipher.replace(cipher)
    file.save()
    return file


def updateFileOneField(
    emailUser: str,
    fileName: str,
    fieldName: str,
    newValue: str,
):
    file = getOneFile(emailUser, fileName)
    file[fieldName] = newValue
    file.save()
    return file


def updateFileMetadataOneField(
    emailUser: str,
    fileName: str,
    fieldName: str,
    newValue: str,
):
    file = getOneFile(emailUser, fileName)
    file.cipher[fieldName] = newValue
    file.save()
    return file
