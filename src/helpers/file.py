def readFile(fileName: str, mode: str = "r"):
    with open(fileName, mode) as file:
        return file.read()


def writeFile(fileName: str, content: str | bytes, mode: str = "w"):
    with open(fileName, mode) as file:
        file.write(content)


def writeFileToFolder(
    filePath: str, folderPath: str, content: str | bytes, mode: str = "w"
):

    from pathlib import Path

    fileName = Path(filePath).name

    writeFile(Path(folderPath).joinpath(fileName), content, mode)
