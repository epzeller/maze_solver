class cell():
    def __init__(self, x1, y1,x2,y2, left, right, top, down, win):
        self.has_left_wall = left
        self.has_right_wall = right
        self.has_top_wall = top
        self.has_bottom_wall = down
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._win = win

    def draw(self):
        if self.has_left_wall:
            self._win.draw_line(self._x1, self._y1, self._x1, self._y2)
        if self.has_right_wall:
            self._win.draw_line(self._x2, self._y1, self._x2, self._y2)
        if self.has_top_wall:
            self._win.draw_line(self._x1, self._y1, self._x2, self._y1)
        if self.has_bottom_wall:
            self._win.draw_line(self._x1, self._y2, self._x2, self._y2)