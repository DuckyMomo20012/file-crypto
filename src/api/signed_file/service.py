from schema import SignedFile


def getOneFileSignature(filename):
    return SignedFile.objects(name=filename).first()


def getAllFileSignatures():
    return SignedFile.objects()


def uploadSignedFile(name, path, content, signatureContent, size):
    file = SignedFile(name=name, path=path, content=content, size=size)
    file.save()
    return file
