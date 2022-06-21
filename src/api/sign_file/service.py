from schema import SignFile


def getOneFileSignature(filename):
    return SignFile.objects(name=filename).first()

def getAllFileSignatures():
    return SignFile.objects()

def uploadSignedFile(name, path, content, signatureContent, size):
    file = SignFile(name=name, path=path, content=content, size=size)
    file.save()
    return file