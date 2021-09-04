#  TODO: Switch to factory in future

import ctypes

from utils.runtime import isWindows

class Commands:
    def __init__(self):
        if isWindows:
            self.user32 = ctypes.windll.user32
    
    def lock_pc(self):
        if isWindows:
            self.__windows_lock_pc()
        else:
            raise NotImplementedError()

    def alert(self, message: str, title: str = "alert") -> None:
        if isWindows:
            self.__windows_alert(message, title)
        else:
            raise NotImplementedError()

    def __windows_alert(self, message: str, title: str) -> None:
        self.user32.MessageBoxW(0, message, title, 0)
    def __linux_alert(self, message: str, title: str) -> None:
        raise NotImplementedError(f'{self.__class__.__name__}.__linux_alert()') 
    def __mac_alert(self, message: str, title: str) -> None:
        raise NotImplementedError(f'{self.__class__.__name__}.__mac_alert()') 

    def __windows_lock_pc(self) -> None:
        self.user32.LockWorkStation()        
    def __linux_lock_pc(self) -> None:
        raise NotImplementedError(f'{self.__class__.__name__}.__linux_lock_pc()')        
    def __mac_lock_pc(self) -> None:
        raise NotImplementedError(f'{self.__class__.__name__}.__mac_lock_pc()')
