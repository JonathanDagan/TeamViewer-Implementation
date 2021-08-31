import ctypes

MOUSEEVENTF_RIGHTDOWN = 1
MOUSEEVENTF_LEFTDOWN = 2
MOUSEEVENTF_RIGHTUP = 3
MOUSEEVENTF_LEFTUP = 4

class cursor:
    
    def __init__(self):
        # TODO: Have the viewport measurments be taken from the widget
        self.viewport_screen_x = 600
        self.viewport_screen_y = 300
        # TODO: Have the observed measurments be taken from the actual screen size
        self.observed_screen_x = 1920
        self.observed_screen_y = 1080
        
        self.user32 = ctypes.windll.user32
    
    def right_click(self):
        self.user32.mouse_event(MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)
        self.user32.mouse_event(MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)

    def set_pos(self, x, y):
        # TODO: im hereeeee
        pass

    def motion(self, event):
        x, y = event.x, event.y
        self._relative_pos(x,y)
        # print('{}, {}'.format(x, y))
        # TODO: have this trigger a func to send cordinate pos
    
    def _relative_pos(self, x: int, y: int):
        x = x * (self.observed_screen_x/self.viewport_screen_x)
        y = y * (self.observed_screen_y/self.viewport_screen_y)
        print(f'relative x:{x} relative y:{y}')

# This sets currsos position to top right
# rundll32 user32.dll,SetCursorPos