import psutil


def getCPUPercent(inputStr: str):

    # When we use "[!cpu]CPU: {cpu}%", macro will call this function with
    # "inputStr" is "CPU: {cpu}%". What we have to do is pass value to {cpu}
    # using format function.
    cpu = psutil.cpu_percent()
    return inputStr.format(cpu=cpu)


def getRAMPercent(inputStr: str):

    ram = psutil.virtual_memory().percent
    return inputStr.format(ram=ram)
