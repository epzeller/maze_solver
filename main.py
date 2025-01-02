from graphics import Window
from cell import cell
from maze import maze
import time


def main():
    win = Window(800, 600)
    # cell1 = cell(50, 50, 100, 100, True, False, True, False, win)
    # cell2 = cell(150, 50, 200, 100, False, True, True, False, win)
    # cell1.draw()
    # cell2.draw()
    # cell1.cell_draw_move(cell2)
    this_maze = maze(50, 50, 40, 40, 10, 10, win=win)
    print("created maze")
    this_maze._break_entrance_and_exit()
    # this_maze._break_wall(0, 4, "left")
    # this_maze._break_wall(2, 2, "down")
    this_maze._break_walls_r(0, 0)
    this_maze._reset_cells_visited()
    this_maze.solve()

   

    win.wait_for_close()


main()