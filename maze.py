from cell import cell
import time, random

class maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        self._create_cells()

    def _create_cells(self):
        self._cells = []
        for i in range(self._num_cols):
            cell_col = []
            for j in range(self._num_rows):
                x1 = self._x1 + i * self._cell_size_x
                y1 = self._y1 + j * self._cell_size_y
                x2 = x1 + self._cell_size_x
                y2 = y1 + self._cell_size_y
                left = True
                right = True
                top = True
                down = True
                this_cell = cell(x1, y1, x2, y2, left, right, top, down, win=self._win)
                cell_col.append(this_cell)
            self._cells.append(cell_col)

        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cells(i,j)

    def _draw_cells(self, i, j): 
        self._cells[i][j].draw()
        self._animate()


    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        # print("redraw")
        time.sleep(0.02)

    def _break_entrance_and_exit(self):
        # print("breaking entrance and exit")
        self._cells[0][0].has_top_wall = False
        self._cells[self._num_cols-1][self._num_rows-1].has_bottom_wall = False
        self._draw_cells(0,0)
        self._draw_cells(self._num_cols-1,self._num_rows-1)
        self._animate()

    def _break_wall(self, i, j, direction):
        # print(f"breaking wall at {i}, {j} in direction {direction}")
        # time.sleep(1)
        if direction == "left" and i > 0:
            self._cells[i][j].has_left_wall = False
            self._cells[i-1][j].has_right_wall = False
            self._draw_cells(i,j)
            self._draw_cells(i-1,j)
            self._animate()
        elif direction == "right" and i < self._num_cols - 1:
            self._cells[i][j].has_right_wall = False
            self._cells[i+1][j].has_left_wall = False
            self._draw_cells(i,j)
            self._draw_cells(i+1,j) 
            self._animate()
        elif direction == "top" and j > 0:
            self._cells[i][j].has_top_wall = False
            self._cells[i][j-1].has_bottom_wall = False
            self._draw_cells(i,j)
            self._draw_cells(i,j-1)
            self._animate()
        elif direction == "down" and j < self._num_rows - 1:
            self._cells[i][j].has_bottom_wall = False
            self._cells[i][j+1].has_top_wall = False
            self._draw_cells(i,j)
            self._draw_cells(i,j+1)
            self._animate()
        # print("Done breaking wall")

    def _break_walls_r(self, i, j):
        # print(f"breaking walls at {i}, {j}")
        self._cells[i][j].visited = True
        while True:
            to_visit = []
            if i > 0 and not self._cells[i-1][j].visited:
                to_visit.append("left")
            if i < self._num_cols - 1 and not self._cells[i+1][j].visited:
                to_visit.append("right")
            if j > 0 and not self._cells[i][j-1].visited:
                to_visit.append("top")
            if j < self._num_rows - 1 and not self._cells[i][j+1].visited:
                to_visit.append("down")
            if len(to_visit) == 0:
                self._cells[i][j].draw()
                return
            direction = random.choice(to_visit)
            if direction == "left":
                self._break_wall(i, j, "left")
                self._break_walls_r(i-1, j)
            elif direction == "right":
                self._break_wall(i, j, "right")
                self._break_walls_r(i+1, j)
            elif direction == "top":
                self._break_wall(i, j, "top")
                self._break_walls_r(i, j-1)
            elif direction == "down":
                self._break_wall(i, j, "down")
                self._break_walls_r(i, j+1)

    def _reset_cells_visited(self):
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._cells[i][j].visited = False

    def solve(self):
        self._solve_r(0, 0)

    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True
        if i == self._num_cols - 1 and j == self._num_rows - 1:
            return True
        if i > 0 and not self._cells[i][j].has_left_wall and not self._cells[i-1][j].visited:
            self._cells[i][j].cell_draw_move(self._cells[i-1][j])
            if self._solve_r(i-1, j):
                return True
            self._cells[i][j].cell_draw_move(self._cells[i-1][j], undo=True)
        if i < self._num_cols - 1 and not self._cells[i][j].has_right_wall and not self._cells[i+1][j].visited:
            self._cells[i][j].cell_draw_move(self._cells[i+1][j])
            if self._solve_r(i+1, j):
                return True
            self._cells[i][j].cell_draw_move(self._cells[i+1][j], undo=True) 
        if j > 0 and not self._cells[i][j].has_top_wall and not self._cells[i][j-1].visited:
            self._cells[i][j].cell_draw_move(self._cells[i][j-1])
            if self._solve_r(i, j-1):
                return True
            self._cells[i][j].cell_draw_move(self._cells[i][j-1], undo=True)
        if j < self._num_rows - 1 and not self._cells[i][j].has_bottom_wall and not self._cells[i][j+1].visited:
            self._cells[i][j].cell_draw_move(self._cells[i][j+1])
            if self._solve_r(i, j+1):
                return True
            self._cells[i][j].cell_draw_move(self._cells[i][j+1], undo=True)
        self._cells[i][j].visited = False
        return False
    
