import os

def isWindows() -> bool:
    if os.name == 'nt':
        return True
    return False