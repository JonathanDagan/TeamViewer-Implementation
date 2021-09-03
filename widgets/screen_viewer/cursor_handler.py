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
        self.cursor.get_pos()

    def set_pos(self, x, y):
        self.cursor.set_pos(x,y)

    def motion(self, event, viewport: Screen, remote: Screen):
        p = Point (event.x, event.y)
        point = self._relative_pos(p,viewport,remote)
        self.set_pos(point.getX, point.getY)
    
    def _relative_pos(self, p: Point, viewport: Screen, remote: Screen) -> Point:
        x = p.getX * (remote.getX/viewport.getX)
        y = p.getY * (remote.getY/viewport.getY)
        return Point(x, y)
