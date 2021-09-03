import ctypes

# Cant get enum to work properly with mouse_event method, fix in future
MOUSEEVENT_RIGHTDOWN = 1
MOUSEEVENT_LEFTDOWN = 2
MOUSEEVENT_RIGHTUP = 3
MOUSEEVENT_LEFTUP = 4


class Cursor:
    def __init__(self):        
        self.user32 = ctypes.windll.user32
    
    def right_click(self):
        self.user32.mouse_event(MOUSEEVENT_RIGHTDOWN, 0, 0, 0, 0)
        self.user32.mouse_event(MOUSEEVENT_RIGHTUP, 0, 0, 0, 0)
    
    def left_click(self):
        self.user32.mouse_event(MOUSEEVENT_LEFTDOWN, 0, 0, 0, 0)
        self.user32.mouse_event(MOUSEEVENT_LEFTUP, 0, 0, 0, 0)

    def get_pos(self):
        # TODO: Figgure out how to use the GetCursorPos() method from the dll
        raise NotImplementedError(f'{self.__class__.__name__}.get_pos(): Fix TODO here')

    def set_pos(self, x, y):
        x , y = int(x), int(y)
        self.user32.SetCursorPos(x,y)

