import psutil
import pytermgui as ptg


# E.g: ptg.Label("[!selection_length]Length: {select_len}")
def getSelectionLength(inputField: ptg.InputField):
    def _macro(inputStr: str):
        return inputStr.format(select_len=inputField._selection_length)

    return _macro


# E.g: ptg.Label("[!cursor]Cursor: {row}:{col}")
def getCursor(inputField: ptg.InputField):
    def _macro(inputStr: str):
        return inputStr.format(row=inputField.cursor.row, col=inputField.cursor.col)

    return _macro


# E.g: ptg.Label("[!cpu]CPU: {cpu}%")
def getCPUPercent(inputStr: str):

    # When we use "[!cpu]CPU: {cpu}%", macro will call this function with
    # "inputStr" is "CPU: {cpu}%". What we have to do is pass value to {cpu}
    # using format function.
    cpu = psutil.cpu_percent()
    return inputStr.format(cpu=cpu)


# E.g: ptg.Label("[!ram]RAM: {ram}%")
def getRAMPercent(inputStr: str):

    ram = psutil.virtual_memory().percent
    return inputStr.format(ram=ram)
