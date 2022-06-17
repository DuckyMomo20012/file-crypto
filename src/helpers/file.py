def readFile(fileName: str):
    with open(fileName, "r") as file:
        return file.read()
