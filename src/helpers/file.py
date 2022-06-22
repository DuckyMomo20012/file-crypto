from datetime import datetime
from pathlib import Path


def readFile(fileName: str, mode: str = "r"):
    with open(fileName, mode) as file:
        return file.read()


def writeFile(fileName: str, content: str | bytes, mode: str = "w"):
    with open(fileName, mode) as file:
        file.write(content)


def writeFileToFolder(
    filePath: str, folderPath: str, content: str | bytes, mode: str = "w"
):

    fileName = Path(filePath).name

    writeFile(str(Path(folderPath).joinpath(fileName)), content, mode)


def generateRandomFileName(fileName: str):

    return f"{fileName}_%s" % (datetime.now().strftime("%Y%m%d%H%M%S"))
