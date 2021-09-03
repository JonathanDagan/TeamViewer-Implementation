from utils.cursor import Cursor
from utils.point import Point
from utils.screen import Screen

class CursorHandler:
    def __init__(self):
        self.cursor = Cursor()
    
    def right_click(self):
        self.cursor.right_click()
    
    def left_click(self):
        self.cursor.left_click()

    def get_pos(self, x, y):
        self.cursor.set_pos()

    def set_pos(self, x, y):
        self.cursor.set_pos(x,y)

    def motion(self, event):
        x, y = event.x, event.y
        self._relative_pos(x,y)
        # print('{}, {}'.format(x, y))
        # TODO: have this trigger a func to send cordinate pos
    
    def _relative_pos(self, p: Point, viewport: Screen, remote: Screen):
        x = p.getX * (remote.getX/viewport.getX)
        y = p.getY * (remote.getY/viewport.getY)
        return Point(x, y)
