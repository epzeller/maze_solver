class cell():
    def __init__(self, x1, y1,x2,y2, left, right, top, down, win=None):
        self.has_left_wall = left
        self.has_right_wall = right
        self.has_top_wall = top
        self.has_bottom_wall = down
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self.x_center = (x1 + x2) / 2
        self.y_center = (y1 + y2) / 2
        self._win = win
        self.visited = False

    def draw(self):
        if self._win is None:
            return
        if self.has_left_wall:
            self._win.draw_line(self._x1, self._y1, self._x1, self._y2)
        else:
            self._win.draw_line(self._x1, self._y1, self._x1, self._y2, fill_color="white")
        if self.has_right_wall:
            self._win.draw_line(self._x2, self._y1, self._x2, self._y2)
        else:
            self._win.draw_line(self._x2, self._y1, self._x2, self._y2, fill_color="white")
        if self.has_top_wall:
            self._win.draw_line(self._x1, self._y1, self._x2, self._y1)
        else:
            self._win.draw_line(self._x1, self._y1, self._x2, self._y1, fill_color="white")
        if self.has_bottom_wall:
            self._win.draw_line(self._x1, self._y2, self._x2, self._y2)
        else:
            self._win.draw_line(self._x1, self._y2, self._x2, self._y2, fill_color="white")

    def cell_draw_move(self, target, undo=False):
        if undo:
            color = "white"
        else:
            color = "red"
        self._win.draw_line(self.x_center, self.y_center, target.x_center, target.y_center, fill_color=color)

 