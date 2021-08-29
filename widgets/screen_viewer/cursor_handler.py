
class cursor:
    
    def __init__(self):
        # TODO: Have the viewport measurments be taken from the widget
        self.viewport_screen_x = 600
        self.viewport_screen_y = 300
        # TODO: Have the observed measurments be taken from the actual screen size
        self.observed_screen_x = 1920
        self.observed_screen_y = 1080
        pass
    
    def motion(self, event):
        x, y = event.x, event.y
        self.relative_pos(x,y)
        # print('{}, {}'.format(x, y))
        # TODO: have this trigger a func to send cordinate pos
    
    def relative_pos(self, x: int, y: int):
        x = x * (self.observed_screen_x/self.viewport_screen_x)
        y = y * (self.observed_screen_y/self.viewport_screen_y)
        print(f'relative x:{x} relative y:{y}')