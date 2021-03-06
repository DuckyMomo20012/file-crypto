import json
from datetime import datetime
from pathlib import Path
from typing import TypeVar, Union


def readFile(fileName: str, mode: str = "r"):
    with open(fileName, mode) as file:
        return file.read()


def writeFile(fileName: str, content: Union[str, bytes], mode: str = "w"):
    with open(fileName, mode) as file:
        file.write(content)


def writeFileToFolder(
    filePath: str, folderPath: str, content: Union[str, bytes], mode: str = "w"
):

    fileName = Path(filePath).name

    writeFile(str(Path(folderPath).joinpath(fileName)), content, mode)


def generateRandomFileName(fileName: str):

    fileNamePath = Path(fileName)
    # First, we get all the suffixes of the file name
    suffixes = fileNamePath.suffixes

    # Then, we "inject" the timestamp before the first suffix
    newFileName = str(fileNamePath).replace(
        suffixes[0], f'_{datetime.now().strftime("%Y%m%d%H%M%S")}{suffixes[0]}'
    )

    return newFileName


T = TypeVar("T")


def getSettingField(setting: str, default: T) -> T:

    try:

        with open("settings.json") as file:
            settings = json.loads(file.read())

        return settings.get(setting, default)

    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return default
