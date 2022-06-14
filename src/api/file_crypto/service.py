from schema import FileCrypto

def getOneFile(filename):
    return FileCrypto.objects(name=filename).first()

def getAllFiles():
    return FileCrypto.objects()

def uploadFile (name, path, content, size, sessionKey):
    file = FileCrypto(name=name, path=path, content=content, size=size, sessionKey=sessionKey)
    file.save()
    return file